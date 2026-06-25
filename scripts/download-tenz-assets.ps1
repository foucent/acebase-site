$ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
$gearDir = "c:\1Work\acebase.cc\static\images\player-config\tenz\gear"
$skinsDir = "c:\1Work\acebase.cc\static\images\player-config\tenz\skins"
$staticAvatarDir = "c:\1Work\acebase.cc\static\images\player-config"
New-Item -ItemType Directory -Force -Path $gearDir, $skinsDir | Out-Null
curl.exe -sL -A $ua -H "Referer: https://prosettings.net/players/tenz/" -o "$staticAvatarDir\tenz.webp" "https://prosettings.net/wp-content/uploads/tenz-200x200-fitcontain-q99-gb283-s1.png"
Write-Output "tenz.webp: $((Get-Item (Join-Path $staticAvatarDir 'tenz.webp')).Length) bytes"
$items = @(
    @{ file = "monitor.png"; url = "https://prosettings.net/wp-content/uploads/sony-inzone-m10s-187x187-fitcontain.png" },
    @{ file = "mouse.png"; url = "https://prosettings.net/wp-content/uploads/pulsar-tenz-187x187-fitcontain.png" },
    @{ file = "keyboard.webp"; url = "https://prosettings.net/wp-content/uploads/wooting-80he-tenz-187x187-fitcontain.webp" },
    @{ file = "headset.webp"; url = "https://prosettings.net/wp-content/uploads/sony-inzone-h9-ii-187x187-fitcontain.webp" },
    @{ file = "mousepad.png"; url = "https://prosettings.net/wp-content/uploads/artisan-ninja-fx-zero-xsoft-187x187-fitcontain.png" },
    @{ file = "earphones.png"; url = "https://prosettings.net/wp-content/uploads/sony-inzone-e9-187x187-fitcontain.webp" }
)
foreach ($item in $items) {
    $dir = if ($item.file -match "^(monitor|mouse|keyboard|headset|mousepad|earphones)") { $gearDir } else { $skinsDir }
    $dest = Join-Path $dir $item.file
    curl.exe -sL -A $ua -o $dest $item.url
    Write-Output "$($item.file): $((Get-Item $dest).Length) bytes"
}
$crosshairDir = "c:\1Work\acebase.cc\static\images\player-config\crosshair"
New-Item -ItemType Directory -Force -Path $crosshairDir | Out-Null
$crosshairBase = "https://prosettings.net/wp-content/plugins/prosettings-customization/assets/cs2-crosshair-images"
foreach ($map in @("inferno","vertigo","anubis","ancient","dust2","mirage","nuke","overpass")) {
    $dest = Join-Path $crosshairDir "$map.jpeg"
    if (-not (Test-Path $dest)) { curl.exe -sL -A $ua -o $dest "$crosshairBase/$map.jpeg" }
}
