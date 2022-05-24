from audioop import reverse
from django.db import models
from django.urls import reverse


class Qso(models.Model):
    mode = models.CharField(max_length=25)
    our_call = models.CharField(max_length=8)
    our_category = models.CharField(max_length=8)
    our_section = models.CharField(max_length=8)
    their_call = models.CharField(max_length=8)
    their_category = models.CharField(max_length=8)
    their_section = models.CharField(max_length=8)
    

    class Meta:
        verbose_name = ("QSO")
        verbose_name_plural = ("QSOs")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("qso_detail", kwargs={"pk": self.pk})
