from typing import List, Union
from ninja import Router, FormEx
from schemas.addresses import AddressRegisterSchema, AddressRetrievalSchema
from user.models import Address
from user.models.client import Client


router = Router(tags=['Address Endpoints'])


@router.get('list_address', response=List[AddressRetrievalSchema])
def get_addresss(request):
    qs = Address.objects.all()
    return qs


@router.get('address_by_id/{address_id}', response=Union[str, AddressRetrievalSchema])
def get_address_by_id(request, address_id):
    qs = Address.objects.filter(id=address_id)

    if qs.exists():
        return qs[0]
    return f"address with ID {address_id} does not exist"


@router.post('address/add_address', response=Union[str, AddressRetrievalSchema])
def add_address(request,client_id, data: AddressRegisterSchema = FormEx(...)):
    qs_client = Client.objects.filter(id=client_id)
    if qs_client.exists():
        client = qs_client[0]
        qs = Address.objects.create(**data.dict())
        client.shipping_address.add(qs)
        qs.save()
        return qs
    return f"Client with {client_id} does not exist "

# Delete


@router.delete('address/delete_address/{address_id}')
def delete_address(request, address_id):
    qs = Address.objects.filter(id=address_id)
    if qs.exists():
        address = qs[0]
        address.delete()
        return f"address {address.address} deleted successfuly"
    return f"address with ID {address_id} doesn't exist"


@router.put('address/{address_id}/update')
def update_address(request, address_id, address):
    qs = Address.objects.filter(id=address_id)
    if qs.exists():
        address = qs[0]
        address.address = address
        address.save()
        return f'address {address.address} has been Updated Successfuly'
    return f"address with ID {address_id} doesn't exist"
