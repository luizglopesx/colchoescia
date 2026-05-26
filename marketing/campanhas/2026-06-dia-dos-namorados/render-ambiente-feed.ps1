$ErrorActionPreference = "Stop"
Add-Type -AssemblyName System.Drawing

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = Resolve-Path (Join-Path $root "..\..\..")
$outDir = Join-Path $root "aprovacao"
New-Item -ItemType Directory -Force -Path $outDir | Out-Null

$logoPath = Join-Path $projectRoot "identidade\Logo Cc fundo Transparente.png"
$productPath = Join-Path $projectRoot "marketing\Cj Box Prime.png"
$outPath = Join-Path $outDir "peca-feed-ambiente-cama-box-casal.png"

$blue = [System.Drawing.ColorTranslator]::FromHtml("#0064A6")
$cyan = [System.Drawing.ColorTranslator]::FromHtml("#00AFEF")
$navy = [System.Drawing.ColorTranslator]::FromHtml("#071B3D")
$deep = [System.Drawing.ColorTranslator]::FromHtml("#031126")
$white = [System.Drawing.Color]::White
$offWhite = [System.Drawing.ColorTranslator]::FromHtml("#F7FBFF")
$wood1 = [System.Drawing.ColorTranslator]::FromHtml("#8A4F2A")
$wood2 = [System.Drawing.ColorTranslator]::FromHtml("#C07A3E")
$wood3 = [System.Drawing.ColorTranslator]::FromHtml("#5F321A")
$green = [System.Drawing.ColorTranslator]::FromHtml("#16B84E")
$yellow = [System.Drawing.ColorTranslator]::FromHtml("#FFE45C")
$ink = [System.Drawing.ColorTranslator]::FromHtml("#1E1E1E")
$purple = [System.Drawing.ColorTranslator]::FromHtml("#5A28E8")

function Font($size, $style = [System.Drawing.FontStyle]::Regular) {
  try { return [System.Drawing.Font]::new("Arial Rounded MT Bold", $size, $style, [System.Drawing.GraphicsUnit]::Pixel) }
  catch { return [System.Drawing.Font]::new("Arial", $size, $style, [System.Drawing.GraphicsUnit]::Pixel) }
}

function Brush($color) { return [System.Drawing.SolidBrush]::new($color) }

function RoundRect($g, $brush, $x, $y, $w, $h, $r) {
  $path = [System.Drawing.Drawing2D.GraphicsPath]::new()
  $d = $r * 2
  $path.AddArc($x, $y, $d, $d, 180, 90)
  $path.AddArc($x + $w - $d, $y, $d, $d, 270, 90)
  $path.AddArc($x + $w - $d, $y + $h - $d, $d, $d, 0, 90)
  $path.AddArc($x, $y + $h - $d, $d, $d, 90, 90)
  $path.CloseFigure()
  $g.FillPath($brush, $path)
  $path.Dispose()
}

function Text($g, $text, $font, $brush, $x, $y, $w, $h, $align = "Near", $valign = "Near") {
  $sf = [System.Drawing.StringFormat]::new()
  $sf.Alignment = [System.Drawing.StringAlignment]::$align
  $sf.LineAlignment = [System.Drawing.StringAlignment]::$valign
  $sf.Trimming = [System.Drawing.StringTrimming]::Word
  $rect = [System.Drawing.RectangleF]::new([float]$x, [float]$y, [float]$w, [float]$h)
  $g.DrawString([string]$text, $font, $brush, $rect, $sf)
  $sf.Dispose()
}

function Bounds($img) {
  $minX = $img.Width; $minY = $img.Height; $maxX = 0; $maxY = 0
  for ($yy = 0; $yy -lt $img.Height; $yy++) {
    for ($xx = 0; $xx -lt $img.Width; $xx++) {
      if ($img.GetPixel($xx, $yy).A -gt 8) {
        if ($xx -lt $minX) { $minX = $xx }
        if ($yy -lt $minY) { $minY = $yy }
        if ($xx -gt $maxX) { $maxX = $xx }
        if ($yy -gt $maxY) { $maxY = $yy }
      }
    }
  }
  return [System.Drawing.Rectangle]::new($minX, $minY, $maxX - $minX + 1, $maxY - $minY + 1)
}

function DrawFit($g, $img, $src, $x, $y, $w, $h) {
  $scale = [Math]::Min($w / $src.Width, $h / $src.Height)
  $dw = [int]($src.Width * $scale)
  $dh = [int]($src.Height * $scale)
  $dx = [int]($x + (($w - $dw) / 2))
  $dy = [int]($y + (($h - $dh) / 2))
  $dest = [System.Drawing.Rectangle]::new($dx, $dy, $dw, $dh)
  $g.DrawImage($img, $dest, $src, [System.Drawing.GraphicsUnit]::Pixel)
}

function DrawPlant($g, $x, $y, $scale) {
  $pot = Brush ([System.Drawing.ColorTranslator]::FromHtml("#1F1F1F"))
  $leaf1 = Brush ([System.Drawing.ColorTranslator]::FromHtml("#0A6A35"))
  $leaf2 = Brush ([System.Drawing.ColorTranslator]::FromHtml("#118A45"))
  RoundRect $g $pot $x ($y + [int](210*$scale)) ([int](112*$scale)) ([int](92*$scale)) ([int](24*$scale))
  for ($i = 0; $i -lt 16; $i++) {
    $angle = ($i * 22) * [Math]::PI / 180
    $lx = $x + [int](52*$scale) + [int]([Math]::Cos($angle) * 52*$scale)
    $ly = $y + [int](120*$scale) + [int]([Math]::Sin($angle) * 62*$scale)
    $brush = if ($i % 2 -eq 0) { $leaf1 } else { $leaf2 }
    $g.FillEllipse($brush, $lx, $ly, [int](72*$scale), [int](34*$scale))
  }
  $pot.Dispose(); $leaf1.Dispose(); $leaf2.Dispose()
}

function DrawLamp($g, $x, $y) {
  $cord = [System.Drawing.Pen]::new([System.Drawing.Color]::FromArgb(190, 30, 22, 15), 5)
  $light = Brush ([System.Drawing.Color]::FromArgb(235, 255, 238, 194))
  $glow = Brush ([System.Drawing.Color]::FromArgb(60, 255, 225, 160))
  $g.DrawLine($cord, $x + 32, 0, $x + 32, $y)
  $g.FillEllipse($glow, $x - 35, $y - 28, 135, 135)
  $g.FillEllipse($light, $x, $y, 64, 64)
  $cord.Dispose(); $light.Dispose(); $glow.Dispose()
}

$w = 1080
$h = 1350
$bmp = [System.Drawing.Bitmap]::new($w, $h)
$g = [System.Drawing.Graphics]::FromImage($bmp)
$g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$g.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit

$logo = [System.Drawing.Image]::FromFile($logoPath)
$product = [System.Drawing.Image]::FromFile($productPath)
$logoBounds = Bounds $logo
$productBounds = Bounds $product

try {
  $whiteBrush = Brush $white
  $blueBrush = Brush $blue
  $cyanBrush = Brush $cyan
  $navyBrush = Brush $navy
  $deepBrush = Brush $deep
  $inkBrush = Brush $ink
  $yellowBrush = Brush $yellow
  $greenBrush = Brush $green

  $sky = [System.Drawing.Drawing2D.LinearGradientBrush]::new([System.Drawing.Rectangle]::new(0,0,$w,$h), [System.Drawing.ColorTranslator]::FromHtml("#F8FBFF"), [System.Drawing.ColorTranslator]::FromHtml("#E8F2F8"), 90)
  $g.FillRectangle($sky, 0, 0, $w, $h)

  # Left white offer area, like the reference banners, but adapted to feed.
  $g.FillRectangle($whiteBrush, 0, 0, 390, $h)

  # Warm bedroom environment.
  $woodGrad = [System.Drawing.Drawing2D.LinearGradientBrush]::new([System.Drawing.Rectangle]::new(350,0,730,820), $wood2, $wood1, 0)
  $g.FillRectangle($woodGrad, 350, 0, 730, 820)
  for ($x = 365; $x -lt 1080; $x += 38) {
    $penDark = [System.Drawing.Pen]::new([System.Drawing.Color]::FromArgb(110, 60, 28, 12), 3)
    $penLight = [System.Drawing.Pen]::new([System.Drawing.Color]::FromArgb(70, 255, 220, 150), 2)
    $g.DrawLine($penDark, $x, 0, $x, 820)
    $g.DrawLine($penLight, $x + 8, 0, $x + 8, 820)
    $penDark.Dispose(); $penLight.Dispose()
  }

  $curtain = [System.Drawing.Drawing2D.LinearGradientBrush]::new([System.Drawing.Rectangle]::new(300,0,96,820), [System.Drawing.Color]::FromArgb(250,255,255,255), [System.Drawing.Color]::FromArgb(130,255,255,255), 0)
  $g.FillRectangle($curtain, 300, 0, 96, 820)
  for ($x = 310; $x -lt 392; $x += 18) {
    $p = [System.Drawing.Pen]::new([System.Drawing.Color]::FromArgb(55, 170, 190, 210), 2)
    $g.DrawLine($p, $x, 0, $x + 20, 820)
    $p.Dispose()
  }

  DrawLamp $g 505 96
  DrawLamp $g 865 118
  DrawPlant $g 900 310 1.08

  # Floor and rug.
  $floor = [System.Drawing.Drawing2D.LinearGradientBrush]::new([System.Drawing.Rectangle]::new(350,760,730,590), [System.Drawing.ColorTranslator]::FromHtml("#D7B590"), [System.Drawing.ColorTranslator]::FromHtml("#9A6135"), 90)
  $g.FillRectangle($floor, 350, 760, 730, 590)
  $rug = Brush ([System.Drawing.Color]::FromArgb(230, 232, 232, 228))
  $g.FillEllipse($rug, 365, 790, 680, 310)

  # Blue side curve gives brand ownership without losing the bedroom.
  $brandCurve = Brush ([System.Drawing.Color]::FromArgb(240, 0, 100, 166))
  $g.FillPie($brandCurve, -500, -160, 920, 1660, 270, 180)
  $g.FillRectangle($whiteBrush, 0, 0, 335, $h)

  # Logo.
  RoundRect $g $whiteBrush 46 46 285 96 24
  DrawFit $g $logo $logoBounds 68 60 242 68

  # Product inserted in the room.
  $shadow = Brush ([System.Drawing.Color]::FromArgb(105, 0, 0, 0))
  $g.FillEllipse($shadow, 390, 798, 620, 112)
  DrawFit $g $product $productBounds 335 485 720 430

  # Main copy on left.
  Text $g "CAMA BOX CASAL" (Font 42 ([System.Drawing.FontStyle]::Bold)) $navyBrush 42 188 310 110
  Text $g "MOLAS" (Font 86 ([System.Drawing.FontStyle]::Bold)) $navyBrush 42 322 300 108
  Text $g "ENSACADAS" (Font 38 ([System.Drawing.FontStyle]::Bold)) $navyBrush 42 438 315 72

  RoundRect $g $yellowBrush 42 542 270 66 20
  Text $g "DIA DOS NAMORADOS" (Font 22 ([System.Drawing.FontStyle]::Bold)) $inkBrush 42 542 270 66 "Center" "Center"

  # Price offer block.
  $priceGrad = [System.Drawing.Drawing2D.LinearGradientBrush]::new([System.Drawing.Rectangle]::new(455, 900, 570, 210), $blue, $purple, 0)
  RoundRect $g $priceGrad 455 900 570 210 28
  Text $g "R$" (Font 38 ([System.Drawing.FontStyle]::Bold)) $whiteBrush 488 930 92 58
  Text $g "1.590,00" (Font 88 ([System.Drawing.FontStyle]::Bold)) $whiteBrush 560 925 430 102 "Far"
  Text $g "EM ATE 12X S/ JUROS" (Font 34 ([System.Drawing.FontStyle]::Bold)) $whiteBrush 492 1030 500 56 "Center" "Center"

  RoundRect $g $greenBrush 455 1140 570 86 28
  Text $g "Chama no WhatsApp" (Font 42 ([System.Drawing.FontStyle]::Bold)) $whiteBrush 455 1140 570 86 "Center" "Center"

  Text $g "Pensou colchao," (Font 24 ([System.Drawing.FontStyle]::Bold)) $navyBrush 46 1252 290 34
  Text $g "Colchoes e Cia" (Font 24 ([System.Drawing.FontStyle]::Bold)) $navyBrush 46 1286 290 34

  $bmp.Save($outPath, [System.Drawing.Imaging.ImageFormat]::Png)

  $whiteBrush.Dispose(); $blueBrush.Dispose(); $cyanBrush.Dispose(); $navyBrush.Dispose(); $deepBrush.Dispose(); $inkBrush.Dispose(); $yellowBrush.Dispose(); $greenBrush.Dispose()
  $sky.Dispose(); $woodGrad.Dispose(); $curtain.Dispose(); $floor.Dispose(); $rug.Dispose(); $brandCurve.Dispose(); $shadow.Dispose(); $priceGrad.Dispose()
}
finally {
  $logo.Dispose()
  $product.Dispose()
  $g.Dispose()
  $bmp.Dispose()
}

Write-Host $outPath
