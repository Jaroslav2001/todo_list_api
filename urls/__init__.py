from fastapi import APIRouter

from . import user
from . import todo_list

api = APIRouter(prefix='/api')

api.include_router(user.api)
api.include_router(todo_list.api)
