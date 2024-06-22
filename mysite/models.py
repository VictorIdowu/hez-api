from django.db import models

# Create your models here.

class Clients(models.Model):

  def __str__(self):
    return self.clients_ip

  clients_ip = models.CharField(max_length=200)
  greeting = models.CharField(max_length=500)