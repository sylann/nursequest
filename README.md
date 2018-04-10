# WETA
# Workshop Enhanced Token Administration

# Initial Project forked thanks to https://github.com/SylannBin

## Team Members :

- Valentin Mele
- William Besseau
- Michael Martinez
- Adrien Ceccaldi

## Objectives :

Create a token administration platform used by several types of users for EPSI Workshops.

### Attended features : 

- TBA
- TBA
- TBA
- TBA
- TBA


## Techs :

- Backend : TBA
- Front-end : TBA
- Versionning system : Github
- Continuous Integration : VSTS - Agile Mode

# Local installation of the project

## Linux
```bash
$ sudo apt-get install python3
$ sudo apt-get install python3-venv
$ sudo apt-get install sqlite3
$ pip install -U pip
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ export FLASK_APP=run.py
```

## Windows
First use installer for python3, then in cmd.exe:
```bash
pip install -U pip
pip install virtualenv
python -m virtualenv .venv
.venv/Scripts/activate
pip install -r requirements.txt
SET FLASK_APP=run.py
```

## Database Integration
```bash
$ sqlite3 nursequest.db
# .tables usually list existing tables but there it'll just force sqlite to create the db
sqlite> .tables
# Exit sqlite shell
sqlite> .exit
# Start python shell
$ flask shell
>>> from app import db
>>> db.create_all()
>>> exit()
```

## Run server (dev)

```bash
flask run --reload
```

## Help 

[Google](https://www.google.fr/search?q=insert+problem+here)

[Flask](http://flask.pocoo.org/docs/0.12/quickstart/)

[Python string format](http://strftime.org/)

[Jinja filters](http://jinja.pocoo.org/docs/2.10/templates/#builtin-filters)

[Bulma](https://bulma.io/documentation/overview/start/)

[Font awesome icons](http://fontawesome.io/icons/)

# Organization
## Routes:

- POST /register
- GET /login
- GET /logout
- GET /
- GET /patients
- GET /patients/<id>
- POST /patients/<id>
- PUT /patients/<id>
- PUT /patients/<id>/assign/<nurse_id>
- DELETE /patients/<id>
- GET /users
- GET /users/<id>
- PUT /users/<id>/reset_password
- GET /diseases
- GET /diseases/update

## Routes temp

- GET /users/fake/<quantity>
- GET /patients/fake/<quantity>
- GET /diseases/fake/caught_diseases

## Folder Organisation
```
.venv/
app/
    static/
        css/
        js/
        img/
        fonts/
    templates/
        *.html
    models/
        __init__.py
        *.py
    views/
        __init__.py
        *.py
    __init__.py
    utils.py
.gitignore
LICENSE
nursequest.db
README.md
requirements.txt
run.py
```
