# Flask Storage System
Flask Storage is a simple project for a storage platform, focused on a interesting and practical use of the [Flask](http://flask.pocoo.org/) framework for Python.

### File Structure
```
.
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── static
│   │   └── css
│   │       └── core.css
│   ├── templates
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── index.html
│   │   ├── login_form.html
│   │   ├── upload_form.html
│   │   └── view_files.html
│   └── uploads
│       └── Welcome.txt
├── config.py
├── docs
│   └── README.md
├── flaskstorage.py
├── Pipfile
├── Pipfile.lock
└── Procfile (on deployment server)
```

## Running deployed server
To see the deployed server on [Heroku](https://heroku.com), enter [this](https://salesvictor-storage.herokuapp.com/) link.

## Running local server
The following instructions are based on Linux (Ubuntu >= 16.04) setup for localhosting of the web application project.

### Prerequisites
First, install ```Python3.6``` (previous versions may not work). Then, install ```pip``` and ```pipenv``` for packages and virtual enviroment management. 

Then install the following dependencies at your virtual enviroment:
* [Flask](http://flask.pocoo.org/)

All these flask dependencies needed are set in the Pipfile configuration for pipenv.

### Running

To run the code, first ```export FLASK_APP=flaskstorage.py```, then execute ```pipenv run flask run``` on root directory.

## Authors

* **Victor Sales** - [salesvictor](https://github.com/salesvictor)

## Acknowledgments

* **Professor Edgar Toshiro Yano** - [Curriculum](http://buscatextual.cnpq.br/buscatextual/visualizacv.do?id=K4798593T1&idiomaExibicao=2)
