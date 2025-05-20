from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Verbindungszeichenfolge für SQLite (lokale Datei)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Engine verbindet sich mit der Datenbank
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal wird verwendet, um DB-Sessions zu erzeugen
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Basisklasse für alle ORM-Modelle
Base = declarative_base()
