pinax-project-socialauth
========================

This project is similar to pinax-project-account in providing a foundation for
sites that have user accounts but it differs in supporting social
authentication rather than local password based authentication.


Usage:

    django-admin.py startproject --template=https://github.com/pinax/pinax-project-socialauth/zipball/master <project_name>


Getting Started:

    pip install virtualenv
    virtualenv mysiteenv
    source mysiteenv/bin/activate
    pip install Django==1.6.5
    django-admin.py startproject --template=https://github.com/pinax/pinax-project-socialauth/zipball/master mysite
    cd mysite
    pip install -r requirements.txt
    python manage.py syncdb
    python manage.py runserver
