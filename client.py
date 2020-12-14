from __future__ import print_function
import logging

import grpc

from server.protos.proto.statistics_processing_pb2_grpc import StatisticsProcesserStub
from server.protos.proto.statistics_processing_pb2 import ProcessDocumentRequest


def run():
    with grpc.insecure_channel('localhost:50050') as channel:
        stub = StatisticsProcesserStub(channel)
        response = stub.ProcessDocument(
            ProcessDocumentRequest(content=b'Test'))
    print(f"Client received: {response.summary.decode()}")


if __name__ == '__main__':
    logging.basicConfig()
    run()
