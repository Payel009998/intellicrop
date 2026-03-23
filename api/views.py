from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
def home(request):
    return Response({"message": "Intellicrop Backend Running 🚀"})
@api_view(['POST'])
def signup(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if User.objects.filter(username=username).exists():
        return Response({"error": "User already exists ❌"})

    user = User.objects.create_user(username=username, password=password)
    return Response({"message": "User created successfully ✅"})
@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user:
        return Response({"message": "Login successful ✅"})
    else:
        return Response({"error": "Invalid credentials ❌"})
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard(request):
    return Response({"message": "Welcome to dashboard 🔐"})