from typing import List, Union
from ninja import Router, FormEx
from orders.models import Order
from orders.models.order_items import OrderItem
from schemas.orders import OrderRegisterSchema, OrderRetrievalSchema


router = Router(tags=['Order Endpoints'])


@router.get('list_orders', response=List[OrderRetrievalSchema])
def list_orders(request):
    qs = Order.objects.all()
    return qs


@router.post('orders/create_order', response=Union[str, OrderRetrievalSchema])
def create_order(request, client_id, shipping_address_id, details: OrderRegisterSchema):
    qs = Order.objects.create(client_id=client_id, shipping_address_id=shipping_address_id)
    orderitem_ids=details.dict().get('orderitem_ids')

    for id in orderitem_ids:
        item = OrderItem.objects.filter(id=id)
        if item.exists():
            itemMain = item[0]
            qs.orderitems.add(itemMain)
            qs.save()
        else:
            continue
    return qs


@router.get('orders/{order_id}', response=OrderRetrievalSchema)
def get_one_order(request, order_id):
    qs = Order.objects.filter(id=order_id)
    if qs.exists():
        order = qs[0]
        return order
    return f"Order with ID {order_id} doesn't exist"
