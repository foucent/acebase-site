$ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
$gearDir = "c:\1Work\acebase.cc\static\images\player-config\gear"
$skinsDir = "c:\1Work\acebase.cc\static\images\player-config\skins"
$crosshairDir = "c:\1Work\acebase.cc\static\images\player-config\crosshair"
New-Item -ItemType Directory -Force -Path $gearDir, $skinsDir, $crosshairDir | Out-Null

$crosshairBase = "https://prosettings.net/wp-content/plugins/prosettings-customization/assets/cs2-crosshair-images"
foreach ($map in @("inferno","vertigo","anubis","ancient","dust2","mirage","nuke","overpass")) {
    $dest = Join-Path $crosshairDir "$map.jpeg"
    curl.exe -sL -A $ua -o $dest "$crosshairBase/$map.jpeg"
    Write-Output "$map.jpeg: $((Get-Item $dest).Length) bytes"
}

$assetsDir = "c:\1Work\acebase.cc\assets\images\player-config"
New-Item -ItemType Directory -Force -Path $assetsDir | Out-Null
curl.exe -sL -A $ua -H "Referer: https://prosettings.net/players/donk/" -o "$assetsDir\donk.webp" "https://prosettings.net/wp-content/uploads/donk-200x200-2x-fitcontain-q99-gb283-s1.webp"
Write-Output "donk.webp: $((Get-Item "$assetsDir\donk.webp").Length) bytes"

$items = @(
    @{ file = "monitor.png";   url = "https://prosettings.net/wp-content/uploads/zowie-xl2586x-1-187x187-fitcontain.png" },
    @{ file = "mouse.png";     url = "https://prosettings.net/wp-content/uploads/zowie-187x187-fitcontain.png" },
    @{ file = "keyboard.png";  url = "https://prosettings.net/wp-content/uploads/logitech-g-pro-x-keyboard-187x187-fitcontain.png" },
    @{ file = "headset.png";   url = "https://prosettings.net/wp-content/uploads/hyperx-cloud-ii-187x187-fitcontain.png" },
    @{ file = "mousepad.png";  url = "https://prosettings.net/wp-content/uploads/steelseries-qck-large-187x187-fitcontain.png" },
    @{ file = "earphones.png"; url = "https://prosettings.net/wp-content/uploads/shure-se215-187x187-fitcontain.png" },
    @{ file = "knife.png";     url = "https://prosettings.net/wp-content/uploads/wmo5wx0_icon-187x187.png" },
    @{ file = "gloves.png";    url = "https://prosettings.net/wp-content/uploads/idvtgiv_icon-187x187.png" },
    @{ file = "ak47.png";      url = "https://prosettings.net/wp-content/uploads/hrgbjbx_icon-187x187.png" },
    @{ file = "m4a1s.png";     url = "https://prosettings.net/wp-content/uploads/qzstzrg_icon-187x187.png" },
    @{ file = "awp.png";       url = "https://prosettings.net/wp-content/uploads/p6fptza_icon-187x187.png" },
    @{ file = "glock.png";     url = "https://prosettings.net/wp-content/uploads/n1gyecn_icon-187x187.png" },
    @{ file = "usps.png";      url = "https://prosettings.net/wp-content/uploads/8gs0ilg_icon-187x187.png" },
    @{ file = "deagle.png";    url = "https://prosettings.net/wp-content/uploads/vorrlpj_icon-187x187.png" }
)

foreach ($item in $items) {
    $dir = if ($item.file -match "^(monitor|mouse|keyboard|headset|mousepad|earphones)") { $gearDir } else { $skinsDir }
    $dest = Join-Path $dir $item.file
    curl.exe -sL -A $ua -o $dest $item.url
    $size = (Get-Item $dest).Length
    Write-Output "$($item.file): $size bytes"
}
