from sqlalchemy import select
from database import TaskOrm, async_session_maker
from shemas import STask, STaskAdd


class TaskRepository:
    @classmethod
    async def add(cls,data:STaskAdd) -> int:
        async with async_session_maker() as session:
            task_dict = data.model_dump()
            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id 
    @classmethod
    async def get_all(cls) -> list[STask]:
        async with async_session_maker() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_shemas = [STask.model_validate(task_model) for task_model in task_models]
            return task_shemas
    
    @classmethod
    async def get_one(cls):
        async with async_session_maker() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            return task_models