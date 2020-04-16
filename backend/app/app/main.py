from fastapi import FastAPI

from app.core import config

app = FastAPI(title=config.PROJECT_NAME, openapi_url="/api/v1/openapi.json")
