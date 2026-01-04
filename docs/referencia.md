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

### Definições

| PyBR | Python | Exemplo |
|------|--------|---------|
| `definir` | `def` | `definir funcao(x):` |
| `classe` | `class` | `classe MinhaClasse:` |
| `retornar` | `return` | `retornar valor` |
| `importar` | `import` | `importar math` |
| `de` | `from` | `de math importar sqrt` |
| `como` | `as` | `importar pandas como pd` |

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
```

### Manipulação

```python
tamanho([1,2,3])           # len() - retorna tamanho
intervalo(1, 10)            # range() - cria sequência
tipo(variavel)              # type() - retorna tipo
```

### Matemática

```python
maximo(1, 2, 3)       # max() - maior valor
minimo(1, 2, 3)       # min() - menor valor  
soma([1,2,3])         # sum() - soma elementos
abs(-5)               # abs() - valor absoluto
arredondar(3.7)       # round() - arredonda
```

### Iteração

```python
enumerar(lista)       # enumerate() - enumera elementos
ordenar(lista)        # sorted() - ordena
reverter(lista)       # reversed() - inverte ordem
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

---

## 🌟 Dicas

- Use **nomes descritivos** para variáveis
- **Indente corretamente** (4 espaços ou 1 tab)
- **Comente** seu código
- **Teste** frequentemente

---

[← Voltar ao Tutorial](tutorial) | [Ver Exercícios →](exercicios)
