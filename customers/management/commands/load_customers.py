from django.core.management.base import BaseCommand
from customers.tasks import injest_customer_data
import os

class Command(BaseCommand):
    def handle(self, *args, **kwargs): 
        file_path = os.path.join('data', 'customer_data.xlsx')
        injest_customer_data.delay(file_path)
