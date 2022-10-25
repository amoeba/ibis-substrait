"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...substrait.ibis import algebra_pb2 as substrait_dot_ibis_dot_algebra__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"substrait/ibis/extension_rel.proto\x12\x0esubstrait.ibis\x1a\x1csubstrait/ibis/algebra.proto"\xdc\x01\n\x0bAsOfJoinRel\x12G\n\ninput_keys\x18\x01 \x03(\x0b2(.substrait.ibis.AsOfJoinRel.AsOfJoinKeysR\tinputKeys\x12\x1c\n\ttolerance\x18\x02 \x01(\x03R\ttolerance\x1af\n\x0cAsOfJoinKeys\x12*\n\x02on\x18\x01 \x01(\x0b2\x1a.substrait.ibis.ExpressionR\x02on\x12*\n\x02by\x18\x02 \x03(\x0b2\x1a.substrait.ibis.ExpressionR\x02byB5\n\x17io.substrait.ibis.protoP\x01\xaa\x02\x17Substrait.Ibis.Protobufb\x06proto3')
_ASOFJOINREL = DESCRIPTOR.message_types_by_name['AsOfJoinRel']
_ASOFJOINREL_ASOFJOINKEYS = _ASOFJOINREL.nested_types_by_name['AsOfJoinKeys']
AsOfJoinRel = _reflection.GeneratedProtocolMessageType('AsOfJoinRel', (_message.Message,), {'AsOfJoinKeys': _reflection.GeneratedProtocolMessageType('AsOfJoinKeys', (_message.Message,), {'DESCRIPTOR': _ASOFJOINREL_ASOFJOINKEYS, '__module__': 'substrait.ibis.extension_rel_pb2'}), 'DESCRIPTOR': _ASOFJOINREL, '__module__': 'substrait.ibis.extension_rel_pb2'})
_sym_db.RegisterMessage(AsOfJoinRel)
_sym_db.RegisterMessage(AsOfJoinRel.AsOfJoinKeys)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x17io.substrait.ibis.protoP\x01\xaa\x02\x17Substrait.Ibis.Protobuf'
    _ASOFJOINREL._serialized_start = 85
    _ASOFJOINREL._serialized_end = 305
    _ASOFJOINREL_ASOFJOINKEYS._serialized_start = 203
    _ASOFJOINREL_ASOFJOINKEYS._serialized_end = 305