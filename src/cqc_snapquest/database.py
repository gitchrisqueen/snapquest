from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Load MySQL connection URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+mysqlconnector://root:password@mysql_db/game_db")

# Create the database engine
engine = create_engine(DATABASE_URL)

# Create a session for handling database interactions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

