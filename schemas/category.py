import uuid
from ninja import Schema



class CategoryRegisterSchema(Schema):
    name : str = None


class CategoryRetrievalSchema(Schema):
    id: uuid.UUID
    name: str = None
