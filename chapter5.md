# Le moteur SQLlite3


<div>
<img src="https://img.shields.io/badge/sqlite-v3.13-brightgreen.svg"> 
</div>

<div style="text-align:center;">
<img src="https://upload.wikimedia.org/wikipedia/commons/3/38/SQLite370.svg" height="150"/>
</div>

## Contexte

Actuellement, notre application utilise une liste Python pour stocker les informations. Lorsque le serveur est relancé, les données sont réinitialisés et toutes les modifications effectuées par l'utilisateur sont perdues. En pratique, il est nécessaire d'utiliser un moyen de stockage persistant. Dans cette partie, nous allons utiliser une **base de données** sqlite. En plus du stockage persistant, comme son nom l'indique, les bases de données SQLite gèrent la gestion des requêtes SQL.

## Le moteur SQLite

> La Documentation de SQLite3 est disponible à l'adresse: (https://www.sqlite.org/index.html)


SQLite est une librairie logicielle implémentant un moteur de base de données SQL.


## Quatrième Implémentation

Dans notre quatrième implémentation, nous allons considérer l'organisation de fichiers suivante:

```
server.py
data.db
/templates
    base.html
    index.html
    form.html
    create.html
    update.html
    delete.html
```


### Fichier data.db

Depuis votre terminal, nous allons créer une base de données SQLite via la commande:

```
$ sqlite3 data.db
```

Nous allons ensuite créer une table `contact` contenant plusieurs champs.

```
sqlite> CREATE TABLE contact(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            prenom TEXT NOT NULL,
            mail TEXT NOT NULL,
            tel TEXT NOT NULL);
```

Une fois que la table `contact` a été crée, nous pouvons y ajouter des élements via la syntaxe `INSERT INTO ... VALUES ...`.

```
sqlite> INSERT INTO CONTACT (nom,prenom,mail,tel)
            VALUES
                ("Einstein","Albert","albert@emc2.com","06.00.00.00.00"),
                ("Shannon","Claude","claude@fesup2fmax.com","06.00.00.00.00"),
                ("Fourier","Joseph","joseph@maserie.fr","09.00.03.00.01");
```

Pour vérifier que tout s'est bien passé, il est possible de lister l'ensemble des élements de la table `contact` via la commande

```
SELECT * FROM contact;
```

La commande `.exit` permet de quitter l'invite de commande sqlite3.

### Modification des Templates

Dans notre première implémentation, les urls permettant de modifier ou de supprimer les enregistrements étaient basées sur l'indexation de la liste `contact_list`. Nous allons maintenant utiliser le champ `ìd` de la table `contact`. Pour réaliser cette modification, nous devons remplacer les lignes 21 et 22 du template `ìndex.html` par

[import:21-22,unindent:"true"](./src/src5/templates/index.html)

### Modification du fichier `server.py`

Le code complet de notre application est disponible sur [Github](https://github.com/vincentchoqueuse/gitbook_flask/tree/master/src/src5).

[import](./src/src5/server.py)


