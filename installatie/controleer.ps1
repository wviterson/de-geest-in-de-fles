<#
.SYNOPSIS
    Controleert of deze laptop geschikt is voor De Geest in de Fles.
.PARAMETER Doel
    De map waar de installatie komt (of staat).
.PARAMETER Online
    Controleer ook of de downloadsites bereikbaar zijn (nodig voor installeer.ps1).
.PARAMETER NodigGB
    Benodigde vrije schijfruimte in GB.
.NOTES
    Exitcode = aantal FOUT-meldingen (0 = alles in orde).
#>
param(
    [string]$Doel = (Join-Path $env:USERPROFILE 'GeestInDeFles'),
    [switch]$Online,
    [double]$NodigGB = 9
)

$fouten = 0
function Meld([string]$Status, [string]$Tekst) {
    $kleur = @{ 'OK' = 'Green'; 'LET OP' = 'Yellow'; 'FOUT' = 'Red' }[$Status]
    Write-Host ("[{0,-6}] {1}" -f $Status, $Tekst) -ForegroundColor $kleur
    if ($Status -eq 'FOUT') { $script:fouten++ }
}

Write-Host "Controle voor De Geest in de Fles" -ForegroundColor Cyan
Write-Host ""

# Besturingssysteem en processor
$arch = if ($env:PROCESSOR_ARCHITEW6432) { $env:PROCESSOR_ARCHITEW6432 } else { $env:PROCESSOR_ARCHITECTURE }
$build = [Environment]::OSVersion.Version.Build
if (-not [Environment]::Is64BitOperatingSystem) { Meld 'FOUT' "Windows is 32-bits; Ollama heeft 64-bits Windows nodig." }
elseif ($build -lt 17763) { Meld 'FOUT' "Windows-versie te oud (build $build); Windows 10 1809 of nieuwer nodig." }
else { Meld 'OK' "Windows build $build, processor $arch" }

# Geheugen
$os = Get-CimInstance Win32_OperatingSystem
$totaalGB = [math]::Round((Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory / 1GB, 1)
$vrijGB = [math]::Round($os.FreePhysicalMemory / 1MB, 1)
if ($totaalGB -lt 6) { Meld 'FOUT' "Werkgeheugen $totaalGB GB; minimaal 8 GB aanbevolen. Gebruik de docent-server." }
elseif ($totaalGB -lt 8) { Meld 'LET OP' "Werkgeheugen $totaalGB GB (vrij: $vrijGB GB); dat wordt krap. Sluit andere programma's." }
else { Meld 'OK' "Werkgeheugen $totaalGB GB (vrij: $vrijGB GB)" }

# Schijfruimte en bestandssysteem
$volledigDoel = [IO.Path]::GetFullPath($Doel)
$schijf = [IO.Path]::GetPathRoot($volledigDoel)
try {
    $info = New-Object IO.DriveInfo $schijf
    $vrijeSchijfGB = [math]::Round($info.AvailableFreeSpace / 1GB, 1)
    $nodig = $NodigGB
    if (Test-Path (Join-Path $volledigDoel 'modellen')) { $nodig = 1 }   # al (grotendeels) geïnstalleerd
    if ($vrijeSchijfGB -lt $nodig) { Meld 'FOUT' "Vrije ruimte op $schijf is $vrijeSchijfGB GB; nodig: ongeveer $nodig GB." }
    else { Meld 'OK' "Vrije ruimte op $schijf`: $vrijeSchijfGB GB" }
    if ($info.DriveFormat -eq 'FAT32') {
        Meld 'FOUT' "$schijf is FAT32 (max. 4 GB per bestand). Formatteer de USB-stick als exFAT of NTFS."
    }
    if ($info.DriveType -eq 'Removable') {
        Meld 'LET OP' "$schijf is een USB-stick. Opstarten vanaf de stick werkt, maar is trager dan vanaf de laptop."
    }
} catch {
    Meld 'FOUT' "Kan schijf $schijf niet controleren: $($_.Exception.Message)"
}

# Uitvoeringsbeleid voor scripts (kan door school vastgezet zijn)
$beleid = Get-ExecutionPolicy -List
$vast = $beleid | Where-Object { $_.Scope -in 'MachinePolicy', 'UserPolicy' -and $_.ExecutionPolicy -in 'Restricted', 'AllSigned' }
if ($vast) { Meld 'FOUT' "Scripts zijn door een beheerder geblokkeerd ($($vast[0].Scope) = $($vast[0].ExecutionPolicy)). Vraag de ICT-beheerder of volg de handmatige stappen." }
else { Meld 'OK' "PowerShell-scripts mogen draaien" }

# Benodigde hulpprogramma's van Windows
foreach ($tool in 'curl.exe', 'tar.exe', 'robocopy.exe') {
    if (Get-Command $tool -ErrorAction SilentlyContinue) { Meld 'OK' "$tool aanwezig" }
    else { Meld 'FOUT' "$tool ontbreekt (zit in Windows 10 1803 en nieuwer)." }
}

# Een andere Ollama op deze laptop?
$andereOllama = Get-Command ollama.exe -ErrorAction SilentlyContinue | Where-Object { -not $_.Source.StartsWith($volledigDoel, [StringComparison]::OrdinalIgnoreCase) }
$poort = Get-NetTCPConnection -LocalPort 11434 -State Listen -ErrorAction SilentlyContinue | Select-Object -First 1
if ($poort) {
    $p = Get-Process -Id $poort.OwningProcess -ErrorAction SilentlyContinue
    if ($p.Path -and $p.Path.StartsWith($volledigDoel, [StringComparison]::OrdinalIgnoreCase)) { Meld 'OK' "Onze eigen Ollama draait al" }
    else { Meld 'LET OP' "Poort 11434 is bezet door '$($p.ProcessName)'. Sluit die (andere) Ollama af voor je start.bat gebruikt." }
} elseif ($andereOllama) {
    Meld 'LET OP' "Er staat al een Ollama op deze laptop ($($andereOllama.Source)). Zorg dat die niet draait tijdens de les."
} else {
    Meld 'OK' "Poort 11434 is vrij"
}

# Geluid (de geest praat via Piper; die stemmen staan in de installatiemap zelf)
$geluid = Get-CimInstance Win32_SoundDevice -ErrorAction SilentlyContinue | Where-Object { $_.Status -eq 'OK' }
if ($geluid) { Meld 'OK' "Geluidskaart gevonden" }
else { Meld 'LET OP' "Geen werkende geluidskaart gevonden; de geest kan dan niet hardop praten." }

# Internet (alleen nodig om te installeren)
if ($Online) {
    [Net.ServicePointManager]::SecurityProtocol = [Net.ServicePointManager]::SecurityProtocol -bor [Net.SecurityProtocolType]::Tls12
    foreach ($site in 'https://github.com', 'https://registry.ollama.ai/v2/', 'https://pypi.org/simple/', 'https://huggingface.co') {
        try {
            Invoke-WebRequest $site -Method Head -UseBasicParsing -TimeoutSec 15 | Out-Null
            Meld 'OK' "Bereikbaar: $site"
        } catch {
            $code = $null
            if ($_.Exception.Response) { $code = [int]$_.Exception.Response.StatusCode }
            if ($code) { Meld 'OK' "Bereikbaar: $site" }   # een HTTP-fout betekent wel dat de site bereikbaar is
            else { Meld 'FOUT' "Niet bereikbaar: $site ($($_.Exception.Message)). Gebruik een USB-stick." }
        }
    }
}

Write-Host ""
if ($fouten -eq 0) { Write-Host "Alles in orde." -ForegroundColor Green }
else { Write-Host "$fouten probleem/problemen gevonden." -ForegroundColor Red }
exit $fouten
