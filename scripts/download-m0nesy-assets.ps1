$ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
$gearDir = "c:\1Work\acebase.cc\static\images\player-config\m0nesy\gear"
$skinsDir = "c:\1Work\acebase.cc\static\images\player-config\m0nesy\skins"
New-Item -ItemType Directory -Force -Path $gearDir, $skinsDir | Out-Null

$assetsDir = "c:\1Work\acebase.cc\assets\images\player-config"
$staticAvatarDir = "c:\1Work\acebase.cc\static\images\player-config"
New-Item -ItemType Directory -Force -Path $assetsDir, $staticAvatarDir | Out-Null
curl.exe -sL -A $ua -H "Referer: https://prosettings.net/players/m0nesy/" -o "$assetsDir\m0nesy.webp" "https://prosettings.net/wp-content/uploads/m0nesy-200x200-fitcontain-q99-gb283-s1.png"
Copy-Item "$assetsDir\m0nesy.webp" "$staticAvatarDir\m0nesy.webp" -Force
Write-Output "m0nesy.webp: $((Get-Item "$staticAvatarDir\m0nesy.webp").Length) bytes"

$items = @(
    @{ file = "monitor.png";   url = "https://prosettings.net/wp-content/uploads/zowie-xl2586x-1-187x187-fitcontain.png" },
    @{ file = "mouse.png";     url = "https://prosettings.net/wp-content/uploads/logitech-g-pro-x-superlight-white-187x187-fitcontain.png" },
    @{ file = "keyboard.png";  url = "https://prosettings.net/wp-content/uploads/logitech-g-pro-x-tkl-rapid-white-187x187-fitcontain.png" },
    @{ file = "headset.png";   url = "https://prosettings.net/wp-content/uploads/logitech-g-pro-x-wired-187x187-fitcontain.png" },
    @{ file = "mousepad.png";  url = "https://prosettings.net/wp-content/uploads/steelseries-qck-heavy-187x187-fitcontain.png" },
    @{ file = "earphones.png"; url = "https://prosettings.net/wp-content/uploads/logitech-g333-white-187x187-fitcontain.png" },
    @{ file = "knife.png";     url = "https://prosettings.net/wp-content/uploads/p5r1zlv_icon-187x187.png" },
    @{ file = "gloves.png";    url = "https://prosettings.net/wp-content/uploads/gzsnrq3_icon-187x187.png" },
    @{ file = "ak47.png";      url = "https://prosettings.net/wp-content/uploads/0ydbjvf_icon-187x187.png" },
    @{ file = "m4a1s.png";     url = "https://prosettings.net/wp-content/uploads/aolnzaa_icon-187x187.png" },
    @{ file = "awp.png";       url = "https://prosettings.net/wp-content/uploads/hvdbvkh_icon-187x187.png" },
    @{ file = "glock.png";     url = "https://prosettings.net/wp-content/uploads/wky3gzm_icon-187x187.png" },
    @{ file = "usps.png";      url = "https://prosettings.net/wp-content/uploads/ebq4nxt_icon-187x187.png" },
    @{ file = "deagle.png";    url = "https://prosettings.net/wp-content/uploads/vpvoak8_icon-187x187.png" }
)

foreach ($item in $items) {
    $dir = if ($item.file -match "^(monitor|mouse|keyboard|headset|mousepad|earphones)") { $gearDir } else { $skinsDir }
    $dest = Join-Path $dir $item.file
    curl.exe -sL -A $ua -o $dest $item.url
    Write-Output "$($item.file): $((Get-Item $dest).Length) bytes"
}
