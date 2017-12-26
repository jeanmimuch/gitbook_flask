# Les formulaires HTML5

<div>
<img src="https://img.shields.io/badge/HTML-v5-brightgreen.svg"> 
</div>

<div style="text-align:center;">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/HTML5_logo_and_wordmark.svg/512px-HTML5_logo_and_wordmark.svg.png" height="150" style="padding-bottom: 20px;"/>
</div>

Dans toutes les applications informatiques de gestion, l'utilisateur peut consulter des informations mais également, si il en a l'autorisation, les éditer (création, modification ou suppression). Pour éditer ces informations, l'utilisateur (client) doit renvoyer un formulaire HTML5 au serveur.

## Principe

> La documentation HTML5 sur les formulaires est disponible à l'adresse: (https://www.w3schools.com/tags/tag_form.asp)

Un formulaire HTML est composé d'un ou plusieurs élements. Ceux-ci peuvent être des zones de texte, des boîtes de sélection, des boutons, des cases à cocher ou des boutons radio. Sauf cas particulier, un formulaire intègre également un bouton de soumission permettant de déclencher la transmission des données vers le serveur.

Pour réaliser un formulaire en HTML, il fait encapsuler un ensemble d'élements (`<input>`, `<select>`, etc) dans une balise `<form>`. 

```
<form action="#" method="get">
Nom: <input type="text" name="nom">
<input type="submit" value="Submit">
</form>
```

La balise `<form>` contient plusieurs attributs:
* L'attribut `action` (optionnel) indique à quelle adresse les données seront envoyées. Si l'attribut `action` n'est pas spécifiée, le formulaire est renvoyé à la même url.
* L'attribut `method` indique comment les données seront envoyées. Il existe deux methodes possibles: `get`et `post`. En utilisant la méthode `get`, les données sont envoyées via l'url. En utilisant la méthode `post`, les données sont envoyées dans le corps de la requête (méthode recommandée). 

## Troisième Implémentation

### Templates HTML

Dans notre application, nous allons utiliser plusieurs templates pour la création, la modification et la suppression des contacts. 

```
server.py
/templates
    base.html
    index.html
    form.html
    create.html
    update.html
    delete.html
```

#### index.html

Le template `index.html` permet de lister l'ensemble des contacts dans un tableau html. Par rapport à notre version précédente, nous avons ajouté une colonne `action`. Cette colonne indique les urls à utiliser pour modifier ou supprimer un contact particulier. Ces urls utilisent la variable `loop.index` pour identifier de manière unique un contact. 

[import](./src/src4/templates/index.html)

#### form.html

Le template `form.html` contient un formulaire permettant d'éditer les informations d'un contact. Ce formulaire utilise la méthode `post` pour transmettre les informations aux serveurs. Les différents élements du formulaire sont initialisés via la variable `contact`.

[import](./src/src4/templates/form.html)

#### create.html et update.html

Les fichiers `create.html` et `update.html` héritent du template `form.html`. Ces deux fichiers surchargent simplement le bloc `title`.

[import](./src/src4/templates/create.html)

[import](./src/src4/templates/update.html)

#### Fichier delete.html

Le fichier `delete.html` contient un formulaire permettant à l'utilisateur de confirmer la suppression d'un contact.

[import](./src/src4/templates/delete.html)

### Application Flask

Pour gérer la consultation et l'édition des informations, notre fichier `server.py` intègre trois nouveaux décorateurs de fonctions . Les fonctions `create`, `update`, `delete` gèrent à la fois le traitement des requêtes `get` (envoi des formulaires au client) que le traitement des requêtes `post` (modification des informations au niveau du serveur). Concernant les fonctions `update` et `delete`, ces deux fonctions prennent en entrée un paramètre entier `ìd`. Ce paramètre permet d'identifier de manière unique un contact.

[import](./src/src4/server.py)

Le code complet de notre application est disponible sur [Github](https://github.com/vincentchoqueuse/gitbook_flask/tree/master/src/src4). La vidéo présentée ci dessous illustre le fonctionnement de notre application.
 
<iframe width="100%" height="400" src="https://www.youtube.com/embed/CZIkn_bdoDg?rel=0" frameborder="0" allowfullscreen></iframe>

