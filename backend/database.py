import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Pull the database URL from environment variables, or fallback to our PostgreSQL container settings
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:mysecretpassword@localhost:5432/loganalyzer")

# 1. Create the SQLAlchemy engine for PostgreSQL
engine = create_engine(DATABASE_URL)

# 2. Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3. Base class for our database models to inherit from
Base = declarative_base()

# 4. FastAPI dependency to provide a DB session per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()