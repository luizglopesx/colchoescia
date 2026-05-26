$ErrorActionPreference = "Stop"
Add-Type -AssemblyName System.Drawing

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = Resolve-Path (Join-Path $root "..\..\..")
$feedDir = Join-Path $root "feed"
$storyDir = Join-Path $root "story"
New-Item -ItemType Directory -Force -Path $feedDir, $storyDir | Out-Null

$logoPath = Join-Path $projectRoot "identidade\Logo Cc fundo Transparente.png"
$productPath = Join-Path $projectRoot "marketing\Cj Box Prime.png"

$blue = [System.Drawing.ColorTranslator]::FromHtml("#0064A6")
$blue2 = [System.Drawing.ColorTranslator]::FromHtml("#00AFEF")
$navy = [System.Drawing.ColorTranslator]::FromHtml("#062B49")
$deep = [System.Drawing.ColorTranslator]::FromHtml("#03192B")
$white = [System.Drawing.Color]::White
$ink = [System.Drawing.ColorTranslator]::FromHtml("#1E1E1E")
$soft = [System.Drawing.ColorTranslator]::FromHtml("#EAF7FF")
$whats = [System.Drawing.ColorTranslator]::FromHtml("#16B84E")
$yellow = [System.Drawing.ColorTranslator]::FromHtml("#FFE45C")

$pieces = @(
  @{
    Slug="01-abertura"; Date="01/06"; Eyebrow="CAMPANHA DE NAMORADOS"; Headline="Cj Box Prime para o casal"; Proof="Cama completa, descanso todo dia"; Offer="01 a 13/06"; Cta="Ver preco"; Badge="JUNHO"
  },
  @{
    Slug="02-cama-casal"; Date="03/06"; Eyebrow="QUARTO NOVO"; Headline="Presente que nao fica guardado"; Proof="Vai para o quarto e melhora a noite"; Offer="Cj Box Prime"; Cta="Ver modelos"; Badge="CASAL"
  },
  @{
    Slug="03-colchao-velho"; Date="05/06"; Eyebrow="TROCA CERTA"; Headline="Colchao velho cobra no corpo"; Proof="Acordou cansado? Ja passou da hora"; Offer="Box + colchao"; Cta="Falar agora"; Badge="TROCA"
  },
  @{
    Slug="04-box-bau"; Date="08/06"; Eyebrow="CONFORTO PARA OS DOIS"; Headline="A cama certa muda o quarto"; Proof="Mais apoio, mais conforto, mais descanso"; Offer="Consulte tamanhos"; Cta="Chamar"; Badge="PRIME"
  },
  @{
    Slug="05-ainda-da-tempo"; Date="10/06"; Eyebrow="RETA FINAL"; Headline="Ainda da tempo de acertar"; Proof="Namorados com presente de verdade"; Offer="Junho especial"; Cta="Escolher"; Badge="2 DIAS"
  },
  @{
    Slug="06-dia-dos-namorados"; Date="12/06"; Eyebrow="12 DE JUNHO"; Headline="Dorme junto, acorda bem"; Proof="Presente bom o casal usa toda noite"; Offer="Namorados"; Cta="Chamar"; Badge="HOJE"
  },
  @{
    Slug="07-ultimo-dia"; Date="13/06"; Eyebrow="ULTIMA CHAMADA"; Headline="Acaba hoje"; Proof="Ultimo dia da campanha de Namorados"; Offer="So hoje"; Cta="Chamar agora"; Badge="13/06"
  }
)

function New-Font($size, $style = [System.Drawing.FontStyle]::Regular) {
  try { return [System.Drawing.Font]::new("Arial Rounded MT Bold", $size, $style, [System.Drawing.GraphicsUnit]::Pixel) }
  catch { return [System.Drawing.Font]::new("Arial", $size, $style, [System.Drawing.GraphicsUnit]::Pixel) }
}

function New-Brush($color) {
  return [System.Drawing.SolidBrush]::new($color)
}

function Draw-RoundRect($g, $brush, $x, $y, $w, $h, $r) {
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

function Draw-Centered($g, $text, $font, $brush, $rect, $wrap = $false) {
  $sf = [System.Drawing.StringFormat]::new()
  $sf.Alignment = [System.Drawing.StringAlignment]::Center
  $sf.LineAlignment = [System.Drawing.StringAlignment]::Center
  if (-not $wrap) { $sf.FormatFlags = [System.Drawing.StringFormatFlags]::NoWrap }
  $sf.Trimming = [System.Drawing.StringTrimming]::EllipsisCharacter
  $r = [System.Drawing.RectangleF]::new([float]$rect.X, [float]$rect.Y, [float]$rect.Width, [float]$rect.Height)
  $g.DrawString([string]$text, $font, $brush, $r, $sf)
  $sf.Dispose()
}

function Draw-Text($g, $text, $font, $brush, $x, $y, $w, $h, $align = "Near") {
  $sf = [System.Drawing.StringFormat]::new()
  $sf.Alignment = [System.Drawing.StringAlignment]::$align
  $sf.LineAlignment = [System.Drawing.StringAlignment]::Near
  $sf.Trimming = [System.Drawing.StringTrimming]::Word
  $r = [System.Drawing.RectangleF]::new([float]$x, [float]$y, [float]$w, [float]$h)
  $g.DrawString([string]$text, $font, $brush, $r, $sf)
  $sf.Dispose()
}

function Get-VisibleBounds($img) {
  $minX = $img.Width
  $minY = $img.Height
  $maxX = 0
  $maxY = 0
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
  if ($maxX -le $minX -or $maxY -le $minY) {
    return [System.Drawing.Rectangle]::new(0, 0, $img.Width, $img.Height)
  }
  return [System.Drawing.Rectangle]::new($minX, $minY, $maxX - $minX + 1, $maxY - $minY + 1)
}

function Draw-ImageFit($g, $img, $x, $y, $w, $h, $mode = "contain", $srcRect = $null) {
  if ($null -eq $srcRect) { $srcRect = [System.Drawing.Rectangle]::new(0, 0, $img.Width, $img.Height) }
  $scaleX = $w / $srcRect.Width
  $scaleY = $h / $srcRect.Height
  $scale = if ($mode -eq "cover") { [Math]::Max($scaleX, $scaleY) } else { [Math]::Min($scaleX, $scaleY) }
  $dw = [int]($srcRect.Width * $scale)
  $dh = [int]($srcRect.Height * $scale)
  $dx = [int]($x + (($w - $dw) / 2))
  $dy = [int]($y + (($h - $dh) / 2))
  $dest = [System.Drawing.Rectangle]::new($dx, $dy, $dw, $dh)
  $g.DrawImage($img, $dest, $srcRect, [System.Drawing.GraphicsUnit]::Pixel)
}

function Draw-Logo($g, $logo, $x, $y, $w, $h) {
  $whiteBrush = New-Brush $white
  Draw-RoundRect $g $whiteBrush $x $y $w $h 28
  Draw-ImageFit $g $logo ($x + 20) ($y + 8) ($w - 40) ($h - 16) "contain" $script:logoBounds
  $whiteBrush.Dispose()
}

function Draw-ProductSpotlight($g, $product, $x, $y, $w, $h) {
  $shadow = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::FromArgb(85, 0, 0, 0))
  $shine = [System.Drawing.Drawing2D.LinearGradientBrush]::new([System.Drawing.Rectangle]::new($x, $y, $w, $h), [System.Drawing.Color]::FromArgb(255, 255, 255, 255), [System.Drawing.Color]::FromArgb(255, 215, 245, 255), 25)
  Draw-RoundRect $g $shine $x $y $w $h 42
  $g.FillEllipse($shadow, $x + [int]($w * .12), $y + [int]($h * .75), [int]($w * .76), [int]($h * .16))
  Draw-ImageFit $g $product ($x - 55) ($y + 2) ($w + 110) ($h - 4) "contain" $script:productBounds
  $shadow.Dispose()
  $shine.Dispose()
}

function Draw-Art($piece, $format, $path, $logo, $product) {
  if ($format -eq "feed") {
    $w = 1080; $h = 1350
    $logoRect = @(58, 52, 330, 112)
    $dateRect = @(842, 64, 180, 70)
    $eyebrowRect = @(58, 198, 500, 60)
    $headlineRect = @(58, 278, 770, 255)
    $badgeRect = @(770, 224, 230, 130)
    $productRect = @(62, 540, 956, 370)
    $panelRect = @(58, 930, 964, 285)
    $footerY = 1265
  } else {
    $w = 1080; $h = 1920
    $logoRect = @(58, 72, 350, 120)
    $dateRect = @(842, 86, 180, 72)
    $eyebrowRect = @(58, 260, 520, 64)
    $headlineRect = @(58, 350, 850, 365)
    $badgeRect = @(760, 270, 250, 150)
    $productRect = @(55, 800, 970, 440)
    $panelRect = @(58, 1310, 964, 360)
    $footerY = 1810
  }

  $bmp = [System.Drawing.Bitmap]::new($w, $h)
  $g = [System.Drawing.Graphics]::FromImage($bmp)
  $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
  $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
  $g.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit

  $bg = [System.Drawing.Drawing2D.LinearGradientBrush]::new([System.Drawing.Rectangle]::new(0,0,$w,$h), $deep, $blue, 35)
  $g.FillRectangle($bg, 0, 0, $w, $h)
  $cyanWash = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::FromArgb(115, 0, 175, 239))
  $navyWash = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::FromArgb(90, 3, 25, 43))
  $g.FillEllipse($cyanWash, 670, -170, 620, 620)
  $g.FillEllipse($navyWash, -260, 610, 720, 720)

  $whiteBrush = New-Brush $white
  $blueBrush = New-Brush $blue
  $blue2Brush = New-Brush $blue2
  $inkBrush = New-Brush $ink
  $softBrush = New-Brush $soft
  $whatsBrush = New-Brush $whats
  $yellowBrush = New-Brush $yellow

  $eyebrowFont = New-Font 25 ([System.Drawing.FontStyle]::Bold)
  $dateFont = New-Font 31 ([System.Drawing.FontStyle]::Bold)
  $headlineFont = if ($format -eq "feed") { New-Font 78 ([System.Drawing.FontStyle]::Bold) } else { New-Font 92 ([System.Drawing.FontStyle]::Bold) }
  $productFont = if ($format -eq "feed") { New-Font 54 ([System.Drawing.FontStyle]::Bold) } else { New-Font 64 ([System.Drawing.FontStyle]::Bold) }
  $proofFont = if ($format -eq "feed") { New-Font 39 ([System.Drawing.FontStyle]::Bold) } else { New-Font 48 ([System.Drawing.FontStyle]::Bold) }
  $offerFont = if ($format -eq "feed") { New-Font 40 ([System.Drawing.FontStyle]::Bold) } else { New-Font 45 ([System.Drawing.FontStyle]::Bold) }
  $ctaFont = if ($format -eq "feed") { New-Font 42 ([System.Drawing.FontStyle]::Bold) } else { New-Font 46 ([System.Drawing.FontStyle]::Bold) }
  $smallFont = New-Font 25 ([System.Drawing.FontStyle]::Bold)
  $badgeFont = New-Font 30 ([System.Drawing.FontStyle]::Bold)

  Draw-Logo $g $logo $logoRect[0] $logoRect[1] $logoRect[2] $logoRect[3]
  Draw-RoundRect $g $softBrush $dateRect[0] $dateRect[1] $dateRect[2] $dateRect[3] 26
  Draw-Centered $g $piece.Date $dateFont $blueBrush ([System.Drawing.RectangleF]::new($dateRect[0], $dateRect[1], $dateRect[2], $dateRect[3]))

  Draw-RoundRect $g $yellowBrush $eyebrowRect[0] $eyebrowRect[1] $eyebrowRect[2] $eyebrowRect[3] 20
  Draw-Centered $g $piece.Eyebrow $eyebrowFont $inkBrush ([System.Drawing.RectangleF]::new($eyebrowRect[0], $eyebrowRect[1], $eyebrowRect[2], $eyebrowRect[3]))

  Draw-RoundRect $g $blue2Brush $badgeRect[0] $badgeRect[1] $badgeRect[2] $badgeRect[3] 34
  Draw-Centered $g $piece.Badge $badgeFont $whiteBrush ([System.Drawing.RectangleF]::new($badgeRect[0] + 12, $badgeRect[1] + 12, $badgeRect[2] - 24, $badgeRect[3] - 24), $true)

  Draw-Text $g $piece.Headline $headlineFont $whiteBrush $headlineRect[0] $headlineRect[1] $headlineRect[2] $headlineRect[3]
  Draw-ProductSpotlight $g $product $productRect[0] $productRect[1] $productRect[2] $productRect[3]

  Draw-RoundRect $g $whiteBrush $panelRect[0] $panelRect[1] $panelRect[2] $panelRect[3] 40
  Draw-Text $g "CJ BOX PRIME" $productFont $blueBrush ($panelRect[0] + 50) ($panelRect[1] + 34) ($panelRect[2] - 100) 78
  Draw-Text $g $piece.Proof $proofFont $inkBrush ($panelRect[0] + 50) ($panelRect[1] + 112) ($panelRect[2] - 100) 105
  Draw-RoundRect $g $softBrush ($panelRect[0] + 50) ($panelRect[1] + $panelRect[3] - 92) 500 64 22
  Draw-Centered $g $piece.Offer $offerFont $blueBrush ([System.Drawing.RectangleF]::new($panelRect[0] + 50, $panelRect[1] + $panelRect[3] - 92, 500, 64))
  Draw-RoundRect $g $whatsBrush ($panelRect[0] + 590) ($panelRect[1] + $panelRect[3] - 104) 330 88 28
  Draw-Centered $g $piece.Cta $ctaFont $whiteBrush ([System.Drawing.RectangleF]::new($panelRect[0] + 590, $panelRect[1] + $panelRect[3] - 104, 330, 88), $true)

  Draw-Text $g "Pensou colchao, Colchoes e Cia" $smallFont $whiteBrush 58 $footerY 660 44
  Draw-Text $g "01 a 13/06" $smallFont $whiteBrush 820 $footerY 200 44 "Far"

  $bmp.Save($path, [System.Drawing.Imaging.ImageFormat]::Png)

  $eyebrowFont.Dispose(); $dateFont.Dispose(); $headlineFont.Dispose(); $productFont.Dispose(); $proofFont.Dispose(); $offerFont.Dispose(); $ctaFont.Dispose(); $smallFont.Dispose(); $badgeFont.Dispose()
  $whiteBrush.Dispose(); $blueBrush.Dispose(); $blue2Brush.Dispose(); $inkBrush.Dispose(); $softBrush.Dispose(); $whatsBrush.Dispose(); $yellowBrush.Dispose(); $cyanWash.Dispose(); $navyWash.Dispose(); $bg.Dispose(); $g.Dispose(); $bmp.Dispose()
}

$logo = [System.Drawing.Image]::FromFile($logoPath)
$product = [System.Drawing.Image]::FromFile($productPath)
$script:logoBounds = Get-VisibleBounds $logo
$script:productBounds = Get-VisibleBounds $product

try {
  foreach ($piece in $pieces) {
    Draw-Art $piece "feed" (Join-Path $feedDir "$($piece.Slug)-feed.png") $logo $product
    Draw-Art $piece "story" (Join-Path $storyDir "$($piece.Slug)-story.png") $logo $product
  }
}
finally {
  $logo.Dispose()
  $product.Dispose()
}

Write-Host "Campanha renderizada com logo e produto reais em:"
Write-Host "  $feedDir"
Write-Host "  $storyDir"
