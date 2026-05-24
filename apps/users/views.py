from django.shortcuts import render
from rest_framework import viewsets
from .serializer import skillserializer,userprofileserializer,RegisterSerializer
from .models import Skill,Userprofile
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from .permissons import IsOwnerOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class UserViewset(viewsets.ModelViewSet):
    queryset = Userprofile.objects.all()
    serializer_class = userprofileserializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields = ['user__username']
    pagination_class = LimitOffsetPagination
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    
    def perform_create(self, serializer):
        if Userprofile.objects.filter(user=self.request.user).exists():
         raise ValidationError("Profile already exists")
        serializer.save(user=self.request.user)

class SkillViewset(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    queryset = Skill.objects.all()
    serializer_class = skillserializer
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticatedOrReadOnly()]

class RegisterViewset(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(
                {"message": "User created successfully."},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = []
    authentication_classes =[]

    