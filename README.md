# Nurse Quest

## Team members

- Nicolas Bouyssounousse
- Romain Vincent
- Yaniss Fournet
- Michael Martinez
- Valentin Mele
- Alexis Clément

## Objectifs

Créer une plateforme de gestion de patients pour infirmières qui aura comme fonctionnalités:

### Fonctionnalitées attendues
- Page d’accueil qui affiche les différents patients gérés par l’infirmière
- Pouvoir Créer/modifier/supprimer une rubrique patient
- Une rubrique patient contient:
    - Nom,
    - Prénom
    - Numéro de sécurité sociale (générez automatiquement)
    - Pathologie
    - Date de la plus récente visite
- Gérer les utilisateurs :
    - login/register
    - Gestion de mots de passes oubliés
    - Gestion des patients d’une infirmière (affectation/ non affectation)


## Choix technologiques en suspend

- Backend:
    - Serveur: Flask, Django
    - ORM : SQLAlchemy, ...
    - Base de données : sqlite, 
    - Hébergement/support: ?
- Front-end:
    - Static (le serveur envoie les pages html toutes faites, genre php): Jinja
    - Dynamique (besoin application client en javascript): angularjs, ...
    - template css: Bootstrap
    - pas de preprocesseur css
- Versionning : Github
- Intégration continue: Travis CI, jenkins
- Tests unitaires: Pytest, ... ?

# Lancer le serveur du projet sur sa machine
## Setup

### Linux
- `$ sudo apt-get install python3`
- `$ sudo apt-get install python3-venv`
- `$ pip install -U pip`
- `$ python3 -m venv .venv`
- `$ source .venv/bin/activate`
- `$ pip install -r requirements.txt`
- `$ export FLASK_APP=app/app.py`

### Windows
First use installer for python3, then in cmd.exe:
- `pip install -U pip`
- `pip install virtualenv`
- `python -m virtualenv .venv`
- `.venv/Scripts/activate`
- `pip install -r requirements.txt`
- `SET FLASK_APP=app/app.py`

### Mac
- `brew install python`
- `pip3 install virtualenv`
- `python3 -m virtualenv .venv`
- `source .venv/bin/activate`
- `pip install -r requirements.txt`
- `export FLASK_APP=app/app.py`

## Lancer le serveur (dev)

`flask run --reload`

# Organisation de l'application
## Routes:

- POST /register
- GET /login
- GET /logout
- GET /
- GET /patients
- GET /patients/<id>
- POST /patients/<id>
- PUT /patients/<id>
- PUT /patients/<id>/affect/<nurse_id>
- DELETE /patients/<id>
- GET /users
- GET /users/<id>
- PUT /users/<id>/resetpassword

## Folder Organisation
```
.venv/
app/
    static/
        css/
        js/
        img/
    templates/
        *.html
    Users/
        views.py
        models.py
        [schemas.py]
    Patients/
        views.py
        models.py
        [schemas.py]
    run.py
.gitignore
README.md
requirements.txt
```