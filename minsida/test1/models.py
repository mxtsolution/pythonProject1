from django.db import models

class Namnlista(models.Model):

    ao = models.CharField(max_length=6, default="")
    direktiv = models.CharField(max_length=20, default="")
    objektid = models.TextField(max_length=20, default="")
    avd = models.TextField(max_length=20, default="")
    avstallt = models.BooleanField(default=False)
    operator = models.CharField(max_length=20, default="")
    utforare = models.TextField(max_length=20, default="")
    status = models.CharField(max_length=20, default="")
    startad = models.DateTimeField(auto_now=True)
    avslutad = models.DateTimeField(auto_now=True)
    utfort = models.BooleanField(default=False)
    avstallt_datum = models.DateTimeField(auto_now=True)
    las_lista = models.CharField(max_length=20, default="")
