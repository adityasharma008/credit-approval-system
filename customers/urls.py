from django.urls import path
from .views import test_hello_world

urlpatterns = [
   path('test/', test_hello_world)
]
