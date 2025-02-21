import grpc
import weather_pb2
import weather_pb2_grpc

def get_weather(city_name):
    channel = grpc.insecure_channel('127.0.0.1:50051')
    stub = weather_pb2_grpc.WeatherServiceStub(channel)
    
    weather_request = weather_pb2.WeatherRequest(city=city_name)
    
    try:
        response = stub.GetWeather(weather_request)
        print(f"Weather in {city_name}: {response.temperature}, {response.description}")
    except grpc.RpcError as e:
        print(f"RPC failed: {e.code()} - {e.details()}")

if __name__ == '__main__':
    city_name = input("Enter city name: ")
    get_weather(city_name)
