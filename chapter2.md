# Le micro framework Flask

<div>
<img src="https://img.shields.io/badge/flask-v0.12.2-brightgreen.svg"> 
<img src="https://img.shields.io/badge/python-v3.4-brightgreen.svg">
</div>

<div style="text-align:center;">
<img src="http://flask.pocoo.org/static/logo/flask.svg" height="150"/>
</div>

Dans cette première partie, nous allons afficher une liste de contacts stockés dans une liste python dans un tableau html au moyen du Framework Flask.

## Pourquoi un framework web ?

Lors du développement d'une application web, il faut gérer des fonctionnalités très diverses telles que la gestion des requêtes http, leur routage, les interactions avec la base de données, l'authentification des utilisateurs, la protection du site vis à vis des requêtes malveillantes, le renvoi de pages html, etc. Le codage de l'ensemble de ses fonctionnalités peut rapidement devenir complexe. Pour aller plus vite (et éviter de réinventer la roue), il est possible d'utiliser un framework web intégrant déjà l'ensemble de ses fonctionnalités.

## Premiers pas

> Installation de Flask: `pip install flask`

Pour créer un application web en Flask, nous allons créer un fichier `server.py`. Dans ce fichier, nous allons inscrire le code Python suivant:

[import](./src/src1/server.py)

Les deux premières lignes permettent d'importer la librairie Flask et de créer votre application web. La 4ieme ligne est un décorateur de fonction Python. Ce décorateur indique que les requêtes pointant vers l'url "/" doivent être traitées par la fonction hello\_world. Ici, cette fonction va renvoyer la chaine "Hello, World!"

Pour lancer votre première application web, rien de plus simple.

1. Dans votre terminal, lancez les commandes suivantes

```
$ export FLASK_APP=server.py
$ flask run
```

Si tout se passe bien, Flask doit alors afficher les lignes suivantes sur votre terminal:

```
$ * Serving Flask app "server"
$ * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

1. Pour tester votre application, ouvrez votre navigateur internet à l'adresse: `http://127.0.0.1:5000/`. Si tout se passe bien, votre navigateur va afficher une page avec le contenu "Hello, World!".

## Première implémentation

Dans notre première implémentation, nous allons considérer que les contacts sont stockés dans une liste python nommée `contact_list`. Cette liste est initialisée dans le fichier `server.py`.

Le programme suivant permet d'afficher les contacts dans un tableau html \(balise `<table>`\).

[import](./src/src2/server.py)






