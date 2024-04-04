from django.http import HttpResponse
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny


message = '<h1>Welcome to moodtracker-api</h1>'
message += '<h3>see <a href="/docs">Swagger</a> for documentation</h3>'

@permission_classes([AllowAny])
def index_view(request):
    return HttpResponse(message)
