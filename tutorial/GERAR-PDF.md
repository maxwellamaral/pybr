# Como Gerar PDF com Suporte a Emojis

Este guia explica como gerar o PDF do tutorial PyBR com renderização completa de emojis.

## 📋 Pré-requisitos

### 1. Pandoc
**Instalar Pandoc:**

- **Windows:** Baixe em [pandoc.org](https://pandoc.org/installing.html)
- **macOS:** `brew install pandoc`
- **Ubuntu/Debian:** `sudo apt install pandoc texlive-xetex`
- **Fedora:** `sudo dnf install pandoc texlive-xetex`

### 2. XeLaTeX
XeLaTeX é necessário para suportar fontes Unicode e emojis.

- **Windows:** Instale [MiKTeX](https://miktex.org/) ou [TeX Live](https://www.tug.org/texlive/)
- **macOS:** `brew install --cask mactex` (ou BasicTeX: `brew install basictex`)
- **Linux:** Já incluído com texlive-xetex

### 3. Fontes com Suporte a Emoji

#### Windows
- **Segoe UI Emoji** (já vem com Windows 10/11)
- **Noto Color Emoji** (baixe de [Google Fonts](https://fonts.google.com/noto/specimen/Noto+Color+Emoji))

#### macOS
- **Apple Color Emoji** (já vem instalado)
- **Noto Color Emoji** (opcional)

#### Linux
```bash
# Ubuntu/Debian
sudo apt install fonts-noto-color-emoji fonts-dejavu

# Fedora
sudo dnf install google-noto-emoji-fonts

# Arch Linux
sudo pacman -S noto-fonts-emoji
```

## 🚀 Uso

### Método 1: Scripts Automatizados (Recomendado)

#### Windows (PowerShell)
```powershell
.\gerar-pdf.ps1
```

#### macOS/Linux (Bash)
```bash
chmod +x gerar-pdf.sh
./gerar-pdf.sh
```

### Método 2: Comando Manual

```bash
pandoc tutorial-iniciantes.md \
  -o tutorial-iniciantes.pdf \
  --pdf-engine=xelatex \
  -H header.tex \
  -V geometry:margin=1in \
  -V documentclass=article \
  -V papersize=a4 \
  --toc \
  --toc-depth=2 \
  -V lang=pt-BR
```

### Método 3: Sem Emojis (Mais Simples)

Se você não precisa dos emojis, use o comando básico:

```bash
pandoc tutorial-iniciantes.md \
  -o tutorial-iniciantes.pdf \
  --pdf-engine=xelatex \
  -V geometry:margin=1in
```

## 📝 Arquivos Criados

- **header.tex** - Configurações LaTeX para suporte a emojis
- **gerar-pdf.ps1** - Script PowerShell para Windows
- **gerar-pdf.sh** - Script Bash para macOS/Linux
- **GERAR-PDF.md** - Este arquivo de documentação

## ⚠️ Solução de Problemas

### Erro: "pandoc: command not found"
**Solução:** Instale o Pandoc (veja pré-requisitos acima)

### Erro: "xelatex not found"
**Solução:** Instale XeLaTeX/TeX Live:
- Windows: Instale MiKTeX ou TeX Live
- macOS: `brew install basictex`
- Linux: `sudo apt install texlive-xetex`

### Aviso: "Missing character" para emojis
**Causas possíveis:**
1. Fonte de emoji não instalada
2. Fonte incorreta no header.tex

**Soluções:**
1. Instale as fontes recomendadas (veja pré-requisitos)
2. Edite header.tex e mude a linha:
   ```latex
   \newfontfamily\emojifont{Segoe UI Emoji}
   ```
   Para:
   - macOS: `{Apple Color Emoji}`
   - Linux: `{Noto Color Emoji}`

### PDF gerado, mas sem emojis
**Solução:** Verifique se a fonte está instalada corretamente:

```bash
# macOS/Linux - listar fontes instaladas
fc-list | grep -i emoji

# Se não aparecer nada, instale a fonte
```

### Compilação muito lenta
**Causa:** Primeira compilação do LaTeX baixa pacotes

**Solução:** Aguarde. Nas próximas vezes será mais rápido.

## 🎨 Personalização

### Mudar Margem
Edite o parâmetro `-V geometry:margin=1in`:
```bash
-V geometry:margin=2cm        # 2 centímetros
-V geometry:margin=0.5in      # meia polegada
```

### Mudar Tamanho do Papel
```bash
-V papersize=a4     # Padrão
-V papersize=letter # Americano
```

### Adicionar Mais Emojis
Edite `header.tex` e adicione:
```latex
\newunicodechar{🔥}{\emojifont 🔥}
\newunicodechar{💪}{\emojifont 💪}
```

### Remover Índice (TOC)
Remova as linhas:
```bash
--toc \
--toc-depth=2 \
```

## 📚 Referências

- [Pandoc Documentation](https://pandoc.org/MANUAL.html)
- [XeLaTeX Font Tutorial](https://www.overleaf.com/learn/latex/XeLaTeX)
- [Noto Emoji Fonts](https://fonts.google.com/noto/specimen/Noto+Color+Emoji)

## ✅ Checklist de Instalação

- [ ] Pandoc instalado e funcionando
- [ ] XeLaTeX/TeX Live instalado
- [ ] Fontes de emoji instaladas
- [ ] Arquivo header.tex presente
- [ ] Script de geração (gerar-pdf.ps1 ou gerar-pdf.sh) presente
- [ ] Teste: executar script e verificar PDF gerado

## 💡 Dicas

1. **Primeira vez:** A compilação pode demorar alguns minutos enquanto baixa pacotes LaTeX
2. **Cache:** Depois da primeira vez, será muito mais rápido
3. **Fontes:** Se alguns emojis não aparecem, pode ser limitação da fonte
4. **Alternativa:** Use fontes diferentes editando header.tex
5. **Qualidade:** XeLaTeX produz PDFs de alta qualidade para impressão

---

**Pronto!** Agora você pode gerar PDFs profissionais com emojis completos! 🎉
