# PyBR - Python Internacional (Multilenguaje)

[Português](README.md) | **Español** | [Deutsch](README.de.md) | [Italiano](README.it.md) | [Français](README.fr.md)

## Descripción

PyBR es un transpilador que permite escribir código Python utilizando palabras clave y funciones nativas en varios idiomas (originalmente portugués, ahora expandido a español, alemán, italiano y francés). El proyecto traduce el código a Python válido, permitiendo que estudiantes practiquen programación con una sintaxis más accesible.

## Funcionalidades

- **Palabras clave localizadas**: Usa `si`, `sino`, `para`, `mientras`, `definir`, `clase`, etc.
- **Funciones nativas traducidas**: `imprimir()`, `entrada()`, `longitud()`, `rango()`, etc.
- **Soporte Multi-idioma**: Elige tu idioma con la bandera `--lang`.
- **REPL Interactivo**: Shell interactivo para probar código en tiempo real.

## 📚 Aprender a Programar

¿Nuevo en la programación? ¡Consulte nuestra **[Guía para Principiantes](tutorial/tutorial-es.md)**!
    - Para generar los PDFs: `python3 tutorial/gerar_pdf.py`

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

### Ejemplos

Puede encontrar ejemplos de código para todos los idiomas soportados en la carpeta `examples/`:

- **Español**: `examples/ejemplo_es.pybr`
- **Portugués**: `examples/exemplo_pt.pybr`
- ...

Para ejecutar el ejemplo en español:

```bash
python3 pybr.py examples/ejemplo_es.pybr --lang es
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

## Limitaciones

- El transpilador traduce los mensajes de error más comunes de Python al idioma seleccionado.
- Algunas funciones avanzadas pueden no estar mapeadas.
- La traducción se realiza en tiempo de ejecución (no genera archivos `.py`).

## Contribuir con nuevos idiomas 🌍

¡PyBR quiere hablar todos los idiomas y tú puedes ayudar! Añadir un nuevo idioma es extremadamente sencillo:

1.  **Crea un archivo JSON**: En la carpeta `languages/`, crea un archivo con el código de tu idioma (ej: `jp.json`).
2.  **Usa una plantilla**: Copia el contenido de [es.json](languages/es.json).
3.  **Traduce las secciones**: `keywords`, `builtins` y `messages`.
4.  **Envía un Pull Request**: ¡Ayuda a estudiantes de todo el mundo a aprender en su propio idioma!

## Contribuir

¡Las contribuciones son bienvenidas! Puedes añadir nuevos idiomas creando un archivo `.json` en la carpeta `languages/`.
