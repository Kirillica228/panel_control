from contextlib import asynccontextmanager
from fastapi import FastAPI

from database import create_tables, delete_tables
from shemas import STaskAdd

from router import router as task_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    await delete_tables()
    print("очистка")
    await create_tables()
    print("создание")
    yield
    print("Выключение")


app = FastAPI(lifespan=lifespan)
app.include_router(task_router)
