Echildcare
==========

.. image:: http://i.imgur.com/M7EqAE5.png

The health sector in India is broken. A number of children die every year because their parents do not know general things or various government vaccination/medicines schemes in their area. With **echildcare** - SMS application, parents can register with a simple SMS and now they will receive general advice for child care, various medicines/vaccination to be given to their child on exact dates.

Features
--------

- Users can register with the service with simple SMS.
- Now they will receive notifications about medicines, vaccination centres in their area. Also other government schemes.
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


You should now be able to run the development server::

    python manage.py runserver
