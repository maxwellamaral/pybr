---
layout: default
title: Exercícios - PyBR
---

# 💪 Exercícios Práticos PyBR

22 exercícios progressivos para você dominar programação do básico ao avançado!

## 📚 Sobre os Exercícios

Os exercícios foram cuidadosamente desenvolvidos para ensinar programação de forma progressiva. Cada exercício introduz novos conceitos enquanto reforça os anteriores.

**Tempo estimado:** 10-20 minutos por exercício  
**Pré-requisitos:** Python 3.6+ instalado  
**Localização:** Pasta [`exercicios/`](https://github.com/maxwellamaral/pybr/tree/main/exercicios)

## 🎯 Trilhas de Aprendizado

### 🟢 Nível 1: Fundamentos (Exercícios 1-6)
**Objetivo:** Aprender conceitos básicos de programação  
**Tempo:** 2-3 horas  
**Você vai aprender:** Variáveis, tipos de dados, entrada/saída, operadores

### 🟡 Nível 2: Controle e Estruturas (Exercícios 7-14)
**Objetivo:** Dominar estruturas de controle e funções  
**Tempo:** 4-5 horas  
**Você vai aprender:** Condicionais, laços, listas, funções

### 🔴 Nível 3: Programação Avançada (Exercícios 15-22)
**Objetivo:** Criar projetos completos com OOP  
**Tempo:** 5-6 horas  
**Você vai aprender:** Classes, projetos reais, boas práticas

---

## 🟢 Exercícios Básicos (1-6)

### 01. Olá Mundo 👋
**Conceitos:** `imprimir()`, strings  
**Dificuldade:** ⭐☆☆☆☆  
**Tempo:** 5 minutos

Seu primeiro programa! Aprenda a exibir mensagens na tela.

```python
imprimir("Olá, Mundo!")
imprimir("Bem-vindo ao PyBR!")
```

**O que você aprende:**
- Como usar a função `imprimir()`
- Sintaxe básica do PyBR
- Executar um programa

**Desafio extra:**
- Exiba seu nome e idade
- Crie uma mensagem de boas-vindas personalizada

---

### 02. Variáveis 📦
**Conceitos:** Variáveis, tipos de dados  
**Dificuldade:** ⭐☆☆☆☆  
**Tempo:** 10 minutos

Aprenda a armazenar informações em variáveis.

```python
# Textos (strings)
nome = "Ana"
sobrenome = "Silva"

# Números inteiros
idade = 15
ano = 2024

# Números decimais
altura = 1.65
peso = 52.5

# Booleanos
estudante = Verdadeiro

imprimir(f"{nome} {sobrenome} tem {idade} anos")
```

**O que você aprende:**
- Criar e usar variáveis
- Tipos de dados (string, int, float, bool)
- Concatenação e formatação de strings

**Desafio extra:**
- Crie variáveis para um personagem de jogo
- Use diferentes tipos de dados

---

### 03. Cálculos ➕➖✖️➗
**Conceitos:** Operadores aritméticos  
**Dificuldade:** ⭐☆☆☆☆  
**Tempo:** 10 minutos

Faça operações matemáticas com Python.

```python
a = 10
b = 3

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
potencia = a ** b

imprimir(f"Soma: {soma}")
imprimir(f"Divisão: {divisao:.2f}")
```

**O que você aprende:**
- Operadores: `+`, `-`, `*`, `/`, `%`, `**`
- Ordem de precedência
- Formatação de números

**Desafio extra:**
- Calcule a área de um círculo (π × r²)
- Converta temperatura Celsius para Fahrenheit

---

### 04. Entrada e Saída 🔄
**Conceitos:** `entrada()`, conversão de tipos  
**Dificuldade:** ⭐⭐☆☆☆  
**Tempo:** 15 minutos

Interaja com o usuário recebendo dados.

```python
nome = entrada("Qual é o seu nome? ")
idade = inteiro(entrada("Qual é a sua idade? "))

imprimir(f"Olá, {nome}!")
imprimir(f"Você tem {idade} anos")

se idade >= 18:
    imprimir("Você é maior de idade")
senao:
    imprimir("Você é menor de idade")
```

**O que você aprende:**
- Usar `entrada()` para receber dados
- Converter tipos com `inteiro()` e `flutuante()`
- Validar entrada do usuário

**Desafio extra:**
- Peça nome, idade e cidade do usuário
- Crie uma calculadora de soma de dois números

---

### 05. Calculadora de IMC 📊
**Conceitos:** Fórmulas, conversão, condicionais  
**Dificuldade:** ⭐⭐☆☆☆  
**Tempo:** 15 minutos

Crie uma calculadora de Índice de Massa Corporal.

```python
peso = flutuante(entrada("Digite seu peso (kg): "))
altura = flutuante(entrada("Digite sua altura (m): "))

imc = peso / (altura ** 2)

imprimir(f"Seu IMC é: {imc:.2f}")

se imc < 18.5:
    imprimir("Abaixo do peso")
senaose imc < 25:
    imprimir("Peso normal")
senaose imc < 30:
    imprimir("Sobrepeso")
senao:
    imprimir("Obesidade")
```

**O que você aprende:**
- Aplicar fórmulas matemáticas
- Estruturas condicionais
- Classificação por faixas

**Desafio extra:**
- Adicione mais faixas de IMC
- Mostre dicas de saúde baseadas no resultado

---

### 06. Estruturas Condicionais 🔀
**Conceitos:** `se`, `senao`, `senaose`  
**Dificuldade:** ⭐⭐☆☆☆  
**Tempo:** 15 minutos

Tome decisões no código com condicionais.

```python
nota = flutuante(entrada("Digite sua nota (0-10): "))

se nota >= 9:
    conceito = "A - Excelente!"
senaose nota >= 7:
    conceito = "B - Bom"
senaose nota >= 5:
    conceito = "C - Regular"
senao:
    conceito = "D - Insuficiente"

imprimir(f"Seu conceito é: {conceito}")
```

**O que você aprende:**
- Condicionais simples e compostas
- Operadores de comparação
- Lógica de decisão

**Desafio extra:**
- Crie um sistema de desconto baseado no valor da compra
- Verifique se um ano é bissexto

---

## 🟡 Exercícios Intermediários (7-14)

### 07. Sistema de Login 🔐
**Conceitos:** Dicionários, validação  
**Dificuldade:** ⭐⭐☆☆☆  
**Tempo:** 20 minutos

Crie um sistema simples de autenticação.

```python
usuarios = {
    "admin": "123456",
    "maria": "senha123",
    "joao": "abc456"
}

usuario = entrada("Usuário: ")
senha = entrada("Senha: ")

se usuario em usuarios e usuarios[usuario] == senha:
    imprimir(f"✓ Bem-vindo, {usuario}!")
senao:
    imprimir("✗ Usuário ou senha incorretos!")
```

**O que você aprende:**
- Dicionários (chave-valor)
- Operador `em` (in)
- Validação de dados

**Desafio extra:**
- Limite o número de tentativas
- Adicione opção de cadastro de novos usuários

---

### 08. Laços com Para 🔁
**Conceitos:** `para`, `intervalo()`  
**Dificuldade:** ⭐⭐☆☆☆  
**Tempo:** 20 minutos

Repita ações com laços de repetição.

```python
# Contagem de 1 a 10
para i em intervalo(1, 11):
    imprimir(f"Número: {i}")

# Números pares de 0 a 20
para num em intervalo(0, 21, 2):
    imprimir(num, fim=" ")

# Iterando sobre listas
frutas = ["maçã", "banana", "laranja"]
para fruta em frutas:
    imprimir(f"Eu gosto de {fruta}")
```

**O que você aprende:**
- Laço `para` (for)
- Função `intervalo()` (range)
- Iterar sobre sequências

**Desafio extra:**
- Imprima todos os múltiplos de 5 até 100
- Calcule a soma de números de 1 a 100

---

### 09. Tabuada ✖️
**Conceitos:** Laços aninhados, formatação  
**Dificuldade:** ⭐⭐⭐☆☆  
**Tempo:** 20 minutos

Gere tabuadas completas.

```python
numero = inteiro(entrada("Digite um número: "))

imprimir(f"\n=== TABUADA DO {numero} ===")
para i em intervalo(1, 11):
    resultado = numero * i
    imprimir(f"{numero} x {i:2d} = {resultado:3d}")

# Tabuada completa (1 a 10)
para n em intervalo(1, 11):
    imprimir(f"\n=== Tabuada do {n} ===")
    para i em intervalo(1, 11):
        imprimir(f"{n} x {i} = {n*i}")
```

**O que você aprende:**
- Laços aninhados
- Formatação de saída
- Organização de código

**Desafio extra:**
- Crie uma tabuada completa de 1 a 10 em formato de tabela
- Adicione cores ou emojis na saída

---

### 10. Laço Enquanto 🔄
**Conceitos:** `enquanto`, `quebre`, `continue`  
**Dificuldade:** ⭐⭐⭐☆☆  
**Tempo:** 25 minutos

Use laços com condição.

```python
# Contagem regressiva
contador = 10
enquanto contador >= 0:
    imprimir(f"{contador}...")
    contador -= 1
imprimir("🚀 Lançamento!")

# Menu com loop
enquanto Verdadeiro:
    imprimir("\n1. Opção 1")
    imprimir("2. Opção 2")
    imprimir("3. Sair")
    
    escolha = entrada("Escolha: ")
    
    se escolha == "3":
        quebre
    senaose escolha == "1":
        imprimir("Você escolheu 1")
    senao:
        imprimir("Opção inválida!")
```

**O que você aprende:**
- Laço `enquanto` (while)
- Palavras-chave `quebre` e `continue`
- Loops infinitos controlados

**Desafio extra:**
- Crie um sistema de senha com tentativas limitadas
- Faça um programa que some números até o usuário digitar 0

---

### 11. Jogo de Adivinhação 🎮
**Conceitos:** Números aleatórios, loops, lógica  
**Dificuldade:** ⭐⭐⭐☆☆  
**Tempo:** 30 minutos

Crie um jogo interativo!

```python
importar random

numero_secreto = random.randint(1, 100)
tentativas = 0

imprimir("=== JOGO DE ADIVINHAÇÃO ===")
imprimir("Adivinhe o número entre 1 e 100")

enquanto Verdadeiro:
    palpite = inteiro(entrada("\nSeu palpite: "))
    tentativas += 1
    
    se palpite == numero_secreto:
        imprimir(f"🎉 Parabéns! Acertou em {tentativas} tentativas!")
        quebre
    senaose palpite < numero_secreto:
        imprimir("📈 Tente um número maior!")
    senao:
        imprimir("📉 Tente um número menor!")
```

**O que você aprende:**
- Importar módulos
- Números aleatórios
- Lógica de jogo

**Desafio extra:**
- Limite o número de tentativas
- Mostre a distância do número secreto
- Adicione níveis de dificuldade

---

### 12. Trabalhando com Listas 📝
**Conceitos:** Listas, métodos, manipulação  
**Dificuldade:** ⭐⭐⭐☆☆  
**Tempo:** 25 minutos

Aprenda a trabalhar com coleções de dados.

```python
# Criando listas
numeros = [1, 2, 3, 4, 5]
frutas = ["maçã", "banana", "laranja"]
mista = [1, "texto", 3.14, Verdadeiro]

# Adicionando elementos
frutas.append("uva")
frutas.insert(0, "morango")

# Removendo elementos
frutas.remove("banana")
ultima = frutas.pop()

# Acessando elementos
imprimir(frutas[0])  # Primeiro
imprimir(frutas[-1])  # Último

# Fatiamento
imprimir(frutas[1:3])

# Percorrendo
para i, fruta em enumerar(frutas):
    imprimir(f"{i+1}. {fruta}")
```

**O que você aprende:**
- Criar e manipular listas
- Métodos: append, insert, remove, pop
- Indexação e fatiamento
- Enumerar elementos

**Desafio extra:**
- Crie uma lista de compras interativa
- Ordene uma lista de números

---

### 13. Funções Simples 🔧
**Conceitos:** `definir`, parâmetros  
**Dificuldade:** ⭐⭐⭐☆☆  
**Tempo:** 25 minutos

Organize código em funções reutilizáveis.

```python
definir saudar(nome):
    imprimir(f"Olá, {nome}!")

definir somar(a, b):
    resultado = a + b
    imprimir(f"{a} + {b} = {resultado}")

definir exibir_menu():
    imprimir("=== MENU ===")
    imprimir("1. Opção 1")
    imprimir("2. Opção 2")
    imprimir("3. Sair")

# Usando as funções
saudar("Maria")
somar(5, 3)
exibir_menu()
```

**O que você aprende:**
- Criar funções com `definir`
- Passar parâmetros
- Organizar código

**Desafio extra:**
- Crie funções para calcular área e perímetro de formas
- Faça uma função que valida CPF

---

### 14. Funções com Retorno ↩️
**Conceitos:** `retornar`, funções que retornam valores  
**Dificuldade:** ⭐⭐⭐☆☆  
**Tempo:** 30 minutos

Crie funções que retornam resultados.

```python
definir somar(a, b):
    retornar a + b

definir calcular_media(notas):
    soma = sum(notas)
    retornar soma / tamanho(notas)

definir eh_par(numero):
    retornar numero % 2 == 0

# Usando funções
resultado = somar(10, 5)
imprimir(f"Soma: {resultado}")

notas = [8.5, 9.0, 7.5]
media = calcular_media(notas)
imprimir(f"Média: {media:.2f}")

se eh_par(10):
    imprimir("10 é par")
```

**O que você aprende:**
- Retornar valores com `retornar`
- Usar retorno em expressões
- Funções booleanas

**Desafio extra:**
- Crie funções matemáticas (fatorial, fibonacci)
- Faça uma função que valida email

---

## 🔴 Exercícios Avançados (15-22)

### 15. Calculadora com Funções 🧮
**Conceitos:** Múltiplas funções, menu, organização  
**Dificuldade:** ⭐⭐⭐⭐☆  
**Tempo:** 40 minutos

Crie uma calculadora completa e organizada.

```python
definir somar(a, b):
    retornar a + b

definir subtrair(a, b):
    retornar a - b

definir multiplicar(a, b):
    retornar a * b

definir dividir(a, b):
    se b == 0:
        retornar "Erro: divisão por zero"
    retornar a / b

enquanto Verdadeiro:
    imprimir("\n=== CALCULADORA ===")
    imprimir("1. Somar")
    imprimir("2. Subtrair")
    imprimir("3. Multiplicar")
    imprimir("4. Dividir")
    imprimir("5. Sair")
    
    opcao = entrada("Escolha: ")
    
    se opcao == "5":
        quebre
    
    # Resto do código...
```

**O que você aprende:**
- Múltiplas funções relacionadas
- Validação de entrada
- Tratamento de erros

**Desafio extra:**
- Adicione mais operações (potência, raiz)
- Implemente histórico de cálculos

---

### 16. Classe Cachorro 🐕
**Conceitos:** Classes, `__init__`, métodos  
**Dificuldade:** ⭐⭐⭐⭐☆  
**Tempo:** 35 minutos

Introdução à Programação Orientada a Objetos!

```python
classe Cachorro:
    definir __init__(self, nome, idade, raca):
        self.nome = nome
        self.idade = idade
        self.raca = raca
    
    definir latir(self):
        imprimir(f"{self.nome} diz: Au au!")
    
    definir aniversario(self):
        self.idade += 1
        imprimir(f"{self.nome} fez {self.idade} anos!")
    
    definir apresentar(self):
        imprimir(f"Nome: {self.nome}")
        imprimir(f"Idade: {self.idade} anos")
        imprimir(f"Raça: {self.raca}")

# Criando objetos
rex = Cachorro("Rex", 3, "Labrador")
bobby = Cachorro("Bobby", 5, "Poodle")

rex.apresentar()
rex.latir()
rex.aniversario()
```

**O que você aprende:**
- Criar classes com `classe`
- Método `__init__` (construtor)
- Atributos e métodos
- Criar objetos (instâncias)

**Desafio extra:**
- Adicione método para comer e dormir
- Crie uma classe Gato similar

---

### 17. Classe Conta Bancária 💰
**Conceitos:** Métodos, encapsulamento  
**Dificuldade:** ⭐⭐⭐⭐☆  
**Tempo:** 40 minutos

Simule operações bancárias.

```python
classe ContaBancaria:
    definir __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    
    definir depositar(self, valor):
        se valor > 0:
            self.saldo += valor
            imprimir(f"✓ Depósito de R$ {valor:.2f}")
        senao:
            imprimir("✗ Valor inválido")
    
    definir sacar(self, valor):
        se valor > self.saldo:
            imprimir("✗ Saldo insuficiente")
        senaose valor > 0:
            self.saldo -= valor
            imprimir(f"✓ Saque de R$ {valor:.2f}")
        senao:
            imprimir("✗ Valor inválido")
    
    definir extrato(self):
        imprimir(f"Titular: {self.titular}")
        imprimir(f"Saldo: R$ {self.saldo:.2f}")

conta = ContaBancaria("João", 1000)
conta.extrato()
conta.depositar(500)
conta.sacar(200)
conta.extrato()
```

**O que você aprende:**
- Lógica de negócio em classes
- Validações em métodos
- Estado do objeto

**Desafio extra:**
- Adicione histórico de transações
- Implemente transferência entre contas
- Adicione taxa de saque

---

### 18. Classe Retângulo 📐
**Conceitos:** Propriedades calculadas, geometria  
**Dificuldade:** ⭐⭐⭐⭐☆  
**Tempo:** 35 minutos

Calcule área e perímetro geometricamente.

```python
classe Retangulo:
    definir __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    definir calcular_area(self):
        retornar self.largura * self.altura
    
    definir calcular_perimetro(self):
        retornar 2 * (self.largura + self.altura)
    
    definir eh_quadrado(self):
        retornar self.largura == self.altura
    
    definir exibir_info(self):
        imprimir(f"Largura: {self.largura}")
        imprimir(f"Altura: {self.altura}")
        imprimir(f"Área: {self.calcular_area()}")
        imprimir(f"Perímetro: {self.calcular_perimetro()}")
        
        se self.eh_quadrado():
            imprimir("É um quadrado!")

ret = Retangulo(10, 5)
ret.exibir_info()
```

**O que você aprende:**
- Métodos com cálculos
- Propriedades derivadas
- Lógica matemática em OOP

**Desafio extra:**
- Crie classes para Círculo e Triângulo
- Adicione método para comparar áreas

---

### 19. Classe Aluno com Notas 🎓
**Conceitos:** Listas em classes, cálculos  
**Dificuldade:** ⭐⭐⭐⭐☆  
**Tempo:** 40 minutos

Gerencie notas e aprovação de alunos.

```python
classe Aluno:
    definir __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []
    
    definir adicionar_nota(self, nota):
        se 0 <= nota <= 10:
            self.notas.append(nota)
            imprimir(f"✓ Nota {nota} adicionada")
        senao:
            imprimir("✗ Nota inválida (0-10)")
    
    definir calcular_media(self):
        se tamanho(self.notas) == 0:
            retornar 0
        retornar sum(self.notas) / tamanho(self.notas)
    
    definir situacao(self):
        media = self.calcular_media()
        
        se media >= 7:
            retornar "Aprovado"
        senaose media >= 5:
            retornar "Recuperação"
        senao:
            retornar "Reprovado"
    
    definir boletim(self):
        imprimir(f"\n=== BOLETIM ===")
        imprimir(f"Aluno: {self.nome}")
        imprimir(f"Matrícula: {self.matricula}")
        imprimir(f"Notas: {self.notas}")
        imprimir(f"Média: {self.calcular_media():.2f}")
        imprimir(f"Situação: {self.situacao()}")

aluno = Aluno("Maria Silva", "2024001")
aluno.adicionar_nota(8.5)
aluno.adicionar_nota(9.0)
aluno.adicionar_nota(7.5)
aluno.boletim()
```

**O que você aprende:**
- Listas como atributos
- Cálculos com dados da classe
- Sistema completo de gerenciamento

**Desafio extra:**
- Adicione diferentes disciplinas
- Implemente sistema de faltas

---

### 20. Projeto: Lista de Tarefas ✅
**Conceitos:** Projeto completo, CRUD  
**Dificuldade:** ⭐⭐⭐⭐⭐  
**Tempo:** 60 minutos

Sistema completo de gerenciamento de tarefas!

**Funcionalidades:**
- ✅ Adicionar tarefas
- ✅ Listar tarefas
- ✅ Marcar como concluída
- ✅ Remover tarefas
- ✅ Prioridades
- ✅ Interface em menu

**O que você aprende:**
- CRUD completo (Create, Read, Update, Delete)
- Estruturas de dados complexas
- Interface de usuário
- Validações

**Desafio extra:**
- Salvar tarefas em arquivo
- Adicionar datas de vencimento
- Filtrar por prioridade

---

### 21. Projeto: Quiz Interativo 🎯
**Conceitos:** Dicionários, lógica de jogo  
**Dificuldade:** ⭐⭐⭐⭐⭐  
**Tempo:** 60 minutos

Crie um jogo de perguntas e respostas!

**Funcionalidades:**
- 📚 Banco de perguntas
- ⏱️ Sistema de pontuação
- 📊 Estatísticas
- 🎮 Feedback imediato

**O que você aprende:**
- Trabalhar com dicionários
- Lógica de pontuação
- Interface interativa

**Desafio extra:**
- Adicione categorias
- Implemente ranking
- Adicione dificuldades

---

### 22. Projeto: Conversor de Temperatura 🌡️
**Conceitos:** Menu completo, funções, validação  
**Dificuldade:** ⭐⭐⭐⭐⭐  
**Tempo:** 50 minutos

Conversor completo de temperaturas!

**Conversões:**
- 🌡️ Celsius ↔ Fahrenheit
- 🌡️ Celsius ↔ Kelvin
- 🌡️ Fahrenheit ↔ Kelvin

**Funcionalidades:**
- Menu interativo
- Validação de entrada
- Múltiplas conversões
- Interface amigável

**O que você aprende:**
- Projeto completo
- Múltiplas funções
- Validação robusta
- Interface profissional

**Desafio extra:**
- Adicione histórico de conversões
- Implemente conversão em lote
- Crie gráficos de temperatura

---

## 🚀 Como Fazer os Exercícios

### Passo a Passo

1. **Clone o repositório**
   ```bash
   git clone https://github.com/maxwellamaral/pybr.git
   cd pybr
   ```

2. **Execute um exercício**
   ```bash
   python pybr.py exercicios/01-ola-mundo.pybr
   ```

3. **Estude o código**
   - Leia os comentários
   - Entenda cada linha
   - Teste modificações

4. **Faça os desafios**
   - Tente resolver sozinho primeiro
   - Pesquise quando travar
   - Compare com a solução

### Dicas de Estudo

- ✅ **Faça na ordem** - Os exercícios são progressivos
- ✅ **Pratique todo dia** - Mesmo que seja 30 minutos
- ✅ **Não copie** - Digite o código para aprender
- ✅ **Experimente** - Modifique o código e veja o que acontece
- ✅ **Anote dúvidas** - Pesquise depois ou pergunte
- ✅ **Refaça** - Revise exercícios anteriores

### Recursos de Apoio

- 📖 [Tutorial Completo](tutorial) - Conceitos detalhados
- 📚 [Referência](referencia) - Documentação da linguagem
- 💬 [Issues no GitHub](https://github.com/maxwellamaral/pybr/issues) - Tire dúvidas
- 🎓 [Tutorial Original](tutorial-completo) - Versão estendida

---

## 📊 Acompanhe seu Progresso

### Checklist de Exercícios

#### 🟢 Básico
- [ ] 01. Olá Mundo
- [ ] 02. Variáveis
- [ ] 03. Cálculos
- [ ] 04. Entrada/Saída
- [ ] 05. Calculadora IMC
- [ ] 06. Condicionais

#### 🟡 Intermediário
- [ ] 07. Sistema Login
- [ ] 08. Laços Para
- [ ] 09. Tabuada
- [ ] 10. Enquanto
- [ ] 11. Jogo Adivinhação
- [ ] 12. Listas
- [ ] 13. Funções Simples
- [ ] 14. Funções Retorno

#### 🔴 Avançado
- [ ] 15. Calculadora Funções
- [ ] 16. Classe Cachorro
- [ ] 17. Conta Bancária
- [ ] 18. Classe Retângulo
- [ ] 19. Classe Aluno
- [ ] 20. Lista de Tarefas
- [ ] 21. Quiz
- [ ] 22. Conversor Temp

### Conquistas 🏆

- 🥉 **Bronze** - Complete os 6 exercícios básicos
- 🥈 **Prata** - Complete até exercício 14
- 🥇 **Ouro** - Complete todos os 22 exercícios
- 💎 **Diamante** - Complete todos com desafios extras

---

## ❓ Dúvidas Frequentes

**P: Preciso fazer na ordem?**  
R: Sim! Os exercícios são progressivos e cada um usa conceitos dos anteriores.

**P: Quanto tempo leva para completar todos?**  
R: Aproximadamente 12-15 horas, fazendo com calma e entendendo.

**P: E se eu travar em um exercício?**  
R: Revise o [tutorial](tutorial), consulte a [referência](referencia), ou abra uma [issue](https://github.com/maxwellamaral/pybr/issues).

**P: Posso pular exercícios?**  
R: Não é recomendado, mas você pode fazer exercícios intermediários se já souber o básico.

**P: Os desafios extras são obrigatórios?**  
R: Não, mas são ótimos para praticar e fixar o conteúdo!

---

**Bons estudos e divirta-se programando! 🚀**

[← Voltar ao Tutorial](tutorial) | [Ver Referência →](referencia) | [Início](index)
