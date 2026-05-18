"""
**AveyTense Extensions**

Availability: >= 0.3.26b3 \\
© 2024-Present Aveyzan // License: MIT \\
https://aveyzan.xyz/aveytense#aveytense.extensions

Similarly as `typing_extensions`, this module provides backports for Python types,
functions, classes and ABCs (especially generic).

About AVT types visit https://aveyzan.xyz/aveytense/glossary#avt_prefixed_types

This module occurred in many names:

- `aveytense.tcs` to 0.3.26rc2
- `aveytense.types_collection` during 0.3.26rc3 - 0.3.51
- `aveytense.types` during 0.3.52 - 0.3.56

Constants have been moved to separate submodule `aveytense.constants`.
"""

from __future__ import annotations

import collections.abc as _collections_abc
import collections as _collections
import hashlib as _hashlib
import sys as _sys
import typing as _typing

from ._collection._extensions import *
from ._collection._version import VERSION
from . import util as _util

if False: # 0.3.68
    NULL = type(None) # 0.3.26b3 (0.3.34 - type[None])
    null = NULL # 0.3.41


if False: # < 0.3.27rc1
    @deprecated("Deprecated since 0.3.27a3, use class 'aveytense.types_collection.ClassVar' instead.")
    def classvar(v: T, /):
        """
        Availability: >= 0.3.26b3 (experimental) \\
        @deprecated 0.3.27a3

        Transform variable in a class to a class variable.

        This will be valid only whether this function is \\
        invoked inside a class.
        Use it as:
        ```py \\
        class Example:
            test = classvar(96000) # has value 96000
        ```
        """
        class _t:
            _v: ClassVar[T] = v
        return _t._v

    @deprecated("Deprecated since 0.3.26c3, use class 'aveytense.FinalVar' instead.")
    def finalvar(v: T, /):
        """
        Availability: >= 0.3.26b3 \\
        @deprecated 0.3.26c3 (use `aveytense.FinalVar` class-like instead)

        Use it as:
        ```py \\
        reassign_me = finalvar(96000) # has value 96000
        reassign_me += 3 # error
        ```
        """
        return _util.FinalVar(v)
    

# EnchantedBookQuantity = _lit[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36] ### >= 0.3.26b3; < 0.3.52

if False: # < 0.3.41
    
    TicTacToeBoard = AVT_List[AVT_List[str]] # 0.3.26b3

    AnySequenceForPick = Union[AVT_Sequence[T], AVT_MutableSequence[T], AVT_Uniqual[T], AVT_MutableUniqual[T]] # 0.3.26c3

    SequencePickType = Union[
        AVT_List[_T],
        AVT_Tuple[_T, ...],
        AVT_Set[_T],
        AVT_FrozenSet[_T],
        ListConvertible[_T]
    ] # 0.3.26c3

    SequencePickNGT = _uni[
        list,
        tuple,
        set,
        frozenset,
        Sequence,
        ListConvertible
    ] # 0.3.26c3

if False: # < 0.3.52
    
    VarLenHash = type(_hashlib.shake_256()) # it can appear as local hashlib._VarLenHash class in Python versions before 3.13 (0.3.41)
    "Availability: >= 0.3.26rc3"

    BlakeHash = _hashlib.blake2b
    "Availability: >= 0.3.26rc3"

    List = list # 0.3.26b3
    "Availability: >= 0.3.26b3"

    if _sys.version_info >= (3, 9):
        Tuple = tuple # 0.3.26b3
        "Availability: >= 0.3.26b3"
        
    else:
        Tuple = _typing.Tuple # 0.3.26b3
        "Availability: >= 0.3.26b3"

    Deque = _collections.deque # 0.3.26b3
    "Availability: >= 0.3.26b3"

    Dict = dict # 0.3.26b3
    "Availability: >= 0.3.26b3"

    Bytes = bytes # 0.3.26b3
    "Availability: >= 0.3.26b3"

    ByteArray = bytearray # 0.3.26b3
    "Availability: >= 0.3.26b3"

    Filter = filter # 0.3.26b3
    "Availability: >= 0.3.26b3"

    Type = type # 0.3.26b3
    "Availability: >= 0.3.26b3"

    Zip = zip # 0.3.26b3
    "Availability: >= 0.3.26b3"

    Slice = slice # 0.3.26c1
    "Availability: >= 0.3.26rc1"

    Object = object
    "Availability: >= 0.3.26rc3"

if False: # < 0.3.41 (if no removal version was provided, then all of these were removed in 0.3.41)
    
    class _FinalVar(NamedTuple, Generic[T]):
        x: T
    
    ModernReplace = _uni[list[T], tuple[T, ...], T]
    # since 0.3.25, expected string; renamed from SupportsModernReplace (0.3.26b3)
    PickSequence = _uni[list[T], tuple[T, ...], set[_T], frozenset[T], _collections.deque[T], _collections_abc.Sequence[T], _collections_abc.MutableSequence[T]]
    # since 0.3.25, added support for Sequence and MutableSequence, renamed from SupportsPick (0.3.26b3)
    SanitizeMode = _lit[0, 1, 2, 3, 4, 5]
    # since 0.3.25, renamed from SupportsSanitizeMode (0.3.26b3)
    SupportsAbroadDivisor = _uni[int, float]
    # since 0.3.25; removed in 0.3.26b3, use FloatOrInteger instead
    ShuffleType = _uni[str, list[T], _collections_abc.MutableSequence[T]]
    # since 0.3.26rc1
    TypeOrFinalVarType = _uni[T, _FinalVar[T]]
    # since 0.3.26rc1
    
    __author__ = "Aveyzan <aveyzan@gmail.com>"
    "Availability: >= 0.3.26rc3"
    __license__ = "MIT"
    "Availability: >= 0.3.26rc3"
    __version__ = VERSION
    "Availability: >= 0.3.26rc3"


if False: # < 0.3.46

    ProbabilityType = _uni[T, list[_opt[T]], tuple[T, _opt[T]], dict[T, _opt[T]], _collections.deque[_opt[T]], set[_opt[T]], frozenset[_opt[T]]]
    # since 0.3.25, expected integer; renamed from SupportsProbabilityValuesAndFrequencies (0.3.26b3)



if False: # < 0.3.48
    
    _IntegerConvertible = Union[str, Buffer, IntegerConvertible, Indexable, Truncable] # since 0.3.26rc1; < 0.3.72
    _FloatConvertible = Union[str, Buffer, FloatConvertible, Indexable] # since 0.3.26rc1; < 0.3.72
    _ComplexConvertible = Union[complex, FloatConvertible, Indexable] # since 0.3.26rc1; 0.3.72
    
    @deprecated("Deprecated since 0.3.41, will be removed on 0.3.48. Migrate to 'int' builtin instead")
    class Integer:
        """
        Availability: >= 0.3.26b3
        
        Equivalent to `int`. Once instantiated, it returns \\
        integer of type `int`. (0.3.26c1)
        """
        def __new__(cls, x: _IntegerConvertible = ..., /):
            """
            Availability: >= 0.3.26b3
            
            Equivalent to `int`. Once instantiated, it returns \\
            integer of type `int`. (0.3.26c1)
            """
            return int(x)
        
        def __instancecheck__(self, obj: object, /) -> TypeIs[int]:
            return isinstance(obj, int)

    @deprecated("Deprecated since 0.3.41, will be removed on 0.3.48. Migrate to 'float' builtin instead")
    class Float:
        """
        Availability: >= 0.3.26b3
        
        Equivalent to `float`. Once instantiated, it returns \\
        number of type `float`. (0.3.26c1)
        """
        def __new__(cls, x: _FloatConvertible = ..., /):
            """
            Availability: >= 0.3.26b3
            
            Equivalent to `float`. Once instantiated, it returns \\
            number of type `float`. (0.3.26c1)
            """
            return float(x)
        
        def __instancecheck__(self, obj: object, /) -> TypeIs[float]:
            return isinstance(obj, float)

    @deprecated("Deprecated since 0.3.41, will be removed on 0.3.48. Migrate to 'complex' builtin instead")
    class Complex:
        """
        Availability: >= 0.3.26b3
        
        Equivalent to `complex`. Once instantiated, it returns \\
        number of type `complex`. (0.3.26c1)
        """
        def __new__(cls, r: _uni[ComplexConvertible, _ComplexConvertible] = ..., i: _ComplexConvertible = ..., /):
            """
            Availability: >= 0.3.26b3
            
            Equivalent to `complex`. Once instantiated, it returns \\
            number of type `complex`. (0.3.26c1)
            """
            return complex(r, i)
        
        def __instancecheck__(self, obj: object, /) -> TypeIs[complex]:
            return isinstance(obj, complex)

    @deprecated("Deprecated since 0.3.41, will be removed on 0.3.48. Migrate to 'str' builtin instead")
    class String:
        """
        Availability: >= 0.3.26b3
        
        Equivalent to `str`. Once instantiated, it returns \\
        string of type `str`. (0.3.26c1)
        """
        def __new__(cls, x: object = ..., /):
            """
            Availability: >= 0.3.26b3
            
            Equivalent to `str`. Once instantiated, it returns \\
            string of type `str`. (0.3.26c1)
            """
            return str(x)
        
        def __instancecheck__(self, obj: object, /) -> TypeIs[str]:
            return isinstance(obj, str)

    @deprecated("Deprecated since 0.3.41, will be removed on 0.3.48. Migrate to 'bool' builtin instead")
    class Boolean:
        """
        Availability: >= 0.3.26b3
        
        Equivalent to `bool`. Once instantiated, it returns \\
        boolean of type `bool`. (0.3.26c1)
        """
        def __new__(cls, x: object = ..., /):
            """
            Availability: >= 0.3.26b3
            
            Equivalent to `bool`. Once instantiated, it returns \\
            boolean of type `bool`. (0.3.26c1)
            """
            return bool(x)
        
        def __instancecheck__(self, obj: object, /) -> TypeIs[bool]:
            return obj is True or obj is False

################ TypeScript References ################
# Remove these on 0.3.54.

if False: # < 0.3.54
    false = False
    "Availability: >= 0.3.26rc3"
    true = True
    "Availability: >= 0.3.26rc3"
    never = Never
    "Availability: >= 0.3.26rc3"
    number = Union[int, float] # on JavaScript there is no 'complex' number type
    "Availability: >= 0.3.26rc3"
    void = type(None)
    "Availability: >= 0.3.26rc3"

__all__ = sorted([n for n in globals() if n[:1] != "_"])
"Availability: >= 0.3.26rc1? All definitions written in `aveytense.extensions` module"

__all_deprecated__ = sorted([n for n in globals() if hasattr(globals()[n], "__deprecated__")])
"""
Availability: >= 0.3.41

Returns all deprecated definitions within this module.
"""

__constants__ = [n for n in __all__ if n.isupper()]
"Availability: >= 0.3.26rc3. All constants in `aveytense.extensions` module"

__non_constants__ = [n for n in __all__ if not n.isupper()]
"Availability: >= 0.3.26rc3. All non-constants (functions, classes, type aliases) in `aveytense.extensions` module"

__abc__ = [n for n in __all__ if is_protocol(globals()[n]) or (isinstance(globals()[n], ABC) and n in _collections_abc.__dict__)]
"Availability: >= 0.3.26rc3. ABCs (Abstract Base Classes) in `aveytense.extensions` module"

if __name__ == "__main__":
    error = RuntimeError("Import-only module")
    raise error
