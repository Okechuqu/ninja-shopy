from typing import List, Union
from django.shortcuts import get_object_or_404
from ninja import Router, FileEx, FormEx, UploadedFile
from products.models.products import Product
from schemas.products import ProductRegisterSchema, ProductRetrivalSchema


router = Router(tags=['Product Endpoints'])


@router.get('product/list', response=List[ProductRetrivalSchema])
def list_product(request):
    qs = Product.objects.all()
    return qs


@router.get('product/{product_id}/get', response=Union[str, ProductRetrivalSchema])
def get_product_by_id(request, product_id):
    qs = Product.objects.filter(id=product_id)
    if qs.exists():
        product = qs[0]
        return product
    return f"Product with ID {product_id} does not exist"


@router.post('product/add_product', response=ProductRetrivalSchema)
def add_product(request, category_id, vendor_id, image: UploadedFile, data: ProductRegisterSchema = FormEx(...)):
    qs = Product.objects.create(
        category_id=category_id, image=image, vendor_id=vendor_id, **data.dict())
    return qs


@router.delete('product/{product_id}/delete_product')
def delete_product(request, product_id):
    qs = Product.objects.filter(id=product_id)
    if qs.exists():
        product = qs[0]
        product.delete()
        return f"Product Deleted"
    return f"Product {product_id} Does not Exist"


@router.put('product/{product_id}/update_product_name', response=List[ProductRetrivalSchema])
def update_product_name(request, product_id, name):
    qs = Product.objects.filter(id=product_id)
    if qs.exists():
        product = qs[0]
        product.name = name
        product.save()
        # return qs
        return f"Product with Name '{product.name}' Successfully Updated"
    return f'Product {product_id} does not Exist'


@router.put('product/{product_id}/increase_stock_quantity', response=ProductRetrivalSchema)
def increase_stock_quantity(request, product_id, stock_quantity: int):
    qs = Product.objects.filter(id=product_id)
    if qs.exists():
        increase = qs[0]
        increase.stock_quantity += stock_quantity
        increase.save()
        return increase
        # return f"Product with Name '{increase.name}' Successfully Updated"
    return f"Product {product_id} does not Exist"


@router.put('product/{product_id}/reduce_stock_quantity', response=ProductRetrivalSchema)
def reduce_stock_quantity(request, product_id, stock_quantity: int):
    reduce = get_object_or_404(Product, id=product_id)
    if stock_quantity > 0 and stock_quantity <= reduce.stock_quantity:
        reduce.stock_quantity -= stock_quantity
        reduce.save()
        return reduce
    return f"Product {product_id} does not Exist"
