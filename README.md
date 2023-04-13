# Setup

Clone repo
```
git clone https://github.com/graham-walker/personal-website-django.git

cd ./personal-website-django
```
Create virtual environment
```
python -m venv env

# Windows
.\env\Scripts\activate.bat

# Linux
source ./env/bin/activate
```

Install requirements
```
pip install -r requirements.txt
```

Add secrets
```
# Windows
echo "" > ./mysite/secret.py

# Linux
touch ./mysite/secret.py
```
```python
# secret.py
SECRET_KEY = 'YOUR SECRET KEY'

ALLOWED_HOSTS = [
    'localhost',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'databasename',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

DEBUG = True
```
Make migrations
```
mkdir ./personal/migrations
python manage.py migrate
```


Start server
```
python manage.py runserver
```


## Sass
Install sass
```
npm install -g sass
# Or
choco install sass
```
Watch
```
cd ./personal-website-django

sass --watch .\personal\static\sass\main.scss:.\personal\static\css\custom.min.css --style compressed --no-source-map
```