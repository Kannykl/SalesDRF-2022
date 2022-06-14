from django.db import models


class Sale(models.Model):
    """Info about sale."""
    order = models.CharField(max_length=100, verbose_name="заказ")
    cost_in_dollar = models.IntegerField(verbose_name="стоимость $")
    cost_in_rubles = models.IntegerField(verbose_name="стоимость RUB")
    delivery_date = models.DateField()
