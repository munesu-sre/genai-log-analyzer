from database import engine, Base
import models  # Import your models so SQLAlchemy knows they exist

def init_db():
    print("Creating database tables...")
    # This command reads all classes that inherit from 'Base' and creates them in PostgreSQL
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")

if __name__ == "__main__":
    init_db()