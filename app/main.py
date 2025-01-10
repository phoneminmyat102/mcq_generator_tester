from fastapi import FastAPI
from db.database import Base, engine, create_db_and_tables
from models.user import User
from models.morning import Morning
from models.afternoon import Afternoon
from models.exam_history import ExamHistory
from routers import morning_router, user_router

app = FastAPI()
async def startup_tasks():
    await create_db_and_tables()


app.include_router(morning_router.router, prefix='/api/v1', tags=["Morning Questions"])
app.include_router(user_router.router, prefix='/api/v1', tags=["Users"])

@app.get('/')
def home():
    return {"hello":"world"}

if __name__ == "__main__":
    import asyncio
    import uvicorn
    
    asyncio.run(startup_tasks())
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

