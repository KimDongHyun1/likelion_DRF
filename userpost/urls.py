from rest_framework.routers import DefaultRouter
from django.urls import path, include
from userpost import views

router = DefaultRouter()
router.register('', views.UserPostViewSet)

urlpatterns = [
    path('', include(router.urls))
]