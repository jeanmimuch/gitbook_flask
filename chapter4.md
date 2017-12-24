# Gestion des formulaires

Dans toutes applications de gestion de données, il est 

# Pourquoi des formulaires

Dans toutes les applications informatiques de gestion, le client peut consulter des informations mais également, si il en a l'autorisation, les éditer. L'ensemble des opérations réalisables est souvent désigné via l'acronyme **CRUD** (Create Read Update Delete). Dans cette partie, nous allons apprendre à gérer ces opérations avec Flask.


## Gestion des templates

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
