from customers.tasks import injest_customer_data

injest_customer_data.delay("/credit_approval_system/data/customer_data.xlsx")