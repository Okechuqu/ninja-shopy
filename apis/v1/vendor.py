from typing import List, Union
from ninja import Router, FormEx, FileEx, UploadedFile
from schemas.addresses import AddressRegisterSchema
from schemas.vendor import *
from user.models.addresses import Address
from user.models.vendor import Vendor


router = Router(tags=['Vendor Endpoints'])


@router.get('list_vendor', response=List[VendorRetrievalSchema])
def get_vendors(request):
    qs = Vendor.objects.all()
    return qs


@router.get('vendor_by_id/{vendor_id}', response=Union[str, VendorRetrievalSchema])
def get_vendor_by_id(request, vendor_id):
    qs = Vendor.objects.filter(id=vendor_id)

    if qs.exists():
        return qs[0]
    return f"vendor with ID {vendor_id} does not exist"


@router.post('vendor/add_vendor', response=Union[str, VendorRetrievalSchema])
def add_vendor(request, category_id, shop_address, shop_img: UploadedFile, password: str = None, data: VendorRegisterSchema = FormEx(...)):
    qs = Vendor.objects.create(
        category_id=category_id, shop_img=shop_img, **data.dict())
    qs.set_password(password)
    address = Address.objects.create(address=shop_address)
    qs.shop_address = address
    qs.save()
    return qs


# add shop_img
@router.post('vendor/update_shop_image/{vendor_id}', response=Union[str, VendorRetrievalSchema])
def update_vendor_shop_image(request, vendor_id, shop_image: UploadedFile = FileEx(...)):
    qs = Vendor.objects.filter(id=vendor_id)
    if qs.exists():
        vendor = qs[0]
        vendor.shop_img = shop_image
        vendor.save()
        return vendor
    return f"Vendor with ID {vendor_id} doesn't exist"


# add address to vendor
@router.post('vendor/update_shop_address/{vendor_id}', response=Union[str, VendorRetrievalSchema])
def update_shop_address(request, vendor_id, address_data: AddressRegisterSchema):
    qs = Vendor.objects.filter(id=vendor_id)
    if qs.exists():
        vendor = qs[0]
        address = Address.objects.create(**address_data.dict())
        vendor.shop_address = address
        vendor.save()
        return vendor
    return f"vendor with ID {vendor_id} doesn't exist"


# Delete
@router.delete('vendor/delete_vendor/{vendor_id}')
def delete_vendor(request, vendor_id):
    qs = Vendor.objects.filter(id=vendor_id)
    if qs.exists():
        vendor = qs[0]
        vendor.delete()
        return f"Vendor {vendor.username} deleted successfuly"
    return f"Vendor with ID {vendor_id} doesn't exist"
