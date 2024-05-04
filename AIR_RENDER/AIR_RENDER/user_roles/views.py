from rest_framework import viewsets, status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import User, Role, UserRole
from .serializers import UserSerializer, RoleSerializer, UserRoleSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class UserRoleViewSet(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer

    @action(detail=True, methods=['put'])
    def disable_user(self, request, pk=None):
        user_role = self.get_object()
        user_role.status = 'disabled'
        user_role.save()
        return Response({"status": "User Disabled"})

