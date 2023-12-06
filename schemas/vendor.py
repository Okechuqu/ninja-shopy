from ninja import Schema
from pydantic import EmailStr

from schemas.addresses import AddressRetrievalSchema
from schemas.category import CategoryRetrievalSchema


class VendorRegisterSchema(Schema):
    email: EmailStr = None
    username: str = None
    first_name: str = None
    last_name: str = None
    phone: str = None
    shop_name : str =None


class VendorRetrievalSchema(Schema):
    id: int
    email: EmailStr = None
    username: str = None
    first_name: str = None
    last_name: str = None
    phone: str = None
    shop_name: str = None
    shop_img: str = None
    shop_address: AddressRetrievalSchema = None
    category : CategoryRetrievalSchema = None
