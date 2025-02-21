import grpc
from concurrent import futures
import time
import random
import weather_pb2
import weather_pb2_grpc

weather_descriptions = [
    "Clear sky", "Partly cloudy", "Cloudy", "Overcast", 
    "Light rain", "Heavy rain", "Thunderstorm", "Snow", 
    "Fog", "Windy"
]

class WeatherService(weather_pb2_grpc.WeatherServiceServicer):
    def GetWeather(self, request, context):
        temperature = f"{random.randint(-10, 40)}°C"
        description = random.choice(weather_descriptions)
        
        return weather_pb2.WeatherResponse(temperature=temperature, description=description)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    weather_pb2_grpc.add_WeatherServiceServicer_to_server(WeatherService(), server)
    server.add_insecure_port('[::]:50051')
    print("Server is running on port 50051...")
    server.start()

    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
