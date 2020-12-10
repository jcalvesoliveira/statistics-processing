# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from proto import system_info_pb2 as proto_dot_system__info__pb2


class SystemInfoStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SystemInfo = channel.unary_unary(
                '/SystemInfo/SystemInfo',
                request_serializer=proto_dot_system__info__pb2.SystemInfoRequest.SerializeToString,
                response_deserializer=proto_dot_system__info__pb2.SystemInfoResponse.FromString,
                )


class SystemInfoServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SystemInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SystemInfoServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SystemInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.SystemInfo,
                    request_deserializer=proto_dot_system__info__pb2.SystemInfoRequest.FromString,
                    response_serializer=proto_dot_system__info__pb2.SystemInfoResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SystemInfo', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SystemInfo(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SystemInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SystemInfo/SystemInfo',
            proto_dot_system__info__pb2.SystemInfoRequest.SerializeToString,
            proto_dot_system__info__pb2.SystemInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
