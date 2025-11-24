from rest_framework import serializers
from .models import *
class UserDetailsSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    email = serializers.EmailField()
    date_of_birth = serializers.DateField()

    class Meta:
        model=UserDetails
        fields="__all__"
