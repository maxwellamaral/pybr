# PyBR - Python International (Multilingue)

[Português](README.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Italiano](README.it.md) | **Français**

## Description

PyBR est un transpileur qui vous permet d'écrire du code Python en utilisant des mots-clés et des fonctions natives dans plusieurs langues. Le projet traduit le code en Python valide, permettant aux étudiants de pratiquer la programmation avec une syntaxe plus accessible.

## Caractéristiques

- **Mots-clés localisés**: Utilisez `si`, `sinon`, `pour`, `tant_que`, `definir`, `classe`, etc.
- **Fonctions natives traduites**: `imprimer()`, `saisir()`, `taille()`, `intervalle()`, etc.
- **Support multilingue**: Choisissez votre langue avec le drapeau `--lang`.
- **REPL Interactif**: Shell interactif pour tester le code en temps réel.

## Comment exécuter

### Mode Interactif (REPL)

Pour lancer le shell en français :

```bash
python pybr.py --lang fr
```

### Exécuter un fichier

```bash
python pybr.py --lang fr mon_programme.pybr
```

### Exemple de code (Français)

```python
# Exemple en PyBR
definir salutation(nom):
    imprimer(f"Bonjour, {nom}!")

pour i dans intervalle(5):
    si i % 2 == 0:
        imprimer(f"{i} est pair")
    sinon:
        imprimer(f"{i} est impair")
```

## Contribuer

Les contributions sont les bienvenues ! Vous pouvez ajouter de nouvelles langues en créant un fichier `.json` dans le dossier `languages/`.
