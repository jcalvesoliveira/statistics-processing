import math
import toml
import numpy as np
from io import BytesIO
import grpc

from server.core.logger import module_logger
from server.proto.statistics_processing_pb2_grpc import StatisticsProcesser
from server.proto.statistics_processing_pb2 import ProcessDocumentReply

default_config = toml.load('server/server.toml')['statistics']


class Calculator(StatisticsProcesser):
    def __init__(self) -> None:
        self.logger = module_logger(__name__)

    def ProcessDocument(self, request, context):
        self.logger.info("Processing document...")
        process_config = {}
        results = ''
        try:
            for param in default_config:
                try:
                    req_param = getattr(request, param)
                    process_config[
                        param] = req_param if req_param else default_config[
                            param]
                except AttributeError:
                    process_config[param] = default_config[param]
                    pass

            document = np.genfromtxt(BytesIO(request.content),
                                     dtype=str,
                                     delimiter=process_config['delimiter'])
            header = list(document[0])
            document = np.delete(document, (0), axis=0)

            agg_cols_idx = []
            try:
                key_column_idx = header.index(process_config['key_column'])
                cols_to_exclude = process_config['cols_exclude'] + [
                    process_config['key_column']
                ]
                agg_cols_idx += [
                    header.index(col) for col in header
                    if col not in cols_to_exclude
                ]
            except ValueError as error:
                self.logger.error(repr(error))
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                context.set_details(str(error))
                return ProcessDocumentReply()
            if len(agg_cols_idx) > process_config['max_agg_cols']:
                msg = ("Number os columns to aggregate exceed!!"
                       f" Resizing from {len(agg_cols_idx)} to the first"
                       f" {process_config['max_agg_cols']}")
                self.logger.warning(msg)
                context.set_details(msg)
                agg_cols_idx = agg_cols_idx[0:process_config['max_agg_cols']]

            results += process_config['summary_header']
            line_idx = 0
            for idx in agg_cols_idx:
                unique_count = np.unique(document[:, idx]).shape[0]
                if (unique_count / document.shape[0]
                    ) <= process_config['max_unique_perc']:
                    companies_id = np.unique(document[:, key_column_idx])
                    for company_id in companies_id:
                        company_doc = document[document[:, key_column_idx] ==
                                               company_id]
                        categories, count = np.unique(company_doc[:, idx],
                                                      return_counts=True)
                        for cat_idx, cat in enumerate(categories):
                            results += f"{line_idx},{company_id},{header[idx]},{cat},{count[cat_idx]}\n"
                            line_idx += 1

            self.logger.info("Document processed.")
            self.logger.info(f"Returning {line_idx+1} summary lines.")
        except Exception as error:
            self.logger.error(repr(error))
            context.set_code(grpc.StatusCode.UNKNOWN)
            context.set_details(str(error))
            return ProcessDocumentReply()
        return ProcessDocumentReply(summary=results.encode())