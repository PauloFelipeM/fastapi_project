from fastapi import APIRouter, Response, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from ..services import fruit_service
from ..entities.Fruit import Fruit


class Item(BaseModel):
    name: str


router = APIRouter()


@router.get("/fruits")
def index(request: Request):
    return fruit_service.get_all(request)


@router.get("/fruits/{id}")
def show(id: str):
    return fruit_service.get_by_id(id)


@router.post("/fruits")
def create(item: Item):
    new_fruit = Fruit(name=item.name)
    fruit_service.create(new_fruit)

    return Response(status_code=201)


@router.put("/fruits/{id}")
def update(id: str, item: Item):
    fruit = fruit_service.get_by_id(id)

    if fruit is None:
        return JSONResponse(status_code=404, content={"message": "Fruit not found"})

    updated_fruit = Fruit(name=item.name)

    fruit_service.update(fruit, updated_fruit)
    return Response(status_code=200)

@router.delete("/fruits/{id}")
def delete(id: str):
    fruit = fruit_service.get_by_id(id)

    if fruit is None:
        return JSONResponse(status_code=404, content={"message": "Fruit not found"})

    fruit_service.remove(fruit)
    return Response(status_code=200)
