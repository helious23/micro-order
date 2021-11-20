from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path(
        "shop",
        views.ShopViewSet.as_view({"get": "list", "post": "create"}),
        name="shop",
    ),
    path(
        "shop/<str:pk>",
        views.ShopViewSet.as_view(
            {"get": "retrive", "put": "update", "delete": "destroy"}
        ),
    ),
    path(
        "order",
        views.OrderViewSet.as_view({"get": "list", "post": "create"}),
        name="order",
    ),
    path(
        "order/<str:pk>",
        views.OrderViewSet.as_view(
            {"get": "retrive", "put": "update", "delete": "destroy"}
        ),
    ),
]
