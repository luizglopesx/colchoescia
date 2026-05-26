$ErrorActionPreference = "Stop"
Add-Type -AssemblyName System.Drawing

$root        = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = Resolve-Path (Join-Path $root "..\..\..")
$outDir      = Join-Path $root "aprovacao"
New-Item -ItemType Directory -Force -Path $outDir | Out-Null

$logoPath    = Join-Path $projectRoot "identidade\Logo Cc fundo Transparente.png"
$productPath = Join-Path $projectRoot "marketing\Cj Box Prime.png"
$bgPath      = Join-Path $root "quarto_namorados.png"
$outPath     = Join-Path $outDir "piloto-cj-box-prime-feed.png"

# ── Paleta ───────────────────────────────────────────────────────────────────
$blue    = [System.Drawing.ColorTranslator]::FromHtml("#0064A6")
$cyan    = [System.Drawing.ColorTranslator]::FromHtml("#00AFEF")
$white   = [System.Drawing.Color]::White
$yellow  = [System.Drawing.ColorTranslator]::FromHtml("#FFE45C")
$green   = [System.Drawing.ColorTranslator]::FromHtml("#16B84E")
$ink     = [System.Drawing.ColorTranslator]::FromHtml("#1E1E1E")

# ── Helpers ───────────────────────────────────────────────────────────────────
function Font($size, $style = [System.Drawing.FontStyle]::Bold) {
  try { return [System.Drawing.Font]::new("Arial Rounded MT Bold", $size, $style, [System.Drawing.GraphicsUnit]::Pixel) }
  catch { return [System.Drawing.Font]::new("Arial", $size, $style, [System.Drawing.GraphicsUnit]::Pixel) }
}
function Br($c) { return [System.Drawing.SolidBrush]::new($c) }

function RoundRect($g, $brush, $x, $y, $w, $h, $r) {
  $path = [System.Drawing.Drawing2D.GraphicsPath]::new()
  $d = $r * 2
  $path.AddArc($x, $y, $d, $d, 180, 90)
  $path.AddArc($x+$w-$d, $y, $d, $d, 270, 90)
  $path.AddArc($x+$w-$d, $y+$h-$d, $d, $d, 0, 90)
  $path.AddArc($x, $y+$h-$d, $d, $d, 90, 90)
  $path.CloseFigure()
  $g.FillPath($brush, $path)
  $path.Dispose()
}

function Txt($g, $text, $font, $brush, $x, $y, $w, $h, $ha = "Near", $va = "Near") {
  $sf = [System.Drawing.StringFormat]::new()
  $sf.Alignment = [System.Drawing.StringAlignment]::$ha
  $sf.LineAlignment = [System.Drawing.StringAlignment]::$va
  $sf.Trimming = [System.Drawing.StringTrimming]::Word
  $g.DrawString([string]$text, $font, $brush, [System.Drawing.RectangleF]::new([float]$x,[float]$y,[float]$w,[float]$h), $sf)
  $sf.Dispose()
}

function CoverCrop($g, $img, $canvasW, $canvasH) {
  $scaleX = $canvasW / $img.Width
  $scaleY = $canvasH / $img.Height
  $scale  = [Math]::Max($scaleX, $scaleY)
  $dw = [int]($img.Width  * $scale)
  $dh = [int]($img.Height * $scale)
  $dx = [int](($canvasW - $dw) / 2)
  $dy = [int](($canvasH - $dh) / 2)
  $g.DrawImage($img, [System.Drawing.Rectangle]::new($dx, $dy, $dw, $dh),
    [System.Drawing.Rectangle]::new(0,0,$img.Width,$img.Height),
    [System.Drawing.GraphicsUnit]::Pixel)
}

function FitCenter($g, $img, $ia, $x, $y, $w, $h) {
  $b = Bounds $img
  $scale = [Math]::Min($w / $b.Width, $h / $b.Height)
  $dw = [int]($b.Width * $scale); $dh = [int]($b.Height * $scale)
  $dx = [int]($x + ($w - $dw) / 2); $dy = [int]($y + ($h - $dh) / 2)
  $dest = [System.Drawing.Rectangle]::new($dx, $dy, $dw, $dh)
  if ($ia) {
    $g.DrawImage($img, $dest, $b.X, $b.Y, $b.Width, $b.Height,
      [System.Drawing.GraphicsUnit]::Pixel, $ia)
  } else {
    $g.DrawImage($img, $dest, $b, [System.Drawing.GraphicsUnit]::Pixel)
  }
}

function Bounds($img) {
  $minX=$img.Width; $minY=$img.Height; $maxX=0; $maxY=0
  for ($yy=0; $yy -lt $img.Height; $yy+=3) {
    for ($xx=0; $xx -lt $img.Width; $xx+=3) {
      if ($img.GetPixel($xx,$yy).A -gt 8) {
        if($xx -lt $minX){$minX=$xx}; if($yy -lt $minY){$minY=$yy}
        if($xx -gt $maxX){$maxX=$xx}; if($yy -gt $maxY){$maxY=$yy}
      }
    }
  }
  return [System.Drawing.Rectangle]::new($minX,$minY,$maxX-$minX+1,$maxY-$minY+1)
}

# ── Canvas ────────────────────────────────────────────────────────────────────
$W=1080; $H=1350
$bmp = [System.Drawing.Bitmap]::new($W, $H)
$g   = [System.Drawing.Graphics]::FromImage($bmp)
$g.SmoothingMode     = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$g.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit

$logo    = [System.Drawing.Image]::FromFile($logoPath)
$product = [System.Drawing.Bitmap]::FromFile($productPath)
$bg      = [System.Drawing.Image]::FromFile($bgPath)

# Remove fundo branco do produto (pixels quase-brancos → transparentes)
$productClean = [System.Drawing.Imaging.ImageAttributes]::new()
$productClean.SetColorKey(
  [System.Drawing.Color]::FromArgb(230,230,230),
  [System.Drawing.Color]::FromArgb(255,255,255)
)

try {
  # ── 1. Foto de ambiente — full bleed ──────────────────────────────────────
  CoverCrop $g $bg $W $H

  # ── 2. Vinheta escura — cria profundidade e faz o texto respirar ──────────
  # Overlay geral leve
  $g.FillRectangle((Br ([System.Drawing.Color]::FromArgb(80,0,0,0))), 0, 0, $W, $H)

  # Topo: gradiente escuro ↓ (logo + texto no topo)
  $topFade = [System.Drawing.Drawing2D.LinearGradientBrush]::new(
    [System.Drawing.Rectangle]::new(0,0,$W,320),
    [System.Drawing.Color]::FromArgb(200,0,0,0),
    [System.Drawing.Color]::FromArgb(0,0,0,0), 90)
  $g.FillRectangle($topFade, 0, 0, $W, 320)
  $topFade.Dispose()

  # Base: gradiente escuro ↑ (preço + CTA ficam legíveis)
  $botFade = [System.Drawing.Drawing2D.LinearGradientBrush]::new(
    [System.Drawing.Rectangle]::new(0,820,$W,530),
    [System.Drawing.Color]::FromArgb(0,0,0,0),
    [System.Drawing.Color]::FromArgb(230,0,10,20), 90)
  $g.FillRectangle($botFade, 0, 820, $W, 530)
  $botFade.Dispose()

  # Barra de acento cyan no topo
  $g.FillRectangle((Br $cyan), 0, 0, $W, 6)

  # ── 3. Brushes ────────────────────────────────────────────────────────────
  $bW = Br $white; $bC = Br $cyan; $bY = Br $yellow
  $bG = Br $green; $bI = Br $ink; $bB = Br $blue

  # ── 4. Header — logo + badge data ─────────────────────────────────────────
  $logoBounds = Bounds $logo
  RoundRect $g $bW 44 18 230 84 18
  $g.DrawImage($logo,
    [System.Drawing.Rectangle]::new(58, 26, 202, 68),
    $logoBounds, [System.Drawing.GraphicsUnit]::Pixel)

  RoundRect $g $bC 806 18 230 84 22
  Txt $g "01 A 13/06" (Font 28) $bW 806 18 230 84 "Center" "Center"

  # ── 5. Badge campanha ─────────────────────────────────────────────────────
  RoundRect $g $bY 44 118 480 46 14
  Txt $g "DIA DOS NAMORADOS" (Font 20) $bI 44 118 480 46 "Center" "Center"

  # ── 6. Headline — topo esquerdo ───────────────────────────────────────────
  Txt $g "Presente de Namorados" (Font 58) $bW 44 180 860 68
  Txt $g "que dura anos."        (Font 58) $bC 44 250 860 68

  # ── 7. PRODUTO — herói da peça ────────────────────────────────────────────
  # Halo sutil atrás do produto para "grounding"
  $haloPath = [System.Drawing.Drawing2D.GraphicsPath]::new()
  $haloPath.AddEllipse(80, 380, 920, 440)
  $halo = [System.Drawing.Drawing2D.PathGradientBrush]::new($haloPath)
  $halo.CenterColor    = [System.Drawing.Color]::FromArgb(70, 255, 255, 255)
  $halo.SurroundColors = @([System.Drawing.Color]::FromArgb(0, 0, 0, 0))
  $g.FillPath($halo, $haloPath)
  $halo.Dispose(); $haloPath.Dispose()

  FitCenter $g $product $productClean 30 320 1020 540

  # ── 8. Tag do produto ─────────────────────────────────────────────────────
  Txt $g "CJ BOX PRIME"             (Font 44) $bC  44 870 992 52 "Center"
  Txt $g "Cama Box Casal completa"  (Font 24) $bW  44 924 992 32 "Center"

  # ── 9. Preço — impossível ignorar ─────────────────────────────────────────
  # Card preço (azul escuro semitransparente)
  $cardBrush = Br ([System.Drawing.Color]::FromArgb(200, 4, 40, 74))
  RoundRect $g $cardBrush 44 964 992 244 28
  $cardBrush.Dispose()

  # Lado esquerdo: parcelamento
  Txt $g "12x de"    (Font 26) $bW 72  982 460  30
  Txt $g "R$"        (Font 36) $bY 72 1014 100  44
  Txt $g "132,50"    (Font 90) $bY 155 1002 420 108
  Txt $g "sem juros no cart$([char]227)o" (Font 23) $bC 72 1114 460 30

  # Divider
  $pen = [System.Drawing.Pen]::new([System.Drawing.Color]::FromArgb(80,255,255,255), 2)
  $g.DrawLine($pen, 570, 978, 570, 1200)
  $pen.Dispose()

  # Lado direito: à vista
  Txt $g "ou $([char]224) vista"  (Font 24) $bC  594  982 420  30
  Txt $g "R$ 1.590,00"            (Font 58) $bW  586 1014 440  70
  Txt $g "sem entrada"            (Font 24) $bC  594 1090 420  30
  Txt $g "Entrega e montagem gr$([char]225)tis" (Font 22) $bW 594 1124 420 28

  # ── 10. Botão WhatsApp ────────────────────────────────────────────────────
  RoundRect $g $bG 44 1218 992 90 28
  Txt $g "Chamar no WhatsApp" (Font 38) $bW 44 1218 992 90 "Center" "Center"

  # ── 11. Rodapé ────────────────────────────────────────────────────────────
  Txt $g "Pensou colch$([char]227)o, Colch$([char]245)es e Cia" (Font 22) $bC 44 1318 992 26 "Center"

  $bmp.Save($outPath, [System.Drawing.Imaging.ImageFormat]::Png)

  $bW.Dispose(); $bC.Dispose(); $bY.Dispose()
  $bG.Dispose(); $bI.Dispose(); $bB.Dispose()
}
finally {
  $logo.Dispose(); $product.Dispose(); $bg.Dispose()
  $productClean.Dispose(); $g.Dispose(); $bmp.Dispose()
}

Write-Host "Salvo: $outPath"
