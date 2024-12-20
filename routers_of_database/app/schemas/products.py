from pydantic import BaseModel


# class Product(BaseModel):
#     id: int
#     name: str
#     category_id: int  # Поле для связи с категорией
#
#
# class Config:
#     orm_mode = True
#
#
# class ProductCreate(BaseModel):
#     name: str
#     category_id: int


class ProductBase(BaseModel):
    name: str
    slug: str
    category_id: int


class ProductCreate(ProductBase):
    pass  # Для создания продукта


class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True  # Позволяет работать с данными ORM
