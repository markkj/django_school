from django.urls import path,include
from .views import SchoolViewSet,StudentViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'school', SchoolViewSet)
router.register(r'student',StudentViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
]
