### Requeriments
- Python 3.x
- PostgreSQL database
- virtualenv

### Install requeriments
```pip install -r requirements.txt```

### Run migrations
- ```python migrate.py db init```
- ```python migrate.py db migrate```
- ```python migrate.py db upgrade```

### Run API
```python run.py```

### Start Containers
```docker-compose up```

### Run Commands Inside Container
```docker-compose exec container_name command```
