from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import UserSerializer, UserLoginSerializer


class LoginView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    @extend_schema(request=UserLoginSerializer)
    def post(self, request, *args, **kwargs):
        """ Login with username/password """
        # check if user exists
        user = get_object_or_404(User, username=request.data['username'])

        # check if password valid
        if not user.check_password(request.data['password']):
            return Response({"error": "user not found"}, status=status.HTTP_404_NOT_FOUND)

        # return token
        token, created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(instance=user)
        return Response({"token": token.key, "user": serializer.data})


class SignupView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    @extend_schema(request=UserSerializer)
    def post(self, request, *args, **kwargs):
        """ Signup with email, username, and password """
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=request.data['username'])
            user.set_password(request.data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestTokenView(GenericAPIView):
    # these are the defaults:
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """ Verifies token is valid """
        return Response({"message": "Token is valid"})
