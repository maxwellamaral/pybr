# PyBR - Python Internacional (Multilenguaje)

[Português](README.md) | **Español** | [Deutsch](README.de.md) | [Italiano](README.it.md) | [Français](README.fr.md)

## Descripción

PyBR es un transpilador que permite escribir código Python utilizando palabras clave y funciones nativas en varios idiomas (originalmente portugués, ahora expandido a español, alemán, italiano y francés). El proyecto traduce el código a Python válido, permitiendo que estudiantes practiquen programación con una sintaxis más accesible.

## Funcionalidades

- **Palabras clave localizadas**: Usa `si`, `sino`, `para`, `mientras`, `definir`, `clase`, etc.
- **Funciones nativas traducidas**: `imprimir()`, `entrada()`, `longitud()`, `rango()`, etc.
- **Soporte Multi-idioma**: Elige tu idioma con la bandera `--lang`.
- **REPL Interactivo**: Shell interactivo para probar código en tiempo real.

## Cómo Ejecutar

### Modo Interactivo (REPL)

Para iniciar el shell en español:

```bash
python pybr.py --lang es
```

### Ejecutar un Archivo

```bash
python pybr.py --lang es mi_programa.pybr
```

### Ejemplo de Código (Español)

```python
# Ejemplo en PyBR
definir saludo(nombre):
    imprimir(f"Hola, {nombre}!")

para i en rango(5):
    si i % 2 == 0:
        imprimir(f"{i} es par")
    sino:
        imprimir(f"{i} es impar")
```

## Contribuir

¡Las contribuciones son bienvenidas! Puedes añadir nuevos idiomas creando un archivo `.json` en la carpeta `languages/`.
