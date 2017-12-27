# Le framework Bootstrap 

<div>
<img src="https://img.shields.io/badge/bootstrap-v4.00-brightgreen.svg"> 
</div>

<div style="text-align:center;">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Boostrap_logo.svg/1920px-Boostrap_logo.svg.png" height="150"/>
</div>

## Contexte

Même si notre application est fonctionnelle, son design reste relativement sommaire. Le Web design est une discipline relativement complexe. En effet, cette discipline nécessite d'avoir des qualités artistiques (ce qui n'est pas donné à tout le monde !) mais pas que: il faut également avoir des notions en UX design et en programmation. Pour developper rapidement une interface de qualité, il est souvent préférable d'utiliser un framework front-end (orienté client). Dans cette partie, nous allons utiliser le framework le plus populaire: Bootstrap.


## Principe

Bootstrap est un framework front-end développé par des employés de Twitter. Ce framework possède en ensemble de classes CSS et de fonctions Javascript permettant de réaliser des pages complexes. Bootstrap permet la construction de pages **Responsive** c-a-d s'adaptant automatiquement à la résolution de l'écran. Cela permet entre autre de developper une seule et même interface pour des plateformes ayant des tailles d'écran très différentes (ordinateur, téléphone, tablette, etc).

L'importation de la librairie Bootstrap s'obtient en ajoutant dans la balise `head` de nos pages HTML, la feuille de style suivante

```
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">
```

Avant la fermeture de la balise `<body>`, il faut également importer un ensemble de libraires javascript:

```
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.3/umd/popper.min.js" integrity="sha384-vFJXuSJphROIrBnz7yo7oB41mKfc8JzQZiCq4NCceLEaO4IHwicKwpJf9c9IpFgh" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js" integrity="sha384-alpBpkh1PFOepccYVYDB4do5UnbKysX5WZXm3XxPqe5iKTfUKjNkCk9SaVuEZflJ" crossorigin="anonymous"></script>
```


## Implémentation (Part V)

La vidéo présentée ci-dessous illustre le rendu final de notre application.

<iframe width="100%" height="400" src="https://www.youtube.com/embed/3TWU1YbLeGA?rel=0" frameborder="0" allowfullscreen></iframe>

Le code complet de notre application est disponible sur [Github](https://github.com/vincentchoqueuse/gitbook_flask/tree/master/src/src6).
