$ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
$gearDir = "c:\1Work\acebase.cc\static\images\player-config\aspas\gear"
$skinsDir = "c:\1Work\acebase.cc\static\images\player-config\aspas\skins"
$staticAvatarDir = "c:\1Work\acebase.cc\static\images\player-config"
New-Item -ItemType Directory -Force -Path $gearDir, $skinsDir | Out-Null
curl.exe -sL -A $ua -H "Referer: https://prosettings.net/players/aspas/" -o "$staticAvatarDir\aspas.webp" "https://prosettings.net/wp-content/uploads/aspas-200x200-fitcontain-q99-gb283-s1.png"
Write-Output "aspas.webp: $((Get-Item (Join-Path $staticAvatarDir 'aspas.webp')).Length) bytes"
$items = @(
    @{ file = "monitor.png"; url = "https://prosettings.net/wp-content/uploads/zowie-xl2586x-187x187-fitcontain.png" },
    @{ file = "mouse.png"; url = "https://prosettings.net/wp-content/uploads/logitech-g-pro-x-superlight-white-187x187-fitcontain.png" },
    @{ file = "keyboard.webp"; url = "https://prosettings.net/wp-content/uploads/atk-rs6-aspas-187x187-fitcontain.webp" },
    @{ file = "headset.webp"; url = "https://prosettings.net/wp-content/uploads/razer-blackshark-v3-pro-187x187-fitcontain.webp" },
    @{ file = "mousepad.png"; url = "https://prosettings.net/wp-content/uploads/vaxee-pa-black-187x187-fitcontain.png" }
)
foreach ($item in $items) {
    $dir = if ($item.file -match "^(monitor|mouse|keyboard|headset|mousepad|earphones)") { $gearDir } else { $skinsDir }
    $dest = Join-Path $dir $item.file
    curl.exe -sL -A $ua -o $dest $item.url
    Write-Output "$($item.file): $((Get-Item $dest).Length) bytes"
}
$vDir = "c:\1Work\acebase.cc\static\images\player-config\crosshair-val"
New-Item -ItemType Directory -Force -Path $vDir | Out-Null
$vBase = "https://prosettings.net/wp-content/plugins/prosettings-customization/assets/valorant-crosshair-images"
foreach ($m in @("valorant-ascent.jpg","valorant-boatie.jpeg","valorant-breeze.jpg","valorant-ice.jpg","valorant-pearl.jpg","valorant-sunset.jpg")) {
    curl.exe -sL -A $ua -o (Join-Path $vDir $m) "$vBase/$m"
}
