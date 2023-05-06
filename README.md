# django-tutorial
Notes on Django taken from [Django Tutorial from Programming With Mosh](https://www.youtube.com/watch?v=rHux0gMZ3Eg). 

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
    By using a `.` at the end of the command will not create sub folder, but will help in creating the file structure for this project.
- Creating Playground folder. It has something to do with `Models`, `admin Page`, `request Handler`.
    ```
    > python manage.py startapp playground
    ```
    Here, `playground` is the name of the folder, you can use anything you like.
- Add `playground` in the list of INSTALLED_APPS in settings.json
- Run Server.
    ```
    > python manage.py runserver [PORT]
    ```
    Note that `PORT` is an optional parameter, and by default it's value is 8000.
- Installing django-debug-toolbar
    ```
    > pipenv install django-debug-toolbar
    ```
- Add `django-debug-toolbar` in the list of `INSTALLED_APPS` in `settings.py`
- Add MIDDLEWARE for `django-debug-toolbar` in `settings.py`
- Update main urls.py to include `debug_toolbar`
- Change values for `INTERNAL_IPS` in settings.py when not using local development. (Refer [Docs](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html))

## Database Design
![](/repo-resources/M0.png?raw=true "Relation between Product and Collection")

![](/repo-resources/M1.png?raw=true "Relation between Product, Cart and CartItem")
- In the above image, `CartItem` is a Association Class, between the many-to-many relation of `Product` and `Cart`. You can understand this better by consider `Cart` similar to something like wishlist in E-Commerce Website.

![](/repo-resources/M1(1).png?raw=true "To better understand the above image")

![](/repo-resources/M3.png?raw=true "Relation between Product, Customer, Order and OrderItem")

![](/repo-resources/M4.png?raw=true "Relation between Product and Tag")
For this project, both anonymous user and `Customer`(registered user) can create a `Cart` but only a `Customer` can Create an `Order`.

The above Mentioned Entity of Database will further be Distributed into different apps, where each app will do a specific task (to avoid [Monolith](https://en.wikipedia.org/wiki/Monolithic_application) and follow [unix philospohy](https://en.wikipedia.org/wiki/Unix_philosophy)).

### Apps for Database 
- Since everything in `Django` is basically an `app`, we will be referring our database models/schemas as Database apps.
- Apps can also be migrated.
- To make sure, that other apps do not break when we update some other apps, we will not be following the structure shown below.
![](/repo-resources/D1.png?raw=true "Poor way of breaking down a project")
- As you can see there are many `dependency` between `apps` such as: 
    - `Orders` -> `Carts`
    - `Carts` -> `Products`
    - `Orders` -> `Customers`
Meaning if a change is made in `Products` app, there is a chance that it might create an issue in `Carts` leading to an issue in `Orders`.
- To avoid the above problem, **we should design apps such that they are self-contained.** Meaning, a change in one `dependency` should not be an issue for other `apps`, and it also became easier to use these `apps` in other projects.
- The `app` design shown below, can be one out of the many possible ways to design, while also avoiding the above stated issues.
![](/repo-resources/D2.png)

#### Creating apps for database
- Store App
 ```
 python manage.py startapp store
 ```
 - Tags app
 ```
 python manage.py startapp tags 
 ```
 - Add the created apps in the list of `INSTALLED_APPS` in ![settings.py](/storefront/settings.py)
