from django.contrib import admin
from user.models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    search_fields = ["email_startswith", "username_startswith"]
    list_display = [
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
        "phone",
        "is_staff",
        "is_superuser",
    ]
    list_filter = ["is_staff", "is_superuser"]
    list_display_links = ["username", "email"]
    ordering = ["id"]
    filter_horizontal = []
    fieldsets = [
        (None, {"fields": ["username", "email", "password"]}),
        ("Personal Info", {"fields": ["first_name", "last_name", "phone"]}),
        ("Permissions", {"fields": ["is_staff", "is_superuser"]}),
    ]


@admin.register(Client)
class ClientAdmin(UserAdmin):
    search_fields = ["email_startswith", "username_startswith"]
    list_display = [
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
    ]
    list_display_links = ["username", "email"]
    list_filter = []
    ordering = ["id"]
    filter_horizontal = []
    fieldsets = [
        (None, {"fields": ["username", "email", "password"]}),
        (
            "Personal Info",
            {"fields": ["first_name", "last_name", "phone",
                        "profile_image", "shipping_address"]},
        ),
        ("Permissions", {"fields": []}),
    ]


@admin.register(Vendor)
class VendorAdmin(UserAdmin):
    search_fields = ["email_startswith", "username_startswith"]
    list_display = [
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
    ]
    list_display_links = ["username", "email"]
    list_filter = []
    ordering = ["id"]
    filter_horizontal = []
    fieldsets = [
        (None, {"fields": ["username", "email", "password"]}),
        (
            "Personal Info",
            {"fields": ["first_name", "last_name", "phone",
                        "shop_name", "shop_address", "shop_img", "category",]},
        ),
        ("Permissions", {"fields": []}),
    ]
