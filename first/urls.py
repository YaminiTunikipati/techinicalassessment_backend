from django.urls import path
from rest_framework import routers
from .views import RegisterUserAPIView, FileViewSet
from . import views

router = routers.DefaultRouter()
router.register('file', views.FileViewSet)

urlpatterns = [
    path('register', RegisterUserAPIView.as_view()),
    path('multiple_upload/', views.multiple_upload)
]
urlpatterns += router.urls