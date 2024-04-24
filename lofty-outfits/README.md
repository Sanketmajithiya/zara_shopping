# lofty-outfits
lofty-outfits

# clone your repo in local
>>> git clone https://github.com/brijeshpytops/lofty-outfits.git
>>> cd lofty-outfits

# create vertiual env for 'lofty-outfits' project
>>> python -m venv <your-env-name>

# activate your vertiual env
>>> <your-env-name>\Scripts\activate

# deactivate your vertiual env
>>> <your-env-name>\Scripts\deactivate

# create requirements.txt file
(<your-env-name>) ...\lofty-outfits> type nul > requirements.txt

# check Python 3.x.y version require for django==5.0.0
(<your-env-name>) ...\lofty-outfits> python --version

# (<your-env-name>) ...\lofty-outfits> python
Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import django
>>> django.get_version()
'5.0.3'

# Installing an official release with pip
(<your-env-name>) ...\lofty-outfits> python -m pip install Django

# check installed packge in <your-env-name>
(<your-env-name>) ...\lofty-outfits> pip list/pip freeze
Package  Version
-------- -------
asgiref  3.7.2
Django   5.0.3
pip      24.0
sqlparse 0.4.4
tzdata   2024.1

# add all installed packge in requirements.txt
(<your-env-name>) ...\lofty-outfits> pip freeze > requirements.txt

# insall package from requirements.txt
(<your-env-name>) ...\lofty-outfits> pip install -r requirements.txt

# create django project
(<your-env-name>) ...\lofty-outfits> django-admin startproject <your-project-name> .

# create django application
(<your-env-name>) ...\lofty-outfits> python manage.py startapp <you-app-name>

# makemigrations
(<your-env-name>) ...\lofty-outfits> python manage.py makemigrations

# migrate table 
(<your-env-name>) ...\lofty-outfits> python manage.py migrate

# run local server
(<your-env-name>) ...\lofty-outfits> python manage.py runserver <yout-port-number>

# craete super user
(<your-env-name>) ...\lofty-outfits> python manage.py createsuperuser
Username (leave blank to use 'admin'): admin
Email address: admin
Error: Enter a valid email address.
Email address: admin@gmail.com
Password:
Password (again):
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.




# razor pay steps
This is the main step of the process. First, we need to understand how payment works in Razorpay.

Create a Razor Order from our Django Server.

Pass Order Id and Other Options to the Frontend.

The user clicks the payment button and pays with one of the payment methods.

Razorpay handles Payment Success and Failure.

On Failure, Razorpay facilitates retry of the payments.

On Success, Razorpay makes a post request to a callback URL on our server.

Verify the payment signature, to confirm that payment is authentic and isn’t tampered with.

Once verified, capture the payment and render the success page.


