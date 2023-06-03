from ctypes import Structure, c_int, c_byte, sizeof
from typing import cast, SupportsBytes

from better_ctypes import typed_structure


def test_decorator():
    @typed_structure
    class Test(Structure):
        field: c_int
        bytes_field: c_byte * 4

    assert sizeof(Test) == 8
    test = Test()

    integer_value = 10
    bytes_value = b"1234"

    test.field = integer_value
    test.bytes_field = type(test.bytes_field)(*bytes_value)
    assert test.field == integer_value
    assert bytes(test.bytes_field) == bytes_value
    assert bytes(cast(SupportsBytes, test)) == integer_value.to_bytes(4, "little") + bytes_value
