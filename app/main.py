from fastapi import FastAPI
from app.api.v1.routes import health

from loguru import logger

# app = FastAPI()
app = FastAPI(swagger_ui_parameters={"syntaxHighlight": {"theme": "obsidian"}})

logger.add("stdout", format="{time} {level} {message}", level="INFO")


@app.get("/")
async def root():
    logger.info("Root endpoint called!")
    return {"message": "Hello, Universe! new from e-mahhir!"}

app.include_router(health.router)