import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class WeatherData(APIView):
    def get(self, request):
        city = request.query_params.get('city', None)
        try:
            url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
            weather_data = requests.get(url.format(city)).json()
            return Response(weather_data)
        except:
            return Response({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)


    def post(self, request):
        city = request.data.get('city', None)
        try:
            url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
            weather_data = requests.get(url.format(city)).json()
            return Response(weather_data)
        except:
            return Response({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
