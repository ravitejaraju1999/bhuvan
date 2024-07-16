from django.db import models

class SoilMoistureData(models.Model):
    id = models.AutoField(primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    soil_moisture = models.FloatField()

    def __str__(self):
        return self.id+self.latitude+self.longitude+self.soil_moisture



