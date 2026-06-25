$ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
$gearDir = "c:\1Work\acebase.cc\static\images\player-config\niko\gear"
$skinsDir = "c:\1Work\acebase.cc\static\images\player-config\niko\skins"
$crosshairDir = "c:\1Work\acebase.cc\static\images\player-config\crosshair"
New-Item -ItemType Directory -Force -Path $gearDir, $skinsDir, $crosshairDir | Out-Null

$crosshairBase = "https://prosettings.net/wp-content/plugins/prosettings-customization/assets/cs2-crosshair-images"
foreach ($map in @("inferno","vertigo","anubis","ancient","dust2","mirage","nuke","overpass")) {
    $dest = Join-Path $crosshairDir "$map.jpeg"
    if (-not (Test-Path $dest)) {
        curl.exe -sL -A $ua -o $dest "$crosshairBase/$map.jpeg"
    }
    Write-Output "$map.jpeg: $((Get-Item $dest).Length) bytes"
}

$assetsDir = "c:\1Work\acebase.cc\assets\images\player-config"
$staticAvatarDir = "c:\1Work\acebase.cc\static\images\player-config"
New-Item -ItemType Directory -Force -Path $assetsDir, $staticAvatarDir | Out-Null
curl.exe -sL -A $ua -H "Referer: https://prosettings.net/players/niko/" -o "$assetsDir\niko.webp" "https://prosettings.net/wp-content/uploads/niko-200x200-fitcontain-q99-gb283-s1.png"
Copy-Item "$assetsDir\niko.webp" "$staticAvatarDir\niko.webp" -Force
Write-Output "niko.webp: $((Get-Item "$staticAvatarDir\niko.webp").Length) bytes"

$items = @(
    @{ file = "monitor.png";   url = "https://prosettings.net/wp-content/uploads/zowie-xl2586x-1-187x187-fitcontain.png" },
    @{ file = "mouse.webp";    url = "https://prosettings.net/wp-content/uploads/razer-deathadder-v4-pro-niko-187x187-fitcontain.webp" },
    @{ file = "keyboard.webp"; url = "https://prosettings.net/wp-content/uploads/razer-huntsman-v3-pro-tkl-niko-187x187-fitcontain.webp" },
    @{ file = "headset.webp";  url = "https://prosettings.net/wp-content/uploads/blackshark-v3-pro-niko-187x187-fitcontain.webp" },
    @{ file = "mousepad.png";  url = "https://prosettings.net/wp-content/uploads/artisan-ninja-fx-zero-soft-187x187-fitcontain.png" },
    @{ file = "earphones.png"; url = "https://prosettings.net/wp-content/uploads/linsoul-7hz-timeless-187x187-fitcontain.png" },
    @{ file = "knife.png";     url = "https://prosettings.net/wp-content/uploads/wmo5wx0_icon-187x187.png" },
    @{ file = "gloves.png";    url = "https://prosettings.net/wp-content/uploads/idvtgiv_icon-187x187.png" },
    @{ file = "ak47.png";      url = "https://prosettings.net/wp-content/uploads/hrgbjbx_icon-187x187.png" },
    @{ file = "m4a1s.png";     url = "https://prosettings.net/wp-content/uploads/30o2urp_icon-187x187.png" },
    @{ file = "awp.png";       url = "https://prosettings.net/wp-content/uploads/kaq0wkt_icon-187x187.png" },
    @{ file = "glock.png";     url = "https://prosettings.net/wp-content/uploads/n1gyecn_icon-187x187.png" },
    @{ file = "usps.png";      url = "https://prosettings.net/wp-content/uploads/7qa1htp_icon-187x187.png" },
    @{ file = "deagle.png";    url = "https://prosettings.net/wp-content/uploads/vorrlpj_icon-187x187.png" }
)

foreach ($item in $items) {
    $dir = if ($item.file -match "^(monitor|mouse|keyboard|headset|mousepad|earphones)") { $gearDir } else { $skinsDir }
    $dest = Join-Path $dir $item.file
    curl.exe -sL -A $ua -o $dest $item.url
    Write-Output "$($item.file): $((Get-Item $dest).Length) bytes"
}
