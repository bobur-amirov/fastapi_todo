from typing import TYPE_CHECKING, List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from services import get_db, get_, create_, list_, update_, delete_
from schema import BaseTodo, BaseTodoList


app = FastAPI(title="Todo app")


@app.post('/create', response_model=BaseTodo)
async def create_todo(todoapp: BaseTodo, db: Session = Depends(get_db)):
    return await create_(todoapp=todoapp, db=db)


@app.get('/list', response_model=List[BaseTodoList])
async def list_todo(db: Session = Depends(get_db)):
    return await list_(db=db)


@app.get('/get/{todo_id}', response_model=BaseTodoList)
async def get_todo(todo_id: int, db: Session = Depends(get_db)):
    return await get_(todo_id=todo_id, db=db)


@app.put('/updte/{todo_id}', response_model=BaseTodo)
async def update_todo(todo_id: int, todoapp: BaseTodo, db: Session = Depends(get_db)):
    return await update_(todo_id=todo_id, db=db, todoapp=todoapp)


@app.delete('/delete/{todo_id}')
async def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    return await delete_(todo_id=todo_id, db=db)
