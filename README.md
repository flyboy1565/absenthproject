README file for {{ project_name }}

Important: keep secrets out of github. Use environment variables.

###USAGE

clone this repo
create a python virtualenv 
```
python3 -v venv <folder>
```
then activate the virtualenv
```
pip install -r requirements.txt
```
once that is done make migrations and run the server
```
python manage.py migrate
python manage.py runserver 
```

### Then go to swagger
```
http://127.0.0.1:8000/swagger/
```