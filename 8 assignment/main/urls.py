from django.urls import path
from . import views
from .api import items_api, item_api

urlpatterns = [
    path("", views.home_page, name="home"),
    path("list/", views.items_page, name="list"),
    path("detail/<int:pk>/", views.item_page, name="detail"),

    # API
    path("api/items/", items_api, name="api_items"),
    path("api/items/<int:pk>/", item_api, name="api_item"),
]
