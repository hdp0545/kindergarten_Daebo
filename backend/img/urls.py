from django.urls import path
from . import views


app_name = 'img'

urlpatterns = [
    path('', views.save_img, name='save_img'),
    
]
