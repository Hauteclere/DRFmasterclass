from django.urls import path
from . import views

urlpatterns = [
    path('climbers/', views.ClimberList.as_view()),
]