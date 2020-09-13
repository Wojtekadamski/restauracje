from django.db import models


# Create your models here.

class Restauracja(models.Model):
    name = models.TextField(max_length=128)
    address = models.TextField(max_length=256)
    type = models.ForeignKey("Type", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name} {self.address}"


class Type(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name}"
