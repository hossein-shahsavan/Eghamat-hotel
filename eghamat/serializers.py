from rest_framework import serializers
from . import models


class Room_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = '__all__'


class User_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class Reservation_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reservation
        fields = '__all__'

