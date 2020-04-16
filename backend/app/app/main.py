from fastapi import FastAPI

from app.core import config

app = FastAPI(title=config.API_V1_STR, openapi_url="/api/v1/openapi.json")
