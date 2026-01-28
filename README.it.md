# PyBR - Python Internazionale (Multilingue)

[Português](README.md) | [Español](README.es.md) | [Deutsch](README.de.md) | **Italiano** | [Français](README.fr.md)

## Descrizione

PyBR è un transpiler che ti permette di scrivere codice Python usando parole chiave e funzioni native in diverse lingue. Il progetto traduce il codice in Python valido, permettendo agli studenti di praticare la programmazione con una sintassi più accessibile.

## Caratteristiche

- **Parole chiave localizzate**: Usa `se`, `altrimenti`, `per`, `mentre`, `definisci`, `classe`, ecc.
- **Funzioni native tradotte**: `stampa()`, `input()`, `lunghezza()`, `intervallo()`, ecc.
- **Supporto multilingue**: Scegli la tua lingua con il flag `--lang`.
- **REPL interattivo**: Shell interattiva per testare il codice in tempo reale.

## Come eseguire

### Modalità interattiva (REPL)

Per avviare la shell in italiano:

```bash
python pybr.py --lang it
```

### Eseguire un file

```bash
python pybr.py --lang it mio_programma.pybr
```

### Esempio di codice (Italiano)

```python
# Esempio in PyBR
definisci saluto(nome):
    stampa(f"Ciao, {nome}!")

per i in intervallo(5):
    se i % 2 == 0:
        stampa(f"{i} è pari")
    altrimenti:
        stampa(f"{i} è dispari")
```

## Contribuire

I contributi sono benvenuti! Puoi aggiungere nuove lingue creando un file `.json` nella cartella `languages/`.
