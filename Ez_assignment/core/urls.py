from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name="home"),
    path('download/<int:file_id>/', download_file, name='download_file'),
    path('download-file/<int:file_id>/', download_file_api, name='download_file_api'),
]