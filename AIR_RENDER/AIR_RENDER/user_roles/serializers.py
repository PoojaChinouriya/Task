from rest_framework import serializers
from .models import User, Role, UserRole
from django.conf import settings
from django.core.mail import send_mail

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'role', 'is_active']
        read_only_fields = ['id']


    def create(self, validated_data):

        send_mail(subject="Thats's Your username :",
                message="use this credential to login to our API....",
                from_email= settings.EMAIL_HOST_USER,
                recipient_list=[  validated_data.get( 'email' )  ]
              )
        print( '-----' )
        return User.objects.create_user(**validated_data)



class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = '__all__'


