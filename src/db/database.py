from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

import config
from src.db.models import Base

DB_URL_PSYCOPG = f"postgresql+psycopg://{config.DB_USER}:{config.DB_PASS}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"
# DB_URL_ASYNCPG = f"postgresql+asyncpg://{config.DB_USER}:{config.DB_PASS}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"

sync_engine = create_engine(url=DB_URL_PSYCOPG, echo=True, pool_pre_ping=5, max_overflow=10)

session_maker = sessionmaker(sync_engine, expire_on_commit=False, autocommit=False)



def create_tables():
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)


create_tables()
