from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.throttling import UserRateThrottle
import requests
from django.conf import settings
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes


class LocationView(APIView):
    """
    Retrieves latitude and longitude based on location info

    Uses Geocoding API from OpenWeatherMap
    """
    throttle_classes = [UserRateThrottle]
    permission_classes = [AllowAny]  # TODO remove

    @extend_schema(
        parameters=[
            OpenApiParameter(name='cityname',
                             description='City (e.g. San Diego)',
                             required=True,
                             type=OpenApiTypes.STR),
            OpenApiParameter(name='statecode',
                             description='State (e.g. CA)',
                             required=True,
                             type=OpenApiTypes.STR),
            OpenApiParameter(name='countrycode',
                             description='Country (e.g. USA)',
                             required=True,
                             type=OpenApiTypes.STR),
            OpenApiParameter(name='limit',
                             description='Limit number of locations returned (up to 5)',
                             required=False,
                             type=OpenApiTypes.STR)
        ],
        responses={200: OpenApiTypes.OBJECT}
    )
    def get(self, request, *args, **kwargs):
        cityname = request.query_params.get('cityname')
        statecode = request.query_params.get('statecode')
        countrycode = request.query_params.get('countrycode')
        limit = request.query_params.get('limit', '')

        if not all([cityname, statecode, countrycode]):
            return Response({'error': 'Missing required parameters: cityname, statecode, countrycode'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            api_key = settings.LOCATION_API_KEY
            if not api_key:
                return Response({'error': 'API key not configured'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            url = f"{settings.LOCATION_API_URL}?appid={api_key}&q={cityname},{statecode},{countrycode}"
            if limit:
                url += f"&limit={limit}"

            response = requests.get(url)
            response.raise_for_status()
            return Response(response.json())

        except requests.RequestException as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
