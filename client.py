from __future__ import print_function
import logging

import grpc

from server.protos.proto.statistics_processing_pb2_grpc import StatisticsProcesserStub
from server.protos.proto.statistics_processing_pb2 import ProcessDocumentRequest


def run():
    with open('server/test/test.csv', 'r') as file:
        document = file.read().encode()
    with grpc.insecure_channel('35.239.102.102:50050') as channel:
        stub = StatisticsProcesserStub(channel)
        response = stub.ProcessDocument(
            ProcessDocumentRequest(content=document))
    print(response.summary.decode())


if __name__ == '__main__':
    logging.basicConfig()
    run()
