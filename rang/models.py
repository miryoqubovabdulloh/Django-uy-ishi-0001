from django.db import models

# Create your models here.
class Rang(models.Model):
    nomi = models.CharField(max_length=100)
    tavsif = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nomi