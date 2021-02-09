# First, some theory...
In class, I'll be talking through the following points to help students frame their understanding of what Django/DRF are and how they can be used.

- MVC vs MVT architecture
- What Django does for us
   -  Manages our database with models (and managers).
   -  Sends and retrieves data between the frontend and the database with views.
   -  Handles the presentation of data to the user with templates. **NB - only relevant for full-stack Django development**
- What DRF does for us
   -  Gives us powerful, readymade serializer classes
   -  Gives us *monstrously* powerful view classes for backend API construction
- Data flow in a DRF API 


# Step 0: Flaps... check! Props... Check! Fuel... Check!
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


# Step 1: Creating a Django project
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

## Exploring the project 
Open /ProjectDirectory/ in VSCode, and let's take a look at a few of the elements that make up the beginning foundation of our project:

- manage.py
: This is the command line utility hooked up to our project. This is a tool that allows us to start the server, interact with our Django project directly through the python interpreter, interact directly with our database, etc... For some useful commands to use with this tool, take a look [here](https://docs.djangoproject.com/en/3.1/ref/django-admin/).

- ClimbingLeague/urls.py
: This is the global list of urls that our project serves. At the moment it only serves the `admin/` url, which gives superusers useful data entry/output functionality. For more information on the Django admin, take a look [here](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/).  We won't be using it for this class, but it's handy to know about.

- ClimbingLeague/settings.py
: The motherlode!  This file is arguably the most important file in any Django project.  It specifies the parameters under which our project operates.  We'll talk through these in class, but if you're reading back through this info later, you can take a look [here](https://docs.djangoproject.com/en/3.1/ref/settings/) for (a lot!) more info.


# Step 2: Creating a Custom User Model

## Starting a 'users' app:
Django ships with some builtin classes for handling users.  By default, it will use the [User](https://docs.djangoproject.com/en/3.1/ref/contrib/auth/#django.contrib.auth.models.User) model, but any serious project should plan to swap in a custom model as the first major step of development.  

This is because:
- The default User model resides in the django.contrib.auth module, which ships with Django, and therefore shouldn't be modified. Correct usage to create your own subclass of this (or another) model, and modify that. 
- When the project database is instantiated, the project's user model is hooked into the Django ORM on a fundamental level.  The User model is unique in this way, and this makes creating a new user model midway through the project's life much more difficult. (Modifying an existing custom user model is fine.)  It's better to install a custom model from the start, before things get complicated.

We will store our CustomUser model inside a modular app within our project. A Django project usually consists of a number of discrete apps which communicate with one another to get the job done.  This division of labour makes it easier to modify a project and keep track of how it works.  

Make sure you are inside the ProjectDirectory, and then run the following command:

`python3 manage.py startapp users`

This command has created another subdirectory in our ProjectDirectory, called `/users/`.  Let's see what it contains:

- migrations/
: This subdirectory will contain the database migrations that the Django ORM generates based on our code. As we haven't generated any yet, it currently only has the python `__init__.py` module file. 

- models.py
: This file is where we will construct the models we use to structure/interact with our data.

- views.py
: This file is where we will construct our views.

---

## Updating our project settings:
We need to register our new app with Django so that the ORM hook into the models we are about to write.  In VS code, inspect the `ClimbingLeague/settings.py` file.  Starting on line 33 we have:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
] 
```

We just need to add our users app onto the end of this list, like so:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
] 
```

We also need to tell Django that one of the models we are about to create is going to be the model we want our project to use for user authorization.  On a new line after the list of installed apps (so around line 42), we can add:

```python
AUTH_USER_MODEL = 'users.CustomUser'
```

This overwrites the default settings of our project, so it knows to use our custom user model instead of the built-in one.  Now let's go write that model!

---

## Writing our model:

In VSCode, let's edit `/users/models.py`. The code we need to create looks like this:

```python
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	pass
	
	def __str__(self):
		return self.username
```

The resulting user model is identical to Django's default, but now that we've done the work of swapping it in to replace the default, we are free to modify it at our leisure.  We're on the way!

Let's go ahead and create a superuser account for ourselves now. In the console, make sure that you are in `/ProjectDirectory`, and run the following command:

`python3 manage.py createsuperuser`

You should be prompted to enter a username, an email address, and a password in turn. Make sure you pick a memorable password!

Finally, let's use the Django shell to interrogate our database, to check that we created a superuser successfully. Run the following command:

`python3 manage.py shell`

This will launch the Python interpreter in the console, with a direct line to our project.  Let's import our user model:

`from users.models import CustomUser`

Models in Django all have an associated "manager", which hooks into the Django ORM and allows rows from the database to be retrieved as model instances. By default, the model manager occupies the .objects field of the model. Let's grab all the rows from the `users` table of our database, and see what we have:

`userlist = CustomUser.objects.all()`

The `userlist` variable now contains the queryset of all user instances.  Querysets are a special Django type - they act like regular sets but with extra functionality. Let's see what's in this queryset:

`userlist`

There's our superuser! The Django shell API is incredibly useful, and worth exploring.  The [official Django tutorial](https://docs.djangoproject.com/en/3.1/intro/tutorial02/#playing-with-the-api) is a great place to start learning more about it if you're curious.


# Step 3: Creating User Endpoints

Remember earlier on in the lesson when we talked about the flow of data through a DRF project?  Right now we have a database table and a model, but in order for our API to be useable, we need serializers, views, and URLs. We are moving past a pure Django project now - the next steps will be our first use of Django Rest Framework.

## Creating a user serializer:

Since we are about to start using DRF, let's first register it as an installed app in our `ClimbingLeague/settings.py` file:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'rest_framework',
    
    'users',
]
```

Note that we've inserted some extra linebreaks here.  This is just cosmetic, but it's helpful for readability to separate out the native Django entries in this list, the third-part apps like Django Rest Framework, and the local apps that we write ourselves.

Next, we'll write our serializer.  Django apps aren't automatically created with a `serializers.py` file in them, so let's use visual studio to create one inside the `/users/` directory. 

Once we've created our file, let's add some serializer code:

```python
from .models import CustomUser
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only' = True}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
```