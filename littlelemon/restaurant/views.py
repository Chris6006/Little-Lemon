from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking, Menu
from .serializers import BookingSerializer,menuSerializer, BookingSerializerStaff
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsManager, IsSuperUser

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
        if self.request.method == "GET":
            if self.request.user.is_superuser or self.request.user.groups.filter(name='Manager').exists():
                return Booking.objects.all().order_by("BookingDate")
            elif self.request.user.groups.count()==0: #normal customer - no group
                return Booking.objects.all().filter(Name=self.request.user).order_by("BookingDate")
    
    #This allows Managers and SuperUsers to use a different Serializer Class, normal users cannot detirmine Name and all bookings are entered under their username
    def get_serializer_class(self):
        if self.request.user.is_superuser or self.request.user.groups.filter(name='Manager').exists():
            return BookingSerializerStaff
        return BookingSerializer


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    #This part prevents anyone but SuperUsers and Managers do anything but seeing the menu
    def get_permissions(self):
        permission_classes = []
        if self.request.method != "GET":
            permission_classes = [IsSuperUser|IsManager]
        return [permission() for permission in permission_classes]

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    #This part prevents anyone but SuperUsers and Managers do anything but seeing the menu items
    def get_permissions(self):
        permission_classes = []
        if self.request.method != "GET":
            permission_classes = [IsSuperUser|IsManager]
        return [permission() for permission in permission_classes]