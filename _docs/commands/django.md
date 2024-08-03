# Django Commands

This guide outlines various commands to run tests using Django.

- **Start the development server**
    ```
    python manage.py runserver
    ```

- **Make migrations (assuming you have models.py with model definitions)**
    ```
    python manage.py makemigrations
    ```

- **Apply migrations to the database**
    ```
    python manage.py migrate
    ```

- **Collect static files (assuming you have static files in your project)**
    ```
    python manage.py collectstatic
    ```

- **Create a superuser account (replace 'username' and 'password' with your desired credentials)**
    ```
    python manage.py createsuperuser username password
    ```

- **Start a Python shell with the Django environment loaded**
    ```
    python manage.py shell
    ```

- **Run tests (assuming you have tests written using a framework like pytest)**
    ```
    pytest
    ```

- **Check for project issues (replace '--all' with specific checks if desired)**
    ```
    python manage.py check
    ```

- **Load fixture data into the database (assuming you have a fixture file named 'mydata.json')**
    ```
    python manage.py loaddata mydata.json
    ```

- **Dump the database contents to a fixture file (replace 'mydata.json' with your desired filename)**
    ```
    python manage.py dumpdata > mydata.json
    ```