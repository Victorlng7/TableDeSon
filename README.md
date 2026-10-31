🚀 Lancement automatique du contrôleur audio Arduino sous Windows

Ce guide explique comment configurer Windows pour lancer automatiquement le contrôleur audio Python au démarrage de la session utilisateur, sans afficher de fenêtre de terminal.

1. Architecture du projet

Le projet utilise trois types de fichiers :

.vbs : lance le fichier BAT en arrière-plan, sans afficher de fenêtre.
.bat : lance le programme Python.
.py : contient le code du contrôleur audio et la communication avec l'Arduino.
Organisation des fichiers

Les fichiers doivent être organisés comme suit :

text
C:\Users\victor\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\
│
├── start_audio.vbs
│
└── src\
 ├── main.py
├── start_audio.bat
├── windows_audio.py
│
└── **pycache**\

Important :

start_audio.vbs doit être directement dans le dossier Startup de Windows.
Les scripts Python doivent être placés dans le dossier src.
start_audio.bat doit également être dans src.
Les autres modules Python utilisés par le programme doivent être accessibles depuis ce dossier. 2. Le fichier VBS

Créer un fichier nommé start_audio.vbs directement dans le dossier de démarrage Windows.

Emplacement :

text
%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup

Contenu de start_audio.vbs :

vbscript
Set WshShell = CreateObject("WScript.Shell")
Set Fso = CreateObject("Scripting.FileSystemObject")

batPath = Fso.BuildPath(Fso.GetParentFolderName(WScript.ScriptFullName), "src\start_audio.bat")
WshShell.Run """" & batPath & """", 0, False

Explication du code

1. Création des objets Windows

vbscript
Set WshShell = CreateObject("WScript.Shell")
Set Fso = CreateObject("Scripting.FileSystemObject")

WshShell permet d'exécuter des commandes Windows.
Fso permet de manipuler les chemins et les fichiers.

2. Récupération du chemin du fichier BAT

vbscript
batPath = Fso.BuildPath(Fso.GetParentFolderName(WScript.ScriptFullName), "src\start_audio.bat")

Cette instruction récupère automatiquement le dossier dans lequel se trouve le fichier VBS, puis construit le chemin vers src\start_audio.bat.

Cela évite d'écrire un chemin absolu dépendant du nom d'utilisateur Windows.

3. Exécution du fichier BAT

vbscript
WshShell.Run """" & batPath & """", 0, False

Les paramètres sont :

batPath : chemin du fichier à exécuter.
0 : exécute le programme sans afficher de fenêtre.
False : n'attend pas la fin du programme pour continuer. 3. Le fichier BAT

Créer un fichier nommé start_audio.bat dans le dossier src.

Contenu :

bat
@echo off
py main.py

Explication
@echo off désactive l'affichage des commandes dans le terminal.
py main.py lance le programme Python principal.

Le fichier BAT étant lancé depuis le dossier Startup via le VBS, il est préférable de préciser le répertoire de travail.

Version recommandée :

bat
@echo off
cd /d "%~dp0"
py main.py

%~dp0 représente le dossier contenant le fichier BAT.

Cela garantit que Python trouve correctement les autres modules du projet, même si le répertoire courant de Windows est différent.

Attention aux environnements virtuels :

Si les bibliothèques Python sont installées dans un environnement .venv, il faut utiliser son interpréteur :

bat
@echo off
cd /d "%~dp0"
..\.venv\Scripts\python.exe main.py

Adapte le chemin si ton .venv se trouve ailleurs.

4. Installation dans le démarrage Windows

Pour ouvrir directement le dossier de démarrage :

Appuyer sur Win + R.
Saisir shell:startup.
Valider avec Entrée.
Placer start_audio.vbs dans ce dossier.

Le dossier doit contenir le VBS et le sous-dossier src contenant les scripts.

5. Fonctionnement au démarrage

Lorsque Windows démarre et que l'utilisateur ouvre sa session :

Windows exécute automatiquement start_audio.vbs.
Le VBS localise src\start_audio.bat.
Le VBS lance le BAT sans afficher de fenêtre.
Le BAT lance main.py.
Le programme Python démarre la communication série avec l'Arduino.
Le contrôleur audio fonctionne en arrière-plan. 6. Dépannage
Le programme ne démarre pas

Lancer manuellement start_audio.bat pour vérifier qu'il fonctionne.

Les bibliothèques Python sont introuvables

Vérifier que le BAT utilise bien le Python de l'environnement virtuel contenant les bibliothèques nécessaires.

L'Arduino n'est pas détecté

Vérifier :

Que l'Arduino est branché.
Que le port COM configuré dans main.py est correct.
Qu'aucun autre programme n'utilise déjà ce port série.
Besoin de déboguer le programme

Pour afficher les erreurs, lancer directement start_audio.bat plutôt que le fichier VBS.

Cela permet de voir les messages print() et les éventuelles exceptions Python.

7. Résultat final

Une fois configuré, le contrôleur audio se lance automatiquement à chaque ouverture de session Windows, sans intervention manuelle et sans fenêtre de terminal visible.

Aucune installation supplémentaire n'est nécessaire pour le lancement automatique, en dehors de Python et des dépendances nécessaires au projet.
