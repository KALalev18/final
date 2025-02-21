# Generated by the gRPC Python protocol compiler plugin.
import grpc
import warnings

import weather_pb2 as weather__pb2

GRPC_GENERATED_VERSION = '1.70.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in weather_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class WeatherServiceStub(object):
    """Service definition
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetWeather = channel.unary_unary(
                '/weather.WeatherService/GetWeather',
                request_serializer=weather__pb2.WeatherRequest.SerializeToString,
                response_deserializer=weather__pb2.WeatherResponse.FromString,
                _registered_method=True)


class WeatherServiceServicer(object):
    """Service definition
    """

    def GetWeather(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WeatherServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetWeather': grpc.unary_unary_rpc_method_handler(
                    servicer.GetWeather,
                    request_deserializer=weather__pb2.WeatherRequest.FromString,
                    response_serializer=weather__pb2.WeatherResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'weather.WeatherService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('weather.WeatherService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class WeatherService(object):
    """Service definition
    """

    @staticmethod
    def GetWeather(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/weather.WeatherService/GetWeather',
            weather__pb2.WeatherRequest.SerializeToString,
            weather__pb2.WeatherResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
