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

The `pinax-project-socialauth` documentation is currently under construction. If you would like to help us write documentation, please join our Pinax Project Slack team and let us know! The Pinax documentation is available at http://pinaxproject.com/pinax/.


Contribute
----------------

See [this blog post](http://blog.pinaxproject.com/2016/02/26/recap-february-pinax-hangout/) including a video, or our [How to Contribute](http://pinaxproject.com/pinax/how_to_contribute/) section for an overview on how contributing to Pinax works. For concrete contribution ideas, please see our [Ways to Contribute/What We Need Help With](http://pinaxproject.com/pinax/ways_to_contribute/) section.

In case of any questions we recommend you [join our Pinax Slack team](http://slack.pinaxproject.com) and ping us there instead of creating an issue on GitHub. Creating issues on GitHub is of course also valid but we are usually able to help you faster if you ping us in Slack.

We also highly recommend reading our [Open Source and Self-Care blog post](http://blog.pinaxproject.com/2016/01/19/open-source-and-self-care/).  


Code of Conduct
----------------

In order to foster a kind, inclusive, and harassment-free community, the Pinax Project has a code of conduct, which can be found here  http://pinaxproject.com/pinax/code_of_conduct/. We ask you to treat everyone as a smart human programmer that shares an interest in Python, Django, and Pinax with you.


Pinax Project Blog and Twitter
-------------------------------

For updates and news regarding the Pinax Project, please follow us on Twitter at [@pinaxproject](https://twitter.com/pinaxproject) and check out our blog http://blog.pinaxproject.com.




