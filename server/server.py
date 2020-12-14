import logging
import signal
import time

from concurrent import futures

import grpc
from grpc_health.v1 import health
from grpc_health.v1 import health_pb2_grpc
from py_grpc_prometheus.prometheus_server_interceptor import PromServerInterceptor

from server.core.logger import module_logger
from server.servicers.statistics_calc import Calculator
from server.protos.proto.statistics_processing_pb2_grpc import add_StatisticsProcesserServicer_to_server

GRPC_MAX_WORKERS = 10
GRPC_INSECURE_PORT = 50050
GRPC_SECURE_PORT = 50051

logger = module_logger(__name__)


class Server(object):
    def __init__(self):
        self._create_server()
        self._add_servicers()

    def _create_server(self):
        logger.info("Creating server")
        logger.debug("ThreadPoolExecutor.max_workers = %s", GRPC_MAX_WORKERS)
        self.server = grpc.server(
            futures.ThreadPoolExecutor(max_workers=GRPC_MAX_WORKERS),
            interceptors=(PromServerInterceptor(), ))

    def _add_servicers(self):
        logger.info("Adding servicers")
        logger.debug("Adding HealthServicer")
        health_servicer = health.HealthServicer()
        health_pb2_grpc.add_HealthServicer_to_server(health_servicer,
                                                     self.server)
        logger.debug("Adding StatisticsServicer")
        add_StatisticsProcesserServicer_to_server(Calculator(), self.server)

    def setup_insecure_server(self):
        logger.info("Setting up an insecure server.")
        self.server.add_insecure_port(
            "[::]:{insecure_port}".format(insecure_port=GRPC_INSECURE_PORT))
        logger.info("Listening on [::]:%s (insecure)", GRPC_INSECURE_PORT)

    def serve(self):
        logger.info("Starting server")
        self.server.start()
        try:
            logger.info("Server ready!!!")
            while True:
                time.sleep(86400)
        except KeyboardInterrupt:
            logger.warn("Gracefully stopping server")
            logging.shutdown()
            self.server.stop(0)


def handle_sigterm(*args):
    logger.warn("SIGTERM issued")
    raise KeyboardInterrupt()


signal.signal(signal.SIGTERM, handle_sigterm)
