# Como Gerar PDF com Suporte a Emojis e Multilíngue

Este guia explica como gerar os PDFs dos tutoriais do PyBR em **todas as línguas** (Português, Espanhol, Alemão, Italiano e Francês) com renderização correta de emojis e metadados.

## 📋 Pré-requisitos

### 1. Python 3
O novo script de geração é escrito em Python para maior compatibilidade.

### 2. Pandoc
**Instalar Pandoc:**
- **Windows:** Baixe em [pandoc.org](https://pandoc.org/installing.html)
- **macOS:** `brew install pandoc`
- **Ubuntu/Debian:** `sudo apt install pandoc texlive-xetex`
- **Fedora:** `sudo dnf install pandoc texlive-xetex`

### 3. Poppler Utils (para verificação)
O script verifica automaticamente se os PDFs foram gerados corretamente.
- **Ubuntu:** `sudo apt install poppler-utils`
- **macOS:** `brew install poppler`
- **Windows:** (Opcional, o script avisa se não encontrar)

### 4. Fontes com Suporte a Emoji
- **Linux:** `sudo apt install fonts-noto-color-emoji fonts-dejavu`
- **macOS/Windows:** Já incluído no sistema

---

## 🚀 Uso (Recomendado)

O método mais seguro e robusto é usar o script Python, que gera e verifica todos os arquivos automaticamente.

```bash
# Na raiz do projeto:
python3 tutorial/gerar_pdf.py
```

**O que ele faz:**
1. ✅ Detecta seu sistema operacional (Linux/macOS).
2. ✅ Escolhe a melhor fonte de emoji disponível.
3. ✅ Traduz dinamicamente a capa (Título, Subtítulo, Rodapé) para cada idioma.
4. ✅ Gera 5 PDFs: `tutorial-iniciantes.pdf`, `tutorial-es.pdf`, `tutorial-fr.pdf`, etc.
5. ✅ Lê os PDFs gerados e verifica se o texto está correto.

### Saída Esperada:
```text
=== PyBR PDF Generator & Verifier ===
✓ Dependencies found
✓ Using emoji font: DejaVu Sans

Processing pt-BR (tutorial-iniciantes.pdf)...
  ✓ PDF generated
  ✓ Verification passed: Subtitle found.

... (repete para todas as línguas) ...

Finished! 5/5 PDFs generated successfully.
```

---



---

## 📝 Arquivos Criados

- **tutorial-iniciantes.pdf** (Português 🇧🇷)
- **tutorial-es.pdf** (Espanhol 🇪🇸)
- **tutorial-de.pdf** (Alemão 🇩🇪)
- **tutorial-it.pdf** (Italiano 🇮🇹)
- **tutorial-fr.pdf** (Francês 🇫🇷)

---

## 💡 Dicas

1. **Fontes no Linux**: Se tiver problemas com emojis quadrados ou faltando, certifique-se de ter instalado `fonts-dejavu` e `fonts-noto-color-emoji`. O script tenta usar falbacks inteligentes.
2. **Pacotes LaTeX**: Na primeira execução, o `xelatex` pode demorar para baixar pacotes de idiomas (como suporte a grego ou cirílico usados pelo hyperref).
