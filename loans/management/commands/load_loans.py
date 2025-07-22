from django.core.management.base import BaseCommand
from loans.tasks import injest_loan_data
import os

class Command(BaseCommand):
    def handle(self, *args, **kwargs): 
        file_path = os.path.join('data', 'loan_data.xlsx')
        injest_loan_data.delay(file_path)
        