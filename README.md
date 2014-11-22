shiny-octo-shame
================

WebTek Project.

A live production version of the web site is available at http://lame.no

## Local project setup

### Install virtualenvwrapper

    sudo pip install virtualenvwrapper

### Create env
We are using Python 3, since we do not recide in the stone age.

    mkvirtualenv -p /path/to/python3 <envname>

### Install requirements
While in environment:

    pip install -r req.txt

### Run
From within the virtualenv:

    python app.py

## Technology

### CSS/LESS

We do not use any pre-made CSS framework in our project, like Bootstrap or similar frameworks. We do, however take advantage of the LESS syntax for CSS, which allows us to write CSS in a much more efficiant matter.
LESS is really just regular CSS, but with the ability to assign variables, use a few simple functions like "lighten" or "darken" to lighten or darken color hex values, and also adds the ability to separate your style sheets into seperate files.
LESS also supports nesting of statements, which means you can create style hierarchies without having to repeat yourself that much.

### XML

We decided to provide a API interface for users who would like to use our data on their own pages or apps. The data is available as XML and can be found at the /car/xml/ url.
This API provides details of all cars available in our database, as well as all the connected ratings to each individual car, provided by the customers.

### Javascript

In our project, we have used the jQuery 2.1.1 library. This allows us to abstract away differences in how individual browsers interperet the JavaScript, allowing for easy cross browser and version compatibility. Also, jQuery provides a vast array of helper methods that allows us to perform the tasks required, while having to write less code. This follows jQuery's slogan: "Write less, do more.".

Our JavaScript also follows the Module Pattern approach, instead of prototyping, as this allows us to mimic the class based object oriented style of languages like Java, with private and public methods and variables, resulting in clean modules with a tight scope.

We have used JavaScript in the following locations of our application:

- Contact Form: Input validation
- Rent Now Form (Car details pages): Input validation
- Rate Car Form (Car details pages): Asynchronous form posting and dynamic DOM updates on POST success.

### Backend (Flask)

We chose to use Python3 as a server side programming solution to ease the creation of the different pages through a template engine.

Here we choose to use Flask as our minimal framwork and Jinja2 as our template engine. Flask is a microframework for python that includes the minimal needed features for creating a dynamic website. This features includes templating and a basic routing scheme for URLs.

Jinja2 allows us to create a base html template which can be used on every page on our website. This drasticly decreases the repetetive tasks we would have done if we needed to create every page manually. Jinja2s template syntax is similar to many other template syntaxes like twig (php), nunjucks (node/javascript) and django (python).

For more information on Flask, visit ... http://flask.pocoo.org/

For more information on Jinja2, visit ... http://jinja.pocoo.org/docs/dev/
