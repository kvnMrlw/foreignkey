from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Produto(models.Model):
    produto = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    criado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.produto