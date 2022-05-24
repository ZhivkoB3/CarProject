from django.utils import timezone

from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response


def destroy_sample(car_object):
    """
    function used to override the default "DELETE" method with "SOFT DELETE".
    When an entry/object is marked with "is_deleted = True" in the database
    when we perform a "GET" request it would not be returned in the results.
    Adds time of deletion in the "deleted_at" column and saves the entry/object.
    """
    try:
        car_object.is_deleted = True
        car_object.deleted_at = timezone.now()
        car_object.save()
        return Response(
            {"message": "Data deleted successfully!"}, status=status.HTTP_200_OK
        )
    except car_object.DoesNotExist:
        return Response(
            {"message": "Data does not exist"}, status=status.HTTP_404_NOT_FOUND
        )


def multiple_destroy_sample(car_object):
    """
    "SOFT DELETE" for multiple entries
    """
    if car_object.exists():
        for x in car_object:
            destroy_sample(x)
        return Response(
            {"message": f"{car_object.count()} data points deleted successfully!"},
            status=status.HTTP_200_OK,
        )
    else:
        return Response(
            {"message": "Data does not exist"}, status=status.HTTP_404_NOT_FOUND
        )


def restore_object(model, id):
    """
    1.Since we are using a "soft delete" we can restore
    the deleted elements.
    2.Restore a deleted entry/object in the CarBrand table.
    3.Marks the entry/object as "is_deleted=False" and also
    makes the "deleted_at = null"
    """
    try:
        a_model = model.objects_restore.get(id=id)
    except model.DoesNotExist:
        return JsonResponse(
            {"message": "Data does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    a_model.restore()
    return JsonResponse(
        {"message": "Data restored successfully!"}, status=status.HTTP_200_OK
    )
