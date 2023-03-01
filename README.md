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

#### Add PostgreSQL db

```bash
db.sqlite3
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
