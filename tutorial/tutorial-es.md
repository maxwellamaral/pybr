# Aprende a Programar con PyBR - Guía Completa para Principiantes
Autor: Maxwell Anderson Ielpo do Amaral
Traducción: AI Assistant

Publicado en Enero de 2026

## ¡Bienvenido al Mundo de la Programación! 🚀

Esta guía fue creada especialmente para ti que nunca has programado antes y quieres aprender de forma fácil y en español. Con **PyBR**, aprenderás a programar usando palabras en español en lugar del inglés tradicional de Python.

---

## Índice

1. [Usando la Terminal - Guía para Principiantes](#usando-la-terminal---guía-para-principiantes)
2. [Instalando Python](#instalando-python)
3. [Cómo Ejecutar PyBR](#cómo-ejecutar-pybr)
4. [¿Qué es la Programación?](#que-es-la-programación)
5. [Tu Primer Programa](#tu-primer-programa)
6. [Variables - La Memoria de la Computadora](#variables---la-memoria-de-la-computadora)
7. [Cálculos y Operaciones Matemáticas](#cálculos-y-operaciones-matemáticas)
8. [Entrada y Salida de Datos](#entrada-y-salida-de-datos)
9. [Tomando Decisiones - Estructuras Condicionales](#tomando-decisiones---estructuras-condicionales)
10. [Repitiendo Acciones - Bucles](#repitiendo-acciones---bucles)
11. [Organizando el Código - Funciones](#organizando-el-código---funciones)
12. [Creando Objetos - Clases](#creando-objetos---clases)

---

## 💻 Usando la Terminal - Guía para Principiantes

Si nunca has usado la **Terminal** (también llamada **Línea de Comandos**), ¡no te preocupes! Es más simple de lo que parece.

### ¿Qué es la Terminal?

La Terminal es una interfaz de texto donde escribes comandos para que la computadora los ejecute.

### Comandos Básicos (Windows/Mac/Linux)

| Acción | Windows | Mac/Linux |
|---|---|---|
| ¿Dónde estoy? | `cd` | `pwd` |
| Listar archivos | `dir` | `ls` |
| Entrar en carpeta | `cd carpeta` | `cd carpeta` |
| Volver atrás | `cd ..` | `cd ..` |
| Limpiar pantalla | `cls` | `clear` |

---

## 🐍 Instalando Python

Antes de comenzar, necesitas tener **Python** instalado.

1. Abre la terminal y escribe: `python --version`
2. Si aparece `Python 3.x.x`, ¡estás listo!
3. Si no, descárgalo en [python.org](https://www.python.org/downloads/).
   - **Windows**: ¡Marca la casilla **"Add Python to PATH"** al instalar!

---

## Cómo Ejecutar PyBR

### Lo que necesitas
✅ **Python 3.6+**
✅ **Archivos de PyBR** (`pybr.py`)

### Formas de Ejecutar

#### Opción 1: Modo Interactivo (REPL)
Perfecto para pruebas rápidas. En la terminal:

```bash
python pybr.py --lang es
```

Verás:
```
PyBR - Python Internacional (Multilenguaje)
Escribe 'salir()' para terminar.
>>>
```

#### Opción 2: Ejecutar Archivos
Crea un archivo `mi_programa.pybr` y ejecútalo:

```bash
python pybr.py mi_programa.pybr --lang es
```

---

## Tu Primer Programa

Vamos a empezar con el clásico "¡Hola, Mundo!":

```python
imprimir("¡Hola, Mundo!")
```

### Experimenta tú mismo:

```python
imprimir("Mi nombre es Juan")
imprimir("¡Estoy aprendiendo a programar con PyBR!")
```

---

## Variables - La Memoria de la Computadora

Las **variables** son como cajas donde guardas información.

### Cómo crear variables:

```python
# Guardando un nombre
nombre = "Maria"

# Guardando una edad
edad = 25

# Usando las variables
imprimir(nombre)
imprimir(edad)
```

### Tipos de Datos:

```python
# TEXTO (string)
ciudad = "Madrid"

# NÚMEROS ENTEROS (int)
cantidad = 10

# NÚMEROS DECIMALES (float)
precio = 19.99

# VERDADERO o FALSO (boolean)
es_lunes = Verdadero
esta_lloviendo = Falso
```

---

## Cálculos y Operaciones Matemáticas

```python
# SUMA (+)
suma = 10 + 5
imprimir(suma)  # Muestra: 15

# RESTA (-)
diferencia = 20 - 8
imprimir(diferencia)  # Muestra: 12

# MULTIPLICACIÓN (*)
producto = 6 * 7
imprimir(producto)  # Muestra: 42

# DIVISIÓN (/)
resultado = 15 / 3
imprimir(resultado)  # Muestra: 5.0

# POTENCIA (**)
potencia = 2 ** 3
imprimir(potencia)  # Muestra: 8
```

---

## Entrada y Salida de Datos

### Salida (Mostrar información):
```python
nombre = "Carlos"
imprimir(f"Mi nombre es {nombre}")
```

### Entrada (Recibir información):
```python
nombre = entrada("¿Cuál es tu nombre? ")
imprimir(f"¡Hola, {nombre}!")

# Para números, necesitamos convertir:
edad = entero(entrada("¿Cuál es tu edad? "))
imprimir(f"Tienes {edad} años")
```

### Ejemplo: Calculadora de IMC
```python
imprimir("=== Calculadora de IMC ===")
peso = flotante(entrada("Peso (kg): "))
altura = flotante(entrada("Altura (m): "))

imc = peso / (altura ** 2)

imprimir(f"Tu IMC es: {imc:.2f}")
```

---

## Tomando Decisiones - Estructuras Condicionales

El programa toma decisiones con `si`, `sino_si` y `sino`.

```python
edad = 18

si edad >= 18:
    imprimir("Eres mayor de edad")
sino:
    imprimir("Eres menor de edad")
```

### Ejemplo con SI-SINO_SI-SINO (if-elif-else):

```python
nota = 75

si nota >= 90:
    imprimir("¡Excelente!")
sino_si nota >= 70:
    imprimir("¡Bien!")
sino:
    imprimir("Necesitas mejorar")
```

### Operadores Lógicos:
- `y` (and)
- `o` (or)
- `no` (not)

```python
si tienes_entrada y eres_mayor:
    imprimir("Puedes entrar")
```

---

## Repitiendo Acciones - Bucles

### Bucle PARA (for):

```python
# Contando de 0 a 4
para i en rango(5):
    imprimir(i)
```

### Bucle MIENTRAS (while):

```python
contador = 0

mientras contador < 5:
    imprimir(f"Contador: {contador}")
    contador = contador + 1
```

---

## Organizando el Código - Funciones

Las funciones son bloques de código reutilizables.

```python
definir saludar(nombre):
    imprimir(f"¡Hola, {nombre}!")

saludar("Ana")
saludar("Pedro")
```

### Funciones con Retorno:

```python
definir sumar(a, b):
    retornar a + b

resultado = sumar(10, 20)
imprimir(resultado)  # 30
```

---

## Creando Objetos - Clases

Las clases son "moldes" para crear objetos.

```python
clase Perro:
    definir __init__(propio, nombre, raza):
        propio.nombre = nombre
        propio.raza = raza
    
    definir ladrar(propio):
        imprimir(f"{propio.nombre}: ¡Guau guau!")

# Creando objetos
rex = Perro("Rex", "Labrador")
rex.ladrar()
```

---

## ¡Felicidades! 🎉

Has completado la guía básica de PyBR en español. ¡Sigue practicando!
