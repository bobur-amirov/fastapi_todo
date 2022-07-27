from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session

from database import Base, engine, session_local
from models import TodoApp


def add_table():
    return Base.metadata.create_all(bind=engine)


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()


async def create_(todoapp: TodoApp, db: Session = Depends(get_db)) -> TodoApp:
    todoapp = TodoApp(**todoapp.dict())
    db.add(todoapp)
    db.commit()
    db.refresh(todoapp)
    return todoapp


async def list_(db: Session = Depends(get_db)) -> List[TodoApp]:
    todo = db.query(TodoApp).all()
    return todo


async def get_(todo_id: int, db: Session = Depends(get_db)) -> List[TodoApp]:
    todo = db.query(TodoApp).filter(TodoApp.id == todo_id).first()
    return todo


async def update_(todo_id: int, todoapp: TodoApp, db: Session = Depends(get_db)):
    todo = db.query(TodoApp).filter(TodoApp.id == todo_id).first()
    todo.title = todoapp.title
    todo.description = todoapp.description
    db.commit()
    db.refresh(todo)
    return todo


async def delete_(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(TodoApp).filter(TodoApp.id == todo_id).first()
    db.delete(todo)
    db.commit()
    return {'mess': f'{todo_id} todo delete'}
