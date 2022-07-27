from pydantic import BaseModel


class BaseTodo(BaseModel):
    title: str
    description: str

    class Config:
        orm_mode = True

class BaseTodoList(BaseTodo):
    id: int

    class Config:
        orm_mode = True