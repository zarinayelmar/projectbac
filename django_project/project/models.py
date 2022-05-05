from django.db import models
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[a-zA-Z0-9]*$', 'Only alphanumeric characters are allowed.')
validators=[alphanumeric]

# Create your models here.
class Salt(models.Model):
    atu = models.CharField(max_length=250)
    malimet = models.TextField(blank=True)

    def get_absolute_url(self):
        return f'/project/{self.id}'

class Makal(models.Model):
    atu = models.TextField(blank=True)
    avtor = models.CharField(max_length=250)

class Urum(models.Model):
    atu = models.TextField(blank=True)

    def str(self):
        return self.title
