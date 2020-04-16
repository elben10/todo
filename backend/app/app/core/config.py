import os

API_V1_STR = "/api/v1"

POSTGRES_USER = os.environ["POSTGRES_USER"]
POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]
POSTGRES_SERVER = os.environ["POSTGRES_SERVER"]
POSTGRES_DB = os.environ["POSTGRES_DB"]

SQLALCHEMY_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"