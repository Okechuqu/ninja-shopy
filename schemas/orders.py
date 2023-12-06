from typing import List
import uuid
from ninja import Schema
from schemas.addresses import AddressRetrievalSchema

from schemas.clients import ClientRetrievalSchema
from schemas.orderitems import OrderitemRetrievalSchema


class OrderRegisterSchema(Schema):
    orderitem_ids: List[str]


class OrderRetrievalSchema(Schema):
    id: uuid.UUID = None
    status: str = None
    code: str = None
    client: ClientRetrievalSchema = None
    orderitems: List[OrderitemRetrievalSchema] = None
    shipping_address: AddressRetrievalSchema = None
