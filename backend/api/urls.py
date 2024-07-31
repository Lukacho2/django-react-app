from django.urls import path
from .views import index, my_profile

urlpatterns = [
    path('', index, name='home'),
    path('my_profile/<pk>', my_profile, name='my_profile'),
]