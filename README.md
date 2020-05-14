## Django-Blog
Django blog is a beginner friendly blog application. This project illustrate Django Class Based views, How to use django models with custom
model manager, how to use custom template tags, django Forms and model form, how to send mail with django, how to add rss syndication,
and generate sitemap and unit test for model, view, form and template tags and also how to seed database with Factory Boy, Faker and management commands.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Installing
```
open terminal and type
git clone https://github.com/devmahmud/DjangoBlog.git
```

#### or simply download using the url below
```
https://github.com/devmahmud/DjangoBlog.git
```

## Requirements
```
Create a virtual environment and active it
and install requirements type:

pip install -r requirements.txt
```

### In this project i have used postgres as a database, change db information in settings with your database information
## To migrate the database open terminal in project directory and type
```
python manage.py makemigrations
python manage.py migrate
```

## Static files collection
```
python manage.py collectstatic
```

## Creating Superuser
```
python manage.py createsuperuser
```

## Creating Dummy data using faker
```
python manage.py seed --posts number_of_post
example: python manage.py seed --posts 50
```

## For sharing post with email change the email configuration
```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your email'
EMAIL_HOST_PASSWORD = 'your email password'
```

## To run the program in local server use the following command
```
python manage.py runserver
Then go to http://127.0.0.1:8000 in your browser
```

## To test the project
```
python manage.py test
```

## To test the project and pep8 style guide
```
python manage.py test && flake8
```
or you can simple run `flake8`


## Project snapshot

### Home Page
![image](https://user-images.githubusercontent.com/19981097/81924503-08809680-9601-11ea-9df2-2096f265b0e1.png)

### Detail Page
![image](https://user-images.githubusercontent.com/19981097/81924659-37970800-9601-11ea-8433-8b21e75594b1.png)

### Comment Page
![image](https://user-images.githubusercontent.com/19981097/81924734-51d0e600-9601-11ea-9df9-14b9c47c11ac.png)

### Post share page
![image](https://user-images.githubusercontent.com/19981097/81926022-2a7b1880-9603-11ea-9cd6-3f465389f250.png)

## Author
```
  Mahmudul alam
  Email: expelmahmud@gmail.com
```

<div align="center">
    <h3>========Thank You !!!=========</h3>
</div>

