from django.urls import path
from .views import *

urlpatterns = [
    path('sign-up', RegisterView, name="sign-up"),
    path('sign-in', LoginView, name="sign-in"),
    path('logout', LogoutView, name="logout"),
]