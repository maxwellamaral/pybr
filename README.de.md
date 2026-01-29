# PyBR - Internationales Python (Mehrsprachig)

[Português](README.md) | [Español](README.es.md) | **Deutsch** | [Italiano](README.it.md) | [Français](README.fr.md)

## Beschreibung

PyBR ist ein Transpiler, mit dem Sie Python-Code unter Verwendung von Schlüsselwörtern und nativen Funktionen in verschiedenen Sprachen schreiben können. Das Projekt übersetzt den Code in gültiges Python, sodass Schüler das Programmieren mit einer zugänglicheren Syntax üben können.

## Funktionen

- **Lokalisierte Schlüsselwörter**: Verwenden Sie `wenn`, `sonst`, `fuer`, `solange`, `definiere`, `klasse` usw.
- **Übersetzte integrierte Funktionen**: `drucke()`, `eingabe()`, `laenge()`, `bereich()`, usw.
- **Mehrsprachige Unterstützung**: Wählen Sie Ihre Sprache mit der Flagge `--lang`.
- **Interaktives REPL**: Interaktive Shell zum Testen von Code in Echtzeit.

## 📚 Programmieren Lernen

Neu beim Programmieren? Schauen Sie sich unser **[Einsteigerhandbuch](tutorial/tutorial-de.md)** an!
    - Um die PDFs zu generieren: `python3 tutorial/gerar_pdf.py`

## Verwendung

### Beispiele

Beispielcode für alle unterstützten Sprachen finden Sie im Ordner `examples/`:

- **Deutsch**: `examples/beispiel_de.pybr`
- **Portugiesisch**: `examples/exemplo_pt.pybr`
- ...

Um das deutsche Beispiel auszuführen:

```bash
python3 pybr.py examples/beispiel_de.pybr --lang de
```

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

## Einschränkungen

- Der Transpiler übersetzt die häufigsten Python-Fehlermeldungen in die gewählte Sprache.
- Einige fortgeschrittene Funktionen sind möglicherweise nicht zugeordnet.
- Die Übersetzung erfolgt zur Laufzeit (es werden keine `.py`-Dateien generiert).

## Neue Sprachen hinzufügen 🌍

PyBR möchte alle Sprachen sprechen und du kannst helfen! Das Hinzufügen einer neuen Sprache ist ganz einfach:

1.  **JSON-Datei erstellen**: Erstelle im Ordner `languages/` eine Datei mit deinem Sprachcode (z. B. `tr.json`).
2.  **Vorlage verwenden**: Kopiere den Inhalt von [de.json](languages/de.json).
3.  **Abschnitte übersetzen**: `keywords`, `builtins` und `messages`.
4.  **Pull Request senden**: Hilf Schülern weltweit, in ihrer Muttersprache zu lernen!

## Beitragen

Beiträge sind willkommen! Sie können neue Sprachen hinzufügen, indem Sie eine `.json`-Datei im Ordner `languages/` erstellen.
