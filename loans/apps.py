from django.apps import AppConfig
import os

class LoansConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'loans'

    def ready(self):
        if os.environ.get('RUN_MAIN', None) != 'true':
            return
        
        from loans.tasks import injest_loan_data
        from django.conf import settings

        file_path = os.path.join(settings.BASE_DIR, "data", "loan_data.xlsx")
        injest_loan_data.delay(file_path)
