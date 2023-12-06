from ninja import NinjaAPI
from apis.v1.clients import router as client_router
from apis.v1.vendor import router as vendor_router
from apis.v1.category import router as category_router
from apis.v1.address import router as address_router
from apis.v1.products import router as product_router
from apis.v1.orders import router as order_router
from apis.v1.orderitems import router as order_items_router
from apis.v1.search import router as search_router


api = NinjaAPI(title='Shopy Endpoints')

api.add_router('Clients', client_router)
api.add_router('Vendor', vendor_router)
api.add_router('Address', address_router)
api.add_router('Category', category_router)
api.add_router('Products', product_router)
api.add_router('Orders', order_router)
api.add_router('OrderItems', order_items_router)
api.add_router('Search', search_router)
