from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


def make_sqlalchemy_database_uri() -> str:
    sqlalchemy_database_uri = (
        f"{settings.DATABASE_SCHEME}://{settings.DATABASE_USER}:{settings.DATABASE_PASS}@{settings.DATABASE_HOST}"
    )
    sqlalchemy_database_uri += f":{settings.DATABASE_PORT}" if settings.DATABASE_PORT else ""
    sqlalchemy_database_uri += f"/{settings.DATABASE_NAME}"
    sqlalchemy_database_uri += f"?{settings.DATABASE_ARGS}" if settings.DATABASE_ARGS else ""

    return sqlalchemy_database_uri


engine = create_engine(
    make_sqlalchemy_database_uri(),
    pool_size=settings.SQLALCHEMY_POOL_SIZE
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
