# django-tutorial
Following Django Tutorial from Programming With Mosh. 

## Setup
- Install a Django in virtual environment.
    ```
     > pip install pipenv.
     > pipenv install django.
     ```
- Run shell for your created virtual environment.
    ```
    > pipenv shell
    ```
- Create Django Template.
    ```
    > django-admin startproject storefront .
    ```
    By using a ```.``` at the end of the command will not create sub folder, but will help in creating the file structure for this project.
- Creating Playground folder. It has something to do with database Models, admin Page, request Handler.
    ```
    > python manage.py startapp playground
    ```
    Here, playground is the name of the folder, you can use anything you like.

- Run Server.
    ```
    > python manage.py runserver [PORT]
    ```
    Note that PORT is an optional parameter, and by default it's value is 8000.
