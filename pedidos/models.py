from django.db import models

from django.contrib.auth import get_user_model
from django.db.models import Sum, F, FloatField
from tienda.models import Producto

# Create your models here.

User = get_user_model()


class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

    @property
    def total(self):
        return self.lineapedido_set.aggregate(
            total=Sum(F('precio') * F('cantidad'), output_field=FloatField)

        )['total']

    class Meta:
        db_table = 'pedidos'
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        ordering = ['id']


class LineaPedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cantidad} unidades de {self.producto.nombre}'

    class Meta:
        db_table = 'lineapedidos'
        verbose_name = 'linea de pedido'
        verbose_name_plural = 'lineas de pedidos'
        ordering = ['id']
