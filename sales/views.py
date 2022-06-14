import datetime

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Sale
from .services.get_sales import get_all_values
from .services.get_sales import get_current_dollar_course
from .services.get_sales import get_deleted_sales
from .serializers import SaleSerializer


class SaleRefresh(APIView):
    """Create new orders or update existing"""

    def post(self, request):
        sales = get_all_values()
        one_dollar = get_current_dollar_course()

        existing_orders = Sale.objects.values_list("order")

        new_orders = tuple(sale[0] for sale in sales)

        deleted_orders = get_deleted_sales(new_orders, existing_orders)

        for sale in sales:
            order, cost_in_dollar, delivery_date = sale

            data = {
                "order": order,
                "cost_in_dollar": int(cost_in_dollar),
                "cost_in_rubles": int(cost_in_dollar) * one_dollar,
                "delivery_date": datetime.date(int(delivery_date.split(".")[2]),
                                               int(delivery_date.split(".")[1]),
                                               int(delivery_date.split(".")[0])
                                               )

            }
            serializer = SaleSerializer(data=data)

            if serializer.is_valid():
                serializer.save()

        for order in deleted_orders:
            Sale.objects.filter(order=order).delete()

        return Response(status=201)


class SaleList(generics.ListAPIView):
    """List sales"""
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
