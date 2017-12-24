# Le micro framework Flask

<div>
<img src="https://img.shields.io/badge/flask-v0.12.2-brightgreen.svg"> 
<img src="https://img.shields.io/badge/python-v3.4-brightgreen.svg">
</div>

(http://flask.pocoo.org/static/logo/flask.svg)

> Installation de Flask: `pip install flask`

Dans ce tutorial, nous allons apprendre à créer une application web pour gérer ses contacts. Dans un premier temps, nous allons considérer ici que nos contacts sont stockés dans une liste python. Notre premier objectif sera d'afficher les contacts dans un tableau html.

## Premier pas en Flask

Pour créer un application web en Flask, nous allons créer un fichier `server.py`. Dans ce fichier, nous allons inscrire le code Python suivant:

[import](./src/src1/server.py)

Les deux premières lignes perment d'importer la librairie Flask de créer votre application web. La 4ieme ligne indique que les requêtes pointant vers l'url "/" doivent être traitées par la fonction hello\_world. Ici, cette fonction va renvoyer la chaine "Hello, World!"

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

Dans cette section, nous allons développer une application web minimale pour gérer ses contacts. Nous allons considérer ici que nos contacts sont stockés dans une liste de dictionnaires python initialisée dans le fichier server.py. Dans un premier temps, notre objectif sera d'afficher les contacts dans un tableau html \(balise `<table>`\).

[import](./src/src2/server.py)





