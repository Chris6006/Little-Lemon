from rest_framework import serializers
from .models import Menu, Booking
#from rest_framework.fields import CurrentUserDefault

#This class allows it to return the current user, can be used as a default so users cannot enter other usernames while booking
class CurrentUserDefault:
    """
    May be applied as a `default=...` value on a serializer field.
    Returns the current user.
    """
    requires_context = True

    def __call__(self, serializer_field):
        return serializer_field.context['request'].user

class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

#This serializer does not allow users to chose a name, rather it defaults to their username
class BookingSerializer(serializers.ModelSerializer):
    Name = serializers.HiddenField(default = CurrentUserDefault())
    class Meta:
        model = Booking
        fields = ['Name','No_of_guests', 'BookingDate']

#Superusers and Managers are directed to this serializer, whidh does allow manual input of a name
class BookingSerializerStaff(serializers.ModelSerializer):
    Name = serializers.CharField(default = CurrentUserDefault)
    class Meta:
        model = Booking
        fields = '__all__'