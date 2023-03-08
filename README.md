# INTRODUCTION

Bonjour jeune développeur, aujourd'hui on vas avoir un sujet un peu particulier, on vas parler de résolution de problème, d'algorithme et de programmation.
Le but de ce projet est de faire un programme qui vas s'enfuir par lui même d'un labyrinthe.
Pour cela on vas utiliser ce qu'on appelle un algorithme naïf, c'est à dire un algorithme qui vas chercher à résoudre le problème en essayant toutes les possibilités.
Le langage utilisé aujourd'hui est le python et la librairie Tkinter pour l'affichage graphique.

# INSTALLATION

Vous pouvez choisir entre l'installation sur votre machine directement ou bien utiliser un environnement en ligne.

## Installation sur votre machine

Pour ce projet vous aurez besoin d'installer:
- Python3
- Pip3
- Tkinter
Les installations dépendent de votre système d'exploitation, je vous laisse chercher comment faire sur internet.

## Utilisation d'un environnement en ligne

Vous pouvez utiliser un environnement en ligne pour faire ce projet, je vous conseille [repl.it](https://repl.it/).

# THEORIE

Dans la théorie, c'est assez simple, on vas utiliser ce qu'on appelle un `algorithme naïf`, c'est à dire un algorithme qui vas chercher à résoudre le problème en essayant toutes les possibilités.
Dans les faits ça ressemble à ça:

```
Tant qu'on est pas arrivé à la sortie:
    - On regarde si on peut aller à droite, en bas, à gauche ou en haut
        - Si oui, on vas dans cette direction
        - Sinon, on reviens sur nos pas
```

Comme vous pouvez le voir, c'est assez simple sur le papier. On vas maintenant voir comment on vas coder ça.

# CODE

Voci les instructions à suivre pour pouvoir faire ce projet sans trop de difficulté. Ce sont les étapes dont vous avez besoin pour faire ce projet, avec les explications nécessaires.

Attention: Il y a des détails, des parties du code qui sont volontairement omises, à vous de comprendre le code et de réfléchir pour les compléter.

## Initialisation

Pour commencer, on vas créer un fichier `main.py` et on vas y mettre le code suivant:

```python
from tkinter import *

def main():
    pass

if __name__ == "__main__":
    main()
```

Ceci sera la base de notre programme, comme vous pouvez le voir on importe la librairie Tkinter et on crée une fonction `main` qui vas contenir tout notre code.

### C'est quoi Tkinter?

Tkinter est une librairie python qui permet de faire des interfaces graphiques, c'est à dire des fenêtres avec des boutons, des textes, des images, etc.
Ici on vas juste utiliser Tkinter pour afficher un labyrinthe et un personnage qui vas se déplacer dedans.

### C'est quoi `if __name__ == "__main__":` ?

C'est une condition qui permet de vérifier si le fichier est exécuté directement ou si il est importé par un autre fichier.
Dans notre cas, on vas juste exécuter le fichier `main.py` donc on vas juste mettre notre code dans la fonction `main` et on vas l'exécuter directement.

## Step 1: Création de la fenêtre

Il nous faut d'abord une fenêtre pour afficher notre labyrinthe, il faut savoir que tkinter marche avec des `canvas` ainsi qu'avec un objet `Tk` qui vas contenir tout les canvas.

Un canvas est une zone dans laquelle on vas pouvoir dessiner des formes, des images, du texte, etc.

Pour créer un canvas, on vas utiliser la fonction `Canvas` de la librairie Tkinter, on vas donc ajouter le code suivant dans notre fonction `main`:

```python
def main():
    window = Tk()
    window.title("Labyrinthe") # On peux même donner un titre à notre fenêtre
    canvas = Canvas(window, width=1280, height=620)  # On crée un canvas de 500x500
    canvas.pack()       # On affiche le canvas dans la fenêtre
    window.mainloop()   # Cette fonction permet de garder la fenêtre ouverte
```

Vous êtes censé voir une fenêtre s'ouvrir avec un titre `Labyrinthe` et un fond noir.

## Step 2: Création du labyrinthe

Maintenant qu'on a une fenêtre, on vas pouvoir créer notre labyrinthe, pour cela on vas utiliser un tableau de tableau de caractères.
Pour vous faciliter la vie, je vous ai déja créé un labyrinthe, vous avez juste à le copier coller dans un fichier nommé `map.txt` (vous pouvez changer le nom mais il faudra le changer dans le code).

```
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
x--------x--------x--------------------------------------------x
x--xxxx--x--xxxxxxx--xxxxxxxxxxxxxxxxxxxxxxxxxxxx--xxxxxxxxxx--x
x-----x--------------x-----x-----x--------------x-----x--------x
xxxx--x--xxxx--xxxxxxx--x--x--x--x--xxxxxxxxxx--xxxx--x--xxxxxxx
x-----x--x--------------x-----x--x--------x--x--x-----x-----x--x
x--xxxx--x--xxxx--xxxxxxxxxxxxxxxxxxx--xxxxxxx--xxxxxxxxxx--xxxx
x--x-----x--x--x-----------------x--x--x-----x--------x--x-----x
x--xxxxxxx--xxxx--x--xxxxxxxxxx--x--x--x--x--xxxx--x--xxxxxxx--x
x--------x--x-----x-----------x--x--x-----x-----x--x-----------x
x--xxxx--x--x--xxxxxxx--xxxx--x--xxxxxxxxxxxxx--x--xxxxxxxxxxxxx
x--x-----x--x--------x-----x--x--------------x--x-----------x--x
x--x--xxxx--xxxxxxxxxxxxx--x--xxxxxxxxxxxxx--x--xxxx--xxxx--xxxx
x--x--x--------------------x--------------x--x-----x--x--x-----x
x--x--x--xxxxxxxxxxxxxxxxxxxxxx--xxxxxxx--xx-xxxx--x--x--xxxx--x
x--x--------x-----x--------------------x--x-----x--x-----x-----x
x--xxxxxxx--x--x--x--xxxx--xxxxxxx--xxxxxxx--x--x--xxxx--x--xxxx
x--x--------x--x--x-----x--------x-----------x--x--x--x--x-----x
x--x--xxxxxxx--x--xxxx--x--xxxxxxxxxx--xxxxxxxxxx--x--x--xxxx--x
x--x--x--------x-----x--x-----x-----x-----------x--x-----x--x--x
x--x--x--xxxxxxxxxxxxx--xxxx--x--xxxxxxxxxxxxx--x--xxxxxxxxxx--x
x--x-----------------------x--x-----x--x--x----ox--------x--x--x
x--x--xxxxxxxxxxxxxxxxxxxxxxxxxxxx--xxxxxxx--xxxxxxxxxx--xxxx--x
x--x--------x-----x--x--------x--x--x--x--------------x--x-----x
xxxxxxxxxx--x--x--x--x--xxxx--xxxx--xxxx--xxxx--xxxxxxx--x--xxxx
x-----x-----x--x--x--x--x--x--------x--x--x-----x-----x--x-----x
x--xxxx--xxxx--x--x--x--xxxxxxxxxxxxxxxx--x--xxxx--x--x--xxxxxxx
x-----------x--x--x--x-----------------x--x--x-----x--x--------x
xxxxxxxxxx--xxxx--x--xxxxxxxxxxxxxxxx--x--x--xxxxxxxxxxxxxxxx--x
x-----------------x-----------------x-----x--------------x-----x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
- 'x' représente un mur
- '-' représente un chemin
- 'o' représente la sortie

On vas devoir lire ce fichier et le transformer en tableau de string, pour cela voici une fonction qui vas le faire de façon propre:

```python
def load_map(filename):
    mapContent = []
    with open(filename) as f:
        mapContent = f.readlines()
    mapContent = [x.strip() for x in mapContent]
    return mapContent
```
Si vous voulez plus d'explication sur cette fonction, je vous invite à demander à un encadrant mais tout ce que vous avez à savoir c'est que cette fonction prends le chemin vers le fichier en paramètre et retourne un tableau de string. Chaque index du tableau représente une ligne du fichier.

## Step 3: Affichage du labyrinthe

Maintenant que l'on a notre tableau de string, on vas pouvoir l'afficher dans notre fenêtre, pour cela on vas utiliser une fonction qui vas dessiner un carré de 20x20 pixels à une position donnée.

```python
def draw_square(canvas, x, y, color):
    canvas.create_rectangle(x*20, y*20, x*20+20, y*20+20, fill=color, outline='#476042', width=2)
```

## Step 4: Place à l'algo

On vas mettre place l'algorithme de recherche. Pour ça, on vas définir un nombre maximum de pas que le personnage vas pouvoir faire, aussi on vas faire en sorte de voir l'avancement de l'algorithme pas à pas.

Pour ça, vous devez créer une fonction `algo` qui prends les paramètres que vous voulez et qui ne retourne rien.

Vous devez aussi placer ces lignes de code entre le `canvas.pack()` et le `window.mainloop()`:

```python
for value in range(0, max_loop):
    tkMap.after(value * 100, algo, param1, param2, param3, etc)
```

Vous aurez besoin de paramètres essentiels pour l'algorithme:
la liste des positions déja visitées, la position actuelle, le canvas et la map.

Un conseil pour la map, vous pouvez transformer le tableau de string en tableau de nombre ou:
- 0 représente un chemin
- 1 représente un mur
- 2 représente la sortie

L'utilisation de global pour la position actuelle et la liste des positions déja visitées est fortement conseillé.

Comment utiliser les global ?

```python
posX = 0 # On déclare une variable globale

def algo():
    global posX # On déclare que l'on va utiliser la variable globale posX
    posX += 1 # On modifie la variable globale posX
```

# Bonus

Félicitation, vous avez réussi à faire fonctionner l'algorithme de recherche, maintenant vous pouvez vous amuser à le modifier pour qu'il soit plus efficace.

Voici une liste de choses que vous pouvez faire:
- Ajouter des boutons pour:
    - Changer la vitesse de l'algorithme
    - Changer la taille du labyrinthe
    - Changer la position de départ
    - Changer la position de fin
    - Ajouter un bouton pour faire une pause
- Générer un labyrinthe aléatoire

