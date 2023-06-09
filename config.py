import os
from dotenv import load_dotenv


load_dotenv()

DB_HOST = os.environ.get("POSTGRES_HOST")
DB_NAME = os.environ.get("POSTGRES_DB")
DB_PORT = os.environ.get("POSTGRES_PORT")
DB_USER = os.environ.get("POSTGRES_USER")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")

# jwt
SECRET = os.environ.get("SECRET")
