# Le moteur de template Jinja2


<div>
<img src="https://img.shields.io/badge/flask-v0.12.2-brightgreen.svg"> 
<img src="https://img.shields.io/badge/python-v3.4-brightgreen.svg">
</div>

<div style="text-align:center;">
<img src="http://jinja.pocoo.org/docs/2.10/_static/jinja-small.png" height="150"/>
</div>


## Pourquoi un moteur de template

Dans notre première implémentation du code, nous avons créer le code html de notre site directement dans notre code Python. En pratique, le fait de mixer du code html avec du code Python peut rapidement devenir fastidieux. Pour éviter ce problème, il est possible de sous-traiter la conception des pages à un moteur de template comme Jinja2 (le plus populaire ne Python). A chacun son rôle, Flask pour le traitement des informations et Jinja2 pour la création des pages. En adoptant cette approche, nous respectons un principe de base de la programmation: le celèbre **Separation of Concerns**.

Concrêtement, un moteur de template permet à partir de plusieurs informations passées en entrée (dictionnaire Python par exemple) de construire un fichier avec une structure bien spécifique (html, xml, txt, tex). Tout comme d'autres langage de programmation, le moteur de template intègre certaines structures de contrôle de base comme le `for` ou le `ìf`. Le moteur de template possède également un mécanisme d'héritage permettant d'éviter les répétitions de codes et de respecter le dogmatique principe **Don't Repeat Yourself**.

## Premier pas

> Installation de Jinja2: pip install jinja2

Pour illustrer le fonctionnement de Jinja2, nous allons créer le contenu html de notre application à partir de deux templates html: `base.html`et `index.html`
Pour intégrer ces templates à notre application, les fichiers doivent respecter une arborescence particulière. Plus précisement, le répertoire de votre projet doit être organisé de la manière suivante:

```
server.py
/templates
    base.html
    index.html
```

Le fichier `base.html` intègre le structure de base de chaque page html. Ce fichier définit deux blocs nommée `titre` et `contenu`.

[import](./src/src3/templates/base.html)

Le fichier `index.html` spécifie comment convertir une liste de contact, passée en entrée via une variable `contact_list`, en contenu html. Ce second fichier hérite de la structure du template `base.html`. En particulier, ce template rédefinit le contenu des blocs `titre` et `contenu`. Notons que pour construire les différentes lignes du tableau html, le template utilise une boucle `{% for ... in ... %}{% endfor %}`. 

[import](./src/src3/templates/index.html)

Pour tester le bon fonctionnement de nos templates, il est possible de créer un script python dans le répertoire template.

[import](./src/src3/templates/test.py)

Ce script permet de charger le template `index.html` et d'afficher le résultat. Il peut être éxecuté en lancant la commande `python test.py` dans votre terminal. Notons que pour l'instant, la méthode `render()` du template Jinja2 est appelée sans argument d'entrée, et notamment sans la variable `contact_list`. Pour cette raison, notre tableau html ne contiendra pour l'instant aucune ligne.

## Seconde implémentation

Pour utiliser le moteur de template Jinja2 avec Flask, il est nécessaire d'importer la fonction `render_template` (`from flask import render_template`). La fonction `render_template` prend en entrée plusieurs arguments:

* un template html disponible dans le repertoire `templates`.
* une liste de variables à passer au template.

Le programme suivant montre comment intégrer nos templates Jinja2 à notre première version de l'application.

[import](./src/src3/server.py)
