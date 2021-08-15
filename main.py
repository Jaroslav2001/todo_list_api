from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from setting import setting
from urls import api


app = FastAPI(title='Todo List')

app.add_middleware(
    CORSMiddleware,
    **setting.CORS
)

app.include_router(api)
