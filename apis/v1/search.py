from typing import List
from ninja import Router
from products.models.products import Product
from django.db.models import Q

from schemas.products import ProductRetrivalSchema


router = Router(tags=['Search Endpoints'])


@router.get('search_by_category_name/', response=List[ProductRetrivalSchema])
def search_by_category_name(request, name: str):
    qs = Product.objects.filter(category__name__icontains=name)
    return qs


@router.get('filter_products_by_product_and_vendor_name/', response=List[ProductRetrivalSchema])
def filter_products_by_product_and_vendor_name(request, query: str):
    qs = Product.objects.filter(
        Q(name__icontains=query) | Q(vendor__shop_name__icontains=query))
    return qs


@router.get('filter_by_id/{category_id}', response=List[ProductRetrivalSchema])
def filter_by_id(request, category_id: str):
    qs = Product.objects.filter(category_id=category_id)
    return qs


@router.get('filter_by_category_id_and_price/', response=List[ProductRetrivalSchema])
def filter_by_category_id_and_price(request,category_id, min_price:int, max_price:int):
    qs = Product.objects.filter(category_id=category_id)
    prices = []
    for item in qs:
        if min_price< item.price < max_price: 
            prices.append(item)
    return prices
