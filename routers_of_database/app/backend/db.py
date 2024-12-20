from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "sqlite:///shop.db"  # Путь к базе данных SQLite

# Создаём движок для подключения к базе данных
engine = create_engine(DATABASE_URL)

# Создаём фабрику сессий для работы с базой данных
SessionLocal = sessionmaker(bind=engine)


# Базовый класс для всех моделей SQLAlchemy
class Base(DeclarativeBase):
    pass
