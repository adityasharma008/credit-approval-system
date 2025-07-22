from django.db import connection

def reset_pk(model_class):
    with connection.cursor() as cursor:
        pk_name = model_class._meta.pk.column
        table_name = model_class._meta.db_table

        cursor.execute(f"SELECT MAX({pk_name}) FROM {table_name};")
        max_id = cursor.fetchone()[0]

        # Postgre seq name convention
        sequence_name = f"{table_name}_{pk_name}_seq"

        cursor.execute(f"SELECT setval('{sequence_name}', {max_id + 1});")
