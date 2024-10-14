from django.db import models


class Exel(models.Model):
    date = models.DateField()
    kod_client = models.IntegerField(default=0)
    count_tovar = models.IntegerField(default=0)
    ves = models.FloatField(default=0)
    trek_cod = models.CharField(max_length=32)


