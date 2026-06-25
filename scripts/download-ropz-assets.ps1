$ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
$gearDir = "c:\1Work\acebase.cc\static\images\player-config\ropz\gear"
$skinsDir = "c:\1Work\acebase.cc\static\images\player-config\ropz\skins"
$staticAvatarDir = "c:\1Work\acebase.cc\static\images\player-config"
New-Item -ItemType Directory -Force -Path $gearDir, $skinsDir | Out-Null
curl.exe -sL -A $ua -H "Referer: https://prosettings.net/players/ropz/" -o "$staticAvatarDir\ropz.webp" "https://prosettings.net/wp-content/uploads/ropz-200x200-fitcontain-q99-gb283-s1.png"
Write-Output "ropz.webp: $((Get-Item (Join-Path $staticAvatarDir 'ropz.webp')).Length) bytes"
$items = @(
    @{ file = "monitor.png"; url = "https://prosettings.net/wp-content/uploads/zowie-xl2586x-1-187x187-fitcontain.png" },
    @{ file = "mouse.png"; url = "https://prosettings.net/wp-content/uploads/razer-deathadder-v3-hyperspeed-187x187-fitcontain.png" },
    @{ file = "keyboard.webp"; url = "https://prosettings.net/wp-content/uploads/asus-rog-falchion-ace-75-he-white-187x187-fitcontain.webp" },
    @{ file = "headset.png"; url = "https://prosettings.net/wp-content/uploads/steelseries-arctis-nova-pro-wireless-187x187-fitcontain.png" },
    @{ file = "mousepad.png"; url = "https://prosettings.net/wp-content/uploads/vaxee-pa-black-187x187-fitcontain.png" },
    @{ file = "earphones.png"; url = "https://prosettings.net/wp-content/uploads/razer-hammerhead-pro-v2-187x187-fitcontain.png" },
    @{ file = "knife.png"; url = "https://prosettings.net/wp-content/uploads/jgh4gjf_icon-187x187.png" },
    @{ file = "gloves.png"; url = "https://prosettings.net/wp-content/uploads/idvtgiv_icon-187x187.png" },
    @{ file = "ak47.png"; url = "https://prosettings.net/wp-content/uploads/e0mvffd_icon-187x187.png" },
    @{ file = "m4a1s.png"; url = "https://prosettings.net/wp-content/uploads/dl1xv17_icon-187x187.png" },
    @{ file = "awp.png"; url = "https://prosettings.net/wp-content/uploads/n1gyecn_icon-187x187.png" },
    @{ file = "glock.png"; url = "https://prosettings.net/wp-content/uploads/8gs0ilg_icon-187x187.png" },
    @{ file = "usps.png"; url = "https://prosettings.net/wp-content/uploads/vorrlpj_icon-187x187.png" }
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
