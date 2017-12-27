# Les formulaires HTML5

<div>
<img src="https://img.shields.io/badge/HTML-v5-brightgreen.svg"> 
</div>

<div style="text-align:center;">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/HTML5_logo_and_wordmark.svg/512px-HTML5_logo_and_wordmark.svg.png" height="150" />
</div>

## Contexte

Dans toutes les applications informatiques de gestion, l'utilisateur peut consulter des informations mais également, si il en a l'autorisation, les éditer. Pour éditer ces informations, l'utilisateur doit renvoyer un formulaire au serveur. Ce formulaire est le plus ouvent codé en HTML5.

## Principe

> La documentation HTML5 sur les formulaires est disponible à l'adresse: (https://www.w3schools.com/tags/tag_form.asp)

Un formulaire HTML est composé d'un ou plusieurs élements. Ceux-ci peuvent être des zones de texte, des boîtes de sélection, des boutons, des cases à cocher ou des boutons radio. Sauf cas particulier, un formulaire intègre également un bouton de soumission permettant de déclencher la transmission des données vers le serveur.

Pour réaliser un formulaire en HTML, il faut utiliser une balise `<form>`. 

```
<form action="#" method="get">
Nom: <input type="text" name="nom">
<input type="submit" value="Submit">
</form>
```

La balise `<form>` contient plusieurs attributs:
* L'attribut `action` (optionnel) indique à quelle adresse les données seront envoyées. Si l'attribut `action` n'est pas spécifiée, le formulaire est renvoyé à la même url.
* L'attribut `method` indique comment les données seront envoyées. Il existe deux methodes possibles: `get`et `post`. En utilisant la méthode `get`, les données sont envoyées via l'url. En utilisant la méthode `post`, les données sont envoyées dans le corps de la requête (méthode recommandée). 

Plusieurs champs peuvent être encapsulé dans une balise `<form>`. Le plus souvent, ces champs sont définis via la balise

```
<input type= ... value= ... >
```

Le tableau présenté ci-dessous présente la liste des types disponibles en HTML5.



<table>
    <tr>
        <th>Type</th>
        <th>Rendu</th>
    </tr>
    <tr><td>button</td><td><input type="button" value="button" /></td></tr>
    <tr><td>checkbox</td><td><input type="checkbox" /></td></tr>
    <tr><td>color</td><td><input type="color" /></td></tr>
    <tr><td>date</td><td><input type="date" /></td></tr>
    <tr><td>datetime-local</td><td><input type="datetime-local" /></td></tr>
    <tr><td>email</td><td><input type="email" /></td></tr>
    <tr><td>file</td><td><input type="file" /></td></tr>
    <tr><td>image</td><td><input type="image" /></td></tr>
    <tr><td>month</td><td><input type="month" /></td></tr>
    <tr><td>number</td><td><input type="number" /></td></tr>
    <tr><td>password</td><td><input type="password" /></td></tr>
    <tr><td>radio</td><td><input type="radio" /></td></tr>
    <tr><td>range</td><td><input type="range" /></td></tr>
    <tr><td>search</td><td><input type="search" /></td></tr>
    <tr><td>submit</td><td><input type="submit" /></td></tr>
    <tr><td>tel</td><td><input type="tel" /></td></tr>
    <tr><td>text</td><td><input type="text" /></td></tr>
    <tr><td>time</td><td><input type="time" /></td></tr>
    <tr><td>url</td><td><input type="url" /></td></tr>
    <tr><td>week</td><td><input type="week" /></td></tr>

</table>



## Implémentation (Part III)

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

Le template `index.html` permet de lister l'ensemble des contacts dans un tableau html. Par rapport à notre version précédente, nous avons ajouté une colonne `action`. Cette colonne comporte deux liens hypertextes (balise `<a href= ... > ... </a>```). Ces liens pointent vers des urls permettant la modification ou la suppression d'un contact particulier. Pour identifier de manière unique un contact, ces urls utilisent la variable `loop.index`.

[import](./src/src4/templates/index.html)

#### form.html

Le template `form.html` contient un formulaire permettant d'éditer les informations d'un contact. Ce formulaire utilise la méthode `post` pour transmettre les informations aux serveurs. Les différents élements du formulaire sont initialisés via la variable `contact`.

[import](./src/src4/templates/form.html)

#### create.html et update.html

Les fichiers `create.html` et `update.html` héritent du template `form.html`. Ces deux fichiers surchargent simplement le bloc `title`.

[import](./src/src4/templates/create.html)

[import](./src/src4/templates/update.html)

#### delete.html

Le fichier `delete.html` contient un formulaire permettant à l'utilisateur de confirmer la suppression d'un contact.

[import](./src/src4/templates/delete.html)

### Application Flask

Pour gérer la consultation et l'édition des informations, notre fichier `server.py` intègre trois nouveaux décorateurs de fonctions . Les fonctions `create`, `update`, `delete` gèrent à la fois le traitement des requêtes `get` (envoi des formulaires au client) que le traitement des requêtes `post` (modification des informations côté serveur). Concernant les fonctions `update` et `delete`, ces deux fonctions prennent en entrée un paramètre entier `ìd`. Ce paramètre permet d'identifier de manière unique un contact.

[import](./src/src4/server.py)

Le code complet de notre application est disponible sur [Github](https://github.com/vincentchoqueuse/gitbook_flask/tree/master/src/src4). La vidéo présentée ci dessous illustre le fonctionnement de notre application.
 
<iframe width="100%" height="400" src="https://www.youtube.com/embed/CZIkn_bdoDg?rel=0" frameborder="0" allowfullscreen></iframe>

