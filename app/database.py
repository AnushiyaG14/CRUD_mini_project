from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "mysql+mysqlconnector://root:Admin@localhost/students_db"

engine = create_engine(DATABASE_URL, echo=True)  # REMOVE connect_args
SessionLocal = sessionmaker(bind=engine, autoflush=False)
Base = declarative_base()
