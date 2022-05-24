from rest_framework import serializers
from cars.models import CarBrand, CarModel, UserCar


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = ("id", "name", "created_at", "is_deleted")


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = "__all__"


class UserCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCar
        fields = "__all__"
