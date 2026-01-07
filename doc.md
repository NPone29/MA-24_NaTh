## Doc Othello

Rédiger par [Natan Humblet](https://github.com/NPone29) et transformer en .md par [Théo Läderach](https://github.com/pj43svh)

![image couverture](/Assets/default/backgrounds/menu_background.png)

### Table des matière
1. [Comment ça marche ?](#Comment-ça-Marche)
    - [Présentation](#Présentation)
    - [Matériel et mise en place](#matériel-et-mise-en-place-)
    - [Déroulement du jeu](#déroulement-du-jeu-)
    - [Règle de retournement](#règle-du-retournement-)
    - [Passage et fin de partie](#passage-et-fin-de-partie-)
    - [Conseil stratégiques essentiels](#conseils-stratégiques-essentiels-)
2. [Création du jeu](#création-du-jeu)
3. [Installer et jouer](#installer-et-jouer-à-notre-jeu-othello-)
    - [Prérequis](#prérequis-)
    - [Installation du jeu](#installation-du-jeu-)
    - [Installation des dépendances](#installation-des-dépendances-)
    - [Lancement du jeu](#lancement-du-jeu-)
    

## Comment ça Marche

### Présentation

**Objectif du jeu :** avoir la majorité des pions de sa couleur à la fin de la partie
**Plateau :** 8x8 cases
Pions : bicolores, habituellement en noir et blanc (notre version est en rouge et bleu)

### Matériel et mise en place : 

Plateau 8x8 et 64 pions (32 noir/rouge et 32 blanc/bleu)
**Placement initial :** deux pions noirs et deux pions blancs au centre selon la disposition officielle. Voici un *exemple* si dessous :
![image debut](/Assets/screenshots/debut_partie.png)

### Déroulement du jeu : 
- Le joueur avec les pions noir commence la partie.

- À chaque tour, un joueur place un pion de sa couleur sur une case vide de façon à encadrer une ou plusieurs rangées continues de pions adverses entre le pion posé et un autre pion de sa couleur déjà présent sur le plateau.

- Les directions valides sont les 8 directions (horizontales, verticales, diagonales). Un coup est valide seulement s’il encadre au moins un pion adverse ; sinon il est illégal.

### Règle du retournement : 
Quand un joueur place un pion, tous les pions adverses pris en sandwich entre ce pion et un autre pion de sa couleur sont retournés, quelle que soit la direction (ligne, colonne ou diagonale). Voici un *exemple* pour qui vous visualisez bien comment cela marche :

![retournement](/Assets/screenshots/gameplay_retournement.gif)

### Passage et fin de partie : 

Si un joueur **n’a aucun coup valide**, il **passe** son tour ; si les deux joueurs passent consécutivement ou si le plateau est plein, la partie se termine.
**Comptage final :** on compte les pions de chaque couleur, celui qui en a le plus gagne.

### Conseils stratégiques essentiels : 

- **Contrôler les coins** est crucial parce qu’ils ne peuvent pas être retournés une fois pris, ils offrent un immense avantage pendant toute la partie.

- La priorité est **de conserver de la mobilité** (c’est‑à‑dire avoir plusieurs coups disponibles) tout en **limitant** ceux de l’adversaire. Cela **compte souvent plus** que de retourner quelques pions immédiatement.

## Création du jeu

Le jeu a tout d’abord été créé pour un projet qui fera sujet d’une note au CPNV.
Voici des questions qui nous sont souvent posée :

-	Pourquoi avoir choisi les couleurs bleu et rouge pour vos pions ?

    **Natan :** Nous voulions que notre jeu se distingue des autres et qu’il ait sa propre identité visuelle. Le bleu et le rouge nous semblaient parfaits pour lui donner une personnalité unique.

-	Comment fonctionnait votre équipe ?

    **Natan :** Notre équipe était bien organisée. Théo préférait travailler sur le frontend, tandis que je me concentrais sur le backend. Nous avons donc réparti les tâches en fonction de nos forces, et ça a très bien marché.
-	Avez-vous utilisé de l’AI pour vous aider dans votre projet ?

    **Natan :** Pour être totalement honnête, oui. Nous avons demandé de l’aide à l’IA lorsque nous ne savions pas comment avancer. Toutes les utilisations ont été clairement indiquées dans le code à l’aide de commentaires.
    
-	Votre jeu est sur github, cela veut dire que je peux le télécharger gratuitement ?

    **Natan :** Exactement ! Notre but est que vous puissiez y jouer librement et vous amuser. Vous pouvez aussi le modifier si vous le souhaitez. En revanche, il est strictement interdit d’utiliser ce projet pour gagner de l’argent.

-	Avez-vous mis des easter eggs dans votre jeu ?

    **Natan :** Oui ! Il y a deux mode visuel caché dans le menu des paramètres. Je ne dirai pas lesquels. Bonne chance à ceux qui voudront les trouver !
*Dev Art mode :*
![dev-art mode](/Assets/screenshots/devart_mode.png)
*glitched mode :*
![Glitched mode](/Assets/screenshots/glitched_mode.png)

# Installer et jouer à notre jeu Othello :

Notre jeu propose deux méthodes d’installation, selon ce que vous souhaitez faire :
- Installation simple (pour jouer uniquement):
Cette méthode est la plus rapide : il vous suffit d’installer le fichier .exe et vous pouvez commencer à jouer immédiatement.
- Installation complète (pour modifier le jeu) :
Cette version est destinée aux personnes qui veulent accéder au code source et personnaliser le jeu. L’installation est un peu plus technique, mais elle vous donne accès à l’ensemble des fichiers du projet.

## Installation simple : 

Vous pouvez installer notre fichier .exe de deux manières : 

- Installation via le terminal (CMD)
- Installation en téléchargeant directement le fichier .exe

### Installation via le CMD
1. Ouvrez le CMD
2. Exécutez la commande suivante pour télécharger l'exécutable :
```
curl -L -o RELEASE.Othello.1.1.2.exe https://github.com/NPone29/MA-24_NaTh/releases/download/V1.1/RELEASE.Othello.1.1.2.exe

```

### Installation en téléchargeant le fichier
1. Cliquer sur le lien de notre **release** : https://github.com/NPone29/MA-24_NaTh/releases
2. Téléchargez le fichier .exe.

## Installation complète



### Prérequis :

Avant d’installer le jeu, assurez-vous d’avoir Git et Python installés sur votre ordinateur :

- Git : https://git-scm.com/install/
- Python : https://www.python.org/downloads/

### Installation du jeu :
1.	Ouvrez Git CMD (ou tout autre terminal compatible). 
2.	Si vous souhaitez installer le jeu dans un dossier spécifique, utilisez la commande suivante pour vous y déplacer : cd "votre chemin d’accès"
3.	Clonez le dépôt Git avec la commande suivante :
``` bash
git clone "https://github.com/NPone29/MA-24_NaTh"
```
Une fois le dépôt cloné, vous êtes presque prêt à jouer à notre version d’Othello !

### Installation des dépendances :

*Pygame :*

Pour installer Pygame, exécutez cette commande dans le terminal : pip install pygame


Si vous avez du mal avec l’installation de pygame ou alors que le terminal vous affiche une erreur, voici la solution pour pouvoir quand même l’installer :
- Télécharger [Pycharm](https://www.jetbrains.com/pycharm/download/?section=windows ) Community (gratuit)
- Ou installer une version antérieure de python (ex : 3.11)

*Tkinter :*

Installez Tkinter avec : 
``` bash
pip install tkinter
```

*Pillow :*

Installez Pillow avec : 

``` bash
pip install pillow
```

### Lancement du jeu :

Une fois tous les packages installés, le jeu devrait fonctionner correctement.

Pour démarrer le jeu, vous avez juste à aller dans le dossier du dépot et exécuter le main.py :
``` bash
cd MA-24_NaTh/
python main.py
```

Si vous rencontrez des problèmes, n’hésitez pas à nous contacter par email :
*natan.humblet@eduvaud.com*

Nous espérons que vous prendrez autant de plaisir à jouer que nous en avons eu à le développer.

**Bonne partie !**

