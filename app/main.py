from fastapi import FastAPI
from app.api.routes import test

# app = FastAPI()
app = FastAPI(swagger_ui_parameters={"syntaxHighlight": {"theme": "obsidian"}})

@app.get("/")
async def root():
    return {"message": "Hello, Universe! from e-mahhir!"}

app.include_router(test.router)