from django.urls import path
from .views import test_view, records

# paths
urlpatterns = [
    path("test_view/", test_view, name="test_view"),
    path("records/", records, name="records")
]