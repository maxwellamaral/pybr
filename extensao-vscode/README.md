# PyBR - Extensão VS Code

Extensão para Visual Studio Code que fornece syntax highlighting e snippets para a linguagem PyBR (Python Brasileiro).

PyBR é um transpilador que permite escrever código Python usando palavras-chave e funções nativas em português, ideal para aulas introdutórias de programação e algoritmos!

## Funcionalidades

### 🎨 Syntax Highlighting

Destaque de sintaxe completo para:

- **Palavras-chave de controle de fluxo**: `se`, `senao`, `senaose`, `para`, `enquanto`, `retornar`, `quebre`, `continue`, `passar`
- **Palavras-chave de exceção**: `tente`, `exceto`, `finalmente`, `levantar`
- **Palavras-chave de definição**: `definir`, `classe`, `importar`, `de`, `como`
- **Operadores lógicos**: `e`, `ou`, `nao`, `em`, `eh`
- **Constantes**: `Verdadeiro`, `Falso`, `Nulo`
- **Funções nativas**: `imprimir`, `entrada`, `tamanho`, `intervalo`, `inteiro`, `texto`, `lista`, `dicionario`, `abrir`, `ajuda`, `sair`
- **Comentários**: suporte para `#` e comentários de bloco com `'''` ou `"""`
- **Strings**: suporte completo para strings simples, duplas e f-strings
- **Números**: inteiros e decimais

### 📝 Snippets

Snippets prontos para uso rápido:

- `definir` - Cria uma função
- `classe` - Cria uma classe
- `se` - Estrutura condicional
- `sesenao` - Estrutura se/senão completa
- `para` - Loop para
- `parai` - Loop para com intervalo
- `enquanto` - Loop enquanto
- `tente` - Bloco tente/exceto
- `imprimir` - Comando imprimir
- `imprimirf` - Imprimir com f-string
- `principal` - Bloco principal do programa
- `docstring` - Comentário docstring

### ⚙️ Configurações de Linguagem

- Auto-fechamento de parênteses, colchetes e chaves
- Auto-fechamento de aspas
- Indentação automática baseada em contexto
- Suporte a folding (dobramento) de código
- Comentários de linha e bloco

## Extensões de Arquivo Suportadas

- `.pybr` - Arquivos PyBR
- `.pybr.py` - Arquivos PyBR alternativos

## Como Usar

1. Instale a extensão no VS Code
2. Crie um arquivo com extensão `.pybr` ou `.pybr.py`
3. Comece a escrever código em português!

## Exemplo de Código

```pybr
# Programa exemplo em PyBR
definir saudacao(nome):
    """Função que imprime uma saudação"""
    imprimir(f"Olá, {nome}!")

classe Animal:
    definir __init__(proprio, nome):
        proprio.nome = nome
    
    definir falar(proprio):
        imprimir(f"{proprio.nome} faz um som")

# Bloco principal
se __name__ == "__main__":
    para i em intervalo(5):
        se i % 2 == 0:
            imprimir(f"{i} é par")
        senao:
            imprimir(f"{i} é ímpar")
    
    cachorro = Animal("Rex")
    cachorro.falar()
```

## Instalação

### Método 1: Instalar a partir do arquivo .vsix (Recomendado)

Se você já possui o arquivo `pybr-language-1.0.0.vsix`:

1. Abra o VS Code
2. Use uma das opções abaixo:
   - **Via linha de comando**:
     ```bash
     code --install-extension pybr-language-1.0.0.vsix
     ```
   - **Via interface gráfica**:
     - Abra a aba de Extensões (Ctrl+Shift+X)
     - Clique nos três pontos `...` no topo
     - Selecione "Install from VSIX..."
     - Navegue até o arquivo `pybr-language-1.0.0.vsix` e selecione-o
3. Reinicie o VS Code se necessário

### Método 2: A partir do Código Fonte

1. Clone ou baixe este repositório
2. Copie a pasta `extensao-vscode` para:
   - **Windows**: `%USERPROFILE%\.vscode\extensions\pybr-language-1.0.0`
   - **macOS/Linux**: `~/.vscode/extensions/pybr-language-1.0.0`
3. Reinicie o VS Code

### Criar seu próprio pacote .vsix

Para gerar o arquivo `pybr-language-1.0.0.vsix`:

```bash
# Instale o vsce (VS Code Extension Manager)
npm install -g @vscode/vsce

# Na pasta da extensão
cd extensao-vscode
vsce package

# Isso criará o arquivo pybr-language-1.0.0.vsix
```

## Temas Recomendados

Esta extensão funciona bem com a maioria dos temas do VS Code. Temas recomendados:

- **Dark+** (padrão)
- **Monokai**
- **One Dark Pro**
- **Dracula**

## Requisitos

- Visual Studio Code versão 1.75.0 ou superior

## Problemas Conhecidos

- A extensão não valida a sintaxe em tempo real (apenas highlighting)
- Para executar código PyBR, você precisa do transpilador PyBR instalado

## Links Relacionados

- **Repositório Principal**: [https://github.com/maxwellamaral/pybr](https://github.com/maxwellamaral/pybr)
- **Transpilador PyBR**: Veja o arquivo `pybr.py` no repositório principal

## Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do repositório em [https://github.com/maxwellamaral/pybr](https://github.com/maxwellamaral/pybr)
2. Crie uma branch para sua feature
3. Faça commit das suas mudanças
4. Envie um pull request

## Autor

**Maxwell Anderson Ielpo do Amaral**

## Licença

Esta extensão está licenciada sob a Licença MIT com Requisito de Atribuição. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Citação

Se você utilizar esta extensão em trabalhos acadêmicos ou educacionais, por favor cite:

```bibtex
@software{amaral2026pybr,
  author = {Amaral, Maxwell Anderson Ielpo},
  title = {PyBR - Python Brasileiro: Um Transpilador Python com Sintaxe em Português},
  year = {2026},
  url = {https://github.com/maxwellamaral/pybr},
  note = {Ferramenta educacional para programação em Python com palavras-chave em português}
}
```

## Changelog

### 1.0.0

- Lançamento inicial
- Syntax highlighting completo para PyBR
- Snippets para estruturas comuns
- Configuração de linguagem com auto-fechamento e indentação
