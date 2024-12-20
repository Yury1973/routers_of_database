from sqlalchemy import Column, Integer, String
from app.backend.db import Base
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__ = "categories"  # Имя таблицы в базе данных

    id = Column(Integer, primary_key=True, index=True)  # Уникальный идентификатор
    name = Column(String, unique=True, index=True)  # Название категории
    slug = Column(String, unique=True, index=True)  # Человекочитаемый URL

    # Определяем отношение "один ко многим"
    products = relationship("Product", back_populates="category")
