# Le moteur de templates Jinja2


<div>
<img src="https://img.shields.io/badge/jinja-v2.10-brightgreen.svg"> 
</div>

<div style="text-align:center;">
<img src="http://jinja.pocoo.org/docs/2.10/_static/jinja-small.png" height="150"/>
</div>


## Pourquoi un moteur de templates ?

Dans notre première implémentation du code, nous avons créer le code html de notre site directement dans notre code Python. En pratique, le fait de mixer du code html avec du code Python peut rapidement devenir fastidieux. Pour éviter ce problème, il est possible de sous-traiter la conception des pages à un moteur de template comme Jinja2 (le plus populaire ne Python). A chacun son rôle, Flask pour le traitement des informations et Jinja2 pour la création des pages. En adoptant cette approche, nous respectons un principe de base de la programmation: le celèbre **Separation of Concerns**.

Concrêtement, un moteur de template permet à partir de plusieurs informations passées en entrée (dictionnaire Python par exemple) de construire un fichier avec une structure bien spécifique (html, xml, txt, tex).


## Le moteur Jinja2

> La Documentation de Jinja2 est disponible à l'adresse: (http://jinja.pocoo.org/docs/2.10/)

Les templates Jinja2 sont stockés dans des fichiers html intègrant des **tags** particuliers. Certains tags permettent notamment d'inclure des structures de contrôle. Le moteur de template possède également un mécanisme d'héritage permettant d'éviter les répétitions de codes et de respecter le dogmatique **Don't Repeat Yourself**.

### Variables

L'affichage d'une variable passée en entrée s'obtient via la syntaxe

```
{{ma_variable}}
```

### Structures de contrôle

Jinja2 intègre deux structures de contrôles: le for et le if. 

```
{% for variable in variable_list %}
    Ma variable {{variable}}
{% endfor %}
```

```
{% if ma_variable %}
    La variable est égale à {{ma_variable}}
{% else %}
    La variable n'existe pas
{% endif %}
```

### Bloc personnalisé

Jinja2 permet d'intégrer des blocs personnalisés. Ces blocs sont souvent surchargés via un mécanisme d'heritage. Le recours à un mécanisme d'heritage permet d'éviter des recopies de codes inutiles.

```
{% block titre%} Mon Titre {% endblock %}
```

### Héritage

Un template peut hériter d'un autre template en ajoutant au début du fichier le tag

```
{% extend "base.html" %}
```

## Implémentation.

Pour notre application, nous allons créer le contenu des pages html à partir de deux templates: `base.html`et `index.html`
Pour intégrer ces templates à notre application, les fichiers doivent respecter une arborescence particulière. Plus précisement, le répertoire de votre projet doit être organisé de la manière suivante:

```
server.py
/templates
    base.html
    index.html
```

### Templates (fichiers base.html et index.html)

Le fichier `base.html` intègre le structure de base de chaque page html. Ce fichier définit deux blocs nommée `titre` et `contenu`.

[import](./src/src3/templates/base.html)

Le fichier `index.html` spécifie comment convertir une liste de contact, passée en entrée via une variable `contact_list`, en contenu html. Ce second fichier hérite de la structure du template `base.html`. En particulier, ce template rédefinit le contenu des blocs `titre` et `contenu`. Notons que pour construire les différentes lignes du tableau html, le template utilise une boucle `{% for ... in ... %}{% endfor %}`. 

[import](./src/src3/templates/index.html)


### Flask (fichier server.py)

Pour utiliser nos templates Jinja2 avec notre application Flask, il faut préalablement importer la fonction `render_template` (`from flask import render_template`). La fonction `render_template` prend en entrée plusieurs arguments:

* un template html disponible dans le repertoire `templates`.
* une liste de variables à passer au template.

Le programme suivant montre comment intégrer les templates `base.html` et `index.html` (voir partie précédente) à notre première version de l'application.

[import](./src/src3/server.py)

Le code complet est disponible sur [Github](https://github.com/vincentchoqueuse/gitbook_flask/tree/master/src/src3).
