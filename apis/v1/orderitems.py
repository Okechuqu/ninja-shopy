from typing import List, Union
from django.shortcuts import get_object_or_404
from ninja import Router, FormEx
from orders.models.order_items import OrderItem
from schemas.orderitems import OrderitemRegisterSchema, OrderitemRetrievalSchema


router = Router(tags=['Order-Items Endpoints'])


@router.get('all_items', response=List[OrderitemRetrievalSchema])
def all_items(request):
    qs = OrderItem.objects.all()

    return qs


@router.post('add_item', response=Union[str, OrderitemRetrievalSchema])
def add_item(request, client_id, product_id, details: OrderitemRegisterSchema = FormEx(...)):
    qs = OrderItem.objects.create(
        client_id=client_id, product_id=product_id, **details.dict())
    return qs


@router.put('increase_orderitem/{order_item_id}', response=OrderitemRetrievalSchema)
def increase_orderitem(request, order_item_id, stock_quantity: int):
    qs = get_object_or_404(OrderItem, id=order_item_id)
    if stock_quantity > 0:
        qs.quantity += stock_quantity
        qs.save()
        return qs
    return f"Product {order_item_id} does not Exist"


@router.put('reduce_orderitem/{order_item_id}', response=OrderitemRetrievalSchema)
def reduce_orderitem(request, order_item_id, stock_quantity: int):
    qs = get_object_or_404(OrderItem, id=order_item_id)
    if stock_quantity > 0 and stock_quantity <= qs.quantity:
        qs.quantity -= stock_quantity
        qs.save()
        return qs
    return f"Product {order_item_id} does not Exist"


@router.delete('delete_orderitem/{order_item_id}')
def delete_orderitem(request, order_item_id):
    qs = get_object_or_404(OrderItem, id=order_item_id)
    if qs:
        qs.delete()
        return f"Deleted {order_item_id.id} Successfully"
    return f"Product {order_item_id} does not Exist"
