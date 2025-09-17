from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine
from core.configs import settings

engine: AsyncEngine = create_async_engine(settings.DB_URL)

Session : AsyncSession =  sessionmaker(autoflush=False,
                            autocommit=False,
                            bind=engine, class_=AsyncSession, expire_on_commit=False)