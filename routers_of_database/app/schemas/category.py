from pydantic import BaseModel


# class Category(BaseModel):
#     id: int  # Поле для уникального идентификатора
#     name: str  # Поле для названия категории
#
#
# class Config:
#     orm_mode = True  # Указывает, что объект может быть преобразован из ORM (например, SQLAlchemy)
#
#
# class CategoryCreate(BaseModel):
#     name: str  # Поле для ввода названия категории при создании


class CategoryBase(BaseModel):
    name: str
    slug: str


class CategoryCreate(CategoryBase):
    pass  # Для создания категории


class Category(CategoryBase):
    id: int

    class Config:
        from_attributes = True  # Позволяет работать с данными ORM
