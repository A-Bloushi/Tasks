from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

# 1) Database URL: tells SQLAlchemy which database and driver to use
DATABASE_URL = "sqlite+aiosqlite:///./tasks.db"

# 2) Create an asynchronous engine: this is the starting point for any SQLAlchemy application
engine = create_async_engine(DATABASE_URL, echo=True)

# 3) Create a session factory: this is used to create new sessions
AsyncSessionLocal = sessionmaker(
    bind=engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)

Base = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session