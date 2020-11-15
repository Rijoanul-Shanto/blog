# Django Example Blog

## Setup

- Clone the repository

```shell script
$ git clone https://github.com/Rijoanul-Shanto/blog
$ cd blog
```
- Create Virtual environment and Install dependencies
```shell script
$ virtualenv env
$ source ./env/bin/activate
$ pip install -r requirements.txt
```
- Make .env file to the root directory of the project including following variables without space between '=' sign.
```shell script
DEBUG=True-or-False
SECRET_KEY=your-project-secret-key
SQLITE_URL=sqlite:///your-sqlite-file
```

## Running

```shell script
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

Then visit `http://localhost:8000` to view the app.

## Deploy to Heroku
This application is currently available on Heroku.

visit: https://example-blog.herokuapp.com/

