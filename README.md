## Initialization

#### Create a virtual environment

```python
python3 -m venv venv-api
source venv-api/bin/activate
```

#### Install requirements.txt

```python
pip install -r requirements.txt
```

#### Add sqlite db

```bash
db.sqlite3
```

#### Add PostgreSQL db (discomment the code in settings.py)

```bash
LOCAL_DB_NAME=db-name
LOCAL_DB_USER=
LOCAL_DB_PASSWORD=
LOCAL_DB_HOST=127.0.0.1
LOCAL_DB_PORT=5432
```

#### Migrate models

```python
python manage.py makemigrations
python manage.py migrate
```

#### Run

```python
python manage.py runserver
```
