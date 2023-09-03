from django.db import models

# Create your models here.
class Writer(models.Model):
    name = models.CharField()