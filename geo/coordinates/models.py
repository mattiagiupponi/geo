from django.db import models


class Coordinate(models.Model):
    id = models.AutoField(primary_key=True)
    x_axes = models.FloatField(null=False, default=0)
    y_axes = models.FloatField(null=False, default=0)

    def __str__(self):
        return f"Coordinate: {self.x_axes}/{self.y_axes}"


class RequestHistory(models.Model):
    id = models.AutoField(primary_key=True)
    request = models.CharField(max_length=2000, null=True)

    def __str__(self):
        return self.request
