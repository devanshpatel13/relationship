from django.db import models


# Create your models here.


class palce(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class hotel(models.Model):
    palce = models.OneToOneField(palce, on_delete=models.CASCADE)
    pizza = models.BooleanField()
    burger = models.BooleanField()

    def __str__(self):
        return str(self.palce)


class waiter(models.Model):
    hotel = models.ForeignKey(hotel, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
