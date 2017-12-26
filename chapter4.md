# Gestion des formulaires

Dans toutes les applications informatiques de gestion, le client peut consulter des informations mais également, si il en a l'autorisation, les éditer. L'ensemble des opérations réalisables est souvent désigné sous l'acronyme **CRUD** (Create Read Update Delete). Dans cette partie, nous allons apprendre à gérer ces opérations avec le framework Flask. Contrêtement, la gestion de ces opérations va nécessiter deux ajouts.

* Ajout de nouveaux templates HTML pour la création, la modification et la suppression des données.
* Ajout de plusieurs urls dans le fichier `server.py` pour le traitement des requêtes de création, de modification et de suppression.

## Formulaire HTML

> La documentation HTML5 sur les formulaires est disponible à l'adresse: (https://www.w3schools.com/tags/tag_form.asp)

Un formulaire HTML est composé d'un ou plusieurs élements. Ceux-ci peuvent être des zones de texte, des boîtes de sélection, des boutons, des cases à cocher ou des boutons radio. La plupart du temps, un formulaire intègre également un bouton de soumission permettant de déclancher la transmission des données vers le serveur.

![Formulaire HTML](img/formulaire.png)

Pour réaliser un formulaire en HTML, il fait encapsuler un ensemble d'élements (`<input>`, `<select>`, etc) dans une balise `<form>`. 

```
<form action="#" method="get">
Nom: <input type="text" name="nom">
<input type="submit" value="Submit">
</form>
```

La balise `<form>` contient plusieurs attributs:
* L'attribut `action` indique à quelle adresse les données seront envoyées. En indiquant la valeur `"#"`, les données sont renvoyées à la même adresse.
* L'attribut `method` indique comment les données seront envoyées. Il existe deux methodes possibles: `get`et `post`. En utilisant la méthode `get`, les données seront envoyées via l'url. En utilisant la méthode `post`, les données seront envoyées dans le corps de la requête (méthode recommandée). 

## Templates HTML

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

### Fichier index.html

[import](./src/src4/templates/index.html)

### Fichier form.html

Le fichier `form.html` décrit le formulaire pour l'édition d'un contact. Ce formulaire utilise la méthode `post` et revoie les données à la même adresse. Notons que les différents élements sont initialisés via la variable `contact`.

[import](./src/src4/templates/form.html)

### Fichiers create.html et update.html

Les fichiers `create.html' et 'update.html' héritent du template `form.html`. Ces deux fichiers surchargent simplement le bloc `title`.

[import](./src/src4/templates/create.html)

[import](./src/src4/templates/update.html)

### Fichier delete.html

[import](./src/src4/templates/delete.html)

## Application Web (fichier server.py)

[import](./src/src4/server.py)

## Résultat

Le code complet est disponible sur [Github](https://github.com/vincentchoqueuse/gitbook_flask/tree/master/src/src4). La vidéo ci dessous montre le resultat final.
 
<iframe width="100%" height="400" src="https://www.youtube.com/embed/CZIkn_bdoDg?rel=0" frameborder="0" allowfullscreen></iframe>

