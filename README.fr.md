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

## Limitations

- Le transpileur traduit les messages d'erreur Python les plus courants dans la langue sélectionnée.
- Certaines fonctions avancées peuvent ne pas être mappées.
- La traduction est effectuée au moment de l'exécution (ne génère pas de fichiers `.py`).

## Contribuer avec de nouvelles langues 🌍

PyBR souhaite parler toutes les langues et vous pouvez aider ! Ajouter une nouvelle langue est très simple :

1.  **Créez un fichier JSON** : Dans le dossier `languages/`, créez un fichier avec votre code de langue (ex : `ar.json`).
2.  **Utilisez un modèle** : Copiez le contenu de [fr.json](languages/fr.json).
3.  **Traduisez les sections** : `keywords`, `builtins` et `messages`.
4.  **Envoyez une Pull Request** : Aidez les étudiants du monde entier à apprendre dans leur propre langue !

## Contribuer

Les contributions sont les bienvenues ! Vous pouvez ajouter de nouvelles langues en créant un fichier `.json` dans le dossier `languages/`.
