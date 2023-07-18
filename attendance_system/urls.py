from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("student/<str:seat_number>/", views.student, name="student"),
]
