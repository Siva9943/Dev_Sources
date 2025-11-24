from django.shortcuts import render,redirect
from rest_framework import status
from rest_framework.views import APIView
from .serializer import UserDetailsSerializer
from .models import UserDetails
from django.http import HttpResponse
# Create your views here.
  
def user_api_view(request):
    if request.method == "POST":
        serializer = UserDetailsSerializer(data=request.POST)
        if serializer.is_valid():
            UserDetails.objects.create(
                first_name=serializer.validated_data['username'],
                last_name=serializer.validated_data['last_name'],
                email=serializer.validated_data['email'],
                date_of_birth=serializer.validated_data['DOB'],
            )
            return redirect("user_details")
        else:
            return HttpResponse("Invalid data.", status=status.HTTP_400_BAD_REQUEST)
    return render(request, 'index.html')

