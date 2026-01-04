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

### 1. Seu Primeiro Programa

Crie um arquivo chamado `ola.pybr`:

```python
# Meu primeiro programa em PyBR!
imprimir("Olá, Mundo!")
imprimir("Bem-vindo ao PyBR!")
imprimir("Programar é incrível!")
```

Execute:

```bash
python pybr.py ola.pybr
```

💡 **O que aprendemos:**
- `imprimir()` exibe texto na tela
- Textos ficam entre aspas `""`
- Linhas com `#` são comentários

📖 [Ver mais exemplos](tutorial-completo#seu-primeiro-programa)

---

### 2. Variáveis

```python
nome = "Maria"      # Texto
idade = 25          # Inteiro
altura = 1.65       # Decimal
ativo = Verdadeiro  # Booleano

imprimir(f"{nome} tem {idade} anos")
```

💡 Variáveis guardam informações para usar depois

✅ **Pode usar:** `nome`, `idade_pessoa`, `valor2`, `_dado`  
❌ **Não pode:** começar com número, usar espaços, usar palavras reservadas

📖 [Guia completo de variáveis](tutorial-completo#variáveis---a-memória-do-computador)

---

### 3. Operações Matemáticas

```python
soma = 10 + 5           # 15
subtracao = 10 - 5      # 5
multiplicacao = 10 * 5  # 50
divisao = 10 / 5        # 2.0
potencia = 2 ** 3       # 8
resto = 10 % 3          # 1
```

📖 [Operadores completos](tutorial-completo#operações-matemáticas)

---

### 4. Entrada e Saída

```python
nome = entrada("Seu nome: ")
idade = inteiro(entrada("Sua idade: "))

imprimir(f"Olá, {nome}! Você tem {idade} anos")
```

💡 `entrada()` recebe texto, `inteiro()` e `flutuante()` convertem

📖 [Entrada/saída detalhada](tutorial-completo#entrada-e-saída-de-dados)

---

### 5. Condicionais

```python
nota = flutuante(entrada("Digite sua nota: "))

se nota >= 9:
    imprimir("Excelente!")
senaose nota >= 7:
    imprimir("Bom!")
senaose nota >= 5:
    imprimir("Regular")
senao:
    imprimir("Precisa estudar mais")
```

**Operadores de Comparação:**  
`==` `!=` `>` `<` `>=` `<=`

**Operadores Lógicos:**  
`e` (and), `ou` (or), `nao` (not)

📖 [Condicionais completas](tutorial-completo#condicionais---tomando-decisões)

---

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

📖 [Laços completos com exemplos](tutorial-completo#laços-de-repetição)

---

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

📖 [Funções completas](tutorial-completo#funções)

---

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

📖 [Classes e OOP completo](tutorial-completo#programação-orientada-a-objetos)

---

## 🎯 Projetos Práticos

Combine tudo que aprendeu em projetos reais! Veja exemplos completos de:

- 📝 **Lista de Tarefas** - CRUD completo com menu interativo
- 🌡️ **Conversor de Temperatura** - Funções e conversões
- 🎮 **Quiz Interativo** - Dicionários e pontuação
- 🎲 **Jogo de Adivinhação** - Números aleatórios e loops

📖 [Ver todos os projetos detalhados](tutorial-completo#projetos-práticos)  
💪 [Praticar com 23 exercícios](exercicios)

---

## 📖 Recursos de Aprendizado

### Aprofundar Conhecimento

- 📚 **[Tutorial Completo](tutorial-completo)** - Guia detalhado com 1800+ linhas
  - Guia completo do Terminal para iniciantes
  - Instalação passo a passo em todos os sistemas
  - Explicações detalhadas de cada conceito
  - Múltiplos exemplos práticos
  - Analogias e comparações do mundo real

- 💪 **[23 Exercícios Práticos](exercicios)** - Progressão do básico ao avançado
  - Nível 1: Fundamentos (8 exercícios)
  - Nível 2: Controle e Estruturas (7 exercícios)
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

[← Início](index) | [📚 Tutorial Completo](tutorial-completo) | [💪 Exercícios](exercicios) | [📖 Referência](referencia)
