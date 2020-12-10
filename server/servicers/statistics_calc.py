from server.proto.statistics_processing_pb2_grpc import StatisticsProcesser
from server.proto.statistics_processing_pb2 import ProcessDocumentReply

class Calculator(StatisticsProcesser):
    def ProcessDocument(self, request, context):
        return ProcessDocumentReply(summary=request.content)