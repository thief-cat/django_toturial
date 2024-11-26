from django.db import models

# Create your models here.
class Hoge(models.Model):
  hoge = models.CharField(_(""), max_length=50)
  foo = models.CharField(_(""), max_length=50)