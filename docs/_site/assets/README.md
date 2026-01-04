# Syntax Highlighting PyBR

Este diretório contém os arquivos de configuração para syntax highlighting da linguagem PyBR nas páginas do site.

## Arquivos

### JavaScript
- **`prism-pybr.js`**: Definição da linguagem PyBR para Prism.js
  - Define todas as palavras-chave, built-ins, e padrões de sintaxe
  - Baseado nas definições do transpilador PyBR

### CSS
- **`prism-pybr.css`**: Estilos de coloração para código PyBR
  - Tema escuro (Monokai-inspired)
  - Tema claro (GitHub-inspired)

## Como Usar

### Em arquivos Markdown

Use blocos de código com a linguagem especificada como `python` ou `pybr`:

\`\`\`python
definir ola_mundo():
    imprimir("Olá, Mundo!")
    
para i em intervalo(5):
    se i % 2 == 0:
        imprimir(f"{i} é par")
\`\`\`

### Palavras-Chave Destacadas

#### Controle de Fluxo
- `se`, `senao`, `senaose`
- `para`, `enquanto`
- `quebre`, `continue`, `retornar`
- `tente`, `exceto`, `finalmente`, `levantar`
- `passar`, `afirmar`, `com`

#### Definições
- `definir`, `funcao`, `classe`
- `global`, `importar`, `de`, `como`, `lambda`

#### Operadores e Constantes
- `e`, `ou`, `nao`, `em`, `eh`
- `Verdadeiro`, `Falso`, `Nulo`

#### Funções Built-in
- **Entrada/Saída**: `imprimir`, `entrada`
- **Conversão**: `inteiro`, `flutuante`, `texto`, `lista`, `dicionario`, `conjunto`, `tupla`
- **Manipulação**: `tamanho`, `intervalo`, `tipo`, `enumerar`
- **Matemática**: `maximo`, `minimo`, `abs`, `arredondar`
- **Iteração**: `ordenar`, `reverter`, `filtrar`, `mapear`, `qualquer`, `todos`
- **Sistema**: `abrir`, `ajuda`, `dir`, `sair`

## Cores do Tema Claro

- **Comentários**: Cinza (#6a737d)
- **Strings**: Azul escuro (#032f62)
- **Keywords**: Vermelho (#d73a49) - negrito
- **Constantes**: Azul (#005cc5) - negrito
- **Built-ins**: Roxo (#6f42c1) - negrito
- **Funções**: Roxo (#6f42c1)
- **Classes**: Roxo (#6f42c1) - negrito
- **Números**: Azul (#005cc5)
- **Operadores**: Vermelho (#d73a49)

## Cores do Tema Escuro

- **Comentários**: Cinza (#75715e) - itálico
- **Strings**: Amarelo (#e6db74)
- **Keywords**: Rosa (#f92672) - negrito
- **Constantes**: Roxo claro (#ae81ff) - negrito
- **Built-ins**: Ciano (#66d9ef) - negrito
- **Funções**: Verde (#a6e22e)
- **Classes**: Verde (#a6e22e) - negrito
- **Números**: Roxo claro (#ae81ff)
- **Operadores**: Rosa (#f92672)

## Customização

Para alterar as cores, edite o arquivo `prism-pybr.css`. O tema atual está configurado como "claro" através da classe `.light-theme` no body do HTML.

Para usar o tema escuro, remova a classe `light-theme` do `<body>` em `_layouts/default.html`.
