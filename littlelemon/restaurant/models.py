from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class Booking(models.Model):
    Name = models.CharField(max_length = 255)
    No_of_guests = models.PositiveIntegerField(validators =[MaxValueValidator(999999)])
    BookingDate = models.DateTimeField()

    def __str__(self):
        return str(self.BookingDate) + " - " + str(self.Name)

class Menu(models.Model):
    Title = models.CharField(max_length = 255)
    Price = models.DecimalField(max_digits = 10, decimal_places = 2)
    Inventory = models.PositiveIntegerField(validators =[MaxValueValidator(99999)])

    def __str__(self):
        return f'{self.Title} : {str(self.Price)}'