<#
.SYNOPSIS
    Beheerscript voor De Geest in de Fles. Wordt aangeroepen door start.bat, stop.bat, enz.
    Werkt met Windows PowerShell 5.1 en PowerShell 7.
#>
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('Start', 'Stop', 'Server', 'Status', 'Kopieer', 'Opruimen')]
    [string]$Actie,
    [int]$Poort = 11434,
    [switch]$GeenThonny
)

$ErrorActionPreference = 'Stop'
$Basis       = Split-Path -Parent $PSScriptRoot
$OllamaExe   = Join-Path $Basis 'ollama\ollama.exe'
$ThonnyExe   = Join-Path $Basis 'thonny\thonny.exe'
$Modellen    = Join-Path $Basis 'modellen'
$Logs        = Join-Path $Basis 'logs'
$StartCode   = Join-Path $Basis 'code\level1_wek_je_geest.py'
if (-not (Test-Path $StartCode)) { $StartCode = Join-Path $Basis 'code\geest.py' }
$OllamaThuis = Join-Path $env:USERPROFILE '.ollama'
$Merkteken   = Join-Path $OllamaThuis 'aangemaakt-door-geest-in-de-fles.txt'

function Schrijf([string]$Tekst, [string]$Kleur = 'Gray') { Write-Host $Tekst -ForegroundColor $Kleur }

function Test-IsOnsPad([string]$Pad) {
    return [bool]$Pad -and $Pad.StartsWith("$Basis\", [StringComparison]::OrdinalIgnoreCase)
}

function Get-OnzeProcessen([string]$Naam) {
    Get-Process -Name $Naam -ErrorAction SilentlyContinue | Where-Object { Test-IsOnsPad $_.Path }
}

function Get-PoortEigenaar([int]$P) {
    $verbinding = Get-NetTCPConnection -LocalPort $P -State Listen -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($verbinding) { Get-Process -Id $verbinding.OwningProcess -ErrorAction SilentlyContinue }
}

function Test-Server([int]$P) {
    try { Invoke-RestMethod "http://127.0.0.1:$P/api/version" -TimeoutSec 2 | Out-Null; return $true } catch { return $false }
}

function Start-Ollama([string]$LuisterAdres, [int]$P) {
    if (-not (Test-Path $OllamaExe)) { throw "Ollama niet gevonden in $OllamaExe. Is de installatie compleet?" }

    $eigenaar = Get-PoortEigenaar $P
    if ($eigenaar) {
        if (Test-IsOnsPad $eigenaar.Path) { Schrijf "Ollama draait al." Green; return }
        throw ("Poort $P is al in gebruik door '$($eigenaar.ProcessName)' ($($eigenaar.Path)).`n" +
               "Waarschijnlijk staat er al een andere Ollama op deze laptop. Sluit die af " +
               "(pictogram rechtsonder bij de klok > Quit) en probeer opnieuw.")
    }

    # Ollama maakt altijd %USERPROFILE%\.ollama aan (ook met OLLAMA_MODELS).
    # Onthoud of wij dat waren, zodat opruimen.bat het netjes kan weghalen.
    if (-not (Test-Path $OllamaThuis)) {
        New-Item -ItemType Directory -Path $OllamaThuis | Out-Null
        Set-Content -Path $Merkteken -Value "Aangemaakt door De Geest in de Fles ($Basis). Mag weg bij opruimen."
    }

    New-Item -ItemType Directory -Path $Logs -Force | Out-Null
    $env:OLLAMA_MODELS = $Modellen
    $env:OLLAMA_HOST   = "${LuisterAdres}:$P"

    Schrijf "Ollama wordt gestart..." Cyan
    Start-Process -FilePath $OllamaExe -ArgumentList 'serve' -WindowStyle Hidden `
        -RedirectStandardError (Join-Path $Logs 'ollama.log') `
        -RedirectStandardOutput (Join-Path $Logs 'ollama-uitvoer.log')

    for ($i = 0; $i -lt 60; $i++) {
        if (Test-Server $P) { Schrijf "Ollama is klaar (poort $P)." Green; return }
        Start-Sleep -Seconds 1
    }
    throw "Ollama reageert niet binnen 60 seconden. Kijk in $Logs\ollama.log."
}

function Stop-Ollama {
    $processen = @(Get-OnzeProcessen 'ollama')
    if ($processen.Count -eq 0) { Schrijf "Ollama draaide niet."; return }
    $processen | Stop-Process -Force
    $processen | Wait-Process -Timeout 10 -ErrorAction SilentlyContinue
    Schrijf "Ollama is gestopt." Green
}

function Get-IpAdressen {
    # Alleen netwerkkaarten met een gateway; dat filtert virtuele adapters (Hyper-V, VPN-stubs) weg.
    Get-NetIPConfiguration -ErrorAction SilentlyContinue |
        Where-Object { $_.IPv4DefaultGateway -and $_.NetAdapter.Status -eq 'Up' } |
        ForEach-Object { $_.IPv4Address.IPAddress }
}

switch ($Actie) {
    'Start' {
        Start-Ollama '127.0.0.1' $Poort
        if (-not $GeenThonny) {
            Schrijf "Thonny wordt gestart..." Cyan
            Start-Process -FilePath $ThonnyExe -ArgumentList "`"$StartCode`""
        }
    }

    'Stop' {
        Stop-Ollama
    }

    'Server' {
        Stop-Ollama
        $env:OLLAMA_NUM_PARALLEL = '4'    # meerdere kinderen tegelijk
        $env:OLLAMA_KEEP_ALIVE   = '-1'   # model blijft de hele les geladen
        Start-Ollama '0.0.0.0' $Poort
        Schrijf ""
        Schrijf "Docent-server draait. Laat de kinderen in code\fles.py deze regel aanpassen:" Yellow
        foreach ($ip in Get-IpAdressen) { Schrijf "    SERVER = `"http://${ip}:$Poort`"" White }
        Schrijf ""
        Schrijf "Krijg je een Windows Firewall-melding? Kies 'Toegang toestaan' (privé netwerk)." Yellow
        Schrijf "Stoppen: dubbelklik stop.bat."
    }

    'Status' {
        Schrijf "Map:    $Basis"
        $versies = Join-Path $Basis 'versies.txt'
        if (Test-Path $versies) { Get-Content $versies | ForEach-Object { Schrijf $_ } }
        $actief = @(Get-OnzeProcessen 'ollama').Count -gt 0
        if ($actief) {
            Schrijf "Ollama: draait" Green
            $env:OLLAMA_HOST = "127.0.0.1:$Poort"
            & $OllamaExe list
        } else {
            Schrijf "Ollama: gestopt" Yellow
        }
    }

    'Kopieer' {
        $doel = Join-Path $env:USERPROFILE 'GeestInDeFles'
        if ($Basis -eq $doel) { Schrijf "Deze map staat al op de laptop; er valt niets te kopiëren." Yellow; break }
        Schrijf "Kopiëren van $Basis naar $doel (dit duurt een paar minuten)..." Cyan
        & robocopy.exe $Basis $doel /E /XD (Join-Path $Basis 'logs') (Join-Path $Basis '_downloads') /NFL /NDL /NJH /NP
        if ($LASTEXITCODE -ge 8) { throw "Kopiëren mislukt (robocopy-code $LASTEXITCODE)." }
        Schrijf "Klaar. Gebruik vanaf nu start.bat in $doel." Green
        Start-Process explorer.exe $doel
        & (Join-Path $doel 'beheer\geest.ps1') -Actie Start
    }

    'Opruimen' {
        Schrijf "Dit verwijdert De Geest in de Fles van deze computer:" Yellow
        Schrijf "    $Basis" White
        if (Test-Path $Merkteken) { Schrijf "    $OllamaThuis" White }
        Schrijf ""
        Schrijf "LET OP: ook alle code in de map 'code' verdwijnt. Kopieer die eerst als je hem wilt bewaren!" Red
        $antwoord = Read-Host "Typ JA om te verwijderen"
        if ($antwoord -cne 'JA') { Schrijf "Niets verwijderd." Green; break }

        Stop-Ollama
        foreach ($naam in 'thonny', 'python', 'pythonw') { Get-OnzeProcessen $naam | Stop-Process -Force }
        Start-Sleep -Seconds 2

        if (Test-Path $Merkteken) { Remove-Item -Recurse -Force $OllamaThuis }
        Set-Location $env:TEMP
        Remove-Item -Recurse -Force $Basis
        Schrijf "Alles is opgeruimd." Green
    }
}
