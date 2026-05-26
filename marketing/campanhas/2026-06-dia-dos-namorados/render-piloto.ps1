$ErrorActionPreference = "Stop"
Add-Type -AssemblyName System.Drawing

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = Resolve-Path (Join-Path $root "..\..\..")
$outDir = Join-Path $root "aprovacao"
$bgPath = Join-Path $root "quarto_namorados.png"
New-Item -ItemType Directory -Force -Path $outDir | Out-Null

$logoPath = Join-Path $projectRoot "identidade\Logo Cc fundo Transparente.png"
$outPath = Join-Path $outDir "piloto-cama-box-molas-ensacadas-feed.png"

$blue = [System.Drawing.ColorTranslator]::FromHtml("#0064A6")
$cyan = [System.Drawing.ColorTranslator]::FromHtml("#00AFEF")
$navy = [System.Drawing.ColorTranslator]::FromHtml("#062B49")
$deep = [System.Drawing.ColorTranslator]::FromHtml("#03192B")
$white = [System.Drawing.Color]::White
$yellow = [System.Drawing.ColorTranslator]::FromHtml("#FFE45C")
$green = [System.Drawing.ColorTranslator]::FromHtml("#16B84E")
$ink = [System.Drawing.ColorTranslator]::FromHtml("#1E1E1E")
$soft = [System.Drawing.ColorTranslator]::FromHtml("#EAF7FF")

$gradStart = [System.Drawing.ColorTranslator]::FromHtml("#0048FE")
$gradEnd = [System.Drawing.ColorTranslator]::FromHtml("#7E00FF")

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

function ShadowText($g, $text, $font, $brush, $x, $y, $w, $h, $align = "Near", $valign = "Near") {
  $shadowBrush = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::FromArgb(140, 0, 10, 20))
  Text $g $text $font $shadowBrush ($x + 3) ($y + 3) $w $h $align $valign
  Text $g $text $font $brush $x $y $w $h $align $valign
  $shadowBrush.Dispose()
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

function DrawFitCover($g, $img, $src, $x, $y, $w, $h) {
  $scaleX = $w / $src.Width
  $scaleY = $h / $src.Height
  $scale = [Math]::Max($scaleX, $scaleY)
  $dw = [int]($src.Width * $scale)
  $dh = [int]($src.Height * $scale)
  $dx = [int]($x + (($w - $dw) / 2))
  $dy = [int]($y + (($h - $dh) / 2))
  $dest = [System.Drawing.Rectangle]::new($dx, $dy, $dw, $dh)
  $g.DrawImage($img, $dest, $src, [System.Drawing.GraphicsUnit]::Pixel)
}

$w = 1080
$h = 1350
$bmp = [System.Drawing.Bitmap]::new($w, $h)
$g = [System.Drawing.Graphics]::FromImage($bmp)
$g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$g.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit

$logo = [System.Drawing.Image]::FromFile($logoPath)
$logoBounds = Bounds $logo

$bedBg = [System.Drawing.Image]::FromFile($bgPath)
$bedBgBounds = Bounds $bedBg

try {
  # 1. Background Cover
  DrawFitCover $g $bedBg $bedBgBounds 0 0 $w $h

  # 2. Left dark wash gradient (horizontal, makes text pop)
  $leftWash = [System.Drawing.Drawing2D.LinearGradientBrush]::new([System.Drawing.Rectangle]::new(0, 0, 700, $h), [System.Drawing.Color]::FromArgb(180, 0, 10, 20), [System.Drawing.Color]::FromArgb(0, 0, 10, 20), 0)
  $g.FillRectangle($leftWash, 0, 0, 700, $h)
  $leftWash.Dispose()

  # 3. Bottom dark wash gradient (vertical, makes tagline and buttons pop)
  $bottomWash = [System.Drawing.Drawing2D.LinearGradientBrush]::new([System.Drawing.Rectangle]::new(0, 600, $w, 750), [System.Drawing.Color]::FromArgb(0, 0, 10, 20), [System.Drawing.Color]::FromArgb(210, 0, 10, 20), 90)
  $g.FillRectangle($bottomWash, 0, 600, $w, 750)
  $bottomWash.Dispose()

  $whiteBrush = Brush $white
  $blueBrush = Brush $blue
  $cyanSolid = Brush $cyan
  $yellowBrush = Brush $yellow
  $greenBrush = Brush $green
  $inkBrush = Brush $ink
  $softBrush = Brush $soft

  # 4. Logo card (white background card for logo readability)
  RoundRect $g $whiteBrush 58 50 280 96 22
  DrawFit $g $logo $logoBounds 76 60 244 76

  # 5. Date badge
  RoundRect $g $cyanSolid 770 50 250 96 24
  Text $g "01 A 13/06" (Font 28 ([System.Drawing.FontStyle]::Bold)) $whiteBrush 770 50 250 96 "Center" "Center"

  # 6. Campaign eyebrow badge
  RoundRect $g $yellowBrush 58 190 480 50 16
  Text $g "ESPECIAL DIA DOS NAMORADOS" (Font 20 ([System.Drawing.FontStyle]::Bold)) $inkBrush 58 190 480 50 "Center" "Center"

  # 7. Headline
  ShadowText $g "Presente de Namorados que dura anos." (Font 52 ([System.Drawing.FontStyle]::Bold)) $whiteBrush 58 260 900 140

  # 8. Product name in cyan
  ShadowText $g "CAMA BOX MOLAS ENSACADAS" (Font 42 ([System.Drawing.FontStyle]::Bold)) $cyanSolid 58 410 900 60

  # 9. USP bullet/description
  ShadowText $g "Molas ensacadas individuais: quando um se mexe, o outro n$([char]227)o sente. O descanso perfeito para o casal." (Font 24 ([System.Drawing.FontStyle]::Bold)) $whiteBrush 58 475 800 100

  # 10. Price Gradient Box (Blue to Purple)
  $priceGrad = [System.Drawing.Drawing2D.LinearGradientBrush]::new([System.Drawing.Rectangle]::new(600, 850, 420, 260), $gradStart, $gradEnd, 45)
  RoundRect $g $priceGrad 600 850 420 260 36
  $priceGrad.Dispose()

  # 11. Pricing text inside box
  Text $g "12x de" (Font 28 ([System.Drawing.FontStyle]::Bold)) $whiteBrush 600 875 420 35 "Center"
  Text $g "R$ 132,50" (Font 64 ([System.Drawing.FontStyle]::Bold)) $whiteBrush 600 910 420 80 "Center"
  Text $g "sem juros" (Font 28 ([System.Drawing.FontStyle]::Bold)) $whiteBrush 600 990 420 35 "Center"
  Text $g "ou R$ 1.590,00 $([char]224) vista" (Font 22 ([System.Drawing.FontStyle]::Bold)) $whiteBrush 600 1050 420 30 "Center"

  # 12. WhatsApp Button below price tag
  RoundRect $g $greenBrush 600 1130 420 90 28
  Text $g "Chamar no WhatsApp" (Font 32 ([System.Drawing.FontStyle]::Bold)) $whiteBrush 600 1130 420 90 "Center" "Center"

  # 13. Footer Tagline
  ShadowText $g "Pensou colch$([char]227)o, Colch$([char]245)es e Cia" (Font 26 ([System.Drawing.FontStyle]::Bold)) $whiteBrush 58 1285 700 40

  $bmp.Save($outPath, [System.Drawing.Imaging.ImageFormat]::Png)

  $whiteBrush.Dispose(); $blueBrush.Dispose(); $cyanSolid.Dispose(); $yellowBrush.Dispose(); $greenBrush.Dispose(); $inkBrush.Dispose(); $softBrush.Dispose()
}
finally {
  $logo.Dispose()
  $bedBg.Dispose()
  $g.Dispose()
  $bmp.Dispose()
}

Write-Host $outPath
