from django.urls import path
from .views import check_eligibility

urlpatterns = [
   path('check-eligibility/', check_eligibility)
]
