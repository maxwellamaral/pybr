#!/bin/bash
# Script para gerar PDF do tutorial PyBR com suporte a emojis
# Uso: ./gerar-pdf.sh

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${CYAN}=========================================="
echo -e "  Gerador de PDF - PyBR"
echo -e "  Com suporte a emojis e Unicode"
echo -e "==========================================${NC}"
echo ""

# Verificar se pandoc está instalado
if ! command -v pandoc &> /dev/null; then
    echo -e "${RED}✗ ERRO: Pandoc não está instalado!${NC}"
    echo ""
    echo -e "${YELLOW}Instale o Pandoc:${NC}"
    echo "  macOS:   brew install pandoc"
    echo "  Ubuntu:  sudo apt install pandoc texlive-xetex"
    echo "  Fedora:  sudo dnf install pandoc texlive-xetex"
    exit 1
fi

PANDOC_VERSION=$(pandoc --version | head -n 1)
echo -e "${GREEN}✓ Pandoc encontrado: $PANDOC_VERSION${NC}"

# Verificar se o arquivo markdown existe
if [ ! -f "tutorial-iniciantes.md" ]; then
    echo -e "${RED}✗ ERRO: Arquivo tutorial-iniciantes.md não encontrado!${NC}"
    exit 1
fi

# Verificar se o header.tex existe
if [ ! -f "header.tex" ]; then
    echo -e "${YELLOW}⚠ AVISO: header.tex não encontrado.${NC}"
    echo ""
    echo -e "${YELLOW}Por favor, crie o arquivo header.tex primeiro.${NC}"
    exit 1
fi

echo -e "${GREEN}✓ Arquivo tutorial-iniciantes.md encontrado${NC}"
echo -e "${GREEN}✓ Arquivo header.tex encontrado${NC}"
echo ""

# Detectar sistema operacional para escolher a fonte de emoji correta
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    EMOJI_FONT="Apple Color Emoji"
    echo -e "${CYAN}Sistema: macOS${NC}"
elif [[ -f /etc/debian_version ]]; then
    # Debian/Ubuntu
    EMOJI_FONT="Noto Color Emoji"
    echo -e "${CYAN}Sistema: Debian/Ubuntu${NC}"
    
    # Verificar se a fonte está instalada
    if ! fc-list | grep -q "Noto Color Emoji"; then
        echo -e "${YELLOW}⚠ Fonte Noto Color Emoji não encontrada${NC}"
        echo -e "${YELLOW}Instale com: sudo apt install fonts-noto-color-emoji${NC}"
    fi
else
    # Outros Linux
    EMOJI_FONT="Noto Color Emoji"
    echo -e "${CYAN}Sistema: Linux${NC}"
fi

echo ""
echo -e "${YELLOW}Gerando PDF com suporte a emojis...${NC}"
echo ""

# Obter data atual formatada
DATA_ATUAL=$(date "+%d/%m/%Y")

# Gerar o PDF
pandoc tutorial-iniciantes.md \
    -o tutorial-iniciantes.pdf \
    --pdf-engine=xelatex \
    -H header.tex \
    -V geometry:margin=1in \
    -V documentclass=article \
    -V papersize=a4 \
    -V title="PyBR - Python em Português" \
    -V author="Maxwell Anderson Ielpo do Amaral" \
    -V date="Janeiro/2026" \
    --toc \
    --toc-depth=2 \
    -V lang=pt-BR

# Verificar se foi bem-sucedido
if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}=========================================="
    echo -e "  ✓ PDF gerado com sucesso!"
    echo -e "==========================================${NC}"
    echo ""
    echo -e "${CYAN}Arquivo criado: tutorial-iniciantes.pdf${NC}"
    echo ""
    
    # Tentar abrir o PDF
    if [[ "$OSTYPE" == "darwin"* ]]; then
        open tutorial-iniciantes.pdf
    elif command -v xdg-open &> /dev/null; then
        xdg-open tutorial-iniciantes.pdf
    else
        echo -e "${YELLOW}PDF gerado. Abra manualmente: tutorial-iniciantes.pdf${NC}"
    fi
else
    echo ""
    echo -e "${RED}✗ Erro ao gerar PDF${NC}"
    echo ""
    echo -e "${YELLOW}Possíveis soluções:${NC}"
    echo "1. Verifique se XeLaTeX está instalado"
    echo "2. Instale as fontes necessárias:"
    echo "   - macOS: Segoe UI Emoji (ou use Apple Color Emoji)"
    echo "   - Linux: sudo apt install fonts-noto-color-emoji fonts-dejavu"
    echo "3. Verifique erros na saída acima"
    exit 1
fi
