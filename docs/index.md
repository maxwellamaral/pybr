---
layout: default
title: PyBR - Python em Português
---

# PyBR - Python Brasileiro 🇧🇷

Aprenda a programar em Python usando palavras em português!

## 🎯 O que é PyBR?

PyBR é um transpilador que permite escrever código Python usando palavras-chave e funções nativas em português. Perfeito para quem está começando a programar e quer aprender com uma sintaxe mais acessível.

## ✨ Características

- **🗣️ Sintaxe em Português**: Use `se`, `senao`, `para`, `enquanto`, `imprimir()` e muito mais
- **📚 Tutorial Completo**: Aprenda do zero com exemplos práticos
- **🎮 23 Exercícios**: Práticas progressivas do básico ao avançado
- **💻 REPL Interativo**: Teste código em tempo real
- **🚀 Fácil de Usar**: Execute arquivos `.pybr` diretamente

## 🚀 Início Rápido

### Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/pybr.git
cd pybr

# Execute um exemplo
python pybr.py exemplo.pybr
```

### Seu Primeiro Programa

Crie um arquivo `ola.pybr`:

```python
imprimir("Olá, Mundo!")
imprimir("Bem-vindo ao PyBR!")

# Variáveis em português
nome = entrada("Qual é o seu nome? ")
imprimir("Prazer em te conhecer,", nome)
```

Execute:

```bash
python pybr.py ola.pybr
```

## 📖 Documentação

- **[Tutorial Completo](tutorial)** - Aprenda programação do zero
- **[Exercícios Práticos](exercicios)** - 23 exercícios progressivos
- **[Referência da Linguagem](referencia)** - Documentação técnica completa

## 🎓 Para Quem é o PyBR?

- **Iniciantes em Programação**: Aprenda sem a barreira do idioma
- **Professores**: Ensine algoritmos em português
- **Estudantes**: Pratique lógica de programação de forma intuitiva
- **Curiosos**: Experimente programar de um jeito diferente

## 💡 Exemplos de Código

### 1. Variáveis e Tipos

```python
# Textos
nome = "Maria"
sobrenome = "Silva"
nome_completo = nome + " " + sobrenome

# Números
idade = 20
altura = 1.65
peso = 58.5

# Booleanos
estudante = Verdadeiro
trabalhando = Falso

# Listas
frutas = ["maçã", "banana", "laranja"]
notas = [8.5, 9.0, 7.5, 10.0]

# Dicionários
pessoa = {
    "nome": "João",
    "idade": 25,
    "cidade": "São Paulo"
}

imprimir(f"{nome_completo} tem {idade} anos")
imprimir(f"Frutas: {frutas}")
imprimir(f"Pessoa: {pessoa['nome']} de {pessoa['cidade']}")
```

### 2. Estruturas Condicionais

```python
# Sistema de notas
nota = flutuante(entrada("Digite sua nota: "))

se nota >= 9.0:
    conceito = "A - Excelente!"
senaose nota >= 7.0:
    conceito = "B - Bom"
senaose nota >= 5.0:
    conceito = "C - Regular"
senao:
    conceito = "D - Insuficiente"

imprimir(f"Seu conceito é: {conceito}")

# Verificação de idade
idade = inteiro(entrada("Sua idade: "))

se idade >= 18:
    imprimir("✓ Você pode dirigir")
    se idade >= 65:
        imprimir("✓ Você tem direito à gratuidade")
senao:
    faltam = 18 - idade
    imprimir(f"✗ Faltam {faltam} anos para você dirigir")
```

### 3. Laços de Repetição

```python
# Tabuada completa
numero = inteiro(entrada("Digite um número: "))

imprimir(f"\n=== TABUADA DO {numero} ===")
para i em intervalo(1, 11):
    resultado = numero * i
    imprimir(f"{numero} x {i:2d} = {resultado:3d}")

# Números pares de 0 a 20
imprimir("\nNúmeros pares:")
para num em intervalo(0, 21, 2):
    imprimir(num, fim=" ")

# Contagem regressiva
imprimir("\n\nContagem regressiva:")
contador = 10
enquanto contador >= 0:
    imprimir(f"{contador}...", fim=" ")
    contador -= 1
imprimir("🚀 Lançamento!")
```

### 4. Funções

```python
# Funções matemáticas
definir somar(a, b):
    retornar a + b

definir multiplicar(a, b):
    retornar a * b

definir potencia(base, expoente=2):
    retornar base ** expoente

# Funções com validação
definir calcular_imc(peso, altura):
    se altura <= 0 ou peso <= 0:
        retornar Nulo
    
    imc = peso / (altura ** 2)
    retornar arredondar(imc, 2)

definir classificar_imc(imc):
    se imc < 18.5:
        retornar "Abaixo do peso"
    senaose imc < 25:
        retornar "Peso normal"
    senaose imc < 30:
        retornar "Sobrepeso"
    senao:
        retornar "Obesidade"

# Usando as funções
peso = 70
altura = 1.75
imc = calcular_imc(peso, altura)

imprimir(f"IMC: {imc}")
imprimir(f"Classificação: {classificar_imc(imc)}")
imprimir(f"5² = {potencia(5)}")
imprimir(f"2⁵ = {potencia(2, 5)}")
```

### 5. Listas e Manipulação

```python
# Criando e manipulando listas
numeros = []

# Adicionando elementos
para i em intervalo(1, 6):
    numeros.adicionar(i * 2)

imprimir("Lista:", numeros)
imprimir("Primeiro:", numeros[0])
imprimir("Último:", numeros[-1])
imprimir("Tamanho:", tamanho(numeros))

# Operações com listas
soma = sum(numeros)
media = soma / tamanho(numeros)
maior = max(numeros)
menor = min(numeros)

imprimir(f"Soma: {soma}")
imprimir(f"Média: {media}")
imprimir(f"Maior: {maior}")
imprimir(f"Menor: {menor}")

# Filtrando listas
pares = [n para n em numeros se n % 2 == 0]
impares = [n para n em numeros se n % 2 != 0]

imprimir("Pares:", pares)
imprimir("Ímpares:", impares)
```

### 6. Classes e Objetos

```python
# Classe Pessoa
classe Pessoa:
    definir __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    definir apresentar(self):
        imprimir(f"Olá! Meu nome é {self.nome}")
        imprimir(f"Tenho {self.idade} anos")
    
    definir fazer_aniversario(self):
        self.idade += 1
        imprimir(f"🎉 Feliz aniversário! Agora tenho {self.idade} anos")

# Criando objetos
maria = Pessoa("Maria", 25)
joao = Pessoa("João", 30)

maria.apresentar()
maria.fazer_aniversario()

# Classe ContaBancaria
classe ContaBancaria:
    definir __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        self.historico = []
    
    definir depositar(self, valor):
        self.saldo += valor
        self.historico.adicionar(f"Depósito: +R$ {valor:.2f}")
        imprimir(f"✓ Depósito de R$ {valor:.2f} realizado")
    
    definir sacar(self, valor):
        se valor <= self.saldo:
            self.saldo -= valor
            self.historico.adicionar(f"Saque: -R$ {valor:.2f}")
            imprimir(f"✓ Saque de R$ {valor:.2f} realizado")
        senao:
            imprimir("✗ Saldo insuficiente!")
    
    definir extrato(self):
        imprimir(f"\n=== EXTRATO - {self.titular} ===")
        para operacao em self.historico:
            imprimir(operacao)
        imprimir(f"Saldo atual: R$ {self.saldo:.2f}")

# Usando a conta
conta = ContaBancaria("Ana Silva", 1000)
conta.depositar(500)
conta.sacar(200)
conta.sacar(2000)  # Vai dar erro
conta.extrato()
```

### 7. Calculadora de IMC Completa

```python
definir calcular_imc(peso, altura):
    """Calcula o IMC (Índice de Massa Corporal)"""
    retornar peso / (altura ** 2)

definir classificar_imc(imc):
    """Retorna a classificação do IMC"""
    se imc < 18.5:
        retornar "Abaixo do peso", "⚠️"
    senaose imc < 25:
        retornar "Peso normal", "✓"
    senaose imc < 30:
        retornar "Sobrepeso", "⚠️"
    senaose imc < 35:
        retornar "Obesidade grau I", "⚠️"
    senaose imc < 40:
        retornar "Obesidade grau II", "⚠️"
    senao:
        retornar "Obesidade grau III", "⚠️"

# Programa principal
imprimir("=== CALCULADORA DE IMC ===\n")

peso = flutuante(entrada("Digite seu peso (kg): "))
altura = flutuante(entrada("Digite sua altura (m): "))

imc = calcular_imc(peso, altura)
classificacao, icone = classificar_imc(imc)

imprimir(f"\nSeu IMC é: {imc:.2f}")
imprimir(f"Classificação: {icone} {classificacao}")

# Dicas baseadas no IMC
se imc < 18.5:
    imprimir("\n💡 Dica: Consulte um nutricionista para ganhar peso de forma saudável")
senaose imc >= 25:
    imprimir("\n💡 Dica: Considere uma dieta balanceada e exercícios físicos")
senao:
    imprimir("\n💡 Dica: Continue mantendo hábitos saudáveis!")
```

### 8. Jogo de Adivinhação Completo

```python
importar aleatorio

definir jogar():
    numero_secreto = aleatorio.inteiro(1, 100)
    tentativas = 0
    max_tentativas = 10
    
    imprimir("=== JOGO DE ADIVINHAÇÃO ===")
    imprimir(f"Adivinhe o número entre 1 e 100")
    imprimir(f"Você tem {max_tentativas} tentativas\n")
    
    enquanto tentativas < max_tentativas:
        tentativas += 1
        restantes = max_tentativas - tentativas + 1
        
        palpite = inteiro(entrada(f"Tentativa {tentativas}/{max_tentativas}: "))
        
        se palpite < 1 ou palpite > 100:
            imprimir("⚠️ Digite um número entre 1 e 100!")
            tentativas -= 1
            continue
        
        se palpite == numero_secreto:
            imprimir(f"\n🎉 PARABÉNS! Você acertou em {tentativas} tentativas!")
            
            se tentativas <= 3:
                imprimir("⭐ Desempenho EXCELENTE!")
            senaose tentativas <= 6:
                imprimir("👍 Bom desempenho!")
            senao:
                imprimir("✓ Você conseguiu!")
            
            retornar Verdadeiro
        
        senaose palpite < numero_secreto:
            diferenca = numero_secreto - palpite
            se diferenca > 20:
                imprimir("📈 Muito baixo! Tente um número BEM maior")
            senao:
                imprimir("📈 Um pouco baixo! Tente maior")
        
        senao:
            diferenca = palpite - numero_secreto
            se diferenca > 20:
                imprimir("📉 Muito alto! Tente um número BEM menor")
            senao:
                imprimir("📉 Um pouco alto! Tente menor")
        
        se restantes > 0:
            imprimir(f"Restam {restantes} tentativas\n")
    
    imprimir(f"\n😞 Game Over! O número era {numero_secreto}")
    retornar Falso

# Jogar
jogar()

# Perguntar se quer jogar novamente
enquanto Verdadeiro:
    resposta = entrada("\nJogar novamente? (s/n): ")
    se resposta.lower() == 's':
        imprimir("\n" + "="*30 + "\n")
        jogar()
    senao:
        imprimir("Obrigado por jogar! 👋")
        quebre
```

### 9. Lista de Tarefas

```python
tarefas = []

definir adicionar_tarefa():
    tarefa = entrada("Digite a tarefa: ")
    prioridade = entrada("Prioridade (alta/média/baixa): ").lower()
    tarefas.adicionar({"tarefa": tarefa, "prioridade": prioridade, "concluida": Falso})
    imprimir("✓ Tarefa adicionada com sucesso!")

definir listar_tarefas():
    se tamanho(tarefas) == 0:
        imprimir("Nenhuma tarefa cadastrada!")
        retornar
    
    imprimir("\n=== SUAS TAREFAS ===")
    para i, item em enumerar(tarefas, 1):
        status = "✓" se item["concluida"] senao "☐"
        prioridade = item["prioridade"].upper()
        tarefa = item["tarefa"]
        
        # Emoji por prioridade
        emoji = "🔴" se prioridade == "ALTA" senao "🟡" se prioridade == "MÉDIA" senao "🟢"
        
        imprimir(f"{i}. {status} {emoji} [{prioridade}] {tarefa}")

definir concluir_tarefa():
    listar_tarefas()
    numero = inteiro(entrada("\nNúmero da tarefa concluída: "))
    
    se 1 <= numero <= tamanho(tarefas):
        tarefas[numero - 1]["concluida"] = Verdadeiro
        imprimir("✓ Tarefa marcada como concluída!")
    senao:
        imprimir("✗ Número inválido!")

definir remover_tarefa():
    listar_tarefas()
    numero = inteiro(entrada("\nNúmero da tarefa a remover: "))
    
    se 1 <= numero <= tamanho(tarefas):
        tarefas.pop(numero - 1)
        imprimir("✓ Tarefa removida!")
    senao:
        imprimir("✗ Número inválido!")

# Menu principal
enquanto Verdadeiro:
    imprimir("\n=== GERENCIADOR DE TAREFAS ===")
    imprimir("1. Adicionar tarefa")
    imprimir("2. Listar tarefas")
    imprimir("3. Concluir tarefa")
    imprimir("4. Remover tarefa")
    imprimir("5. Sair")
    
    opcao = entrada("\nEscolha uma opção: ")
    
    se opcao == "1":
        adicionar_tarefa()
    senaose opcao == "2":
        listar_tarefas()
    senaose opcao == "3":
        concluir_tarefa()
    senaose opcao == "4":
        remover_tarefa()
    senaose opcao == "5":
        imprimir("Até logo! 👋")
        quebre
    senao:
        imprimir("✗ Opção inválida!")
```

## 🎯 Começar Agora

### Trilha de Aprendizado Recomendada

1. **📖 [Tutorial Completo](tutorial)** - 2-3 horas
   - Conceitos básicos de programação
   - Estruturas de dados e controle
   - Funções e classes
   - Projetos práticos

2. **💪 [Exercícios Práticos](exercicios)** - Progressivo
   - Nível 1: Básico (exercícios 1-7)
   - Nível 2: Intermediário (exercícios 8-14)
   - Nível 3: Avançado (exercícios 15-22)

3. **📚 [Referência](referencia)** - Consulta
   - Palavras-chave completas
   - Funções built-in
   - Tipos de dados
   - Operadores

### Por Onde Começar?

#### Se você NUNCA programou:
👉 Comece pelo **[Tutorial Completo](tutorial)** e faça os exercícios na ordem

#### Se você JÁ programa em outra linguagem:
👉 Veja a **[Referência](referencia)** e faça os exercícios avançados (15-22)

#### Se você é PROFESSOR:
👉 Use o **[Material Didático](tutorial-completo)** em suas aulas

## 🌟 Características Detalhadas

### Palavras-Chave Traduzidas

| PyBR | Python | Uso |
|------|--------|-----|
| `imprimir` | `print` | Exibir na tela |
| `entrada` | `input` | Receber dados |
| `se` | `if` | Condicional |
| `senao` | `else` | Alternativa |
| `senaose` | `elif` | Condicional múltipla |
| `para` | `for` | Laço for |
| `enquanto` | `while` | Laço while |
| `definir` | `def` | Criar função |
| `classe` | `class` | Criar classe |
| `retornar` | `return` | Retornar valor |
| `importar` | `import` | Importar módulo |
| `de` | `from` | Importar de |
| `como` | `as` | Alias |
| `em` | `in` | Pertence a |
| `quebre` | `break` | Sair do laço |
| `continue` | `continue` | Próxima iteração |
| `Verdadeiro` | `True` | Valor verdadeiro |
| `Falso` | `False` | Valor falso |
| `Nulo` | `None` | Valor nulo |
| `e` | `and` | E lógico |
| `ou` | `or` | OU lógico |
| `nao` | `not` | NÃO lógico |

### Funções Built-in Traduzidas

| PyBR | Python | Descrição |
|------|--------|-----------|
| `entrada()` | `input()` | Entrada de dados |
| `imprimir()` | `print()` | Saída de dados |
| `inteiro()` | `int()` | Converter para inteiro |
| `flutuante()` | `float()` | Converter para decimal |
| `texto()` | `str()` | Converter para texto |
| `tamanho()` | `len()` | Tamanho de sequência |
| `intervalo()` | `range()` | Intervalo numérico |
| `enumerar()` | `enumerate()` | Enumerar itens |
| `maximo()` | `max()` | Valor máximo |
| `minimo()` | `min()` | Valor mínimo |
| `arredondar()` | `round()` | Arredondar número |
| `tipo()` | `type()` | Tipo da variável |
| `lista()` | `list()` | Criar lista |
| `dicionario()` | `dict()` | Criar dicionário |
| `conjunto()` | `set()` | Criar conjunto |
| `tupla()` | `tuple()` | Criar tupla |
| `ordenar()` | `sorted()` | Ordenar elementos |
| `reverter()` | `reversed()` | Reverter ordem |
| `filtrar()` | `filter()` | Filtrar elementos |
| `mapear()` | `map()` | Mapear função |
| `qualquer()` | `any()` | Algum é verdadeiro |
| `todos()` | `all()` | Todos são verdadeiros |
| `abrir()` | `open()` | Abrir arquivo |
| `ajuda()` | `help()` | Ajuda sobre objeto |
| `dir()` | `dir()` | Listar atributos |
| `sair()` | `exit()` | Sair do programa |
| `abs()` | `abs()` | Valor absoluto |

**Total: 29 funções nativas traduzidas** - [Ver referência completa](referencia)

## 📊 Estatísticas do Projeto

- ✅ **23 Exercícios** progressivos do básico ao avançado
- ✅ **2000+ Linhas** de tutorial detalhado
- ✅ **23 Palavras-chave** traduzidas (controle, exceções, definições)
- ✅ **29 Funções** built-in em português
- ✅ **100% Open Source** sob licença MIT

## 🎓 Material Didático

### Para Estudantes
- Tutorial passo a passo com explicações detalhadas
- Exemplos práticos e aplicados
- Exercícios com dificuldade progressiva
- Projetos reais para praticar

### Para Professores
- Material completo pronto para uso
- Exercícios organizados por nível
- Exemplos testados e funcionais
- Documentação de referência completa

### Vantagens Pedagógicas
1. **Reduz barreira linguística** - Foco na lógica, não no inglês
2. **Sintaxe intuitiva** - Comandos que fazem sentido
3. **Transição natural** - Migração fácil para Python padrão
4. **Feedback imediato** - Executa código real

## 🔧 Instalação Detalhada

### Requisitos
- Python 3.6 ou superior
- Sistema operacional: Windows, Linux ou macOS
- Editor de texto ou IDE (recomendado: VS Code)

### Passo a Passo

#### 1. Instale o Python
- **Windows**: Baixe de [python.org](https://www.python.org/downloads/)
- **Linux**: `sudo apt install python3` (Debian/Ubuntu)
- **macOS**: `brew install python3` (com Homebrew)

#### 2. Clone o Repositório
```bash
git clone https://github.com/seu-usuario/pybr.git
cd pybr
```

#### 3. Execute um Exemplo
```bash
python pybr.py exemplo.pybr
```

#### 4. (Opcional) Instale a Extensão VS Code
1. Copie a pasta `extensao-vscode/`
2. No VS Code: Extensions → Install from VSIX
3. Aproveite syntax highlighting colorido!

## 💻 Modos de Uso

### 1. Executar Arquivo
```bash
python pybr.py meu_programa.pybr
```

### 2. REPL Interativo
```bash
python pybr.py
```
Digite comandos PyBR e veja resultados instantâneos!

### 3. Converter para Python
```bash
python pybr.py meu_programa.pybr --output programa.py
```
Gera código Python padrão equivalente.

## 📱 Compatibilidade

### Funciona Com
- ✅ Todas as bibliotecas Python padrão
- ✅ Bibliotecas externas (numpy, pandas, etc.)
- ✅ Frameworks (Django, Flask, etc.)
- ✅ IDEs e editores populares

### Limitações
- ⚠️ Nomes de bibliotecas permanecem em inglês
- ⚠️ Alguns conceitos avançados requerem Python padrão
- ℹ️ Para projetos grandes, migre para Python padrão

## 🤝 Contribuindo

Contribuições são muito bem-vindas! 

### Como Contribuir
1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

### Áreas para Contribuir
- 📝 Melhorar documentação
- 🐛 Reportar e corrigir bugs
- ✨ Adicionar novas funcionalidades
- 📚 Criar mais exercícios
- 🌍 Traduzir para outros idiomas
- 🎨 Melhorar a extensão VS Code

## ❓ FAQ (Perguntas Frequentes)

**P: PyBR é uma linguagem de programação?**  
R: Não exatamente. PyBR é um transpilador que converte código em português para Python. Você está realmente programando em Python!

**P: Posso usar bibliotecas Python?**  
R: Sim! Você pode usar qualquer biblioteca Python normalmente.

**P: PyBR é indicado para iniciantes?**  
R: Sim! Foi criado especialmente para brasileiros que estão começando a programar.

**P: Depois de aprender PyBR, posso migrar para Python?**  
R: Com certeza! A transição é muito natural, pois os conceitos são os mesmos.

**P: PyBR é usado profissionalmente?**  
R: PyBR é uma ferramenta didática. Para projetos profissionais, recomendamos Python padrão.

**P: É open source?**  
R: Sim! Todo o código está disponível no GitHub sob licença MIT.

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](../LICENSE) para mais detalhes.

## 🔗 Links Úteis

- [📦 GitHub Repository](https://github.com/maxwellamaral/pybr)
- [🐛 Reportar Issues](https://github.com/maxwellamaral/pybr/issues)
- [🤝 Contribuir](https://github.com/maxwellamaral/pybr/pulls)
- [📖 Tutorial Completo](tutorial-completo)
- [🎮 23 Exercícios](exercicios)
- [📚 Referência Completa](referencia)

## 🙏 Agradecimentos

Obrigado a todos que contribuíram para este projeto e à comunidade Python brasileira!

---

**Feito com ❤️ para democratizar o ensino de programação no Brasil**

[🚀 Começar Agora](tutorial) | [📖 Tutorial](tutorial) | [💪 Exercícios](exercicios) | [📚 Referência](referencia)
