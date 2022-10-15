from django.urls import path
from . import views



urlpatterns = [
    path("", views.exampl_view),
]