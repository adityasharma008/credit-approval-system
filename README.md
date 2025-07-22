# Credit Approval System API

- This project implements REST APIs for a credit approval system, allowing for customer registration, loan eligibility checks, loan creation, and detailed loan/customer information retrieval. The entire application is containerized using Docker Compose for quick setup and deployment.

# Technologies Used
- Backend: Django REST Framework (Python)
- Database: PostgreSQL
- Asynchronous Tasks: Celery with Redis (for data ingestion)
- Containerization: Docker & Docker Compose

# Getting Started
- Make sure you have docker installed on your system

## Setup Steps
1. Clone the Repository:
```
git clone https://github.com/adityasharma008/credit-approval-system.git
cd credit-approval-system
```

2. Build and Run Services:
```
docker-compose up --build -d
```

This command will build the Docker images, start the PostgreSQL, Redis, Django (web), and Celery worker services.

# Accessing the API
The API will be available at http://localhost:8000/.

## Endpoints

- `POST api/customers/register`

    - Description: Registers a new customer
    - Request body example:
    ```
    {
        "first_name": "Aditya",
        "last_name": "Sharma",
        "age": 21,
        "monthly_salary": 50000,
        "phone_number": 9876543210
    }
    ```
    - Response body example:
    ```
    {
        "customer_id": 304,
        "name": "Aditya Sharma",
        "age": 21,
        "monthly_income": 50000,
        "approved_limit": 1800000,
        "phone_number": 9876543210
    }
    ```

- `POST /api/loans/check-eligibility`
    - Description: Checks loan eligibility for a customer.
    - Request Body Example:
    - **Case 1: Customer ineligible**
    ```
    {
        "customer_id": 304,
        "loan_amount": 500000,
        "interest_rate": 10.5,
        "tenure": 12
    }
    ```
    - Response body:
    ```
    {
        "customer_id": 304,
        "approval": false,
        "interest_rate": 10.5,
        "corrected_interest_rate": null,
        "tenure": 12,
        "monthly_installment": null
    }
    ```

    - **Case 2: Customer eligible with corrected interest rate**
    ```
    {
        "customer_id": 304,
        "loan_amount": 500000,
        "interest_rate": 10.5,
        "tenure": 24
    }
    ```
    - Response body:
    ```
    {
        "customer_id": 304,
        "approval": false,
        "interest_rate": 10.5,
        "corrected_interest_rate": 12,
        "tenure": 24,
        "monthly_installment": 23536.74
    }
    ```

    - **Case 3: Customer eligible**
    ```
    {
        "customer_id": 304,
        "loan_amount": 500000,
        "interest_rate": 12,
        "tenure": 24
    }
    ```
    - Response body:
    ```
    {
        "customer_id": 304,
        "approval": false,
        "interest_rate": 10.5,
        "corrected_interest_rate": 12,
        "tenure": 24,
        "monthly_installment": 23536.74
    }
    ```

- `POST /api/loans/create-loan`
    - Description: Creates a new loan if the customer is eligible.
    - Request Body Example: (Same as /check-eligibility)
    - **Response Body Example (Rejected):**
    ```
    {
        "loan_id": null,
        "customer_id": 304,
        "loan_approved": false,
        "message": "Loan denied: EMI burden exceeds 50% of monthly salary",
        "monthly_installment": null
    }
    ```
    - **Response Body Example (Approved):**
    ```
    {
        "loan_id": 9979,
        "customer_id": 304,
        "loan_approved": true,
        "message": "Loan approved successfully",
        "monthly_installment": 23536.74
    }
    ```

- `GET /api/loans/view-loan/<int:loan_id>`
    - Description: Retrieves details for a specific loan.
    - Example URL: `/api/loans/view-loan/9979`
    - Response Body Example:
    ```
    {
        "loan_id": 9979,
        "customer_id": 304,
        "customer_first_name": "Aditya",
        "customer_last_name": "Sharma",
        "customer_phone_number": "9876543210",
        "customer_age": 21,
        "loan_amount": "500000.00",
        "interest_rate": "12.00",
        "monthly_installment": "23536.74",
        "tenure": 24
    }
    ```

- `GET /api/view-loans/<int:customer_id>`

    - Description: Retrieves a list of all loans for a specific customer.
    - Example URL: `/api/loans/view-loans/304`
    - Response Body Example:
    ```
    [
        {
            "loan_id": 9979,
            "customer_id": 304,
            "customer_first_name": "Aditya",
            "customer_last_name": "Sharma",
            "customer_phone_number": "9876543210",
            "customer_age": 21,
            "loan_amount": "500000.00",
            "interest_rate": "12.00",
            "monthly_installment": "23536.74",
            "tenure": 24
        }
    ]
    ```