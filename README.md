# TER
Ceci est un projet de recherche par Moulhat, Thivagini SUGUMAR et Julie VARENNE-PAQUET.
Il consiste à faire une affectation d'étudiants à des groupes de TD, en fonction de leurs inscriptions à des modules et d'un emploi du temps donné.

## Pré-requis
Pour que votre code s'exécute dans les meilleures conditions, il faut dans un premier temps disposer de PostgreSQL et d'avoir une Database déjà crée.
Il faudra également modifier le fichier "Connexion.py", qui permet de se connecter à PostgreSQL. Pour cela, vous devrez changer le mot de passe pour insérer le votre, ainsi que le nom de la Database (par défaut Université) par le nom que vous avez mis. Sans cela, la base de données ne pourra pas se créer.

## Exécuter le code
Pour exécuter le code, vous devrez utiliser la commande 
`python front.py`
Cela vous lancera alors l'interface de l'application. Il faudra choisir l'emploi du temps de votre choix, cliquer sur continuer, et cela vous lancera le programme.
Le code n'étant pas abouti, en théorie, la deuxième page d'affichage vous aurait permis d'avoir la liste des groupes et l'option de l'enregistrer.
Vous pouvez cepandant voir les résultats de l'algorithme , en affichage sur la console directement en executant `python App.py`, où on vous demande de faire un choix entre 3 options "a, b, ou c". Entrer  a, puis laissez l'agorithme tourner quelques minutes avant de voir le résultat
Le code est accompagné d'un rapport contenant une description du sujet approfondie, les recherches effectuées et les éventuelles améliorations de l'application.

## Contenu
Notre code possède une **base de données**. Le fichier `script.sql` contient toutes les créations et insertions pour les tables dont nous avons besoin. Le dossier BD, quant à lui, nous permet de regrouper toutes les fonctions qui vont interagir avec la base de données;

 - `Connexion.py`; Qui nous permet de nous connecter à la base de données
 - `Creation_tables.py` ; Qui nous permet la création des tables et la gestion d'erreur
 - `Insertions.py` ; Qui nous permet de créer de nouveaux tuples dans les tables déjà créées
 - `Modifications.py` ; Qui nous permet de faire des updates des tuples. Utile en particulier pour la table Inscription, afin de pouvoir attribuer un groupe de TD pour un élève dans une matière
 - `Recuperations.py` ; Qui nous permet de récupérer toutes les informations nécessaires
 
 Le dossier **Models** nous permet de contenir toutes les classes liées à chaque table, et donc de créer des objets en lien avec les tuples. Il existe un fichier pour chaque table.

Le dossier **Algorithme** est composé du fichier `Donnees.py` et contient toutes les fonctionnalités de l'algorithme, faisant également appel aux fonctions de Models.

