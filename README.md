
___
![Google Logo](https://static.djangoproject.com/img/logos/django-logo-negative.png)


___

# Django Project Template
<br>

___


### Installation
1. If required, remove the existing virtual environment, run the following command:
    ```bash
    rm -rf env
    ```

    ```bash
    sudo rm -rf env
    ```

2. Create a new virtual environment and activate it:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```            
   
4. if any package has been installed, refresh (update) the dependencies document:
    ```bash
    pip freeze > requirements.txt
    ```

### Running the Local Server
Start the development server:

 ```bash
 python manage.py runserver
 ```

   This will launch the Django local server panel at 
   
<http://127.0.0.1:8000>

   This will launch the Django admin panel at 
   
<http://127.0.0.1:8000/admin/>


### Creating Models
1. Models define the data structure for your application. 
2. Create your models in the `models.py` of each app.

3. Register your models in the admin panel by adding them to the `admin.py` file in the same directory. e.g.
    ```python
    from django.contrib import admin
    from .models import Model_01, Model_02, Model_03, Model_etc

    admin.site.register(Model_01)
    admin.site.register(Model_02)
    admin.site.register(Model_03)
    admin.site.register(Model_etc)
    ```

### Applying Database Changes
1. Create migrations:
    ```bash
    python manage.py makemigrations
    ```

2. Apply migrations:
    ```bash
    python manage.py migrate
    ```

### Show Migrations Status 
1. this command will show the migrations status:
    ```bash
    python manage.py showmigrations
    ```

### Rollback Migration 
1. this command will rollback the migrations:
    ```bash
    python manage.py migrate <app_name> <migration_name>
    ```      
   or to rollback all migrations:
    ```bash
    python manage.py migrate <app_name> zero
    ```

### Creating an Admin User
1. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

### Run Local Server 
1. Start the development server:
    ```bash
    python manage.py runserver
    ```

    ```
   

### Admin Panel
1. Access the admin panel at:

    <http://127.0.0.1:8000/admin/>
    ```