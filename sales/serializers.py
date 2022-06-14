from rest_framework import serializers

from .models import Sale


class SaleSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        sale = Sale.objects.update_or_create(
            order=validated_data.get("order", None),
            defaults={
                "cost_in_dollar": validated_data.get("cost_in_dollar"),
                "cost_in_rubles": validated_data.get("cost_in_rubles"),
                "delivery_date": validated_data.get("delivery_date"),
            }
        )

        return sale

    class Meta:
        model = Sale
        fields = ("order", "cost_in_dollar", "cost_in_rubles", "delivery_date")
