# WETA - Workshop Enhanced Token Administration
*Initial Project forked thanks to https://github.com/SylannBin, a classmate.*

## Team Members :

- Valentin Mele
- William Besseau
- Michael Martinez
- Adrien Ceccaldi

## Objectives :

Create a token administration platform used by several types of users for EPSI Workshops.

## Techs :

- Backend : Flask (microframework Python 3)
- Front-end : Jinja2
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
First use installer for python3, then in cmd.exe as administrator :
```bash
pip install -U pip
pip install virtualenv
python -m virtualenv .venv
.venv\Scripts\activate
pip install -r requirements.txt
SET FLASK_APP=run.py
```

## Database Integration
```bash
$ sqlite3 weta.db
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
    errors.py
.gitignore
LICENSE
weta.db
README.md
requirements.txt
run.py
```
