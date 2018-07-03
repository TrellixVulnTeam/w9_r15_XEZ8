# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_detection/protos/input_reader.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='object_detection/protos/input_reader.proto',
  package='object_detection.protos',
  syntax='proto2',
  options=None,
  serialized_pb=_b('\n*object_detection/protos/input_reader.proto\x12\x17object_detection.protos\"\xff\x02\n\x0bInputReader\x12\x18\n\x0elabel_map_path\x18\x01 \x01(\t:\x00\x12\x15\n\x07shuffle\x18\x02 \x01(\x08:\x04true\x12\x1c\n\x0equeue_capacity\x18\x03 \x01(\r:\x04\x32\x30\x30\x30\x12\x1f\n\x11min_after_dequeue\x18\x04 \x01(\r:\x04\x31\x30\x30\x30\x12\x15\n\nnum_epochs\x18\x05 \x01(\r:\x01\x30\x12\x16\n\x0bnum_readers\x18\x06 \x01(\r:\x01\x38\x12\"\n\x13load_instance_masks\x18\x07 \x01(\x08:\x05\x66\x61lse\x12N\n\x16tf_record_input_reader\x18\x08 \x01(\x0b\x32,.object_detection.protos.TFRecordInputReaderH\x00\x12M\n\x15\x65xternal_input_reader\x18\t \x01(\x0b\x32,.object_detection.protos.ExternalInputReaderH\x00\x42\x0e\n\x0cinput_reader\")\n\x13TFRecordInputReader\x12\x12\n\ninput_path\x18\x01 \x03(\t\"\x1c\n\x13\x45xternalInputReader*\x05\x08\x01\x10\xe8\x07')
)




_INPUTREADER = _descriptor.Descriptor(
  name='InputReader',
  full_name='object_detection.protos.InputReader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label_map_path', full_name='object_detection.protos.InputReader.label_map_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shuffle', full_name='object_detection.protos.InputReader.shuffle', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='queue_capacity', full_name='object_detection.protos.InputReader.queue_capacity', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=2000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_after_dequeue', full_name='object_detection.protos.InputReader.min_after_dequeue', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=1000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_epochs', full_name='object_detection.protos.InputReader.num_epochs', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_readers', full_name='object_detection.protos.InputReader.num_readers', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=8,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='load_instance_masks', full_name='object_detection.protos.InputReader.load_instance_masks', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tf_record_input_reader', full_name='object_detection.protos.InputReader.tf_record_input_reader', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='external_input_reader', full_name='object_detection.protos.InputReader.external_input_reader', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='input_reader', full_name='object_detection.protos.InputReader.input_reader',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=72,
  serialized_end=455,
)


_TFRECORDINPUTREADER = _descriptor.Descriptor(
  name='TFRecordInputReader',
  full_name='object_detection.protos.TFRecordInputReader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='input_path', full_name='object_detection.protos.TFRecordInputReader.input_path', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=457,
  serialized_end=498,
)


_EXTERNALINPUTREADER = _descriptor.Descriptor(
  name='ExternalInputReader',
  full_name='object_detection.protos.ExternalInputReader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(1, 1000), ],
  oneofs=[
  ],
  serialized_start=500,
  serialized_end=528,
)

_INPUTREADER.fields_by_name['tf_record_input_reader'].message_type = _TFRECORDINPUTREADER
_INPUTREADER.fields_by_name['external_input_reader'].message_type = _EXTERNALINPUTREADER
_INPUTREADER.oneofs_by_name['input_reader'].fields.append(
  _INPUTREADER.fields_by_name['tf_record_input_reader'])
_INPUTREADER.fields_by_name['tf_record_input_reader'].containing_oneof = _INPUTREADER.oneofs_by_name['input_reader']
_INPUTREADER.oneofs_by_name['input_reader'].fields.append(
  _INPUTREADER.fields_by_name['external_input_reader'])
_INPUTREADER.fields_by_name['external_input_reader'].containing_oneof = _INPUTREADER.oneofs_by_name['input_reader']
DESCRIPTOR.message_types_by_name['InputReader'] = _INPUTREADER
DESCRIPTOR.message_types_by_name['TFRecordInputReader'] = _TFRECORDINPUTREADER
DESCRIPTOR.message_types_by_name['ExternalInputReader'] = _EXTERNALINPUTREADER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InputReader = _reflection.GeneratedProtocolMessageType('InputReader', (_message.Message,), dict(
  DESCRIPTOR = _INPUTREADER,
  __module__ = 'object_detection.protos.input_reader_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.InputReader)
  ))
_sym_db.RegisterMessage(InputReader)

TFRecordInputReader = _reflection.GeneratedProtocolMessageType('TFRecordInputReader', (_message.Message,), dict(
  DESCRIPTOR = _TFRECORDINPUTREADER,
  __module__ = 'object_detection.protos.input_reader_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.TFRecordInputReader)
  ))
_sym_db.RegisterMessage(TFRecordInputReader)

ExternalInputReader = _reflection.GeneratedProtocolMessageType('ExternalInputReader', (_message.Message,), dict(
  DESCRIPTOR = _EXTERNALINPUTREADER,
  __module__ = 'object_detection.protos.input_reader_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.ExternalInputReader)
  ))
_sym_db.RegisterMessage(ExternalInputReader)


# @@protoc_insertion_point(module_scope)
