$ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
$gearDir = "c:\1Work\acebase.cc\static\images\player-config\s1mple\gear"
$skinsDir = "c:\1Work\acebase.cc\static\images\player-config\s1mple\skins"
$staticAvatarDir = "c:\1Work\acebase.cc\static\images\player-config"
New-Item -ItemType Directory -Force -Path $gearDir, $skinsDir | Out-Null
curl.exe -sL -A $ua -H "Referer: https://prosettings.net/players/s1mple/" -o "$staticAvatarDir\s1mple.webp" "https://prosettings.net/wp-content/uploads/s1mple-200x200-fitcontain-q99-gb283-s1.webp"
Write-Output "s1mple.webp: $((Get-Item (Join-Path $staticAvatarDir 's1mple.webp')).Length) bytes"
$items = @(
    @{ file = "monitor.png"; url = "https://prosettings.net/wp-content/uploads/zowie-xl2586x-1-187x187-fitcontain.png" },
    @{ file = "mouse.webp"; url = "https://prosettings.net/wp-content/uploads/logitech-g-pro-x-superlight-2-cyan-187x187-fitcontain.webp" },
    @{ file = "keyboard.png"; url = "https://prosettings.net/wp-content/uploads/logitech-g-pro-x-tkl-keyboard-black-187x187-fitcontain.png" },
    @{ file = "headset.png"; url = "https://prosettings.net/wp-content/uploads/steelseries-arctis-nova-pro-wireless-187x187-fitcontain.png" },
    @{ file = "mousepad.png"; url = "https://prosettings.net/wp-content/uploads/steelseries-qck-performance-speed-187x187-fitcontain.png" },
    @{ file = "earphones.png"; url = "https://prosettings.net/wp-content/uploads/sennheisers-cx-300s-187x187-fitcontain.png" },
    @{ file = "knife.png"; url = "https://prosettings.net/wp-content/uploads/wmo5wx0_icon-187x187.png" },
    @{ file = "gloves.png"; url = "https://prosettings.net/wp-content/uploads/27ema2n_icon-187x187.png" },
    @{ file = "ak47.png"; url = "https://prosettings.net/wp-content/uploads/7cfe7ff6072adf45f56cb4877bcbb565_icon-187x187.png" },
    @{ file = "m4a1s.png"; url = "https://prosettings.net/wp-content/uploads/weapon_m4a1_cu_m4a1_howling_light_png-1-187x187.webp" },
    @{ file = "awp.png"; url = "https://prosettings.net/wp-content/uploads/p6fptza_icon-187x187.png" },
    @{ file = "glock.png"; url = "https://prosettings.net/wp-content/uploads/xrtkjcq_icon-187x187.png" },
    @{ file = "usps.png"; url = "https://prosettings.net/wp-content/uploads/8gs0ilg_icon-187x187.png" },
    @{ file = "deagle.png"; url = "https://prosettings.net/wp-content/uploads/vorrlpj_icon-187x187.png" }
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
