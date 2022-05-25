from django.urls import path

from cars_api import views
from .views import (
    CarBrandList,
    CarBrandSoftDelete,
    CarBrandDetail,
    CarModelDetail,
    CarModelList,
    CarModelSoftDelete,
    CarBrandFilterByName,
    CarBrandFilterByNameContains,
    CarBrandFilterByDate,
    CarBrandDeleteAllByDate,
    CarModelDeleteAllByDate,
    CarModelFilterByName,
    CarModelFilterByNameContains,
    CarModelFilterByDate,
)

urlpatterns = [
    # CarBrand
    path("car-brand/<int:pk>/",
         CarBrandDetail.as_view(),
         name="car-brand-detailed"),
    path(
        "car-brand-delete/<int:pk>/",
        CarBrandSoftDelete.as_view(),
        name="car-brand-delete",
    ),
    path("car-brand/",
         CarBrandList.as_view(),
         name="car-brand-list"),
    path(
        "restore-deleted-car-brand/<int:id>/",
        views.restore_deleted_car_brand,
        name="car-brand-restore",
    ),
    path(
        "car-brand-filter-by-name/<str:name>/",
        CarBrandFilterByName.as_view(),
        name="car-brand-filter-name",
    ),
    path(
        "car-brand-filter-by-starts-with-name/<str:name>/",
        CarBrandFilterByNameContains.as_view(),
        name="car-brand-filter-name-contains",
    ),
    path(
        "car-brand-filter-by-date/<int:created_at>/",
        CarBrandFilterByDate.as_view(),
        name="car-brand-filter-date",
    ),
    path(
        "car-brand-delete-all-by-date/<int:created_at>/",
        CarBrandDeleteAllByDate.as_view(),
        name="car-brand-delete-all-date",
    ),

    # CarModel
    path("car-model/<int:pk>/",
         CarModelDetail.as_view(),
         name="car-model-detailed"),
    path(
        "car-model/delete/<int:pk>/",
        CarModelSoftDelete.as_view(),
        name="car-model-delete",
    ),
    path("car-model/", CarModelList.as_view(), name="car-model-list"),
    path(
        "restore-deleted-car-model/<int:id>/",
        views.restore_deleted_car_model,
        name="car-model-restore",
    ),
    path(
        "car-model-filter-by-name/<str:name>/",
        CarModelFilterByName.as_view(),
        name="car-model-filter-name",
    ),
    path(
        "car-model-filter-by-name-contains/<str:name>/",
        CarModelFilterByNameContains.as_view(),
        name="car-model-filter-name-contains",
    ),
    path(
        "car-model-filter-by-date/<int:created_at>/",
        CarModelFilterByDate.as_view(),
        name="car-model-filter-date",
    ),
    path(
        "car-model-delete-all-by-date/<int:created_at>/",
        CarModelDeleteAllByDate.as_view(),
        name="car-model-delete-all-date",
    ),
]
