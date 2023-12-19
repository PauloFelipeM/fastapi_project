from fastapi import FastAPI

from .endpoints import fruit_endpoint

def create_app():
    app = FastAPI()
    app.include_router(fruit_endpoint.router)
    return app

app = create_app()