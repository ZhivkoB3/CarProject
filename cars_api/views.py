from rest_framework import generics
from rest_framework.decorators import api_view


from cars.models import CarBrand, CarModel
from .serializers import CarBrandSerializer, CarModelSerializer
from .utils import destroy_sample, restore_object, multiple_destroy_sample


# Start CarBrand


class CarBrandList(generics.ListCreateAPIView):
    queryset = CarBrand.soft_delete_objects.all()
    serializer_class = CarBrandSerializer


class CarBrandDetail(generics.RetrieveAPIView):
    queryset = CarBrand.soft_delete_objects.all()
    serializer_class = CarBrandSerializer


class CarBrandSoftDelete(generics.DestroyAPIView):
    queryset = CarBrand.soft_delete_objects.all()
    serializer_class = CarBrandSerializer

    def destroy(self, request, *args, **kwargs):
        """
        override the default "DELETE" method to use
        "soft delete".
        """
        car_brand = self.get_object()
        return destroy_sample(car_brand)


@api_view(["GET", "PATCH"])
def restore_deleted_car_brand(request, id):
    """
    1.Since we are using a "soft delete" we can restore
    the deleted elements.
    2.Restore a deleted entry/object in the CarBrand table.
    3.Marks the entry/object as "is_deleted=False" and also
    makes the "deleted_at = null"
    """
    return restore_object(CarBrand, id)


class CarBrandFilterByName(generics.ListAPIView):
    """
    Filters elements by name.
    """

    serializer_class = CarBrandSerializer

    def get_queryset(self):
        name = self.kwargs["name"]
        return CarBrand.soft_delete_objects.filter(name=name)


class CarBrandFilterByNameContains(generics.ListAPIView):
    """
    Filters elements by partial name.
    """

    serializer_class = CarBrandSerializer

    def get_queryset(self):
        name = self.kwargs["name"]
        return CarBrand.soft_delete_objects.filter(name__icontains=name)


class CarBrandFilterByDate(generics.ListAPIView):
    """
    Filters elements by date.
    """

    serializer_class = CarBrandSerializer

    def get_queryset(self):
        created_at = self.kwargs["created_at"]
        return CarBrand.soft_delete_objects.filter(created_at__icontains=created_at)


class CarBrandDeleteAllByDate(generics.DestroyAPIView):
    """
    Filters elements by date and soft deletes them.
    """

    def destroy(self, request, *args, **kwargs):
        created_at = self.kwargs["created_at"]
        car_brand = CarBrand.soft_delete_objects.filter(
            created_at__icontains=created_at
        )

        return multiple_destroy_sample(car_brand)


# End CarBrand

# Start CarModel


class CarModelList(generics.ListCreateAPIView):
    queryset = CarModel.soft_delete_objects.all()
    serializer_class = CarModelSerializer


class CarModelDetail(generics.RetrieveAPIView):
    queryset = CarModel.soft_delete_objects.all()
    serializer_class = CarModelSerializer


class CarModelSoftDelete(generics.RetrieveDestroyAPIView):
    queryset = CarModel.soft_delete_objects.all()
    serializer_class = CarModelSerializer

    def destroy(self, request, *args, **kwargs):
        """
        override the default "DELETE" method to use
        "soft delete".
        """
        car_model = self.get_object()
        return destroy_sample(car_model)


class CarModelFilterByName(generics.ListAPIView):
    """
    Filters elements by name.
    """

    serializer_class = CarModelSerializer

    def get_queryset(self):
        name = self.kwargs["name"]
        return CarModel.soft_delete_objects.filter(name=name)


class CarModelFilterByNameContains(generics.ListAPIView):
    """
    Filters elements by partial name.
    """

    serializer_class = CarModelSerializer

    def get_queryset(self):
        name = self.kwargs["name"]
        return CarModel.soft_delete_objects.filter(name__icontains=name)


class CarModelFilterByDate(generics.ListAPIView):
    """
    Filters elements by date.
    """

    serializer_class = CarModelSerializer

    def get_queryset(self):
        created_at = self.kwargs["created_at"]
        return CarModel.soft_delete_objects.filter(created_at__icontains=created_at)


@api_view(["GET", "PATCH"])
def restore_deleted_car_model(request, id):
    """
    1.Since we are using a "soft delete" we can restore
    the deleted elements.
    2.Restore a deleted entry/object in the CarModel table.
    3.Marks the entry/object as "is_deleted=False" and also
    makes the "deleted_at = null"
    """
    return restore_object(CarModel, id)


class CarModelDeleteAllByDate(generics.DestroyAPIView):
    """
    Filters elements by date and soft deletes them.
    Override the default "DELETE" method to use
    "SOFT DELETE".
    """

    def destroy(self, request, *args, **kwargs):
        created_at = self.kwargs["created_at"]
        car_model = CarModel.soft_delete_objects.filter(
            created_at__icontains=created_at
        )
        return multiple_destroy_sample(car_model)


# End CarModel
