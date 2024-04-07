from django.http import HttpResponse
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

message = '<h1>Welcome to moodtracker-api</h1>'
message += '<h4>see <a href="/docs">/docs</a> for Swagger documentation</h4>'
message += '<h4>see <a href="/admin">/admin</a> for Django admin site</h4>'


@permission_classes([AllowAny])
def index_view(request):
    return HttpResponse(message)
