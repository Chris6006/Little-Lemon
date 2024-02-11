from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
    
class Booking(models.Model):
    Name = models.CharField(max_length = 255)
    No_of_guests = models.PositiveIntegerField(validators =[MaxValueValidator(20)])
    BookingDate = models.DateTimeField()

    def __str__(self):
        return f'{self.Name} - {str(self.BookingDate.strftime('%Y/%m/%d %H:%M:%S'))} - No. of Guests: {self.No_of_guests}'

class Menu(models.Model):
    Title = models.CharField(max_length = 255)
    Price = models.DecimalField(max_digits = 10, decimal_places = 2)
    Inventory = models.PositiveIntegerField(validators =[MaxValueValidator(99999)])

    def __str__(self):
        return f'{self.Title} : {str(self.Price)}'