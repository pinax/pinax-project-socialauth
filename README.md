Pinax Project Socialauth
========================
[![Join us on Slack](http://slack.pinaxproject.com/badge.svg)](http://slack.pinaxproject.com/)


Pinax
-------

Pinax is an open-source platform built on the Django Web Framework. It is an ecosystem of reusable Django apps, themes, and starter project templates. 
This collection can be found at http://pinaxproject.com.


pinax-project-socialauth
-------------------------

`pinax-project-socialauth` is a starter project that supports social authentication.

This project is similar to pinax-project-account in providing a foundation for
sites that have user accounts but it differs in supporting social
authentication rather than local password based authentication.


Getting Started
-----------------

    pip install virtualenv
    virtualenv mysiteenv
    source mysiteenv/bin/activate
    pip install Django==1.6.5
    django-admin.py startproject --template=https://github.com/pinax/pinax-project-socialauth/zipball/master mysite
    cd mysite
    pip install -r requirements.txt
    python manage.py syncdb
    python manage.py runserver
    


Usage
------

    django-admin.py startproject --template=https://github.com/pinax/pinax-project-socialauth/zipball/master <project_name>


Documentation
--------------

The Pinax documentation is available at http://pinaxproject.com/pinax/.


Code of Conduct
----------------

In order to foster a kind, inclusive, and harassment-free community, the Pinax Project has a code of conduct, which can be found here  http://pinaxproject.com/pinax/code_of_conduct/.


Pinax Project Blog and Twitter
-------------------------------

For updates and news regarding the Pinax Project, please follow us on Twitter at [@pinaxproject](https://twitter.com/pinaxproject) and check out our blog http://blog.pinaxproject.com.




