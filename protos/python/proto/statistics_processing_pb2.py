# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/statistics_processing.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/statistics_processing.proto',
  package='statisticsprocessing',
  syntax='proto3',
  serialized_options=b'ZKgithub.com/jcalvesoliveira/statistics-processing/blob/grpc-api/protos/proto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!proto/statistics_processing.proto\x12\x14statisticsprocessing\"\xb5\x01\n\x16ProcessDocumentRequest\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\x0c\x12\x32\n\x0c\x63ols_exclude\x18\x02 \x03(\x0b\x32\x1c.statisticsprocessing.Column\x12\x17\n\x0fmax_unique_perc\x18\x03 \x01(\x02\x12\x11\n\tdelimiter\x18\x04 \x01(\t\x12\x16\n\x0esummary_header\x18\x05 \x01(\t\x12\x12\n\nkey_column\x18\x06 \x01(\t\"\x16\n\x06\x43olumn\x12\x0c\n\x04name\x18\x01 \x01(\t\"\'\n\x14ProcessDocumentReply\x12\x0f\n\x07summary\x18\x01 \x01(\x0c\x32\x84\x01\n\x13StatisticsProcesser\x12m\n\x0fProcessDocument\x12,.statisticsprocessing.ProcessDocumentRequest\x1a*.statisticsprocessing.ProcessDocumentReply\"\x00\x42MZKgithub.com/jcalvesoliveira/statistics-processing/blob/grpc-api/protos/protob\x06proto3'
)




_PROCESSDOCUMENTREQUEST = _descriptor.Descriptor(
  name='ProcessDocumentRequest',
  full_name='statisticsprocessing.ProcessDocumentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='statisticsprocessing.ProcessDocumentRequest.content', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cols_exclude', full_name='statisticsprocessing.ProcessDocumentRequest.cols_exclude', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_unique_perc', full_name='statisticsprocessing.ProcessDocumentRequest.max_unique_perc', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delimiter', full_name='statisticsprocessing.ProcessDocumentRequest.delimiter', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='summary_header', full_name='statisticsprocessing.ProcessDocumentRequest.summary_header', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='key_column', full_name='statisticsprocessing.ProcessDocumentRequest.key_column', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=241,
)


_COLUMN = _descriptor.Descriptor(
  name='Column',
  full_name='statisticsprocessing.Column',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='statisticsprocessing.Column.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=243,
  serialized_end=265,
)


_PROCESSDOCUMENTREPLY = _descriptor.Descriptor(
  name='ProcessDocumentReply',
  full_name='statisticsprocessing.ProcessDocumentReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='summary', full_name='statisticsprocessing.ProcessDocumentReply.summary', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=267,
  serialized_end=306,
)

_PROCESSDOCUMENTREQUEST.fields_by_name['cols_exclude'].message_type = _COLUMN
DESCRIPTOR.message_types_by_name['ProcessDocumentRequest'] = _PROCESSDOCUMENTREQUEST
DESCRIPTOR.message_types_by_name['Column'] = _COLUMN
DESCRIPTOR.message_types_by_name['ProcessDocumentReply'] = _PROCESSDOCUMENTREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProcessDocumentRequest = _reflection.GeneratedProtocolMessageType('ProcessDocumentRequest', (_message.Message,), {
  'DESCRIPTOR' : _PROCESSDOCUMENTREQUEST,
  '__module__' : 'proto.statistics_processing_pb2'
  # @@protoc_insertion_point(class_scope:statisticsprocessing.ProcessDocumentRequest)
  })
_sym_db.RegisterMessage(ProcessDocumentRequest)

Column = _reflection.GeneratedProtocolMessageType('Column', (_message.Message,), {
  'DESCRIPTOR' : _COLUMN,
  '__module__' : 'proto.statistics_processing_pb2'
  # @@protoc_insertion_point(class_scope:statisticsprocessing.Column)
  })
_sym_db.RegisterMessage(Column)

ProcessDocumentReply = _reflection.GeneratedProtocolMessageType('ProcessDocumentReply', (_message.Message,), {
  'DESCRIPTOR' : _PROCESSDOCUMENTREPLY,
  '__module__' : 'proto.statistics_processing_pb2'
  # @@protoc_insertion_point(class_scope:statisticsprocessing.ProcessDocumentReply)
  })
_sym_db.RegisterMessage(ProcessDocumentReply)


DESCRIPTOR._options = None

_STATISTICSPROCESSER = _descriptor.ServiceDescriptor(
  name='StatisticsProcesser',
  full_name='statisticsprocessing.StatisticsProcesser',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=309,
  serialized_end=441,
  methods=[
  _descriptor.MethodDescriptor(
    name='ProcessDocument',
    full_name='statisticsprocessing.StatisticsProcesser.ProcessDocument',
    index=0,
    containing_service=None,
    input_type=_PROCESSDOCUMENTREQUEST,
    output_type=_PROCESSDOCUMENTREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STATISTICSPROCESSER)

DESCRIPTOR.services_by_name['StatisticsProcesser'] = _STATISTICSPROCESSER

# @@protoc_insertion_point(module_scope)
