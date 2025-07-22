from django.urls import path
from .views import check_eligibility, create_loan

urlpatterns = [
   path('check-eligibility/', check_eligibility),
   path('create-loan/', create_loan)
]
