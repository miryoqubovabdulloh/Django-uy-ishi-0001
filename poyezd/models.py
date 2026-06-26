from django.db import models

# Create your models here.
class Poyezd(models.Model):
    nomi = models.CharField(max_length=100)
    tezlik = models.IntegerField()
    joylar_soni = models.IntegerField()
    yoqilgi_turi = models.CharField(max_length=50)

    def __str__(self):
        return self.nomi