<#
.SYNOPSIS
    Installeert De Geest in de Fles in één map: Ollama, Thonny (met Python) en de taalmodellen.
.DESCRIPTION
    Alles komt in de map -Doel. Niets wordt in Windows zelf geïnstalleerd en er zijn geen
    beheerdersrechten nodig. Weghalen kan met opruimen.bat in die map.

    Installeer je op een USB-stick (bijvoorbeeld -Doel E:\GeestInDeFles), dan kun je de stick
    daarna op elke laptop gebruiken zonder internet: start.bat of kopieer-naar-laptop.bat.

    Het script kan veilig opnieuw worden gestart; wat al klaar is, wordt overgeslagen en
    afgebroken downloads gaan verder waar ze waren.
.EXAMPLE
    .\installeer.ps1
.EXAMPLE
    .\installeer.ps1 -Doel E:\GeestInDeFles -AlleenCpu
#>
param(
    [string]$Doel = (Join-Path $env:USERPROFILE 'GeestInDeFles'),
    [string[]]$Modellen = @('bramvanroy/fietje-2b-chat:Q5_K_M', 'bge-m3'),
    [string[]]$Stemmen = @('nl_NL-pim-medium', 'nl_NL-ronnie-medium', 'nl_BE-nathalie-medium'),
    [switch]$AlleenCpu,
    [switch]$BewaarDownloads,
    [switch]$Ja
)

# Vaste versies, zodat het lesmateriaal over een jaar nog precies zo werkt.
$OllamaVersie   = '0.40.16'
$ThonnyVersie   = '5.0.1'
$PythonPakketten = @('requests==2.34.2', 'pyttsx3==2.99', 'piper-tts==1.8.0', 'onnxruntime==1.31.1')
$StemmenVersie  = 'cf910fb59f1d79ab3b625a63993a108751c6c25d'   # commit van huggingface.co/rhasspy/piper-voices

$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'
# Via installeer.bat komt "-Modellen a,b" binnen als één tekst; splits daarom zelf op komma's.
$Modellen = @($Modellen | ForEach-Object { $_ -split ',' } | ForEach-Object { $_.Trim() } | Where-Object { $_ })
$Stemmen  = @($Stemmen  | ForEach-Object { $_ -split ',' } | ForEach-Object { $_.Trim() } | Where-Object { $_ })
$Bron = $PSScriptRoot
$Doel = [IO.Path]::GetFullPath($Doel)
$Downloads = Join-Path $Doel '_downloads'
$InstallatiePoort = 11435   # andere poort dan normaal, zodat een al draaiende Ollama niet in de weg zit

function Stap([string]$Tekst) { Write-Host ""; Write-Host "==> $Tekst" -ForegroundColor Cyan }
function Info([string]$Tekst) { Write-Host "    $Tekst" }

function Download([string]$Url, [string]$Bestand) {
    if (Test-Path $Bestand) { Info "Al gedownload: $(Split-Path -Leaf $Bestand)"; return }
    $deel = "$Bestand.deel"
    Info "Downloaden: $Url"
    for ($poging = 1; $poging -le 5; $poging++) {
        & curl.exe --location --fail --progress-bar --retry 3 --continue-at - --output $deel $Url
        if ($LASTEXITCODE -eq 0) { Move-Item -Force $deel $Bestand; return }
        Write-Host "    Download onderbroken (code $LASTEXITCODE), poging $poging van 5..." -ForegroundColor Yellow
        Start-Sleep -Seconds 5
    }
    throw "Downloaden mislukt: $Url. Start het script opnieuw; het gaat verder waar het was."
}

function Uitpakken([string]$Zip, [string]$Map) {
    $tijdelijk = "$Map.uitpakken"
    if (Test-Path $tijdelijk) { Remove-Item -Recurse -Force $tijdelijk }
    New-Item -ItemType Directory -Path $tijdelijk | Out-Null
    & tar.exe -xf $Zip -C $tijdelijk
    if ($LASTEXITCODE -ne 0) { throw "Uitpakken mislukt: $Zip" }
    if (Test-Path $Map) { Remove-Item -Recurse -Force $Map }
    Move-Item $tijdelijk $Map
}

Write-Host "De Geest in de Fles - installatie" -ForegroundColor Cyan
Write-Host "Doelmap: $Doel"

# 1. Controle
Stap "Laptop controleren"
& (Join-Path $Bron 'controleer.ps1') -Doel $Doel -Online
if ($LASTEXITCODE -gt 0 -and -not $Ja) {
    $antwoord = Read-Host "Er zijn problemen gevonden. Toch doorgaan? (j/n)"
    if ($antwoord -notmatch '^[jJ]') { exit 1 }
}

New-Item -ItemType Directory -Force -Path $Doel, $Downloads | Out-Null

# 2. Ollama
Stap "Ollama $OllamaVersie"
$arch = if ($env:PROCESSOR_ARCHITEW6432) { $env:PROCESSOR_ARCHITEW6432 } else { $env:PROCESSOR_ARCHITECTURE }
$ollamaZipNaam = if ($arch -eq 'ARM64') { 'ollama-windows-arm64.zip' } else { 'ollama-windows-amd64.zip' }
$ollamaMap = Join-Path $Doel 'ollama'
$ollamaKlaar = Join-Path $ollamaMap "versie-$OllamaVersie.txt"
if (Test-Path $ollamaKlaar) {
    Info "Al geïnstalleerd."
} else {
    $zip = Join-Path $Downloads "ollama-$OllamaVersie-$ollamaZipNaam"
    Download "https://github.com/ollama/ollama/releases/download/v$OllamaVersie/$ollamaZipNaam" $zip
    Info "Uitpakken..."
    Uitpakken $zip $ollamaMap
    Set-Content $ollamaKlaar $ollamaZipNaam
}
if ($AlleenCpu) {
    $gpuMappen = Get-ChildItem (Join-Path $ollamaMap 'lib\ollama') -Directory -ErrorAction SilentlyContinue |
        Where-Object { $_.Name -match '^(cuda|rocm)' }
    foreach ($m in $gpuMappen) { Info "Verwijderen (alleen CPU): $($m.Name)"; Remove-Item -Recurse -Force $m.FullName }
}

# 3. Thonny met Python
Stap "Thonny $ThonnyVersie (met Python)"
$thonnyMap = Join-Path $Doel 'thonny'
$thonnyKlaar = Join-Path $thonnyMap "versie-$ThonnyVersie.txt"
if (Test-Path $thonnyKlaar) {
    Info "Al geïnstalleerd."
} else {
    $zipNaam = "thonny-$ThonnyVersie-windows-portable-x64.zip"
    $zip = Join-Path $Downloads $zipNaam
    Download "https://github.com/thonny/thonny/releases/download/v$ThonnyVersie/$zipNaam" $zip
    Info "Uitpakken..."
    Uitpakken $zip $thonnyMap
    Set-Content $thonnyKlaar 'portable'
}

$pakkettenKlaar = Join-Path $thonnyMap 'geinstalleerde-pakketten.txt'
$pakkettenLijst = $PythonPakketten -join ' '
if ((Test-Path $pakkettenKlaar) -and (Get-Content $pakkettenKlaar -Raw).Trim() -eq $pakkettenLijst) {
    Info "Python-pakketten al geïnstalleerd."
} else {
    Info "Python-pakketten installeren: $($PythonPakketten -join ', ')"
    $env:PYTHONNOUSERSITE = '1'   # niet per ongeluk pakketten van de laptop zelf gebruiken
    & (Join-Path $thonnyMap 'python.exe') -m pip install --no-cache-dir --disable-pip-version-check `
        --no-warn-script-location --quiet @PythonPakketten
    if ($LASTEXITCODE -ne 0) { throw "Installeren van Python-pakketten mislukt." }
    Set-Content $pakkettenKlaar $pakkettenLijst
}

# 3b. Stemmen (Piper, tekst-naar-spraak zonder internet)
Stap "Stemmen: $($Stemmen -join ', ')"
$stemmenMap = Join-Path $Doel 'stemmen'
New-Item -ItemType Directory -Force $stemmenMap | Out-Null
foreach ($stem in $Stemmen) {
    # Naam is taal_REGIO-spreker-kwaliteit, bijvoorbeeld nl_NL-pim-medium
    $delen = $stem -split '-'
    $pad = "$($delen[0].Split('_')[0])/$($delen[0])/$($delen[1])/$($delen[2])/$stem"
    foreach ($ext in '.onnx', '.onnx.json') {
        Download "https://huggingface.co/rhasspy/piper-voices/resolve/$StemmenVersie/$pad$ext" (Join-Path $stemmenMap "$stem$ext")
    }
}

# 4. Startbestanden en code
Stap "Startbestanden en startcode"
Copy-Item -Recurse -Force (Join-Path $Bron 'sjabloon\*') $Doel -Exclude 'code'
Copy-Item -Force (Join-Path $Bron 'controleer.ps1') (Join-Path $Doel 'beheer')
New-Item -ItemType Directory -Force (Join-Path $Doel 'code') | Out-Null
foreach ($bestand in Get-ChildItem (Join-Path $Bron 'sjabloon\code') -File) {
    $bestemming = Join-Path $Doel "code\$($bestand.Name)"
    if (Test-Path $bestemming) { Info "Bestaat al, niet overschreven: code\$($bestand.Name)" }
    else { Copy-Item $bestand.FullName $bestemming }
}

# 5. Modellen
Stap "Taalmodellen: $($Modellen -join ', ')"
$beheer = Join-Path $Doel 'beheer\geest.ps1'
& $beheer -Actie Start -Poort $InstallatiePoort -GeenThonny
try {
    $env:OLLAMA_HOST = "127.0.0.1:$InstallatiePoort"
    $ollamaExe = Join-Path $ollamaMap 'ollama.exe'
    foreach ($model in $Modellen) {
        Info "Model ophalen: $model"
        for ($poging = 1; $poging -le 5; $poging++) {
            & $ollamaExe pull $model
            if ($LASTEXITCODE -eq 0) { break }
            if ($poging -eq 5) { throw "Model $model ophalen mislukt. Start het script opnieuw; het gaat verder waar het was." }
            Write-Host "    Onderbroken, poging $($poging + 1) van 5..." -ForegroundColor Yellow
            Start-Sleep -Seconds 5
        }
    }

    Stap "Testen"
    $test = @{ model = $Modellen[0]; stream = $false; options = @{ temperature = 0; num_predict = 40 }; messages = @(@{ role = 'system'; content = 'Je bent een vriendelijke geest in een fles. Antwoord altijd in het Nederlands, in een korte zin.' }, @{ role = 'user'; content = 'Begroet de kinderen in een korte zin.' }) } | ConvertTo-Json -Depth 5
    $antwoord = Invoke-RestMethod "http://127.0.0.1:$InstallatiePoort/api/chat" -Method Post -Body $test -ContentType 'application/json; charset=utf-8' -TimeoutSec 600
    Info "De geest zegt: $($antwoord.message.content.Trim())"

    $env:PYTHONNOUSERSITE = '1'
    $env:GEEST_TEKST = $antwoord.message.content.Trim()
    $env:GEEST_SPREEK = $(if ($Ja) { 'nee' } else { 'ja' })
    $spreekTest = @'
import os, sys
sys.path.insert(0, sys.argv[1])
import stem
from piper import PiperVoice
assert stem.stemmen(), "geen stemmen gevonden"
tekst = os.environ["GEEST_TEKST"]
if os.environ["GEEST_SPREEK"] == "ja":
    stem.zeg(tekst, stem=stem.stemmen()[0])
else:
    import io, wave
    with wave.open(io.BytesIO(), "wb") as w:
        PiperVoice.load(str(stem.STEMMEN_MAP / (stem.stemmen()[0] + ".onnx"))).synthesize_wav(tekst, w)
print("    Stem werkt.")
'@
    $spreekTest | & (Join-Path $thonnyMap 'python.exe') - (Join-Path $Doel 'code')
    if ($LASTEXITCODE -ne 0) { throw "De stem (Piper) werkt niet." }
} finally {
    & $beheer -Actie Stop
}

# 6. Afronden
@(
    "Geinstalleerd: $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
    "Ollama:  $OllamaVersie ($ollamaZipNaam$(if ($AlleenCpu) { ', alleen CPU' }))"
    "Thonny:  $ThonnyVersie"
    "Python-pakketten: $($PythonPakketten -join ', ')"
    "Modellen: $($Modellen -join ', ')"
    "Stemmen: $($Stemmen -join ', ') (piper-voices $($StemmenVersie.Substring(0, 8)))"
) | Set-Content (Join-Path $Doel 'versies.txt')

if (-not $BewaarDownloads) { Remove-Item -Recurse -Force $Downloads }
Remove-Item -Recurse -Force (Join-Path $Doel 'logs') -ErrorAction SilentlyContinue

$grootte = [math]::Round(((Get-ChildItem $Doel -Recurse -File | Measure-Object Length -Sum).Sum) / 1GB, 1)
Write-Host ""
Write-Host "Klaar! ($grootte GB in $Doel)" -ForegroundColor Green
Write-Host "Dubbelklik start.bat in die map om de geest te wekken."
if (-not $Ja) { Start-Process explorer.exe $Doel }
