# PyBR - Internationales Python (Mehrsprachig)

[Português](README.md) | [Español](README.es.md) | **Deutsch** | [Italiano](README.it.md) | [Français](README.fr.md)

## Beschreibung

PyBR ist ein Transpiler, mit dem Sie Python-Code unter Verwendung von Schlüsselwörtern und nativen Funktionen in verschiedenen Sprachen schreiben können. Das Projekt übersetzt den Code in gültiges Python, sodass Schüler das Programmieren mit einer zugänglicheren Syntax üben können.

## Funktionen

- **Lokalisierte Schlüsselwörter**: Verwenden Sie `wenn`, `sonst`, `fuer`, `solange`, `definiere`, `klasse` usw.
- **Übersetzte integrierte Funktionen**: `drucke()`, `eingabe()`, `laenge()`, `bereich()`, usw.
- **Mehrsprachige Unterstützung**: Wählen Sie Ihre Sprache mit der Flagge `--lang`.
- **Interaktives REPL**: Interaktive Shell zum Testen von Code in Echtzeit.

## Verwendung

### Interaktiver Modus (REPL)

Um die Shell auf Deutsch zu starten:

```bash
python pybr.py --lang de
```

### Eine Datei ausführen

```bash
python pybr.py --lang de mein_programm.pybr
```

### Code-Beispiel (Deutsch)

```python
# Beispiel in PyBR
definiere begrueßung(name):
    drucke(f"Hallo, {name}!")

fuer i in bereich(5):
    wenn i % 2 == 0:
        drucke(f"{i} ist gerade")
    sonst:
        drucke(f"{i} ist ungerade")
```

## Beitragen

Beiträge sind willkommen! Sie können neue Sprachen hinzufügen, indem Sie eine `.json`-Datei im Ordner `languages/` erstellen.
