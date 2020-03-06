# DjangoCMS Dashboard

_This is a modified version of [3mwteam's djangocms-dashboard](https://github.com/3mwteam/djangocms-dashboard) plugin. It has been edited to suit Python 3.8 and Django CMS 3.7._

A simple dashboard to manage DjangoCMS's plugins, apphooks, etc., all on the same place.
Detailed documentation is in the "docs" directory.

## Quick start

1. Install the package with:

On Windows:
```
pip install https://github.com/Grimm-Child/djangocms-dashboard/archive/0.1.5.zip
```

On OS:
```sh
$ pip install https://github.com/Grimm-Child/djangocms-dashboard/archive/0.1.5.tar.gz
```

2. Add `'djangocms_dashboard'` to your INSTALLED_APPS setting like this:
```
    INSTALLED_APPS = [
        ...
        'djangocms_dashboard',
    ]
```
3. Include the URLconf in your project urls.py like this:
```
url(r'^djangocms_dashboard/', include('djangocms_dashboard.urls')),`
```
4. Start the development server and visit http://127.0.0.1:8000/dashboard/
```sh
$ python manage.py runserver
```


## Using the _sample_ app as a starting project base:

1. Create a virtual environment in the project directory, optionally providing a specific Python version; in this case it is 3.8:
_djangocms-dashboard/_
```
$ virtualenv .env --python=python3.8
```

2. Activate the virtual environment. Navigate into the _sample_ project directory:
```
    source .env/bin/activate
    cd djangocms-dashboard/sample
```
3. Update the packages installed in the project, create the database and the local user by running the commands below:
```
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py createsuperuser
```
4. Access the project by starting the server:
```sh
$ python manage.py runserver
```
    
and visit 127.0.0.1:8000/dashboard/ in your browser.
