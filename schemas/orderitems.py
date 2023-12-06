import uuid
from ninja import Schema

from schemas.clients import ClientRetrievalSchema
from schemas.products import ProductRetrivalSchema


class OrderitemRegisterSchema(Schema):
    quantity: int = None


class OrderitemRetrievalSchema(Schema):
    id: uuid.UUID = None
    quantity: int = None
    checked_out: bool = None
    client: ClientRetrievalSchema = None
    product: ProductRetrivalSchema = None
