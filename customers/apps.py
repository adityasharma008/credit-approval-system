from django.apps import AppConfig
import os

class CustomersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customers'

    def ready(self):
        if os.environ.get('RUN_MAIN', None) != 'true':
            return
        
        from customers.tasks import injest_customer_data
        from django.conf import settings

        file_path = os.path.join(settings.BASE_DIR, "data", "customer_data.xlsx")
        injest_customer_data.delay(file_path)
