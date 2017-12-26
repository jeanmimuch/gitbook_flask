# Le moteur SQLlite3


<div>
<img src="https://img.shields.io/badge/sqlite-v3.13-brightgreen.svg"> 
</div>

<div style="text-align:center;">
<img src="https://upload.wikimedia.org/wikipedia/commons/3/38/SQLite370.svg" height="150"/>
</div>

## Pourquoi une base de données ?

Actuellement, notre application utilise une liste Python pour stocker les informations. Lorsque le serveur est relancé, les données sont réinitialisés et toutes les modifications effectuées par l'utilisateur sont perdues. En pratique, il est nécessaire d'utiliser un moyen de stockage persistant. Dans cette partie, nous allons utiliser une **base de données** sqlite. En utilisant cette organisation, nous respectons une fois de plus le célèbre Separation of Concerns: Flask pour le traitement des informations, Jinja2 pour la gestion des templates et SQLite pour le stockage des données.


## Le moteur SQLite

SQLite est une librairie logicielle implémentant un moteur de base de données SQL.


## Implémentation

### Creation de la base de données

Depuis votre terminal, il est possible de créer une base de données SQLite via la commande sqlite3.

```
$ sqlite3 data.db
```

Pour notre application, nous allons créer une table contact contenant plusieurs élèments.

```
sqlite> CREATE TABLE contact(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            prenom TEXT NOT NULL,
            mail TEXT NOT NULL,
            tel TEXT NOT NULL);
```

Une fois que la table CONTACT a été crée, nous pouvons y ajouter des élements via la syntaxe `INSERT INTO ... VALUES ...'.

```
sqlite> INSERT INTO CONTACT (nom,prenom,mail,tel)
            VALUES
                ("Einstein","Albert","albert@emc2.com","06.00.00.00.00"),
                ("Shannon","Claude","claude@fesup2fmax.com","06.00.00.00.00"),
                ("Fourier","Joseph","joseph@maserie.fr","09.00.03.00.01");
```

Pour vérifier que tout s'est bien passé, il est possible de lister l'ensemble des élements contenus dans la table CONTACT via la commande

```
SELECT * FROM contact;
```

Finalement pour quitter sqlite3, il suffit de lancer la commande `.exit`.

### Modification des Templates

Dans notre première implémentation, les urls permettant de modifier ou de supprimer les enregistrements étaient basées sur l'indexation de la liste `contact_list`. Nous allons maintenant utiliser le champ `ìd` de la table `contact`. Pour réaliser cette modification, notre template `ìndex.html` doit être remplacé par le template suivant

[import](./src/src5/templates/index.html)

### Modification du fichier `server.py`

[import](./src/src5/server.py)


