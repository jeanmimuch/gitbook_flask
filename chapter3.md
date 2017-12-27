# Le moteur de templates Jinja2


<div>
<img src="https://img.shields.io/badge/jinja-v2.10-brightgreen.svg"> 
</div>

<div style="text-align:center;">
<img src="http://jinja.pocoo.org/docs/2.10/_static/jinja-small.png" height="150" />
</div>


## Contexte

Dans notre première implémentation, nous avons créé le code html de notre site directement dans notre code Python. En pratique, le fait de mixer du code html avec du code Python peut rapidement devenir fastidieux. Pour éviter ce problème, il est préférable de sous-traiter la conception des pages à un moteur de template comme Jinja2 (le plus populaire en Python). A chacun son rôle, Flask pour le traitement des informations et Jinja2 pour la création des pages. En adoptant cette approche, nous respectons un principe de base de la programmation: le celèbre **Separation of Concerns**.


## Principe

> La Documentation de Jinja2 est disponible à l'adresse: (http://jinja.pocoo.org/docs/2.10/templates/)

Le moteur de template Jinja2 permet, à partir de plusieurs informations passées en entrée, de construire un document avec une structure bien spécifique. Concrêtement, la construction d'un document html s'obtient à partir de deux fichiers.

* Une application Flask appelant la fonction Jinja2 `render_template`. Cette fonction est appelée avec deux paramètres: le nom du template et une liste de variables à passer au template.
* Un template html permettant la construction du document.

Pour construire un document à partir des informations passées en entrée, Jinja2 intègre des **tags** particuliers. 


Pour inclure le contenu d'une variable dans un template Jinja2, il faut utiliser le tag:

```
{{variable}}
``` 

Jinja2 intègre deux structures de contrôle: la boucle et le test conditionnel. Ces structures sont définis par les tags: 

```
{% for ... in ... %} ... {% endfor %}
```

```
{% if ... %} ... {% else %} ... {% endif %}
```

Pour éviter des répétitions entre templates, il est possible de recourir à un mécanisme d'héritage. Pour hériter de la structure d'un template `base.html`, il faut indiquer à la première ligne du template hérité:

```
{% extends 'base.html' %} 
```

Lors de l'héritage, certains blocs de codes peuvent être surchargés. Ces blocs sont définis via le tag


```
{% block mon_block %} ... {% endblock %}
```


## Seconde Implémentation

Pour notre application, nous allons créer le contenu des pages html à partir de deux templates: `base.html`et `index.html`
Pour intégrer ces templates à notre application, les fichiers doivent respecter une arborescence particulière. Plus précisement, le répertoire de notre projet doit être organisé de la manière suivante:

```
server.py
/templates
    base.html
    index.html
```

### Templates HTML

Le fichier `base.html` intègre le structure de base de chaque page html. Ce fichier définit deux blocs nommée `titre` et `contenu`.

[import](./src/src3/templates/base.html)

Le fichier `index.html` spécifie comment construire une page html à partir de la liste `contact_list` passée en entrée. Ce second fichier hérite de la structure du template `base.html`. En particulier, ce template surcharge le contenu des blocs `titre` et `contenu`. Notons que pour construire les différentes lignes du tableau html, le template utilise une boucle `{% for ... in ... %}{% endfor %}`. 

[import](./src/src3/templates/index.html)


### Application Flask 

Pour utiliser nos templates Jinja2 avec notre application Flask, nous devons préalablement importer la fonction `render_template` (`from flask import render_template`). La fonction `render_template` prend en entrée plusieurs arguments:

* un template html disponible dans le repertoire `templates`.
* une liste de variables à passer au template.

Le programme suivant montre comment intégrer les templates `base.html` et `index.html` dans notre application Flask. Le code complet de notre application est disponible sur [Github](https://github.com/vincentchoqueuse/gitbook_flask/tree/master/src/src3).

[import](./src/src3/server.py)

