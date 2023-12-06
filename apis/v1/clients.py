from typing import List, Union
from ninja import Router, FormEx, FileEx, UploadedFile
from schemas.addresses import AddressRegisterSchema
from schemas.clients import *
from user.models.addresses import Address
from user.models.client import Client


router = Router(tags=['Client Endpoints'])


@router.get('list_client', response=List[ClientRetrievalSchema])
def get_clients(request):
    qs = Client.objects.all()
    return qs


@router.get('client_by_id/{client_id}', response=Union[str, ClientRetrievalSchema])
def get_client_by_id(request, client_id):
    qs = Client.objects.filter(id=client_id)

    if qs.exists():
        return qs[0]
    return f"Client with ID {client_id} does not exist"


@router.post('client/add_client', response=Union[str, ClientRetrievalSchema])
def add_client(request, password: str = None, data: ClientRegisterSchema = FormEx(...)):
    qs = Client.objects.create(**data.dict())
    qs.set_password(password)
    return qs


# add profile_img
@router.post('client/update_profile_image/{client_id}', response=Union[str, ClientRetrievalSchema])
def update_client_profile_image(request, client_id, profile_image: UploadedFile):
    qs = Client.objects.filter(id=client_id)
    if qs.exists():
        client = qs[0]
        client.profile_img = profile_image
        client.save()
        return client
    return f"Client with ID {client_id} doesn't exist"


# add address to client
@router.post('client/update_client_address/{client_id}', response=Union[str, ClientRetrievalSchema])
def update_client_address(request, client_id, address_data: AddressRegisterSchema):
    qs = Client.objects.filter(id=client_id)
    if qs.exists():
        client = qs[0]
        address = Address.objects.create(**address_data.dict())
        client.shipping_address.add(address)
        client.save()
        return client
    return f"Client with ID {client_id} doesn't exist"


# Delete
@router.delete('client/delete_client/{client_id}')
def delete_client(request, client_id):
    qs = Client.objects.filter(id=client_id)
    if qs.exists():
        client = qs[0]
        client.delete()
        return f"Client {client.username} deleted successfuly"
    return f"Client with ID {client_id} doesn't exist"


@router.get('client/{client_id}/list_clients_addresses', response=List[AddressRetrievalSchema])
def list_clients_addresses(request, client_id):
    qs = Client.objects.filter(id=client_id)
    if qs.exists():
        client = qs[0]
        return client.shipping_address.all()
        # return client.shipping_address.all()
    return f"Client with ID {client_id} doesn't exist"


@router.post('client/{client_id}/set_current_address/{address_id}')
def set_current_address(request, client_id, address_id):
    qs = Client.objects.filter(id=client_id)
    qs_address = Address.objects.filter(id=address_id)
    if qs.exists():
        if qs_address.exists():
            client = qs[0]
            address = qs_address[0]
            clientAddress = client.shipping_address.all()
            for item in clientAddress:
                item.is_current = False
                item.save()

            address.is_current = True
            address.save()
            return f" Address {address.address} set as Current"
        return f"Address with ID {address_id} doesn't exist"
    return f"Client with ID {client_id} doesn't exist"


@router.post('client/{client_id}/add_address', response=Union[str, AddressRetrievalSchema])
def add_address(request, client_id, data: AddressRegisterSchema = FormEx(...)):
    qs_client = Client.objects.filter(id=client_id)
    if qs_client.exists():
        client = qs_client[0]
        qs = Address.objects.create(**data.dict())
        client.shipping_address.add(qs)
        qs.save()
        return qs
    return f"Client with {client_id} does not exist "
