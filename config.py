import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}/{}'.format(
        os.environ.get('DB_USERNAME'),
        os.environ.get('DB_PASSWORD'),
        os.environ.get('DB_HOSTNAME'),
        os.environ.get('DB_NAME')
    )

# export DB_USERNAME=your_username
# export DB_PASSWORD=your_password
# export DB_HOSTNAME=your_hostname
# export DB_NAME=your_dbname