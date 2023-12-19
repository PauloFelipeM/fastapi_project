from fastapi import Request

from ..models.fruit_model import Fruit as FruitModel
from ..entities.Fruit import Fruit
from ..database import SessionLocal, db_session
from ..paginate import paginate


def create(fruit: Fruit):
    fruit_db = FruitModel(name=fruit.name)
    db_session.add(fruit_db)
    db_session.commit()

def update(prev_fruit: FruitModel, fruit: Fruit):
    prev_fruit.name = fruit.name
    db_session.commit()


def get_all(request: Request):
    return paginate(FruitModel, request)


def get_by_id(id: int):
    return FruitModel.query.filter_by(id=id).first()


def remove(fruit: FruitModel):
    db_session.delete(fruit)
    db_session.commit()
