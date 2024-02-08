from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking, Menu
from .serializers import BookingSerializer,menuSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.decorators import permission_classes, api_view
from .permissions import IsManager, IsSuperUser
from rest_framework.authentication import BasicAuthentication

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
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    def get_permissions(self):
        permission_classes = []
        if self.request.method != "GET":
            permission_classes = [IsManager or IsSuperUser]
        return [permission() for permission in permission_classes]

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer