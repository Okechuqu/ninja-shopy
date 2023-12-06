from typing import List, Union
from ninja import Router, FormEx
from schemas.category import *
from categories.models import Category


router = Router(tags=['Category Endpoints'])


@router.get('list_Category', response=List[CategoryRetrievalSchema])
def get_Categorys(request):
    qs = Category.objects.all()
    return qs


@router.get('category_by_id/{category_id}', response=Union[str, CategoryRetrievalSchema])
def get_Category_by_id(request, category_id):
    qs = Category.objects.filter(id=category_id)

    if qs.exists():
        return qs[0]
    return f"Category with ID {category_id} does not exist"


@router.post('category/add_Category', response=Union[str, CategoryRetrievalSchema])
def add_Category(request, data: CategoryRegisterSchema = FormEx(...)):
    qs = Category.objects.create(**data.dict())

    return qs

# Delete


@router.delete('category/delete_category/{category_id}')
def delete_category(request, category_id):
    qs = Category.objects.filter(id=category_id)
    if qs.exists():
        category = qs[0]
        category.delete()
        return f"Category {category.name} deleted successfuly"
    return f"Category with ID {category_id} doesn't exist"


@router.put('category/{category_id}/update')
def update_category(request, category_id, name):
    qs = Category.objects.filter(id=category_id)
    if qs.exists():
        category = qs[0]
        category.name = name
        category.save()
        return f'Category {category.name} has been Updated Successfuly'
    return f"Category with ID {category_id} doesn't exist"
