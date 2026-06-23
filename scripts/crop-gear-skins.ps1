Add-Type -AssemblyName System.Drawing

function Save-Crop($src, $x, $y, $w, $h, $dest) {
    $img = [System.Drawing.Image]::FromFile($src)
    $bmp = New-Object System.Drawing.Bitmap $w, $h
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $rect = New-Object System.Drawing.Rectangle $x, $y, $w, $h
    $g.DrawImage($img, 0, 0, $rect, [System.Drawing.GraphicsUnit]::Pixel)
    $dir = Split-Path $dest -Parent
    if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Force -Path $dir | Out-Null }
    $bmp.Save($dest, [System.Drawing.Imaging.ImageFormat]::Png)
    $g.Dispose(); $bmp.Dispose(); $img.Dispose()
}

$gearSrc = "c:\1Work\acebase.cc\model\ScreenShot_2026-06-23_160402_476.png"
$skinsSrc = "c:\1Work\acebase.cc\model\ScreenShot_2026-06-23_160443_572.png"
$gearOut = "c:\1Work\acebase.cc\static\images\player-config\gear"
$skinsOut = "c:\1Work\acebase.cc\static\images\player-config\skins"

# Gear grid: 4 + 2 layout (1002x717 source)
$gw = 230; $gh = 150; $gap = 16; $mx = 24; $y1 = 98; $y2 = 318
$gearCrops = @(
    @{ name = "monitor.png";   x = $mx;              y = $y1 },
    @{ name = "mouse.png";     x = $mx + ($gw+$gap); y = $y1 },
    @{ name = "keyboard.png";   x = $mx + 2*($gw+$gap); y = $y1 },
    @{ name = "headset.png";   x = $mx + 3*($gw+$gap); y = $y1 },
    @{ name = "mousepad.png";  x = $mx;              y = $y2 },
    @{ name = "earphones.png";  x = $mx + ($gw+$gap); y = $y2 }
)
foreach ($c in $gearCrops) {
    Save-Crop $gearSrc $c.x $c.y $gw $gh (Join-Path $gearOut $c.name)
}

# Skins grid: 4x2 (1027x776 source)
$sw = 232; $sh = 170; $sgap = 16; $smx = 24; $sy1 = 128; $sy2 = 358
$skinNames = @(
    "knife.png", "gloves.png", "ak47.png", "m4a1s.png",
    "awp.png", "glock.png", "usps.png", "deagle.png"
)
for ($i = 0; $i -lt 8; $i++) {
    $col = $i % 4
    $row = [math]::Floor($i / 4)
    $x = $smx + $col * ($sw + $sgap)
    $y = if ($row -eq 0) { $sy1 } else { $sy2 }
    Save-Crop $skinsSrc $x $y $sw $sh (Join-Path $skinsOut $skinNames[$i])
}

Write-Output "Done: gear $($gearCrops.Count) skins $($skinNames.Count)"
