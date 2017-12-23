# Le micro framework Flask

![version](https://img.shields.io/badge/flask-v0.12.2-brightgreen.svg)
![version](https://img.shields.io/badge/python-v3.4-brightgreen.svg)

> Installation de Flask: `pip install flask`

Dans ce tutorial, nous allons apprendre à créer une application web pour gérer ses contacts. Dans un premier temps, nous allons considérer ici que nos contacts sont stockés dans une liste python. Notre premier objectif sera d'afficher les contacts dans un tableau html.

## Premier pas en Flask 

Pour créer un application web en Flask, nous allons créer un fichier `server.py`. Dans ce fichier, nous allons inscrire le code Python suivant:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

Les deux premières lignes perment d'importer la librairie Flask de créer votre application web. La 4ieme ligne indique que les requêtes pointant vers l'url "/" doivent être traitées par la fonction hello_world. Ici, cette fonction va renvoyer la chaine "Hello, World!"

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

2. Pour tester votre application, ouvrez votre navigateur internet à l'adresse: `http://127.0.0.1:5000/`. Si tout se passe bien, votre navigateur va afficher une page avec le contenu "Hello, World!".

## Première implémentation

Dans cette section, nous allons développer une application web minimale pour gérer ses contacts. Nous allons considérer ici que nos contacts sont stockés dans une liste de dictionnaires python initialisée dans le fichier server.py. Dans un premier temps, notre objectif sera d'afficher les contacts dans un tableau html (balise `<table>`).


```python
from flask import Flask
app = Flask(__name__)

contact_list=[{"nom":"Einstein","prenom":"Albert","tel":"06.00.00.00.00","mail":"albert@e_mc2.com"},
{"nom":"Shannon","prenom":"Claude","tel":"06.00.00.00.00","mail":"claude&fe_sup_2fmax.com"},
{"nom":"Fourier","prenom":"Joseph","tel":"09.00.03.00.01","mail":"joseph&ma_serie.fr"}]

@app.route('/')
def index():
    #construction de la chaine html
    html="<table>\n"
    html=html+"<tr>\n"
    html=html+"<th>Nom</th><th>Prenom</th><th>Telephone</th><th>Email</th>"
    html=html+"</tr>\n"

    for indice in range(len(contact_list)):
    mon_contact=contact_list[indice]

        html=html+"<tr>\n"
        html=html+"<td>"+mon_contact["nom"]+"</td>\n"
        html=html+"<td>"+mon_contact["prenom"]+"</td>\n"
        html=html+"<td>"+mon_contact["tel"]+"</td>\n"
        html=html+"<td>"+mon_contact["mail"]+"</td>\n"
        html=html+"</tr>\n"

    html=html+"</table>\n"
    return html
```






