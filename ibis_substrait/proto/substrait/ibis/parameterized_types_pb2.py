"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...substrait.ibis import type_pb2 as substrait_dot_ibis_dot_type__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(substrait/ibis/parameterized_types.proto\x12\x0esubstrait.ibis\x1a\x19substrait/ibis/type.proto"\x8d \n\x11ParameterizedType\x122\n\x04bool\x18\x01 \x01(\x0b2\x1c.substrait.ibis.Type.BooleanH\x00R\x04bool\x12)\n\x02i8\x18\x02 \x01(\x0b2\x17.substrait.ibis.Type.I8H\x00R\x02i8\x12,\n\x03i16\x18\x03 \x01(\x0b2\x18.substrait.ibis.Type.I16H\x00R\x03i16\x12,\n\x03i32\x18\x05 \x01(\x0b2\x18.substrait.ibis.Type.I32H\x00R\x03i32\x12,\n\x03i64\x18\x07 \x01(\x0b2\x18.substrait.ibis.Type.I64H\x00R\x03i64\x12/\n\x04fp32\x18\n \x01(\x0b2\x19.substrait.ibis.Type.FP32H\x00R\x04fp32\x12/\n\x04fp64\x18\x0b \x01(\x0b2\x19.substrait.ibis.Type.FP64H\x00R\x04fp64\x125\n\x06string\x18\x0c \x01(\x0b2\x1b.substrait.ibis.Type.StringH\x00R\x06string\x125\n\x06binary\x18\r \x01(\x0b2\x1b.substrait.ibis.Type.BinaryH\x00R\x06binary\x12>\n\ttimestamp\x18\x0e \x01(\x0b2\x1e.substrait.ibis.Type.TimestampH\x00R\ttimestamp\x12/\n\x04date\x18\x10 \x01(\x0b2\x19.substrait.ibis.Type.DateH\x00R\x04date\x12/\n\x04time\x18\x11 \x01(\x0b2\x19.substrait.ibis.Type.TimeH\x00R\x04time\x12H\n\rinterval_year\x18\x13 \x01(\x0b2!.substrait.ibis.Type.IntervalYearH\x00R\x0cintervalYear\x12E\n\x0cinterval_day\x18\x14 \x01(\x0b2 .substrait.ibis.Type.IntervalDayH\x00R\x0bintervalDay\x12E\n\x0ctimestamp_tz\x18\x1d \x01(\x0b2 .substrait.ibis.Type.TimestampTZH\x00R\x0btimestampTz\x12/\n\x04uuid\x18  \x01(\x0b2\x19.substrait.ibis.Type.UUIDH\x00R\x04uuid\x12Y\n\nfixed_char\x18\x15 \x01(\x0b28.substrait.ibis.ParameterizedType.ParameterizedFixedCharH\x00R\tfixedChar\x12R\n\x07varchar\x18\x16 \x01(\x0b26.substrait.ibis.ParameterizedType.ParameterizedVarCharH\x00R\x07varchar\x12_\n\x0cfixed_binary\x18\x17 \x01(\x0b2:.substrait.ibis.ParameterizedType.ParameterizedFixedBinaryH\x00R\x0bfixedBinary\x12R\n\x07decimal\x18\x18 \x01(\x0b26.substrait.ibis.ParameterizedType.ParameterizedDecimalH\x00R\x07decimal\x12O\n\x06struct\x18\x19 \x01(\x0b25.substrait.ibis.ParameterizedType.ParameterizedStructH\x00R\x06struct\x12I\n\x04list\x18\x1b \x01(\x0b23.substrait.ibis.ParameterizedType.ParameterizedListH\x00R\x04list\x12F\n\x03map\x18\x1c \x01(\x0b22.substrait.ibis.ParameterizedType.ParameterizedMapH\x00R\x03map\x12_\n\x0cuser_defined\x18\x1e \x01(\x0b2:.substrait.ibis.ParameterizedType.ParameterizedUserDefinedH\x00R\x0buserDefined\x126\n\x14user_defined_pointer\x18\x1f \x01(\rB\x02\x18\x01H\x00R\x12userDefinedPointer\x12X\n\x0etype_parameter\x18! \x01(\x0b2/.substrait.ibis.ParameterizedType.TypeParameterH\x00R\rtypeParameter\x1a^\n\rTypeParameter\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x129\n\x06bounds\x18\x02 \x03(\x0b2!.substrait.ibis.ParameterizedTypeR\x06bounds\x1a\xf0\x01\n\x10IntegerParameter\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12e\n\x15range_start_inclusive\x18\x02 \x01(\x0b21.substrait.ibis.ParameterizedType.NullableIntegerR\x13rangeStartInclusive\x12a\n\x13range_end_exclusive\x18\x03 \x01(\x0b21.substrait.ibis.ParameterizedType.NullableIntegerR\x11rangeEndExclusive\x1a\'\n\x0fNullableInteger\x12\x14\n\x05value\x18\x01 \x01(\x03R\x05value\x1a\xd2\x01\n\x16ParameterizedFixedChar\x12G\n\x06length\x18\x01 \x01(\x0b2/.substrait.ibis.ParameterizedType.IntegerOptionR\x06length\x12+\n\x11variation_pointer\x18\x02 \x01(\rR\x10variationPointer\x12B\n\x0bnullability\x18\x03 \x01(\x0e2 .substrait.ibis.Type.NullabilityR\x0bnullability\x1a\xd0\x01\n\x14ParameterizedVarChar\x12G\n\x06length\x18\x01 \x01(\x0b2/.substrait.ibis.ParameterizedType.IntegerOptionR\x06length\x12+\n\x11variation_pointer\x18\x02 \x01(\rR\x10variationPointer\x12B\n\x0bnullability\x18\x03 \x01(\x0e2 .substrait.ibis.Type.NullabilityR\x0bnullability\x1a\xd4\x01\n\x18ParameterizedFixedBinary\x12G\n\x06length\x18\x01 \x01(\x0b2/.substrait.ibis.ParameterizedType.IntegerOptionR\x06length\x12+\n\x11variation_pointer\x18\x02 \x01(\rR\x10variationPointer\x12B\n\x0bnullability\x18\x03 \x01(\x0e2 .substrait.ibis.Type.NullabilityR\x0bnullability\x1a\x9d\x02\n\x14ParameterizedDecimal\x12E\n\x05scale\x18\x01 \x01(\x0b2/.substrait.ibis.ParameterizedType.IntegerOptionR\x05scale\x12M\n\tprecision\x18\x02 \x01(\x0b2/.substrait.ibis.ParameterizedType.IntegerOptionR\tprecision\x12+\n\x11variation_pointer\x18\x03 \x01(\rR\x10variationPointer\x12B\n\x0bnullability\x18\x04 \x01(\x0e2 .substrait.ibis.Type.NullabilityR\x0bnullability\x1a\xbf\x01\n\x13ParameterizedStruct\x127\n\x05types\x18\x01 \x03(\x0b2!.substrait.ibis.ParameterizedTypeR\x05types\x12+\n\x11variation_pointer\x18\x02 \x01(\rR\x10variationPointer\x12B\n\x0bnullability\x18\x03 \x01(\x0e2 .substrait.ibis.Type.NullabilityR\x0bnullability\x1a\x7f\n\x18ParameterizedNamedStruct\x12\x14\n\x05names\x18\x01 \x03(\tR\x05names\x12M\n\x06struct\x18\x02 \x01(\x0b25.substrait.ibis.ParameterizedType.ParameterizedStructR\x06struct\x1a\xbb\x01\n\x11ParameterizedList\x125\n\x04type\x18\x01 \x01(\x0b2!.substrait.ibis.ParameterizedTypeR\x04type\x12+\n\x11variation_pointer\x18\x02 \x01(\rR\x10variationPointer\x12B\n\x0bnullability\x18\x03 \x01(\x0e2 .substrait.ibis.Type.NullabilityR\x0bnullability\x1a\xf1\x01\n\x10ParameterizedMap\x123\n\x03key\x18\x01 \x01(\x0b2!.substrait.ibis.ParameterizedTypeR\x03key\x127\n\x05value\x18\x02 \x01(\x0b2!.substrait.ibis.ParameterizedTypeR\x05value\x12+\n\x11variation_pointer\x18\x03 \x01(\rR\x10variationPointer\x12B\n\x0bnullability\x18\x04 \x01(\x0e2 .substrait.ibis.Type.NullabilityR\x0bnullability\x1a\xae\x01\n\x18ParameterizedUserDefined\x12!\n\x0ctype_pointer\x18\x01 \x01(\rR\x0btypePointer\x12+\n\x11variation_pointer\x18\x02 \x01(\rR\x10variationPointer\x12B\n\x0bnullability\x18\x03 \x01(\x0e2 .substrait.ibis.Type.NullabilityR\x0bnullability\x1a\x8f\x01\n\rIntegerOption\x12\x1a\n\x07literal\x18\x01 \x01(\x05H\x00R\x07literal\x12R\n\tparameter\x18\x02 \x01(\x0b22.substrait.ibis.ParameterizedType.IntegerParameterH\x00R\tparameterB\x0e\n\x0cinteger_typeB\x06\n\x04kindB5\n\x17io.substrait.ibis.protoP\x01\xaa\x02\x17Substrait.Ibis.Protobufb\x06proto3')
_PARAMETERIZEDTYPE = DESCRIPTOR.message_types_by_name['ParameterizedType']
_PARAMETERIZEDTYPE_TYPEPARAMETER = _PARAMETERIZEDTYPE.nested_types_by_name['TypeParameter']
_PARAMETERIZEDTYPE_INTEGERPARAMETER = _PARAMETERIZEDTYPE.nested_types_by_name['IntegerParameter']
_PARAMETERIZEDTYPE_NULLABLEINTEGER = _PARAMETERIZEDTYPE.nested_types_by_name['NullableInteger']
_PARAMETERIZEDTYPE_PARAMETERIZEDFIXEDCHAR = _PARAMETERIZEDTYPE.nested_types_by_name['ParameterizedFixedChar']
_PARAMETERIZEDTYPE_PARAMETERIZEDVARCHAR = _PARAMETERIZEDTYPE.nested_types_by_name['ParameterizedVarChar']
_PARAMETERIZEDTYPE_PARAMETERIZEDFIXEDBINARY = _PARAMETERIZEDTYPE.nested_types_by_name['ParameterizedFixedBinary']
_PARAMETERIZEDTYPE_PARAMETERIZEDDECIMAL = _PARAMETERIZEDTYPE.nested_types_by_name['ParameterizedDecimal']
_PARAMETERIZEDTYPE_PARAMETERIZEDSTRUCT = _PARAMETERIZEDTYPE.nested_types_by_name['ParameterizedStruct']
_PARAMETERIZEDTYPE_PARAMETERIZEDNAMEDSTRUCT = _PARAMETERIZEDTYPE.nested_types_by_name['ParameterizedNamedStruct']
_PARAMETERIZEDTYPE_PARAMETERIZEDLIST = _PARAMETERIZEDTYPE.nested_types_by_name['ParameterizedList']
_PARAMETERIZEDTYPE_PARAMETERIZEDMAP = _PARAMETERIZEDTYPE.nested_types_by_name['ParameterizedMap']
_PARAMETERIZEDTYPE_PARAMETERIZEDUSERDEFINED = _PARAMETERIZEDTYPE.nested_types_by_name['ParameterizedUserDefined']
_PARAMETERIZEDTYPE_INTEGEROPTION = _PARAMETERIZEDTYPE.nested_types_by_name['IntegerOption']
ParameterizedType = _reflection.GeneratedProtocolMessageType('ParameterizedType', (_message.Message,), {'TypeParameter': _reflection.GeneratedProtocolMessageType('TypeParameter', (_message.Message,), {'DESCRIPTOR': _PARAMETERIZEDTYPE_TYPEPARAMETER, '__module__': 'substrait.ibis.parameterized_types_pb2'}), 'IntegerParameter': _reflection.GeneratedProtocolMessageType('IntegerParameter', (_message.Message,), {'DESCRIPTOR': _PARAMETERIZEDTYPE_INTEGERPARAMETER, '__module__': 'substrait.ibis.parameterized_types_pb2'}), 'NullableInteger': _reflection.GeneratedProtocolMessageType('NullableInteger', (_message.Message,), {'DESCRIPTOR': _PARAMETERIZEDTYPE_NULLABLEINTEGER, '__module__': 'substrait.ibis.parameterized_types_pb2'}), 'ParameterizedFixedChar': _reflection.GeneratedProtocolMessageType('ParameterizedFixedChar', (_message.Message,), {'DESCRIPTOR': _PARAMETERIZEDTYPE_PARAMETERIZEDFIXEDCHAR, '__module__': 'substrait.ibis.parameterized_types_pb2'}), 'ParameterizedVarChar': _reflection.GeneratedProtocolMessageType('ParameterizedVarChar', (_message.Message,), {'DESCRIPTOR': _PARAMETERIZEDTYPE_PARAMETERIZEDVARCHAR, '__module__': 'substrait.ibis.parameterized_types_pb2'}), 'ParameterizedFixedBinary': _reflection.GeneratedProtocolMessageType('ParameterizedFixedBinary', (_message.Message,), {'DESCRIPTOR': _PARAMETERIZEDTYPE_PARAMETERIZEDFIXEDBINARY, '__module__': 'substrait.ibis.parameterized_types_pb2'}), 'ParameterizedDecimal': _reflection.GeneratedProtocolMessageType('ParameterizedDecimal', (_message.Message,), {'DESCRIPTOR': _PARAMETERIZEDTYPE_PARAMETERIZEDDECIMAL, '__module__': 'substrait.ibis.parameterized_types_pb2'}), 'ParameterizedStruct': _reflection.GeneratedProtocolMessageType('ParameterizedStruct', (_message.Message,), {'DESCRIPTOR': _PARAMETERIZEDTYPE_PARAMETERIZEDSTRUCT, '__module__': 'substrait.ibis.parameterized_types_pb2'}), 'ParameterizedNamedStruct': _reflection.GeneratedProtocolMessageType('ParameterizedNamedStruct', (_message.Message,), {'DESCRIPTOR': _PARAMETERIZEDTYPE_PARAMETERIZEDNAMEDSTRUCT, '__module__': 'substrait.ibis.parameterized_types_pb2'}), 'ParameterizedList': _reflection.GeneratedProtocolMessageType('ParameterizedList', (_message.Message,), {'DESCRIPTOR': _PARAMETERIZEDTYPE_PARAMETERIZEDLIST, '__module__': 'substrait.ibis.parameterized_types_pb2'}), 'ParameterizedMap': _reflection.GeneratedProtocolMessageType('ParameterizedMap', (_message.Message,), {'DESCRIPTOR': _PARAMETERIZEDTYPE_PARAMETERIZEDMAP, '__module__': 'substrait.ibis.parameterized_types_pb2'}), 'ParameterizedUserDefined': _reflection.GeneratedProtocolMessageType('ParameterizedUserDefined', (_message.Message,), {'DESCRIPTOR': _PARAMETERIZEDTYPE_PARAMETERIZEDUSERDEFINED, '__module__': 'substrait.ibis.parameterized_types_pb2'}), 'IntegerOption': _reflection.GeneratedProtocolMessageType('IntegerOption', (_message.Message,), {'DESCRIPTOR': _PARAMETERIZEDTYPE_INTEGEROPTION, '__module__': 'substrait.ibis.parameterized_types_pb2'}), 'DESCRIPTOR': _PARAMETERIZEDTYPE, '__module__': 'substrait.ibis.parameterized_types_pb2'})
_sym_db.RegisterMessage(ParameterizedType)
_sym_db.RegisterMessage(ParameterizedType.TypeParameter)
_sym_db.RegisterMessage(ParameterizedType.IntegerParameter)
_sym_db.RegisterMessage(ParameterizedType.NullableInteger)
_sym_db.RegisterMessage(ParameterizedType.ParameterizedFixedChar)
_sym_db.RegisterMessage(ParameterizedType.ParameterizedVarChar)
_sym_db.RegisterMessage(ParameterizedType.ParameterizedFixedBinary)
_sym_db.RegisterMessage(ParameterizedType.ParameterizedDecimal)
_sym_db.RegisterMessage(ParameterizedType.ParameterizedStruct)
_sym_db.RegisterMessage(ParameterizedType.ParameterizedNamedStruct)
_sym_db.RegisterMessage(ParameterizedType.ParameterizedList)
_sym_db.RegisterMessage(ParameterizedType.ParameterizedMap)
_sym_db.RegisterMessage(ParameterizedType.ParameterizedUserDefined)
_sym_db.RegisterMessage(ParameterizedType.IntegerOption)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x17io.substrait.ibis.protoP\x01\xaa\x02\x17Substrait.Ibis.Protobuf'
    _PARAMETERIZEDTYPE.fields_by_name['user_defined_pointer']._options = None
    _PARAMETERIZEDTYPE.fields_by_name['user_defined_pointer']._serialized_options = b'\x18\x01'
    _PARAMETERIZEDTYPE._serialized_start = 88
    _PARAMETERIZEDTYPE._serialized_end = 4197
    _PARAMETERIZEDTYPE_TYPEPARAMETER._serialized_start = 1804
    _PARAMETERIZEDTYPE_TYPEPARAMETER._serialized_end = 1898
    _PARAMETERIZEDTYPE_INTEGERPARAMETER._serialized_start = 1901
    _PARAMETERIZEDTYPE_INTEGERPARAMETER._serialized_end = 2141
    _PARAMETERIZEDTYPE_NULLABLEINTEGER._serialized_start = 2143
    _PARAMETERIZEDTYPE_NULLABLEINTEGER._serialized_end = 2182
    _PARAMETERIZEDTYPE_PARAMETERIZEDFIXEDCHAR._serialized_start = 2185
    _PARAMETERIZEDTYPE_PARAMETERIZEDFIXEDCHAR._serialized_end = 2395
    _PARAMETERIZEDTYPE_PARAMETERIZEDVARCHAR._serialized_start = 2398
    _PARAMETERIZEDTYPE_PARAMETERIZEDVARCHAR._serialized_end = 2606
    _PARAMETERIZEDTYPE_PARAMETERIZEDFIXEDBINARY._serialized_start = 2609
    _PARAMETERIZEDTYPE_PARAMETERIZEDFIXEDBINARY._serialized_end = 2821
    _PARAMETERIZEDTYPE_PARAMETERIZEDDECIMAL._serialized_start = 2824
    _PARAMETERIZEDTYPE_PARAMETERIZEDDECIMAL._serialized_end = 3109
    _PARAMETERIZEDTYPE_PARAMETERIZEDSTRUCT._serialized_start = 3112
    _PARAMETERIZEDTYPE_PARAMETERIZEDSTRUCT._serialized_end = 3303
    _PARAMETERIZEDTYPE_PARAMETERIZEDNAMEDSTRUCT._serialized_start = 3305
    _PARAMETERIZEDTYPE_PARAMETERIZEDNAMEDSTRUCT._serialized_end = 3432
    _PARAMETERIZEDTYPE_PARAMETERIZEDLIST._serialized_start = 3435
    _PARAMETERIZEDTYPE_PARAMETERIZEDLIST._serialized_end = 3622
    _PARAMETERIZEDTYPE_PARAMETERIZEDMAP._serialized_start = 3625
    _PARAMETERIZEDTYPE_PARAMETERIZEDMAP._serialized_end = 3866
    _PARAMETERIZEDTYPE_PARAMETERIZEDUSERDEFINED._serialized_start = 3869
    _PARAMETERIZEDTYPE_PARAMETERIZEDUSERDEFINED._serialized_end = 4043
    _PARAMETERIZEDTYPE_INTEGEROPTION._serialized_start = 4046
    _PARAMETERIZEDTYPE_INTEGEROPTION._serialized_end = 4189