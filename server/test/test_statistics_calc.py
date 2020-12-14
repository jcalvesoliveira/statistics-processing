import sys
import unittest

import toml
import grpc
import grpc_testing

from server.protos.proto.statistics_processing_pb2 import DESCRIPTOR, ProcessDocumentRequest
from server.servicers.statistics_calc import Calculator


class TestStatisticsProcessing(unittest.TestCase):
    def setUp(self):
        servicers = {
            DESCRIPTOR.services_by_name['StatisticsProcesser']: Calculator()
        }
        self.test_server = grpc_testing.server_from_dictionary(
            servicers, grpc_testing.strict_real_time())
        self.default_config = toml.load('server/server.toml')['statistics']
        with open('server/test/test.csv', 'r') as file:
            self.document = file.read().encode()
        with open('server/test/result.csv', 'r') as file:
            self.result = self.default_config['summary_header'] + file.read()
            self.result = self.result.encode()
        with open('server/test/result_full.csv', 'r') as file:
            self.result_full = self.default_config[
                'summary_header'] + file.read()
            self.result_full = self.result_full.encode()

    def process_document_method(self, request):
        return self.test_server.invoke_unary_unary(method_descriptor=(
            DESCRIPTOR.services_by_name['StatisticsProcesser'].
            methods_by_name['ProcessDocument']),
                                                   invocation_metadata={},
                                                   request=request,
                                                   timeout=1)

    def test_statistics_calc_document(self):
        """ Expect to get same result after processing document as result.csv """
        request = ProcessDocumentRequest(content=self.document)
        process_document_method = self.process_document_method(request)
        response, mtdata, code, dtls = process_document_method.termination()
        self.assertEqual(response.summary, self.result)
        self.assertEqual(code, grpc.StatusCode.OK)

    def test_statistics_calc_delimiter(self):
        """ Expect to get same result after processing document as result.csv
            but using  '|' as delimiter.
        """
        document_delimiter = self.document.decode().replace(',', '|')
        request = ProcessDocumentRequest(content=document_delimiter.encode(),
                                         input_delimiter='|')
        process_document_method = self.process_document_method(request)
        response, mtdata, code, dtls = process_document_method.termination()
        self.assertEqual(response.summary, self.result)
        self.assertEqual(code, grpc.StatusCode.OK)

    def test_statistics_calc_invalid_col_key(self):
        """ Expect to get invalid argument for a invalid column key """
        request = ProcessDocumentRequest(content=self.document,
                                         key_column='column_invalid')
        process_document_method = self.process_document_method(request)
        response, mtdata, code, dtls = process_document_method.termination()
        self.assertEqual(response.summary, b'')
        self.assertEqual(code, grpc.StatusCode.INVALID_ARGUMENT)

    def test_statistics_calc_cols_exclude(self):
        """ Expect to get the first 42 lines from result.csv """
        request = ProcessDocumentRequest(
            content=self.document,
            cols_exclude=['AccountNumber', 'AccountTypeName'])
        process_document_method = self.process_document_method(request)
        response, mtdata, code, dtls = process_document_method.termination()
        self.assertEqual(response.summary, self.result[0:1822])
        self.assertEqual(code, grpc.StatusCode.OK)

    def test_statistics_calc_max_unique_perc_negative(self):
        """ Expect to get 0 summary lines once max_unique_perc = -1 """
        request = ProcessDocumentRequest(content=self.document,
                                         max_unique_perc=-1)
        process_document_method = self.process_document_method(request)
        response, mtdata, code, dtls = process_document_method.termination()
        self.assertEqual(response.summary,
                         self.default_config['summary_header'].encode())
        self.assertEqual(code, grpc.StatusCode.OK)

    def test_statistics_calc_max_unique_perc_one(self):
        """ Expect to get all collumns summarized once max_unique_perc = 1 """
        request = ProcessDocumentRequest(content=self.document,
                                         max_unique_perc=1)
        process_document_method = self.process_document_method(request)
        response, mtdata, code, dtls = process_document_method.termination()
        self.assertEqual(response.summary, self.result_full)
        self.assertEqual(code, grpc.StatusCode.OK)

    def test_statistics_calc_header(self):
        """ Expect to get same result after processing document as result.csv """
        new_header = 'Test\n'
        request = ProcessDocumentRequest(content=self.document,
                                         summary_header=new_header)
        process_document_method = self.process_document_method(request)
        response, mtdata, code, dtls = process_document_method.termination()
        result = self.result.decode().replace(
            self.default_config['summary_header'], new_header)
        self.assertEqual(response.summary, result.encode())
        self.assertEqual(code, grpc.StatusCode.OK)


if __name__ == '__main__':
    test_statistics_calc = unittest.TestSuite()
    test_statistics_calc.addTest(unittest.makeSuite(TestStatisticsProcessing))
    result_tests = unittest.TextTestRunner().run(test_statistics_calc)
    if not result_tests.wasSuccessful():
        sys.exit(1)