from rest_framework import serializers
from .models import Menu, Booking
from rest_framework.serializers import ModelSerializer


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ["id", "title", "price", "inventory"]


class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
