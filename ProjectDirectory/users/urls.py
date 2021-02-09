from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('my-profile/', views.UserDetail.as_view()),
    path('new-team/', views.AddTeam.as_view()),
]