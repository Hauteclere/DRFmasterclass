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
...

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

...
```

We just need to add our users app onto the end of this list, like so:

```python
...

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
]

... 
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

`>>> from users.models import CustomUser`

Models in Django all have an associated "manager", which hooks into the Django ORM and allows rows from the database to be retrieved as model instances. By default, the model manager occupies the .objects field of the model. Let's grab all the rows from the `users` table of our database, and see what we have:

`>>> userlist = CustomUser.objects.all()`

The `userlist` variable now contains the queryset of all user instances.  Querysets are a special Django type - they act like regular sets but with extra functionality. Let's see what's in this queryset:

`>>> userlist`

There's our superuser! The Django shell API is incredibly useful, and worth exploring.  The [official Django tutorial](https://docs.djangoproject.com/en/3.1/intro/tutorial02/#playing-with-the-api) is a great place to start learning more about it if you're curious.


# Step 3: Creating User Endpoints

Remember earlier on in the lesson when we talked about the flow of data through a DRF project?  Right now we have a database table and a model, but in order for our API to be useable, we need serializers, views, and URLs. We are moving past a pure Django project now - the next steps will be our first use of Django Rest Framework.

## Creating a user serializer:

Since we are about to start using DRF, let's first register it as an installed app in our `ClimbingLeague/settings.py` file:

```python
...

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

...
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
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
```

It doesn't look like much, but this is a fully functional serializer. DRF is doing some heavy lifting for us by inferring all sorts of things about our models, and Django is lending a helping hand by providing us with the create_user method.  Now let's hook this serializer up to an API endpoint.

## Creating an endpoint:

DRF gives us the tools to create RESTful API endpoints, in the form of specialised Django views. Using VSCode, write the following code in the `ProjectDirectory/users/views.py` file:

```python
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework import generics

class UserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
```

> Q: Is this seriously all of the code we need here?

> A: Yes! 

This endpoint accepts POST requests containing user data in JSON format, and uses them to create new user instances in the database.  It responds to GET requests by returning a list of all users in the database. This is an example of one of DRF's [Generic Views](https://www.django-rest-framework.org/api-guide/generic-views/#generic-views), and believe it or not, these aren't even the most powerful views that DRF offers. Let's hook it up to a URL so we can see it in action!

## Creating a URL:

We can use Django to associate our view with a URL, by adding it to the list of URLS in a `urls.py` file. We already have a global url list in the `/ClimbingLeague` directory, but since our project is going to grow to include more than one app, let's keep things organised by creating a `urls.py` file to store all the urls associated with the `users` app. 

Use VSCode to create a new file called `urls.py` in the `/ProjectDirectory/users` directory, and populate it with the following code:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
]
```

Finally, we need to feed the URLs from our users app through to the global URL list, so that Django can serve them. Inspect the `ClimbingLeague/urls.py` file in VSCode.  At the moment it should look like this:

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

```

We need to make two modifications:
-  we need to import the function `include()` from `django.urls`
-  we need to add an extra urlpattern to the list

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
]

```

Don't forget that import!

We're really getting places now. If everything has gone to plan, we should be able to run our server and use an API testing interface like Insomnia to check our project is working.

Head to the command line, make sure you're in the `/ProjectDirectory`, and enter the following command:

```
python3 manage.py runserver
```

It's traditional at this stage to encounter some errors. If you do, take a look at the errortext that Django spits out and see if you can identify what went wrong. (You may have to read down several lines until you encounter the erroneous bit of code!) Common errors are the usual suspects: misspellings of class names or methods, forgetting to import, forgetting to save your edited file in VSCode, etc... If you encounter an error, don't worry too much, because we're about to take a short break, so you'll have time to troubleshoot. If your server ran correctly, though, load up VSCode with me and let's take our API for a spin!  

Functions to test:
-  make a GET request to 127.0.0.1:8000/users/ and see if your superuser is listed there
-  make a POST request to 127.0.0.1:8000/users/ with no data
   -  what was the response?
   -  try adding the required fields, and see if you can create a new user!
   -  make another GET request to check your new user has been added to the list


---
## Intermission
---

# Step 4: Setting up Token Authentication

In order for our users to perform actions on our website, we want to be able to authenticate them. Since we've decoupled the frontend from the backend, tokens are a great way of avoiding some otherwise-painful elements of the authentication process.

Since we're making another modification to how our app works, we'll once again have to tweak the `settings.py`. This time, we're adding another DRF app to our installed apps list, and also creating a new entry for our DRF settings:

```python
...

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'rest_framework',
    'rest_framework.authtoken',
    
    'users',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication'
    ]
}

AUTH_USER_MODEL = 'users.CustomUser'

...
```

This change involves adding a new table to the database to handle users' tokens. Luckily, the `rest_framework.authtoken` app that we just registered includes the migrations that we need ready-made, so we just need to apply them. Head over to the command line, make sure you're in the project directory with your env running, and run the following command:

`python3 manage.py migrate`

We also need an endpoint for getting a user's token, but luckily DRF also has one of these ready to go for us; we just have to register it to our global URLs. Inspect the `ClimbingLeague/urls.py` file with VSCode.  We need to:
-  add a new import for the view, and
-  add a path to the list of urlpatterns

Here's what that looks like:
```python
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('get-token/', obtain_auth_token)
]
```

In Insomnia, create a new POST request to the url `127.0.0.1:8000/get-token/`, with a JSON containing the username and password for an existing user. (Make sure your server is running first.) You should receive a token in return! Now we are cooking with gas.  

# Step 5: Creating Another Model

So far, we've been generating code that is pretty much standard boilerplate for any new project. Let's create something specific to our use-case: a `Climber` model. Since climbers aren't the same as users, we'll keep the code to handle them in a new app.

`python3 manage.py startapp climbers`

Since we added a new app to our project, we need to register it in the `settings.py`:

```python
...

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'rest_framework',
    'rest_framework.authtoken',
    
    'users',
    'climbers',
]

...
```

Now let's create the model. In VSCode, add the following code to the newly created `ProjectDirectory/climbers/models.py` file:

```python
from django.db import models

class Climber(models.model):
    
    name=models.CharField(max_length=100)

    class Specialties(models.TextChoices):
        SPEED = 'S', 'Speed'
        LEAD = 'L', 'Lead'
        BOULDER = 'B', 'Boulder'

    specialty = models.CharField(
        max_length=1,
        choices=Specialties.choices,
    )

```