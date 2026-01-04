# Script para gerar PDF do tutorial PyBR com suporte a emojis
# Uso: .\gerar-pdf.ps1

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "  Gerador de PDF - PyBR" -ForegroundColor Cyan
Write-Host "  Com suporte a emojis e Unicode" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""

# Verificar se pandoc está instalado
try {
    $pandocVersion = pandoc --version 2>&1 | Select-Object -First 1
    Write-Host "✓ Pandoc encontrado: $pandocVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ ERRO: Pandoc não está instalado!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Instale o Pandoc em: https://pandoc.org/installing.html" -ForegroundColor Yellow
    exit 1
}

# Verificar se o arquivo markdown existe
if (-not (Test-Path "tutorial-iniciantes.md")) {
    Write-Host "✗ ERRO: Arquivo tutorial-iniciantes.md não encontrado!" -ForegroundColor Red
    exit 1
}

# Verificar se o header.tex existe
if (-not (Test-Path "header.tex")) {
    Write-Host "⚠ AVISO: header.tex não encontrado. Criando arquivo padrão..." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Por favor, execute este script novamente após criar header.tex" -ForegroundColor Yellow
    exit 1
}

Write-Host "✓ Arquivo tutorial-iniciantes.md encontrado" -ForegroundColor Green
Write-Host "✓ Arquivo header.tex encontrado" -ForegroundColor Green
Write-Host ""

# Gerar o PDF
Write-Host "Gerando PDF com suporte a emojis..." -ForegroundColor Yellow
Write-Host ""

# Obter data atual formatada
$dataAtual = Get-Date -Format "dd/MM/yyyy"

try {
    pandoc tutorial-iniciantes.md `
        -o tutorial-iniciantes.pdf `
        --pdf-engine=xelatex `
        -H header.tex `
        -V geometry:margin=1in `
        -V documentclass=article `
        -V papersize=a4 `
        -V title="PyBR - Python em Português" `
        -V author="Maxwell Anderson  Ielpo do Amaral" `
        -V date="Janeiro/2026" `
        --toc `
        --toc-depth=2 `
        -V lang=pt-BR
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host ""
        Write-Host "==========================================" -ForegroundColor Green
        Write-Host "  ✓ PDF gerado com sucesso!" -ForegroundColor Green
        Write-Host "==========================================" -ForegroundColor Green
        Write-Host ""
        Write-Host "Arquivo criado: tutorial-iniciantes.pdf" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "Abrindo PDF..." -ForegroundColor Yellow
        Start-Process "tutorial-iniciantes.pdf"
    } else {
        Write-Host ""
        Write-Host "✗ Erro ao gerar PDF (código: $LASTEXITCODE)" -ForegroundColor Red
        Write-Host ""
        Write-Host "Possíveis soluções:" -ForegroundColor Yellow
        Write-Host "1. Verifique se XeLaTeX está instalado" -ForegroundColor White
        Write-Host "2. Instale as fontes necessárias (DejaVu, Segoe UI Emoji)" -ForegroundColor White
        Write-Host "3. Verifique erros na saída acima" -ForegroundColor White
    }
} catch {
    Write-Host ""
    Write-Host "✗ ERRO ao executar pandoc: $_" -ForegroundColor Red
    exit 1
}
