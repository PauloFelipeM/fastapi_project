from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .endpoints import fruit_endpoint

def create_app():
    app = FastAPI()
    app.include_router(fruit_endpoint.router, prefix='/api/v1')

    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app

app = create_app()