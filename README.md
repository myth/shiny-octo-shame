shiny-octo-shame
================

WebTek Prosject

## Setup virtualenv

### Install virtualenvwrapper

    sudo pip install virtualenvwrapper

### Create env
We are using Python 3, since we are not in the stoned age.

    mkvirtualenv -p /path/to/python3 envname

### Install requirements
While in enviroment:

    pip install -r req.txt


## Technology

### Form Controls

### CSS

### XML

We descided to provide a API interface for users who would like to use our data on their own pages or apps. The data is available as XML and can be found at the /car/xml/ url.

### Javascript

### Flask

We chose to use Python3 as a server side programming solution to ease the creation of the different pages through a template engine.

Here we choose to use Flask as out minimal framwork and Jinja2 as our template engine/language. Flask is a microframework for python that includes the minimal needed features for creating a website. This features includes templating and a basic router for urls. We use Flask to provide us with a good URL scheme so our urls look nice and is easily understood and the bindings to Jinja2.

Jinja2 allows us to create a base html template which can be used on every page on our website. This drasticly decreases the repetetive tasks we would have done if we needed to create every page manually. Jinja2s template language is simular to many other template languages like twig (php), nunjucks (node/javascript) and django (python).
