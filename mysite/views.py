from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Clients
from .serializers import DrinkSerializer
from rest_framework.response import Response

# Create your views here.

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


@api_view(['GET'])
def clients(request):
    client_ip = get_client_ip(request)
    response_data = {
        'ip_address': client_ip,
        'greetings': 'Hello world'
    }
    return Response(response_data)