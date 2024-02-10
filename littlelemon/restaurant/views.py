from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking, Menu
from .serializers import BookingSerializer,menuSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet,ViewSet
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
        #items = Booking.objects.all()
        #serializer = BookingSerializer(items, many = True)
        #return Response(serializer.data)
        if self.request.user.is_superuser or IsManager == True:
            serializer = Booking.objects.all()
            return Response(serializer.data)
        elif self.request.user.groups.count == 0: #Normal customer, no groups
            serializer = Booking.objects.all().filter(user=self.request.user)
            return Response(serializer.data)
    
class BookingViewSet(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    #Just to note, if you are not signed in as a SuperUser or Manager, you can only see your own bookings
    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.groups.filter(name='Manager').exists():
            return Booking.objects.all()
        elif self.request.user.groups.count()==0: #normal customer - no group
            return Booking.objects.all().filter(Name=self.request.user)


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    def get_permissions(self):
        permission_classes = []
        if self.request.method != "GET":
            permission_classes = [IsSuperUser|IsManager]
        return [permission() for permission in permission_classes]

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    def get_permissions(self):
        permission_classes = []
        if self.request.method != "GET":
            permission_classes = [IsSuperUser|IsManager]
        return [permission() for permission in permission_classes]