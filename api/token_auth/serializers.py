from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        """ user info in auth responses """
        model = User
        fields = ['id', 'username', 'password', 'email']
