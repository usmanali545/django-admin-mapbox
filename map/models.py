from django.db import models
from jsonfield import JSONField

category = [('verygood', 'verygood'), ('good', 'good'), ('bad', 'bad')]
class Poi(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    category = models.CharField(choices=category, max_length=20)
    geojson = JSONField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.lat}, {self.lon}"