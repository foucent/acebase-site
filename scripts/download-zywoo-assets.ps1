$ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
$gearDir = "c:\1Work\acebase.cc\static\images\player-config\zywoo\gear"
$skinsDir = "c:\1Work\acebase.cc\static\images\player-config\zywoo\skins"
$staticAvatarDir = "c:\1Work\acebase.cc\static\images\player-config"
New-Item -ItemType Directory -Force -Path $gearDir, $skinsDir | Out-Null
curl.exe -sL -A $ua -H "Referer: https://prosettings.net/players/zywoo/" -o "$staticAvatarDir\zywoo.webp" "https://prosettings.net/wp-content/uploads/zywoo-200x200-fitcontain-q99-gb283-s1.png"
Write-Output "zywoo.webp: $((Get-Item (Join-Path $staticAvatarDir 'zywoo.webp')).Length) bytes"
$items = @(
    @{ file = "monitor.png"; url = "https://prosettings.net/wp-content/uploads/zowie-xl2586x-1-187x187-fitcontain.png" },
    @{ file = "mouse.webp"; url = "https://prosettings.net/wp-content/uploads/pulsar-zywoo-the-chosen-one-gen.2-pink-187x187-fitcontain.webp" },
    @{ file = "keyboard.webp"; url = "https://prosettings.net/wp-content/uploads/asus-rog-falchion-ace-hfx-zywoo-edition-187x187-fitcontain.webp" },
    @{ file = "headset.png"; url = "https://prosettings.net/wp-content/uploads/steelseries-arctis-nova-pro-187x187-fitcontain.png" },
    @{ file = "mousepad.png"; url = "https://prosettings.net/wp-content/uploads/the-chosen-mousepad-187x187-fitcontain.png" },
    @{ file = "earphones.png"; url = "https://prosettings.net/wp-content/uploads/acezone-iems-187x187-fitcontain.webp" },
    @{ file = "knife.png"; url = "https://prosettings.net/wp-content/uploads/mzql5au_icon-187x187.png" },
    @{ file = "gloves.png"; url = "https://prosettings.net/wp-content/uploads/idvtgiv_icon-187x187.png" },
    @{ file = "ak47.png"; url = "https://prosettings.net/wp-content/uploads/w3ts71d_icon-187x187.png" },
    @{ file = "m4a1s.png"; url = "https://prosettings.net/wp-content/uploads/30o2urp_icon-187x187.png" },
    @{ file = "awp.png"; url = "https://prosettings.net/wp-content/uploads/kaq0wkt_icon-187x187.png" },
    @{ file = "glock.png"; url = "https://prosettings.net/wp-content/uploads/n1gyecn_icon-187x187.png" },
    @{ file = "usps.png"; url = "https://prosettings.net/wp-content/uploads/8gs0ilg_icon-187x187.png" },
    @{ file = "deagle.png"; url = "https://prosettings.net/wp-content/uploads/bw37suq_icon-187x187.png" }
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
