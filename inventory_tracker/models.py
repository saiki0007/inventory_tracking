from django.db import models


class Items(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=50)
    item_type = models.CharField(max_length=50)
    item_quantity = models.IntegerField(default=0)
