# PyBR - Python Brasileiro

## Descrição

PyBR é um transpilador que permite escrever código Python usando palavras-chave e funções nativas em português. O projeto traduz código escrito em português para Python válido, permitindo que estudantes e desenvolvedores pratiquem programação em Python com uma sintaxe mais acessível para falantes de português. Bom para as aulas introdutórias de programação e algoritmos!

O transpilador utiliza o módulo `tokenize` do Python para analisar o código fonte, traduzindo apenas os tokens de identificadores (palavras-chave e nomes de funções) enquanto preserva strings, comentários e a estrutura do código.

## Funcionalidades

- **Palavras-chave em Português**: Use `se`, `senao`, `para`, `enquanto`, `definir`, `classe` etc.
- **Funções Nativas Traduzidas**: `imprimir()`, `entrada()`, `tamanho()`, `intervalo()` etc.
- **REPL Interativo**: Shell interativo para testar código em tempo real
- **Execução de Arquivos**: Execute arquivos `.pybr` diretamente
- **Demonstração Integrada**: Código de exemplo executado automaticamente

## Mapeamento de Palavras-chave

### Controle de Fluxo
- `se` → `if`
- `senao` → `else`
- `senaose` → `elif`
- `para` → `for`
- `enquanto` → `while`
- `retornar` → `return`
- `quebre` → `break`
- `continue` → `continue`
- `passar` → `pass`

### Definições
- `definir` → `def`
- `classe` → `class`
- `importar` → `import`
- `de` → `from`
- `como` → `as`

### Operadores e Constantes
- `e` → `and`
- `ou` → `or`
- `nao` → `not`
- `em` → `in`
- `eh` → `is`
- `Verdadeiro` → `True`
- `Falso` → `False`
- `Nulo` → `None`

### Funções Nativas
- `imprimir()` → `print()`
- `entrada()` → `input()`
- `tamanho()` → `len()`
- `intervalo()` → `range()`
- `inteiro()` → `int()`
- `texto()` → `str()`
- `lista()` → `list()`
- `dicionario()` → `dict()`

## Como Executar

### Requisitos
- Python 3.6 ou superior

### Modo Interativo (REPL)

Para iniciar o shell interativo:

```bash
python pybr.py
```

Isso executará primeiro o código de demonstração e depois abrirá o REPL onde você pode testar comandos:

```
>>> imprimir("Olá, Mundo!")
Olá, Mundo!
>>> para i em intervalo(5):
...     imprimir(i)
...
0
1
2
3
4
```

Digite `sair()` para encerrar o REPL.

### Executar um Arquivo

Crie um arquivo com código PyBR (ex: `meu_programa.pybr`) e execute:

```bash
python pybr.py meu_programa.pybr
```

### Exemplo de Código PyBR

```python
# Programa de exemplo em PyBR
definir saudacao(nome):
    imprimir(f"Olá, {nome}!")

para i em intervalo(10):
    se i % 2 == 0:
        imprimir(f"{i} é par")
    senao:
        imprimir(f"{i} é ímpar")

classe Animal:
    definir __init__(proprio, nome):
        proprio.nome = nome
    
    definir falar(proprio):
        imprimir(f"{proprio.nome} faz um som")

cachorro = Animal("Rex")
cachorro.falar()
```

## Estrutura do Projeto

- `pybr.py` - Arquivo principal contendo o transpilador e REPL
- `README.md` - Este arquivo
- `LICENSE` - Licença do projeto

## Limitações

- O transpilador traduz palavras-chave mas não mensagens de erro do Python
- Algumas funções avançadas podem não estar mapeadas
- A tradução é feita em tempo de execução (não gera arquivos `.py`)

## Contribuindo

Contribuições são bem-vindas! Sinta-se livre para:
- Adicionar novas traduções de funções nativas
- Melhorar o sistema de detecção de blocos no REPL
- Adicionar suporte para mais construções do Python
- Melhorar a documentação

## Citação

Se você utilizar este projeto em trabalhos acadêmicos ou educacionais, por favor cite:

```bibtex
@software{amaral2026pybr,
  author = {Amaral, Maxwell Anderson Ielpo},
  title = {PyBR - Python Brasileiro: Um Transpilador Python com Sintaxe em Português},
  year = {2026},
  url = {https://github.com/maxwellamaral/pybr},
  note = {Ferramenta educacional para programação em Python com palavras-chave em português}
}
```

## Autor

**Maxwell Anderson Ielpo do Amaral**

## Licença

Este projeto está licenciado sob uma licença de uso educacional - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
