from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import UserSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
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


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    """ Create a new user """
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        # save new user
        serializer.save()

        # hash password
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()

        # create token for user
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)

    # invalid data or user already exists
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def test_token(request):
    """ Test token is valid """
    return Response('pass')
