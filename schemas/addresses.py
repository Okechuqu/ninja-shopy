import uuid
from ninja import Schema
from pydantic import EmailStr


class AddressRegisterSchema(Schema):
    address: str = None
    


class AddressRetrievalSchema(Schema):
    id: uuid.UUID
    address: str = None
    is_current: bool =None