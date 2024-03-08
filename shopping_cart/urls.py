from django.urls import path

from shopping_cart.views import ShoppingCartDetail

urlpatterns = [
    path('detail', ShoppingCartDetail.as_view(), name='detail')
]
