from .models import Menu, Booking
from rest_framework.serializers import ModelSerializer, RelatedField
from django.contrib.auth.models import User, Group


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = ["id", "title", "price", "inventory"]


class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"


class GroupNameField(RelatedField):
    def to_representation(self, value):
        return value.name


class UserSerializer(ModelSerializer):
    groups = GroupNameField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ("url", "username", "email", "groups")
