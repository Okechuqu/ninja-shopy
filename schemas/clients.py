from typing import List
from ninja import Schema
from pydantic import EmailStr

from schemas.addresses import AddressRetrievalSchema


class ClientRegisterSchema(Schema):
    email: EmailStr = None
    username: str = None
    first_name: str = None
    last_name: str = None
    phone: str = None


class ClientRetrievalSchema(Schema):
    id: int
    email: EmailStr = None
    username: str = None
    first_name: str = None
    last_name: str = None
    phone: str = None
    profile_image: str = None
    shipping_address: List[AddressRetrievalSchema] = None
