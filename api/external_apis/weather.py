from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.throttling import UserRateThrottle
import requests
from django.conf import settings
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes


class WeatherView(APIView):
    """
    Retrieve weather data based on latitude and longitude

    Uses One Call API from OpenWeatherMap
    """
    throttle_classes = [UserRateThrottle]
    permission_classes = [AllowAny]  # TODO remove

    @extend_schema(
        parameters=[
            OpenApiParameter(name='lat',
                             description='Latitude',
                             required=True,
                             type=OpenApiTypes.FLOAT),
            OpenApiParameter(name='lon',
                             description='Longitude',
                             required=True,
                             type=OpenApiTypes.FLOAT),
            OpenApiParameter(name='exclude',
                             description='Parts to exclude, comma seperated {current, minutely, hourly, daily, alerts}',
                             required=False,
                             type=OpenApiTypes.STR)
        ],
        responses={200: OpenApiTypes.OBJECT}
    )
    def get(self, request, *args, **kwargs):
        lat = request.query_params.get('lat')
        lon = request.query_params.get('lon')
        part = request.query_params.get('exclude', '')

        if not all([lat, lon]):
            return Response({'error': 'Missing required parameters: lat, lon'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            api_key = settings.WEATHER_API_KEY
            if not api_key:
                return Response({'error': 'API key not configured'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            url = f"{settings.WEATHER_API_URL}?appid={api_key}&lat={lat}&lon={lon}"

            if part:
                url += f"&exclude={part}"

            response = requests.get(url)
            response.raise_for_status()
            return Response(response.json())

        except requests.RequestException as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
