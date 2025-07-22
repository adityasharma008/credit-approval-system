from rest_framework import serializers
from .models import Customer

class RegisterCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'first_name',
            'last_name',
            'age',
            'phone_number',
            'monthly_salary'
        ]
    
    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError("Customer must be 18 or older")
        return value
    
    def validate_phone_number(self, value):
        if value < 1000000000 or value > 9999999999:
            raise serializers.ValidationError("Enter a valid 10 digit phone number")
        if Customer.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("Phone number already in use")
        return value
    
    def validate_monthly_salary(self, value):
        if value < 0:
            raise serializers.ValidationError("Salary cannot be negative")
        return value
    
    def create(self, validated_data):
        monthly_salary = validated_data['monthly_salary']
        approved_limit = round(36 * monthly_salary, -5)
        
        return Customer.objects.create(
            approved_limit=approved_limit,
            **validated_data
        )