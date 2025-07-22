from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RegisterCustomerSerializer
from rest_framework import status

@api_view(['POST'])
def register_customer(request):
   serializer = RegisterCustomerSerializer(data = request.data)

   if serializer.is_valid(raise_exception=True):
      customer = serializer.save()
      full_name = f'{customer.first_name} {customer.last_name}'

      return Response({
         'customer_id': customer.customer_id,
         'name': full_name,
         'age': customer.age,
         'monthly_income': customer.monthly_salary,
         'approved_limit': customer.approved_limit,
         'phone_number': customer.phone_number
      }, status=status.HTTP_201_CREATED)
   
   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)