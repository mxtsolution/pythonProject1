from django.db import models

class pulistan(models.Model):

    avd = models.CharField(max_length=6, default="")
    beskrivning = models.CharField(max_length=20, default="")
    artal = models.TextField(max_length=20, default="")
    kostnad = models.TextField(max_length=20, default="")
    projektnr = models.TextField(max_length=20, default="")
    projektledare = models.TextField(max_length=20, default="")
    projektansvarig = models.TextField(max_length=20, default="")
    ansvar = models.TextField(max_length=7, default="")
    motpart = models.TextField(max_length=7, default="")
    b_start = models.TextField(max_length=7, default="")
    b_klart = models.TextField(max_length=7, default="")
    beviljan_m = models.TextField(max_length=7, default="")
    rs = models.TextField(max_length=7, default="")
    motivering = models.TextField(max_length=500, default="")
    omfattning = models.TextField(max_length=500, default="")
    konsekvens = models.TextField(max_length=500, default="")
    objektid = models.TextField(max_length=500, default="")
    arbetsorder = models.TextField(max_length=500, default="")








    askande_fil = models.FileField(upload_to='test1/resources/', null=True, blank=True)

