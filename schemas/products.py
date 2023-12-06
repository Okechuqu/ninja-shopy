from typing import List
import uuid
from ninja import Schema

from schemas.category import CategoryRetrievalSchema
from schemas.vendor import VendorRetrievalSchema


class ProductRegisterSchema(Schema):
    name: str = None
    description: str = None
    price: int = None
    stock_quantity: int = None


class ProductRetrivalSchema(Schema):
    id: uuid.UUID
    name: str = None
    description: str = None
    price: int = None
    # image:str=None
    stock_quantity: int = None
    vendor: VendorRetrievalSchema = None
    category: CategoryRetrievalSchema = None
