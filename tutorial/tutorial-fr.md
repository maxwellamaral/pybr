# Apprendre à Programmer avec PyBR - Guide pour Débutants
Auteur : Maxwell Anderson Ielpo do Amaral
Traduction : AI Assistant

Publié en Janvier 2026

## Bienvenue dans le Monde de la Programmation ! 🚀

Ce guide a été créé spécialement pour vous qui n'avez jamais programmé auparavant et souhaitez apprendre facilement et en français ! Avec **PyBR**, vous apprendrez à programmer en utilisant des mots en français au lieu de l'anglais traditionnel de Python.

---

## Table des Matières

1. [Utilisation du Terminal](#utilisation-du-terminal)
2. [Installation de Python](#installation-de-python)
3. [Exécuter PyBR](#exécuter-pybr)
4. [Qu'est-ce que la Programmation ?](#quest-ce-que-la-programmation)
5. [Votre Premier Programme](#votre-premier-programme)
6. [Variables - La Mémoire de l'Ordinateur](#variables---la-mémoire-de-lordinateur)
7. [Calculs et Opérations Mathématiques](#calculs-et-opérations-mathématiques)
8. [Entrée et Sortie](#entrée-et-sortie)
9. [Prendre des Décisions - Conditionnelles](#prendre-des-décisions---conditionnelles)
10. [Répéter des Actions - Boucles](#répéter-des-actions---boucles)
11. [Organiser le Code - Fonctions](#organiser-le-code---fonctions)
12. [Créer des Objets - Classes](#créer-des-objets---classes)

---

## 💻 Utilisation du Terminal

Si vous n'avez jamais utilisé le **Terminal**, ne vous inquiétez pas ! C'est plus simple qu'il n'y paraît.

### Commandes de Base

| Action | Windows | Mac/Linux |
|---|---|---|
| Où suis-je ? | `cd` | `pwd` |
| Lister les fichiers | `dir` | `ls` |
| Entrer dans un dossier | `cd dossier` | `cd dossier` |
| Revenir en arrière | `cd ..` | `cd ..` |
| Effacer l'écran | `cls` | `clear` |

---

## 🐍 Installation de Python

Avant de commencer, vous devez avoir **Python** installé.

1. Ouvrez le terminal et tapez : `python --version`
2. Si `Python 3.x.x` apparaît, vous êtes prêt !
3. Sinon, téléchargez-le sur [python.org](https://www.python.org/downloads/).
   - **Windows** : Important ! Cochez **"Add Python to PATH"** lors de l'installation !

---

## Exécuter PyBR

### Prérequis
✅ **Python 3.6+**
✅ **Fichiers PyBR** (`pybr.py`)

### Façons d'Exécuter

#### Option 1 : Mode Interactif (REPL)
Parfait pour des tests rapides. Dans le terminal :

```bash
python pybr.py --lang fr
```

Vous verrez :
```
PyBR - Python International (Multilingue)
Tapez 'quitter()' pour terminer.
>>>
```

#### Option 2 : Exécuter des Fichiers
Créez un fichier `mon_programme.pybr` et exécutez-le :

```bash
python pybr.py mon_programme.pybr --lang fr
```

---

## Votre Premier Programme

Commençons par le classique "Bonjour le Monde" :

```python
imprimer("Bonjour le Monde !")
```

### Essayez vous-même :

```python
imprimer("J'apprends à programmer avec PyBR !")
```

---

## Variables - La Mémoire de l'Ordinateur

Les **variables** sont comme des boîtes où vous stockez des informations.

### Créer des variables :

```python
# Sauvegarder un nom
nom = "Marie"

# Sauvegarder un âge
age = 25

# Utiliser les variables
imprimer(nom)
imprimer(age)
```

### Types de Données :

```python
# TEXTE (String)
ville = "Paris"

# NOMBRES ENTIERS (Int)
quantite = 10

# NOMBRES DÉCIMAUX (Float)
prix = 19.99

# VRAI ou FAUX (Boolean)
est_lundi = Vrai
il_pleut = Faux
```

---

## Calculs et Opérations Mathématiques

```python
# ADDITION (+)
somme = 10 + 5
imprimir(somme)  # Affiche : 15

# SOUSTRACTION (-)
difference = 20 - 8
imprimir(difference)  # Affiche : 12

# MULTIPLICATION (*)
produit = 6 * 7
imprimir(produit)  # Affiche : 42

# DIVISION (/)
resultat = 15 / 3
imprimir(resultat)  # Affiche : 5.0
```

---

## Entrée et Sortie

### Sortie (Afficher des informations) :
```python
nom = "Pierre"
imprimer(f"Je m'appelle {nom}")
```

### Entrée (Recevoir des informations) :
```python
nom = saisir("Comment t'appelles-tu ? ")
imprimer(f"Bonjour, {nom} !")

# Pour les nombres, il faut convertir :
age = entier(saisir("Quel âge as-tu ? "))
imprimer(f"Tu as {age} ans")
```

---

## Prendre des Décisions - Conditionnelles

Le programme prend des décisions avec `si`, `sinon_si` et `sinon`.

```python
age = 18

si age >= 18:
    imprimer("Tu es majeur")
sinon:
    imprimir("Tu es mineur")
```

### Exemple avec SI-SINON_SI-SINON :

```python
note = 85

si note >= 90:
    imprimer("Excellent !")
sinon_si note >= 70:
    imprimer("Bien !")
sinon:
    imprimer("Doit s'améliorer")
```

---

## Répéter des Actions - Boucles

### Boucle POUR (for) :

```python
# Compter de 0 à 4
pour i dans intervalle(5):
    imprimer(i)
```

### Boucle TANT_QUE (while) :

```python
compteur = 0

tant_que compteur < 5:
    imprimer(f"Compteur : {compteur}")
    compteur = compteur + 1
```

---

## Organiser le Code - Fonctions

Les fonctions sont des blocs de code réutilisables.

```python
definir saluer(nom):
    imprimer(f"Bonjour, {nom} !")

saluer("Sophie")
saluer("Marc")
```

### Fonctions avec Retour :

```python
definir additionner(a, b):
    retourner a + b

resultat = additionner(10, 20)
imprimer(resultat)  # 30
```

---

## Créer des Objets - Classes

Les classes sont des "moules" pour créer des objets.

```python
classe Chien:
    definir __init__(soi, nom, race):
        soi.nom = nom
        soi.race = race
    
    definir aboyer(soi):
        imprimer(f"{soi.nom}: Wouf wouf !")

# Créer des objets
rex = Chien("Rex", "Berger Allemand")
rex.aboyer()
```

---

## Félicitations ! 🎉

Vous avez terminé le guide de base de PyBR en français. Continuez à pratiquer !
