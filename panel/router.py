from typing import Annotated
from fastapi import APIRouter, Depends

from repository import TaskRepository
from shemas import STask, STaskAdd

router = APIRouter(prefix="/tasks",tags=["Таски"])

@router.post("")
async def add_tasks(task:Annotated[STaskAdd,Depends()]):
    task_id = await TaskRepository.add(task)
    return {"id":task_id}

@router.get("")
async def get_all() -> list[STask]:
    tasks = await TaskRepository.get_all()
    return tasks