---
layout: default
title: Referência - PyBR
---

# Referência Completa da Linguagem

Documentação de todas as palavras-chave e funções do PyBR.

## 🔑 Palavras-chave

### Controle de Fluxo

| PyBR | Python | Exemplo |
|------|--------|---------|
| `se` | `if` | `se x > 10:` |
| `senao` | `else` | `senao:` |
| `senaose` | `elif` | `senaose x < 5:` |
| `para` | `for` | `para i em intervalo(10):` |
| `enquanto` | `while` | `enquanto x < 100:` |
| `quebre` | `break` | `quebre` |
| `continue` | `continue` | `continue` |
| `passar` | `pass` | `passar` |

### Tratamento de Exceções

| PyBR | Python | Exemplo |
|------|--------|---------|
| `tente` | `try` | `tente:` |
| `exceto` | `except` | `exceto ValueError:` |
| `finalmente` | `finally` | `finalmente:` |
| `levantar` | `raise` | `levantar ValueError("Erro")` |
| `afirmar` | `assert` | `afirmar x > 0` |

### Definições

| PyBR | Python | Exemplo |
|------|--------|---------|
| `definir` | `def` | `definir funcao(x):` |
| `funcao` | `def` | `funcao minhaFuncao(x):` |
| `classe` | `class` | `classe MinhaClasse:` |
| `retornar` | `return` | `retornar valor` |
| `importar` | `import` | `importar math` |
| `de` | `from` | `de math importar sqrt` |
| `como` | `as` | `importar pandas como pd` |
| `com` | `with` | `com abrir("arquivo.txt") como f:` |
| `global` | `global` | `global variavel` |
| `lambda` | `lambda` | `lambda x: x * 2` |

### Operadores Lógicos

| PyBR | Python | Exemplo |
|------|--------|---------|
| `e` | `and` | `se x > 0 e x < 10:` |
| `ou` | `or` | `se x < 0 ou x > 100:` |
| `nao` | `not` | `se nao ativo:` |
| `em` | `in` | `se "a" em palavra:` |
| `eh` | `is` | `se x eh Nulo:` |

### Constantes

| PyBR | Python |
|------|--------|
| `Verdadeiro` | `True` |
| `Falso` | `False` |
| `Nulo` | `None` |

---

## 📦 Funções Nativas

### Entrada/Saída

```python
imprimir("Olá")              # print()
texto = entrada("Nome: ")     # input()
```

### Conversão de Tipos

```python
inteiro("123")        # int() - converte para inteiro
flutuante("3.14")     # float() - converte para decimal
texto(123)            # str() - converte para texto
lista([1,2,3])        # list() - converte para lista
dicionario()          # dict() - cria dicionário
conjunto({1,2,3})     # set() - cria conjunto
tupla((1,2,3))        # tuple() - cria tupla
```

### Manipulação

```python
tamanho([1,2,3])           # len() - retorna tamanho
intervalo(1, 10)            # range() - cria sequência
tipo(variavel)              # type() - retorna tipo
enumerar(lista)             # enumerate() - enumera elementos
```

### Matemática

```python
maximo(1, 2, 3)       # max() - maior valor
minimo(1, 2, 3)       # min() - menor valor  
abs(-5)               # abs() - valor absoluto
arredondar(3.7)       # round() - arredonda
2 ** 3                # potência (2 elevado a 3 = 8)
```

### Iteração e Filtragem

```python
ordenar(lista)        # sorted() - ordena
reverter(lista)       # reversed() - inverte ordem
filtrar(funcao, lista) # filter() - filtra elementos
mapear(funcao, lista) # map() - aplica função a cada elemento
qualquer([F, F, V])   # any() - retorna True se algum for True
todos([V, V, V])      # all() - retorna True se todos forem True
```

### Arquivos e Sistema

```python
arquivo = abrir("dados.txt", "r")  # open() - abre arquivo
ajuda(imprimir)                     # help() - mostra ajuda
dir(objeto)                         # dir() - lista atributos
sair()                              # exit() - sai do programa
```

---

## 🔢 Operadores

### Aritméticos

| Op | Descrição | Exemplo |
|----|-----------|---------|
| `+` | Adição | `5 + 3 = 8` |
| `-` | Subtração | `5 - 3 = 2` |
| `*` | Multiplicação | `5 * 3 = 15` |
| `/` | Divisão | `5 / 2 = 2.5` |
| `//` | Divisão inteira | `5 // 2 = 2` |
| `%` | Módulo (resto) | `5 % 2 = 1` |
| `**` | Potência | `5 ** 2 = 25` |

### Comparação

| Op | Descrição |
|----|-----------|
| `==` | Igual |
| `!=` | Diferente |
| `>` | Maior |
| `<` | Menor |
| `>=` | Maior ou igual |
| `<=` | Menor ou igual |

### Atribuição

| Op | Equivalente |
|----|-------------|
| `+=` | `x = x + y` |
| `-=` | `x = x - y` |
| `*=` | `x = x * y` |
| `/=` | `x = x / y` |

---

## 📝 Exemplos Completos

### Estrutura Condicional

```python
idade = inteiro(entrada("Idade: "))

se idade < 12:
    imprimir("Criança")
senaose idade < 18:
    imprimir("Adolescente")
senaose idade < 60:
    imprimir("Adulto")
senao:
    imprimir("Idoso")
```

### Laço Para

```python
# Iterar sobre intervalo
para i em intervalo(1, 6):
    imprimir(i)

# Iterar sobre lista
frutas = ["maçã", "banana", "laranja"]
para fruta em frutas:
    imprimir(fruta)

# Com enumerar
para indice, fruta em enumerar(frutas):
    imprimir(f"{indice}: {fruta}")
```

### Laço Enquanto

```python
contador = 0
enquanto contador < 5:
    imprimir(contador)
    contador += 1
```

### Função

```python
definir calcular_area(base, altura):
    area = base * altura
    retornar area

resultado = calcular_area(5, 3)
imprimir(f"Área: {resultado}")
```

### Classe

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
imprimir("Área:", ret.calcular_area())
imprimir("Perímetro:", ret.calcular_perimetro())
```

### Trabalhando com Listas

```python
# Criar lista
numeros = [1, 2, 3, 4, 5]

# Adicionar elemento
numeros.append(6)

# Remover elemento
numeros.remove(3)

# Acessar elemento
primeiro = numeros[0]

# Fatiar lista
primeiros_tres = numeros[0:3]

# Tamanho
total = tamanho(numeros)

# Funções úteis
maior = maximo(numeros)      # Maior valor
menor = minimo(numeros)      # Menor valor
total = sum(numeros)         # Soma todos (usar sum nativo)
ordenados = ordenar(numeros) # Lista ordenada
invertidos = lista(reverter(numeros))  # Lista invertida
```

### Dicionários

```python
pessoa = {
    "nome": "Maria",
    "idade": 30,
    "cidade": "São Paulo"
}

# Acessar valor
nome = pessoa["nome"]

# Adicionar/modificar
pessoa["email"] = "maria@email.com"

# Iterar
para chave, valor em pessoa.items():
    imprimir(f"{chave}: {valor}")
```

### Tratamento de Exceções

```python
# Estrutura básica
tente:
    resultado = 10 / 0
exceto ZeroDivisionError:
    imprimir("Erro: divisão por zero!")
finalmente:
    imprimir("Bloco executado sempre")

# Múltiplas exceções
tente:
    numero = inteiro(entrada("Número: "))
    resultado = 100 / numero
exceto ValueError:
    imprimir("Valor inválido!")
exceto ZeroDivisionError:
    imprimir("Não pode dividir por zero!")
exceto:
    imprimir("Erro desconhecido")

# Levantando exceções
definir validar_idade(idade):
    se idade < 0:
        levantar ValueError("Idade não pode ser negativa")
    se idade > 150:
        levantar ValueError("Idade inválida")
    retornar Verdadeiro
```

### Trabalhando com Arquivos

```python
# Lendo arquivo
com abrir("dados.txt", "r") como arquivo:
    conteudo = arquivo.read()
    imprimir(conteudo)

# Escrevendo arquivo
com abrir("saida.txt", "w") como arquivo:
    arquivo.write("Olá, mundo!")

# Lendo linha por linha
com abrir("dados.txt", "r") como arquivo:
    para linha em arquivo:
        imprimir(linha.strip())
```

### Funções Avançadas

```python
# Lambda (funções anônimas)
dobro = lambda x: x * 2
imprimir(dobro(5))  # 10

# Map - aplicar função a cada elemento
numeros = [1, 2, 3, 4, 5]
dobrados = lista(mapear(lambda x: x * 2, numeros))
imprimir(dobrados)  # [2, 4, 6, 8, 10]

# Filter - filtrar elementos
pares = lista(filtrar(lambda x: x % 2 == 0, numeros))
imprimir(pares)  # [2, 4]

# Any - verifica se algum é True
valores = [Falso, Falso, Verdadeiro, Falso]
imprimir(qualquer(valores))  # True

# All - verifica se todos são True
valores = [Verdadeiro, Verdadeiro, Verdadeiro]
imprimir(todos(valores))  # True
```

---

## 🌟 Dicas

- Use **nomes descritivos** para variáveis
- **Indente corretamente** (4 espaços ou 1 tab)
- **Comente** seu código
- **Teste** frequentemente

---

[← Voltar ao Tutorial](tutorial) | [Ver Exercícios →](exercicios)
