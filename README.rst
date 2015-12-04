Echildcare
==========

.. image:: http://i.imgur.com/M7EqAE5.png

A number of children die every year because their parents do not know general things or various government vaccination/medicines schemes in their area. With **echildcare** - SMS application, parents can register with a simple SMS and now they will receive general advice for child care, various medicines/vaccination to be given to their child on exact dates.

Features
--------

- Users can register with the service with simple SMS.
- Now they will receive notifications about medicines, vaccination to be given to their child.
- The messages will be customized for users according to date of birth of child.
- The scheduling of messages will be done automatically. Manual action is not required.
- The admin will have access through web interface.
- Notifications will be sent on SMS.
- This can also act as Birth registration system.

Technologies used
-----------------

- Python/Django
- RapidSMS
- Celery for scheduling tasks
- Redis as message broker
- PostgreSQL database

Getting Started
---------------

To setup your local environment you should create a virtualenv and install the
necessary requirements::

    virtualenv echildcare-env

On Posix systems you can activate your environment like this::

    source echildcare-env/bin/activate

On Windows, you'd use::

    echildcare-env\Scripts\activate

Then::

    cd echildcare
    pip install -U -r requirements/base.txt

Create the database and run migrations. Remember this project requires PostgreSQL so you need to install it before you can continue::

    createdb echildcare
    
Here we have to create migrations because we are extending the contact model of RapidSMS::

    ./manage.py makemigrations
    ./manage.py migrate

The web interface require admin rights. To create superuser::

    ./manage.py createsuperuser 
    
You should now be able to run the development server::

    python manage.py runserver

The Web interface will be accessible at http://localhost:8000/ 

Instructions
------------

The echildcare SMS applications has two interfaces

- **SMS interface**
- **Web Interface**

When users are interacting with the application through SMS, they can start by sending only register. Then they will receive further instructions like::

    register
    Thanks for showing interest in echildcare.
    To register, send JOIN <DATE OF BIRTH OF CHILD
    like YYYY-MM-DD> <MOBILE NUMBER FOR RECEIVING INFORMATION>
    Example: JOIN 2015-04-24 9*********

    join 2014-04-24 9*********
    Thank you for registering your child with
    echildcare born on 2014-04-24. Now you will
    receive notifications on 9*********. You can
    also add more information if you like. Just send
    email, gender, language, name, pincode from your
    registered number. Example: name pappu

And if they send in wrong format, they will receive instructions to send correct data like::

    join 2014-24-04 9*********
    Please register in correct format. Example: JOIN 2015-04-24 9*********

If the user send the email in wrong format::

    email xyz
    Please enter E-mail in correct format.

If user try to add name from an unregistered number::

    name pappu
    You must JOIN or REGISTER yourself before you can set your child name

The registered users can also unsubscribe from the service::

    stop
    You have successfully unsubscribed from
    the echildcare service. To register again
    send REGISTER

The Web interface is for admin. The admin can edit, update or delete the user. The message log section shows all incoming and outgoing messages. Message tester can be used during development phase to test the responses. In events section, the admin can create two type of events.

- **General events**: General event covers things that a child have to undergo after a certain period of time. 
- **Scheduled events**: Events are scheduled on a date and children that are under the event criteria are called to the event.

Setup Celery for local development
----------------------------------

echildcare uses Celery to periodically send SMS notifications to Registered users.

If you have not installed Celery already, you can install it with::
    
    pip install celery==3.1.19
    
The echildcare project is already integrated with Celery. This project uses Redis as a Celery “Broker”.
First install Redis from the official download_ page. Then start redis server by::

    $ redis-server

.. _download: http://redis.io/download

Install Redis in your virtual environment with::

    $ pip install redis==2.10.5

Celery tasks are present at::
    
    events/tasks.py
    
Ready to run these tasks?

With echildcare project and Redis running, open two new terminal windows/tabs. In each new window, navigate to your project directory, activate your virtualenv, and then run the following commands (one in each window)::

    $ celery -A echildcare worker -l info
    $ celery -A echildcare beat -l info
