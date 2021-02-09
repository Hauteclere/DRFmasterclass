# First, some theory...
In class, I'll be talking through the following points to help students frame their understanding of what Django/DRF are and how they can be used.

- MVC vs MVT architecture
- What Django does for us
- What DRF does for us
- Data flow in a DRF API 

---

# Step 0:
# Flaps... check! Props... Check! Fuel... Check!
Before we take off with the practical component of the lesson, let's do some initial checks.  First, navigate to the repo you have (hopefully) already set up with a coding environment in it, activate your env, and check that you have both Django and DRF installed:

`cd DRFmasterclass`

`source venv/bin/activate`

`pip list`

Among the packages installed you should see:

>   ...  
   Django              3.0.8  
   djangorestframework 3.11.0  
   ...    

If you aren't able to get this result, head back to the README.md and see if there's a step you missed, or an error you made.  You'll need Django and DRF to proceed.

# Step 1:
# Creating a Django project
One of the great features of Django is that despite being a very complex and powerful tool, it is extremely quick and easy to get started with.  Let's instantiate a Django project now.  We will be creating an API to serve a fantasy-football style website, only instead of football teams, our league will be filled with professional rock climbers.  This task has been selected because rock climbers are *xxXX.eXtReMe.XXxx* and therefore cool and/or fun. Also, rock climbing events require fewer athletes than football teams, which will make our data entry and testing processes less tedious. 

With your venv running in the DRFmasterclass repo, enter the following commands:

`mkdir ProjectDirectory`

`django-admin startproject ClimbingLeague ProjectDirectory`

Now check out the contents of the ProjectDirectory we just created:

`cd ProjectDirectory`

`ls`

Inside the ProjectDirectory we have created a new directory, called ClimbingLeague, and also a new file named manage.py.  This is the beginnings of our Django/DRF project.  In fact, what we have here is already a working Django project, but it doesn't do anything except turn on and exist.  If it were a number, our current project would be the number zero.  If it were a culinary experience, it would be a glass of water.  Let's see what that looks like by running the project server on localhost and visiting it:

`python3 manage.py runserver`

The program will output some alerts into the terminal to let us know it is running.  One of these alerts warns us that we have unapplied migrations!  We can ignore that for now, we will circle back to it shortly.

Open your web browser and type `http://127.0.0.1:8000` into the address bar, then hit enter.  

If you see a rocket, it worked!  We are on our way!

---

### Exploring the project 
Let's take a look at a few of the elements that make up the beginning foundation of our project:

- manage.py
: This is the command line utility hooked up to our project. This is a tool that allows us to start the server, interact with our Django project directly through the python interpreter, interact directly with our database, etc... For some useful commands to use with this tool, take a look [here](https://docs.djangoproject.com/en/3.1/ref/django-admin/).

- ClimbingLeague/urls.py
: This is the global list of urls that our project serves. At the moment it only serves the `admin/` url, which gives superusers useful data entry/output functionality. For more information on the Django admin, take a look [here](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/).  We won't be using it for this class, but it's handy to know about.

- ClimbingLeague/settings.py
: The motherlode!  This file is arguably the most important file in any Django project.  It specifies the parameters under which our project operates.  We'll talk through these in class, but if you're reading back through this info later, you can take a look [here](https://docs.djangoproject.com/en/3.1/ref/settings/) for (a lot!) more info.

# Step 2:
# Creating a custom user model
Django ships with some builtin classes for handling users.  By default, it will use the [User](https://docs.djangoproject.com/en/3.1/ref/contrib/auth/#django.contrib.auth.models.User) model, but any serious project should plan to swap in a custom model as the first major step of development.  

This is because:
- The default User model resides in the django.contrib.auth module, which ships with Django, and therefore shouldn't be modified. Correct usage to create your own subclass of this (or another) model, and modify that. 
- When the project database is instantiated, the project's user model is hooked into the Django ORM on a fundamental level.  The User model is unique in this way, and this makes changing to a different user model midway through the project's life much more difficult. (Modifying an existing custom user model is fine.)  It's better to install a custom model from the start, before things get complicated.

We will store our CustomUser model inside a modular app within our project. A Django project usually consists of a number of discrete apps which communicate with one another to get the job done.  This division of labour makes it easier to modify a project and keep track of how it works.  

Make sure you are inside the ProjectDirectory, and then run the following command:

`python3 manage.py startapp users`