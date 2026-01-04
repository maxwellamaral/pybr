---
layout: default
title: Tutorial Rápido - PyBR
---

# Tutorial PyBR - Guia Rápido

> ⚡ **Versão Rápida e Objetiva** | [📚 Ver Tutorial Completo Detalhado](tutorial-completo)

Este é um guia rápido para você começar imediatamente. Para explicações detalhadas, exemplos extras e guias para iniciantes absolutos, consulte o [Tutorial Completo](tutorial-completo).

---

## 🚀 Início Rápido

### 1. Instalar Python

```bash
# Baixe de python.org/downloads
# ⚠️ Windows: Marque "Add Python to PATH"
python --version  # Verificar instalação
```

### 2. Baixar PyBR

```bash
git clone https://github.com/maxwellamaral/pybr.git
cd pybr
```

### 3. Executar

```bash
# Arquivo
python pybr.py exemplo.pybr

# Modo interativo
python pybr.py
```

📖 [Guia de instalação detalhado](tutorial-completo#instalando-o-python) | [Guia do Terminal completo](tutorial-completo#usando-o-terminal---guia-para-iniciantes)

---

## 📚 Conceitos Fundamentais

---

## Seu Primeiro Programa

Vamos criar seu primeiro programa PyBR!

### Passo 1: Criar o Arquivo

Crie um arquivo chamado `ola.pybr` com este conteúdo:

```python
# Meu primeiro programa em PyBR!
imprimir("Olá, Mundo!")
imprimir("Bem-vindo ao PyBR!")
imprimir("Programar é incrível!")
```

### Passo 2: Executar

No terminal, na pasta do PyBR, digite:

```bash
python pybr.py ola.pybr
```

### Resultado

```
Olá, Mundo!
Bem-vindo ao PyBR!
Programar é incrível!
```

### O que Aprendemos?

- `imprimir()` exibe texto na tela
- Textos ficam entre aspas `""`
- Linhas com `#` são comentários (não executam)

📖 [Ver mais exemplos](tutorial-completo#seu-primeiro-programa)

---

## Variáveis

### 1. Olá Mundo

```python
imprimir("Olá, Mundo!")
```

💡 `imprimir()` mostra texto na tela  
📖 [Mais sobre primeiro programadade2`, `_valor`

❌ **Não pode:**
- Começar com número
- Usar espaços
- Usar palavras reservadas (se, para, etc.)

📖 [Ver mais sobre variáveis](tutorial-completo#variáveis---a-memória-do-computador)

---

## Cálculos e Operações

Python é uma calculadora poderosa!

### Operadores Básicos

```python
# Operações básicas
soma = 10 + 5          # 15
subtracao = 10 - 5     # 5
multiplicacao = 10 * 5 # 50
divisao = 10 / 5       # 2.0

imprimir("Soma:", soma)
imprimir("Subtração:", subtracao)
```

### Operadores Especiais

```python
potencia = 2 ** 3       # 8 (2 elevado a 3)
divisao_inteira = 10 // 3  # 3
resto = 10 % 3          # 1 (resto da divisão)
### 2. Variáveis

```python
nome = "Maria"      # Texto
idade = 25          # Inteiro
altura = 1.65       # Decimal
ativo = Verdadeiro  # Booleano

imprimir(f"{nome} tem {idade} anos")
```

💡 Variáveis guardam informações para usar depois  
📖 [Guia completo d!")
senaose nota >= 5:
    imprimir("Regular")
senao:
    imprimir("Precisa estudar mais")
```

### Operadores de Comparação

```python
==   # Igual a
!=   # Diferente de
>    # Maior que
<    # Menor que
>=   # Maior ou igual
<=   # Menor ou igual
```

### Operadores Lógicos

```python
# E (ambas condições verdadeiras)
idade = 20
tem_carteira = Verdadeiro

se idade >= 18 e tem_carteira:
    imprimir("Pode dirigir!")

# OU (pelo menos uma verdadeira)
dia = "sábado"
se dia == "sábado" ou dia == "domingo":
    imprimir("Final de semana!")

# NAO (inverte)
chovendo = Falso
se nao chovendo:
    imprimir("Vamos ao parque!")
```

### Exemplo Completo: Sistema de Login
### 3. Operações Matemáticas

```python
soma = 10 + 5           # 15
subtracao = 10 - 5      # 5
multiplicacao = 10 * 5  # 50
divisao = 10 / 5        # 2.0
potencia = 2 ** 3       # 8
resto = 10 % 3          # 1
```

📖 [Operadores completo", i)
# Resultado: 0, 1, 2, 3, 4

# Intervalo personalizado
para numero em intervalo(1, 6):
    imprimir(numero)
# Resultado: 1, 2, 3, 4, 5

# Com passo (pulando de 2 em 2)
para par em intervalo(0, 11, 2):
    imprimir(par)
# Resultado: 0, 2, 4, 6, 8, 10
```

### Iterando sobre Listas

```python
frutas = ["maçã", "banana", "laranja", "uva"]
### 4. Entrada e Saída

```python
nome = entrada("Seu nome: ")
idade = inteiro(entrada("Sua idade: "))

imprimir(f"Olá, {nome}! Você tem {idade} anos")
```

💡 `entrada()` recebe texto, `inteiro()` e `flutuante()` convertem  
📖 [Entrada/saída detalha

```python
numero = inteiro(entrada("Digite um número: "))

imprimir(f"\n=== TABUADA DO {numero} ===")
para i em intervalo(1, 11):
    resultado = numero * i
    imprimir(f"{numero} x {i} = {resultado}")
```

### Controle de Laços

```python
# quebre - para o laço
para i em intervalo(10):
    se i == 5:
        quebre
    imprimir(i)
# Resultado: 0, 1, 2, 3, 4

# continue - pula para próxima iteração
para i em intervalo(5):
    se i == 2:
        continue
    imprimir(i)
# Resultado: 0, 1, 3, 4
```

### Exemplo: Jogo de Adivinhação

```python
importar aleatorio

numero_secreto = aleatorio.inteiro(1, 100)
tentativas = 0

imprimir("Adivinhe o número entre 1 e 100!")

enquanto Verdadeiro:
    palpite = inteiro(entrada("Seu palpite: "))
    tentativas += 1
    
    se palpite == numero_secreto:
        imprimir(f"🎉 Parabéns! Acertou em {tentativas} tentativas!")
        quebre
    senaose palpite < numero_secreto:
### 6. Laços de Repetição

**Laço PARA:**
```python
# Repetir 5 vezes
para i em intervalo(5):
    imprimir(i)  # 0, 1, 2, 3, 4

# Com lista
frutas = ["maçã", "banana", "uva"]
para fruta em frutas:
    imprimir(fruta)
```

**Laço ENQUANTO:**
```python
contador = 0
enquanto contador < 5:
    imprimir(contador)
    contador += 1
```

**Controle:** `quebre` (sai do laço), `continue` (pula iteração)  
📖 [Laços completos com exempla Objetos!

### Conceito

Classes são como "moldes" para criar objetos. Um objeto agrupa dados (atributos) e ações (métodos).

### Criando uma Classe Simples

```python
classe Cachorro:
    definir __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    definir latir(self):
        imprimir(f"{self.nome}: Au au!")
    
    definir informacoes(self):
        imprimir(f"Nome: {self.nome}")
        imprimir(f"Idade: {self.idade} anos")

# Criar objetos (instâncias)
rex = Cachorro("Rex", 3)
bob = Cachorro("Bob", 5)

# Usar os objetos
rex.latir()           # Rex: Au au!
rex.informacoes()     # Nome: Rex, Idade: 3 anos

bob.latir()           # Bob: Au au!
bob.informacoes()     # Nome: Bob, Idade: 5 anos
```

### Exemplo: Conta Bancária

```python
classe ContaBancaria:
    definir __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial
    
    definir depositar(self, valor):
        self.saldo += valor
        imprimir(f"✓ Depósito de R${valor:.2f} realizado!")
    
    definir sacar(self, valor):
        se valor <= self.saldo:
            self.saldo -= valor
            imprimir(f"✓ Saque de R${valor:.2f} realizado!")
        senao:
            imprimir("✗ Saldo insuficiente!")
    
    definir exibir_saldo(self):
        imprimir(f"Titular: {self.titular}")
        imprimir(f"Saldo: R${self.saldo:.2f}")

# Usando a classe
conta = ContaBancaria("Maria Silva", 1000.00)
conta.exibir_saldo()
conta.depositar(500)
conta.sacar(200)
conta.exibir_saldo()
```

### Exemplo: Retângulo

```python
classe Retangulo:
    definir __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    definir calcular_area(self):
        retornar self.largura * self.altura
    
    definir calcular_perimetro(self):
        retornar 2 * (self.largura + self.altura)

ret = Retangulo(5, 3)
### 7. Funções

```python
# Função simples
definir saudar():
    imprimir("Olá!")

# Com parâmetros
definir saudar_pessoa(nome):
    imprimir(f"Olá, {nome}!")

# Com retorno
definir somar(a, b):
    retornar a + b

# Usando
saudar()
saudar_pessoa("Maria")
total = somar(10, 5)  # 15
```

💡 Funções organizam e reutilizam código  
📖 [Funções completa
    senao:
        imprimir("Opção inválida!")
```

### Projeto 2: Conversor de Temperatura

```python
definir celsius_para_fahrenheit(celsius):
    retornar (celsius * 9/5) + 32

definir fahrenheit_para_celsius(fahrenheit):
    retornar (fahrenheit - 32) * 5/9

enquanto Verdadeiro:
    imprimir("\n=== CONVERSOR DE TEMPERATURA ===")
    imprimir("1. Celsius → Fahrenheit")
    imprimir("2. Fahrenheit → Celsius")
    imprimir("3. Sair")
    
    opcao = entrada("\nEscolha: ")
    
    se opcao == "1":
        c = flutuante(entrada("Temperatura em °C: "))
        f = celsius_para_fahrenheit(c)
        imprimir(f"{c}°C = {f:.2f}°F")
    
    senaose opcao == "2":
        f = flutuante(entrada("Temperatura em °F: "))
        c = fahrenheit_para_celsius(f)
        imprimir(f"{f}°F = {c:.2f}°C")
    
    senaose opcao == "3":
        quebre
```

### Projeto 3: Quiz

```python
perguntas = [
    {
        "pergunta": "Qual é a capital do Brasil?",
        "opcoes": ["A) Rio de Janeiro", "B) São Paulo", "C) Brasília"],
        "resposta": "C"
    },
    {
        "pergunta": "Quanto é 5 + 3?",
        "opcoes": ["A) 7", "B) 8", "C) 9"],
        "resposta": "B"
    },
    {
        "pergunta": "Qual é a cor do céu?",
        "opcoes": ["A) Verde", "B) Azul", "C) Vermelho"],
        "resposta": "B"
    }
]

pontos = 0

imprimir("=== QUIZ ===\n")

para i, item em enumerar(perguntas, 1):
    imprimir(f"Pergunta {i}: {item['pergunta']}")
    para opcao em item['opcoes']:
        imprimir(opcao)
    
    resposta = entrada("Sua resposta: ").upper()
### 8. Classes e Objetos

```python
classe Cachorro:
    definir __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    definir latir(self):
        imprimir(f"{self.nome}: Au au!")

# Criar objetos
rex = Cachorro("Rex", 3)
bob = Cachorro("Bob", 5)

rex.latir()  # Rex: Au au!
bob.latir()  # Bob: Au au!
```

💡 Classes são moldes para criar objetos com atributos e métodos  
📖 [Classes e OOP completo🎯 Projetos Práticos

Combine tudo que aprendeu em projetos reais! Veja exemplos completos de:

- 📝 **Lista de Tarefas** - CRUD completo com menu interativo
- 🌡️ **Conversor de Temperatura** - Funções e conversões
- 🎮 **Quiz Interativo** - Dicionários e pontuação
- 🎲 **Jogo de Adivinhação** - Números aleatórios e loops

📖 [Ver todos os projetos detalhados](tutorial-completo#projetos-práticos)  
💪 [Praticar com 22 exercícios](exercici📖 Recursos de Aprendizado

### Aprofundar Conhecimento

- 📚 **[Tutorial Completo](tutorial-completo)** - Guia detalhado com 1800+ linhas
  - Guia completo do Terminal para iniciantes
  - Instalação passo a passo em todos os sistemas
  - Explicações detalhadas de cada conceito
  - Múltiplos exemplos práticos
  - Analogias e comparações do mundo real

- 💪 **[22 Exercícios Práticos](exercicios)** - Progressão do básico ao avançado
  - Nível 1: Fundamentos (6 exercícios)
  - Nível 2: Controle e Estruturas (8 exercícios)
  - Nível 3: Projetos Completos (8 exercícios)

- 📚 **[Referência Completa](referencia)** - Documentação técnica
  - Todas as palavras-chave traduzidas
  - Funções built-in em português
  - Tipos de dados e operadores
  - Guia de migração para Python

### Dicas de Estudo

✅ **Pratique diariamente** - Mesmo que seja 15 minutos  
✅ **Faça os exercícios na ordem** - São progressivos  
✅ **Experimente modificar os exemplos** - Aprenda fazendo  
✅ **Consulte o tutorial completo** - Para dúvidas detalhadas  
✅ **Não tenha medo de errar** - Faz parte do processo!

---

## 🎓 Quadro de Referência Rápida

| Conceito | PyBR | Python |
|----------|------|--------|
| Imprimir | `imprimir()` | `print()` |
| Entrada | `entrada()` | `input()` |
| Se/Senão | `se`/`senao`/`senaose` | `if`/`else`/`elif` |
| Para | `para ... em` | `for ... in` |
| Enquanto | `enquanto` | `while` |
| Definir função | `definir` | `def` |
| Retornar | `retornar` | `return` |
| Classe | `classe` | `class` |
| Verdadeiro/Falso | `Verdadeiro`/`Falso` | `True`/`False` |
| E/OU/NÃO | `e`/`ou`/`nao` | `and`/`or`/`not` |
| Quebrar/Continuar | `quebre`/`continue` | `break`/`continue` |

📖 [Ver referência completa](referencia)

---

**Bons estudos e divirta-se programando! 🚀**

[← Início](index) | [📚 Tutorial Completo](tutorial-completo) | [💪 Exercícios](exercicios) | [📖 Referência