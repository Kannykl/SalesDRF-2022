from django.urls import path
from .views import SaleRefresh, SaleList

urlpatterns = [
    path("refresh_sales/", SaleRefresh.as_view()),
    path("get_sales/", SaleList.as_view()),
]
