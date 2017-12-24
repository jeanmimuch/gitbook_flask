# Gestion des formulaires

Dans toutes applications de gestion de données, il est 

# Pourquoi des formulaires ?

Dans toutes les applications informatiques de gestion, le client peut consulter des informations mais également, si il en a l'autorisation, les éditer. L'ensemble des opérations réalisables est souvent désigné via l'acronyme **CRUD** (Create Read Update Delete). Dans cette partie, nous allons apprendre à gérer ces opérations avec Flask.


## Templates CRUD

En html, un formulaire est encapsulé dans une balise `form` (voir [documentation](https://www.w3schools.com/html/html_form_elements.asp)). En fonction des champs à éditer, différentes balises sont disponibles.


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

[import](./src/src4/templates/form.html)

### Fichier create.html

[import](./src/src4/templates/create.html)

### Fichier update.html

[import](./src/src4/templates/update.html)

### Fichier delete.html

[import](./src/src4/templates/delete.html)

## Application Web (fichier server.py)

[import](./src/src4/server.py)
