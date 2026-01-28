# PyBR - Python Brasileiro / Internacional

**Português** | [Español](README.es.md) | [Deutsch](README.de.md) | [Italiano](README.it.md) | [Français](README.fr.md)

## Descrição

PyBR é um transpilador que permite escrever código Python usando palavras-chave e funções nativas em português. O projeto traduz código escrito em português para Python válido, permitindo que estudantes e desenvolvedores pratiquem programação em Python com uma sintaxe mais acessível para falantes de português. Bom para as aulas introdutórias de programação e algoritmos!

O transpilador utiliza o módulo `tokenize` do Python para analisar o código fonte, traduzindo apenas os tokens de identificadores (palavras-chave e nomes de funções) enquanto preserva strings, comentários e a estrutura do código.

**🎓 Novo para programação?** Consulte nosso [Tutorial Completo para Iniciantes](tutorial/tutorial-iniciantes.md) com exemplos práticos e 22 arquivos prontos para testar!

**🌐 Site Oficial:** [pybr.github.io](https://seu-usuario.github.io/pybr/) - Tutoriais e documentação online

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
- `tente` → `try`
- `exceto` → `except`
- `finalmente` → `finally`
- `levantar` → `raise`
- `afirmar` → `assert`
- `com` → `with`

### Definições
- `definir` → `def`
- `funcao` → `def` (alternativa)
- `classe` → `class`
- `lambda` → `lambda`
- `global` → `global`
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

#### Entrada/Saída
- `imprimir()` → `print()`
- `entrada()` → `input()`
- `abrir()` → `open()`

#### Conversão de Tipos
- `inteiro()` → `int()`
- `flutuante()` → `float()`
- `texto()` → `str()`
- `lista()` → `list()`
- `dicionario()` → `dict()`
- `conjunto()` → `set()`
- `tupla()` → `tuple()`

#### Manipulação
- `tamanho()` → `len()`
- `intervalo()` → `range()`
- `tipo()` → `type()`
- `enumerar()` → `enumerate()`

#### Matemática
- `maximo()` → `max()`
- `minimo()` → `min()`
- `abs()` → `abs()`
- `arredondar()` → `round()`

#### Ordenação/Iteração
- `ordenar()` → `sorted()`
- `reverter()` → `reversed()`
- `filtrar()` → `filter()`
- `mapear()` → `map()`
- `qualquer()` → `any()`
- `todos()` → `all()`

#### Utilidades
- `ajuda()` → `help()`
- `dir()` → `dir()`
- `sair()` → `exit()`

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

## 📚 Aprendendo a Programar com PyBR

### Tutorial para Iniciantes

Se você **nunca programou antes**, temos um guia completo feito especialmente para você! O arquivo [tutorial-iniciantes.md](tutorial/tutorial-iniciantes.md) contém:

- ✅ Explicação de todos os conceitos básicos de programação
- ✅ Exemplos práticos e intuitivos
- ✅ Analogias do mundo real para facilitar o entendimento
- ✅ 22 arquivos `.pybr` prontos para executar na pasta `exercicios/`
- ✅ Projetos completos: lista de tarefas, quiz, conversor de temperatura
- ✅ Exercícios propostos em 3 níveis de dificuldade

**Comece por aqui:** [Tutorial Completo para Iniciantes](tutorial/tutorial-iniciantes.md)

### Arquivos de Exemplo Prontos

A pasta `exercicios/` contém 22 exemplos práticos organizados por dificuldade:

```bash
# Executar qualquer exemplo
python pybr.py exercicios/01-ola-mundo.pybr
python pybr.py exercicios/11-jogo-adivinhacao.pybr
python pybr.py exercicios/20-projeto-lista-tarefas.pybr

# Ver a lista completa
ls exercicios/
```

Consulte o [README dos exercícios](exercicios/README.md) para a lista completa.

## Estrutura do Projeto

- `pybr.py` - Arquivo principal contendo o transpilador e REPL
- `tests/` - Testes funcionais automatizados (transpilador e exercícios)
- `tutorial/` - **Tutorial completo em PDF e Markdown para quem nunca programou antes** 📚
- `exercicios/` - **22 arquivos de exemplo prontos para executar** 💻
- `README.md` - Este arquivo
- `LICENSE` - Licença do projeto
- `extensao-vscode/` - Extensão VS Code para syntax highlighting

## Extensão VS Code

Para melhorar a experiência de desenvolvimento, está disponível uma extensão para Visual Studio Code que fornece syntax highlighting completo para arquivos `.pybr`:

### Instalação da Extensão

**Opção 1: Via arquivo .vsix (Recomendado)**

```bash
# Instalar a extensão usando o arquivo empacotado
code --install-extension extensao-vscode/pybr-language-1.0.1.vsix
```

Ou pela interface do VS Code:
1. Abra a aba de Extensões (Ctrl+Shift+X)
2. Clique nos três pontos `...` no topo
3. Selecione "Install from VSIX..."
4. Navegue até `extensao-vscode/pybr-language-1.0.1.vsix`

**Opção 2: Copiar manualmente**

Copie a pasta `extensao-vscode` para o diretório de extensões do VS Code:
- **Windows**: `%USERPROFILE%\.vscode\extensions\pybr-language-1.0.1`
- **macOS/Linux**: `~/.vscode/extensions/pybr-language-1.0.1`

### Recursos da Extensão

- 🎨 Syntax highlighting completo para palavras-chave em português
- 📝 Snippets para estruturas comuns (funções, classes, loops, etc.)
- ⚙️ Auto-fechamento de parênteses e aspas
- 🔧 Indentação automática inteligente
- 📂 Suporte para arquivos `.pybr` e `.pybr.py`

Para mais detalhes, consulte o [README da extensão](extensao-vscode/README.md).

## Testes Funcionais

O projeto inclui duas suítes completas de testes automatizados que validam todas as funcionalidades do transpilador PyBR e dos arquivos de exemplo.

### Executar os Testes do Transpilador

```bash
# Executar todos os testes com relatório detalhado
python tests/test_pybr.py

# Ou usar unittest diretamente com verbosidade
python -m unittest tests.test_pybr -v
```

### Executar os Testes dos Exercícios

```bash
# Testa todos os 22 arquivos de exemplo
python tests/test_exercicios.py
```

Este segundo conjunto de testes valida que todos os arquivos `.pybr` na pasta `exercicios/` estão funcionando corretamente, executando cada um deles e verificando suas saídas.

### Cobertura dos Testes

A suíte de testes contém **40 testes** que cobrem:

✅ **Tradução de Tokens** (11 testes)
- Palavras-chave de controle de fluxo
- Definições (def, class, import)
- Operadores lógicos (e, ou, nao)
- Constantes (Verdadeiro, Falso, Nulo)
- Funções nativas (imprimir, entrada, tamanho, etc.)

✅ **Transpilação** (9 testes)
- Funções e classes
- Estruturas condicionais
- Loops (para, enquanto)
- Tratamento de exceções
- Preservação de strings e comentários

✅ **Execução** (17 testes)
- Comandos básicos
- Estruturas de controle
- Operadores lógicos
- Listas e dicionários
- Recursão e f-strings

✅ **Exemplos Reais** (3 testes)
- Fibonacci recursivo
- Manipulação de listas
- Algoritmos de busca

### Resultado Esperado

Quando todos os testes passam, você verá:

```
======================================================================
Executando Testes Funcionais do PyBR
======================================================================
...
----------------------------------------------------------------------
Ran 40 tests in 0.0XXs

OK

======================================================================
RESUMO DOS TESTES
======================================================================
Testes executados: 40
Sucessos: 40
Falhas: 0
Erros: 0
======================================================================
```

## Limitações

- O transpilador traduz palavras-chave mas não mensagens de erro do Python
- Algumas funções avançadas podem não estar mapeadas
- A tradução é feita em tempo de execução (não gera arquivos `.py`)

## Contribuindo com Novos Idiomas 🌍

O PyBR quer falar todas as línguas e você pode ajudar! Adicionar um novo idioma é extremamente simples e não exige conhecimentos profundos de programação:

1.  **Crie um arquivo JSON**: Vá para a pasta `languages/` e crie um arquivo com o código da sua língua (ex: `jp.json` para japonês).
2.  **Use um template**: Copie o conteúdo de [pt-br.json](languages/pt-br.json) ou [es.json](languages/es.json).
3.  **Traduza três seções**:
    -   `keywords`: As palavras-chave do Python (if, else, for).
    -   `builtins`: As funções nativas (print, input, len).
    -   `messages`: As mensagens de interface e erro do sistema.
4.  **Envie um Pull Request**: Adicione sua tradução e ajude estudantes do mundo todo!

---

## Contribuindo no Geral

Contribuições são sempre bem-vindas! Sinta-se livre para:
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
