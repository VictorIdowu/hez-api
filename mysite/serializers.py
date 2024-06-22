from rest_framework import serializers
from .models import Clients

class DrinkSerializer(serializers.ModelSerializer):
  class Meta:
    model = Clients
    fields = ['clients_ip', 'greeting']