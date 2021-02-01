# Hi! 

This is the starter repo for my upcoming masterclass on building an API in Django Rest Framework. 
As you can see, it's pretty sparse at the moment - that's because we will be building a small API from the ground up!  
Django and DRF are designed for rapid development of complex systems, so they're the perfect tool for creating a project from scratch in a short period of time.

To follow along you'll need: Python, Pip, and git. We will be querying our API to test it during development, so it's best if you have an API testing tool like Insomnia installed. Finally, you'll also need to have a virtual environment tool: I'll be using virtualenv during the lesson. 

To get ready for the class, clone this repo with the terminal command 

`git clone https://github.com/Hauteclere/DRFmasterclass.git`

If you'd like to push your work to your own github, you'll need to make a new blank repo on github.com and change the origin of your cloned repo to that address, using

`git remote set-url origin <ADDRESS_OF_YOUR_REPO>`

Next, navigate to your newly cloned repo, and set up an environment to make installations in.  Since I'm using virtualenv, the command is 

`virtualenv venv`

(Where venv is the name I've chosen for my new environment.) 

Activate your environment:

`source venv/bin/activate`

And use pip to install the packages listed in requirements.txt. (For this class it's just Django and Django Rest Framework:

`pip install -r requirements.txt`

## OK! That's the prep done.  You're ready to join the masterclass and see what DRF has to offer! 

## Happy coding
##	- Oliver
