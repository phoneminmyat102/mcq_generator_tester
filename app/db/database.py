from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

DATABASE_URL = "mysql+aiomysql://root:@localhost/mcq"

engine = create_async_engine(DATABASE_URL, echo=True)



async_session = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession 
)

Base: DeclarativeMeta = declarative_base()

async def get_db():
    async with async_session() as session:
        yield session

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)