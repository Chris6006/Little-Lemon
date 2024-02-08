from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking, Menu
from .serializers import BookingSerializer,menuSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class bookingview(APIView):
    http_method_names = ['get']
    def get(self,request):
        items = Booking.objects.all()
        serializer = BookingSerializer(items, many = True)
        return Response(serializer.data)
    
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer