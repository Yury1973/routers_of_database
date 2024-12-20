from fastapi import FastAPI
from app.routers import category, products
from app.backend.db import engine, Base


app = FastAPI()


@app.get("/")
def root():
    """Главная страница"""
    return {"message": "Welcome to the Shop API"}


# Подключаем маршруты
app.include_router(category.router)
app.include_router(products.router)

# Создаём таблицы в базе данных
Base.metadata.create_all(bind=engine)
