"""
Availability: >= 0.3.26rc3 \\
© 2024-Present Aveyzan // License: MIT

Core of `aveytense.extensions`; import this module instead
"""

# Table of supported Python versions by 'typing_extensions' (starting with Python 3.6, stats for 'typing_extensions' 4.15.0):
#
# | PY   | FIRST   | LAST
# | ---- | ------- | -------
# | 3.6  | 3.6.2   | 4.1.1 (< 4.2.0)
# | 3.7  | 3.7.4   | 4.7.1 (< 4.8.0)
# | 3.8  | 3.7.4.2 | 4.13.2 (< 4.14.0)
# | 3.9  | 3.7.4.2 | -
# | 3.10 | 3.10.0  | -
# | 3.11 | 4.5.0   | -
# | 3.12 | 4.7.0   | -
# | 3.13 | 4.12.0  | -
# | 3.14 | 4.14.0  | -

# LAST MICRO RELEASES FOR PYTHON 3.6 - 3.12 (* indicates predicted)
#
# | PY   | BUGFIX  | SECURITY |
# | ---- | ------- | -------- |
# | 3.6  | 3.6.8   | 3.6.15   |
# | 3.7  | 3.7.8   | 3.7.17   |
# | 3.8  | 3.8.10  | 3.8.20   |
# | 3.9  | 3.9.13  | 3.9.23   |
# | 3.10 | 3.10.11 | 3.10.18* |
# | 3.11 | 3.11.9  | 3.11.13* |
# | 3.12 | 3.12.10 | 3.12.11* |

from __future__ import annotations
from . import _Immutable, _Final, _Missing
from ._exceptions import _ErrorHandler as _E
from ._typeparams import (
    # TypeVar: >= 0.3.26b3
    # ParamSpec: >= 0.3.26rc1
    # TypeVarTuple: >= 0.3.26rc3
    TypeVar as TypeVar,
    ParamSpec as ParamSpec,
    TypeVarTuple as TypeVarTuple,
    # type parameters: >= 0.3.72
    # public: 'T', 'Ts', 'P'
    T, T1, T2, T3, T4, T5, T6, 
    T_con, T1_con, T2_con, T3_con, T4_con, T5_con, T6_con,
    T_cov, T1_cov, T2_cov, T3_cov, T4_cov, T5_cov, T6_cov,
    S, S_con, S_cov, U, U_con, U_cov,
    Ts, P,
    KT, VT, KT_con, KT_cov, VT_con, VT_cov,
    KT1, VT1, KT1_con, KT1_cov, VT1_con, VT1_cov,
    KT2, VT2, KT2_cov, KT2_con, VT2_con, VT2_cov,
    AnyStr, # >= ?
    # not for export
    AnyStr_cov as _AnyStr_cov,
    T_array as _T_array,
    T_memoryview as _T_memoryview,
    T_count as _T_count,
    T_yield_cov as _T_yield_cov,
    T_send_con as _T_send_con,
    T_return_cov as _T_return_cov,
    T_send_noDefault_con as _T_send_noDefault_con,
    T_return_noDefault_cov as _T_return_noDefault_cov,
    T_start_cov as _T_start_cov,
    T_stop_cov as _T_stop_cov,
    T_step_cov as _T_step_cov
)

### IMPORTS FOR PY3.6+ ###

from abc import (
    # 0.3.27rc2
    abstractmethod as abstractmethod,
    # 0.3.44
    ABC as ABC, 
    ABCMeta as ABCMeta
)
from array import (
    # 0.3.37
    array as array, 
    ArrayType as ArrayType
)
from ast import (
    # 0.3.44
    Expression as Expression, 
    Module as Module,
    Interactive as Interactive,
    # 0.3.54
    AST as AST
)
from collections import (
    # 0.3.37
    ChainMap as ChainMap, 
    Counter as Counter,
    defaultdict as defaultdict,
    deque as deque,
    OrderedDict as OrderedDict,
    # 0.3.44
    UserDict as UserDict,
    UserList as UserList,
    namedtuple as namedtuple,
    UserString as UserString
)
from collections.abc import (
    # < 0.3.50
    AsyncGenerator as AsyncGenerator,
    AsyncIterable as AsyncIterable,
    AsyncIterator as AsyncIterator,
    Awaitable as Awaitable,
    Callable as Callable,
    Collection as Collection,
    Container as Container,
    Coroutine as Coroutine,
    Generator as Generator,
    Hashable as Hashable,
    ItemsView as ItemsView,
    Iterable as Iterable,
    Iterator as Iterator,
    KeysView as KeysView,
    Mapping as Mapping,
    MappingView as MappingView,
    MutableMapping as MutableMapping,
    MutableSequence as MutableSequence,
    MutableSet as MutableSet, # reverted 0.3.73 from MutableUniqual
    Reversible as Reversible,
    Sequence as Sequence,
    Set as AbstractSet, # reverted 0.3.73 from Uniqual
    Sized as Sized,
    ValuesView as ValuesView
)
from contextlib import (
    # 0.3.53
    AbstractAsyncContextManager as AsyncContextManager, # typo found in 0.3.55a2
    AbstractContextManager as ContextManager,
)
from dataclasses import dataclass as dataclass # 0.3.37
from decimal import Decimal # 0.3.60
from enum import EnumMeta as EnumMeta # 0.3.26rc1
from functools import (
    # 0.3.26
    partial as partial,
    # 0.3.37
    cached_property as cachedproperty, 
    partialmethod as partialmethod,
    singledispatchmethod as singledispatchmethod,
    lru_cache as lru_cache,
    singledispatch as singledispatch,
    # 0.3.54
    lru_cache as lruCache,
    singledispatch as singleDispatch
)
from importlib import (
    # 0.3.44
    import_module as import_module,
    # 0.3.54
    import_module as importModule
)
from inspect import (
    # 0.3.26rc3
    ArgInfo as ArgInfo, 
    Arguments as Arguments,
    Attribute as Attribute,
    BlockFinder as BlockFinder,
    BoundArguments as BoundArguments,
    ClosureVars as ClosureVars,
    FrameInfo as FrameInfo,
    FullArgSpec as FullArgSpec,
    Parameter as Parameter,
    Signature as Signature,
    Traceback as Traceback,
)
from numbers import Rational as _Rational # 0.3.60
from os import PathLike as PathLike # 0.3.52
from re import (
    # 0.3.26
    Match as Match, 
    Pattern as Pattern,
    # 0.3.60
    RegexFlag as RegexFlag # only used for 'FlagsType'
)
from types import ( # Imports from 0.3.51 are used for builtin function inspection via ~.util.ParamVar.
    # 0.3.26rc1/0.3.34?
    coroutine as coroutine,
    new_class as new_class,
    # 0.3.26rc3
    new_class as newClass,
    ModuleType as ModuleType,
    TracebackType as TracebackType,
    CodeType as CodeType,
    # 0.3.37
    FunctionType as FunctionType,
    FrameType as FrameType,
    MethodType as MethodType,
    # 0.3.42
    MappingProxyType as MappingProxyType,
    # 0.3.43
    DynamicClassAttribute as DynamicClassAttribute,
    # 0.3.44
    AsyncGeneratorType as AsyncGeneratorType, # >=Py3.6
    CoroutineType as CoroutineType, # >=Py3.5
    # 0.3.51
    BuiltinFunctionType as BuiltinFunctionType,
    # 0.3.53
    SimpleNamespace as SimpleNamespace, 
    # 0.3.54
    prepare_class as prepare_class,
    prepare_class as prepareClass,
)
from typing import (
    # 0.3.26rc1
    no_type_check as noTypeCheck,
    # 0.3.37
    get_type_hints as get_type_hints, 
    no_type_check as no_type_check,
    # 0.3.44
    cast as cast,
    # 0.3.54
    get_type_hints as getTypeHints
)
from uuid import UUID as UUID # 0.3.26rc3
import sys as _sys

__name__ = "aveytense.extensions"

# In this part of the code, we are retrieving currently used version of 'typing_extensions', and
# formalize the version like 'sys.version_info':
class TypingExtensionsVersionInfo:
    """
    Availability: >= 0.3.54
    
    Version info for `typing_extensions`
    """
    
    def __init__(self):
        
        if _sys.version_info >= (3, 8):
            from importlib.metadata import version 
        else: # Py<3.8 will require pypi module importlib_metadata
            from importlib_metadata import version
        
        try:
            _typing_ext_string_ver_ = version("typing_extensions")
        except Exception:
            import subprocess, sys
            
            _typing_ext_string_ver_ = "4.10.0"
            
            try:
                out = subprocess.check_output([sys.executable, "-m", "pip", "list"]).split("\r\n")
            except Exception:
                out = [bytes()]
            
            for subject in out:
                if b"typing_extensions" in subject:
                    _typing_ext_string_ver_ = list(filter(lambda x: len(x) > 0, subject.split(" ")))[1].decode()
                    break
            
        # There I am believing devs won't use the epoch version component.
        # Every version since version 4.0.0 have 3 components, unlike before
        # 4.0.0 some can have 4 (last being submicro)
        _split_components_ = _typing_ext_string_ver_.split(".")
        
        self.major = int(_split_components_[0])
        self.minor = int(_split_components_[1])
        
        _search_ = ("a", "b", "rc")
        _submicro_ = len(_split_components_) == 4
        
        if not _submicro_:
            self.submicro = 0
        else:
            self.micro = int(_split_components_[2])
            
        _search_found_ = False
        
        for search in _search_:
                
            if search in _split_components_[-1]:
                
                _search_found_ = True
                _split_id_ = _split_components_[-1].split(search)
                
                if not _submicro_:
                    self.micro = int(_split_id_[0])
                else:
                    self.submicro = int(_submicro_[0])
                
                if search == "a":
                    self.releaselevel = ("alpha", 1)
                    
                elif search == "b":
                    self.releaselevel = ("beta", 2)
                    
                else:
                    self.releaselevel = ("candidate", 3)
                    
                self.serial = int(_split_id_[1])
                
                break
                
        if not _search_found_:
            
            if not _submicro_:
                self.micro = int(_split_components_[-1])
            else:
                self.submicro = int(_split_components_[-1])
                
            self.releaselevel = ("final", 4)
            self.serial = 0

    def __gt__(self, other: tuple):
        
        if not isinstance(other, tuple):
            return False
        
        if len(other) == 1:
            return other < (self.major,)
        
        elif len(other) == 2:
            return other < (self.major, self.minor)
        
        elif len(other) == 3:
            return other < (self.major, self.minor, self.micro)
        
        elif len(other) == 4:
            
            if self.submicro == 0:
                return other < (self.major, self.minor, self.micro, self.releaselevel[1])
            else:
                return other < (self.major, self.minor, self.micro, self.submicro)
            
        return False
    
    def __lt__(self, other: tuple):
        
        if not isinstance(other, tuple):
            return False
        
        return not self.__gt__(other) and other != (self.major, self.minor, self.micro, self.releaselevel[1] if self.submicro == 0 else self.submicro)[:len(other)]
    
    def __ge__(self, other: tuple):
        
        if not isinstance(other, tuple):
            return False
        
        return not self.__lt__(other)
    
    def __le__(self, other: tuple):
        
        if not isinstance(other, tuple):
            return False
        
        return not self.__gt__(other)
    
    def __eq__(self, other: tuple):
        
        if not isinstance(other, tuple):
            return False
        
        return not self.__gt__(other) and not self.__lt__(other)
    
    def __ne__(self, other: tuple):
        
        if not isinstance(other, tuple):
            return False
        
        return not self.__eq__(other)
    
    def __str__(self):
        
        if self.releaselevel[1] == 1:
            _level_ = "a"
        elif self.releaselevel[1] == 2:
            _level_ = "b"
        elif self.releaselevel[1] == 3:
            _level_ = "rc"
        else:
            _level_ = None
        
        return "typing_extensions {}".format(".".join((
            str(self.major),
            str(self.minor),
            str(self.micro),
        )) + (
            "" if self.submicro == 0 else "." + str(self.submicro)
        ) + (
            _level_ + str(self.serial) if _level_ is not None else ""
        ))

TypingExtensionsVersionInfo = TypingExtensionsVersionInfo()

### Private functions and not for export ###

def _prevent_unused_imports(*_): pass # 0.3.55a2, nothing, only prevent unused imports

# 0.3.72, re-implement this if using typing_extensions version incompatible with Py3.8
def _check_methods(C: type, *methods: str): 
    mro = C.__mro__
    for method in methods:
        for B in mro:
            if method in B.__dict__:
                if B.__dict__[method] is None:
                    return NotImplemented
                break
        else:
            return NotImplemented
    return True

### Enums and Flags ###
# 0.3.44: Additional checking to ensure these enumerator and flag classes exist already.

import enum as _enum

class Enum(_enum.Enum):
    """
    Availability: >= 0.3.26rc1 [`enum.Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)
    """
    
    if False: # attempt 0.3.56
        
        def _add_alias_(self, name: str):
            self.__class__._add_member_(name, self)

        def _add_value_alias_(self, value: Any):
            cls = self.__class__
            try:
                if value in cls._value2member_map_:
                    if cls._value2member_map_[value] is not self:
                        raise ValueError('%r is already bound: %r' % (value, cls._value2member_map_[value]))
                    return
            except TypeError:
                # unhashable value, do long search
                for m in cls._member_map_.values():
                    if m._value_ == value:
                        if m is not self:
                            raise ValueError('%r is already bound: %r' % (value, cls._value2member_map_[value]))
                        return
            try:
                # This may fail if value is not hashable. We can't add the value
                # to the map, and by-value lookups for this value will be
                # linear.
                cls._value2member_map_.setdefault(value, self)
                cls._hashable_values_.append(value)
            except TypeError:
                # keep track of the value in a list so containment checks are quick
                cls._unhashable_values_.append(value)
                cls._unhashable_values_map_.setdefault(self.name, []).append(value)

# 0.3.56: define __len__, __iter__, __ror__, __rand__ and __rxor__ before Python 3.11
class Flag(_enum.Flag):
    """
    Availability: >= 0.3.26rc1 [`enum.Flag`](https://docs.python.org/3/library/enum.html#enum.Flag)
    """
    
    if _sys.version_info < (3, 11):
        
        def __len__(self):
            return self._value_.bit_count()
        
        def __iter__(self):
            """
            Returns flags in definition order.
            """
            yield from self._iter_member_(self._value_) # collections.abc.Iterator[Self]
            
        def __ror__(self, other: Self):
            return super().__or__(other)
        
        def __rand__(self, other: Self):
            return super().__and__(other)
        
        def __rxor__(self, other: Self):
            return super().__xor__(other)
    
class ReprEnum(Enum): # >=Py3.11; practically subclass of enum.Enum and nothing in the body. Try to define for least than Py3.11
    """
    Availability: >= 0.3.26rc1 [`enum.ReprEnum`](https://docs.python.org/3/library/enum.html#enum.ReprEnum)
    """

if _sys.version_info >= (3, 11):
    
    from enum import verify as verify, EnumCheck as EnumCheck, EnumType as EnumType
    
    # If not the same (as before 3.13 it can occur), we need to ensure they are the same by using type assignment
    if ReprEnum != _enum.ReprEnum:
        ReprEnum = _enum.ReprEnum
        
class EnumDict(Enum): # base class ignored after assignment below
    """
    Availability: >= 0.3.26rc1 [`enum.EnumDict`](https://docs.python.org/3/library/enum.html#enum.EnumDict)
    
    Undocumented internal class `enum._EnumDict` before Python 3.13
    """
    
if _sys.version_info >= (3, 13):
    EnumDict = _enum.EnumDict
    
else:
    # questionable: since when enum._EnumDict was in enum.py file?
    EnumDict = _enum._EnumDict
    
class FlagBoundary(Enum): # >=Py3.11. Define for least than Py3.11
    """
    Availability: >= 0.3.26rc1 [`enum.FlagBoundary`](https://docs.python.org/3/library/enum.html#enum.FlagBoundary)
    
    Control how out of range values are handled.
    
    - `STRICT` -> error is raised             (default for `Flag`)
    - `CONFORM` -> extra bits are discarded
    - `EJECT` -> lose flag status
    - `KEEP` -> keep flag status and all bits (default for `IntFlag`)
    """
    STRICT = _enum.auto() # 1; enum.auto accessible for >=Py3.8
    CONFORM = _enum.auto() # 2
    EJECT = _enum.auto() # 3
    KEEP = _enum.auto() # 4

class IntegerFlag(_enum.IntFlag): # accessible for >=Py3.6 (can be recreated via bases: >= Py3.11 (int, ReprEnum, Flag, boundary=FlagBoundary.KEEP), < Py3.11 (int, Flag))
    """
    Availability: >= 0.3.26rc1. [`enum.IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag)
    """

if _sys.version_info >= (3, 11):
    
    class IntegerEnum(_enum.IntEnum):
        """
        Availability: >= 0.3.26rc1. [`enum.IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum)
        """
        
    class StringEnum(_enum.StrEnum):
        """
        Availability: >= 0.3.26rc1. [`enum.StrEnum`](https://docs.python.org/3/library/enum.html#enum.StrEnum)
        """
        
else:
    
    class IntegerEnum(int, ReprEnum):
        """
        Availability: >= 0.3.26rc1. [`enum.IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum)
        """
        
    class StringEnum(str, ReprEnum):
        """
        Availability: >= 0.3.26rc1. [`enum.StrEnum`](https://docs.python.org/3/library/enum.html#enum.StrEnum)
        """
        
        def __new__(cls, *values):
            "values must already be of type `str`"
            if len(values) > 3:
                raise TypeError('too many arguments for str(): %r' % (values, ))
            if len(values) == 1:
                # it must be a string
                if not isinstance(values[0], str):
                    raise TypeError('%r is not a string' % (values[0], ))
            if len(values) >= 2:
                # check that encoding argument is a string
                if not isinstance(values[1], str):
                    raise TypeError('encoding must be a string, not %r' % (values[1], ))
            if len(values) == 3:
                # check that errors argument is a string
                if not isinstance(values[2], str):
                    raise TypeError('errors must be a string, not %r' % (values[2]))
            value = str(*values)
            member = str.__new__(cls, value)
            member._value_ = value
            return member

        @staticmethod
        def _generate_next_value_(name, start, count, last_values):
            """
            Return the lower-cased version of the member name.
            """
            return name.lower()
        
### UTILITY TYPES ###

# It is not worth to use solutions from 'typing_extensions' because these were provided later, and won't be supported in Python 3.6.
# In the following imports this includes 'Optional', 'Union', 'IO', 'BinaryIO', 'TextIO' and 'Generic', which were provided in 4.7.0.
from typing import (
    # ?
    IO as IO,
    # 0.3.26b3
    Generic as Generic, # >=Py3.5
    ClassVar as ClassVar, # >=Py3.5.3
    # 0.3.26rc1
    Optional as Optional, # >=Py3.5
    Union as Union, # >=Py3.5
    # 0.3.26rc3
    BinaryIO as BinaryIO, 
    TextIO as TextIO,
    # 0.3.37
    TYPE_CHECKING as TYPE_CHECKING # >=Py3.5.2
)

# ****************** Py3.6: 10/2017 ************************
# NOTE: LAST BUGFIX: 3.6.8 / SECURITY: 3.6.15
if _sys.version_info >= (3, 6, 2):
    from typing import NoReturn as NoReturn # 0.3.26b3
else:
    from typing_extensions import NoReturn as NoReturn # 0.3.26b3

# ****************** Py3.7: 10/2018 ************************
# NOTE: LAST BUGFIX: 3.7.8 / SECURITY: 3.7.17
if _sys.version_info >= (3, 7):
    
    from types import (
        # 0.3.51
        ClassMethodDescriptorType as ClassMethodDescriptorType,
        MethodDescriptorType as MethodDescriptorType,
        MethodWrapperType as MethodWrapperType,
        WrapperDescriptorType as WrapperDescriptorType,
        # 0.3.54
        resolve_bases as resolve_bases,
        # 0.3.56
        resolve_bases as resolveBases
    )
    from uuid import SafeUUID as SafeUUID
    
else:
    class SafeUUID(Enum):
        safe = 0
        unsafe = -1
        unknown = None

if _sys.version_info >= (3, 7, 4):
    # Py3.14+ = 'annotationlib.ForwardRef'
    from typing import ForwardRef as ForwardRef # 0.3.26rc3
else:
    from typing_extensions import ForwardRef as ForwardRef # 0.3.26rc3

# ****************** Py3.8: 10/2019 ************************
# NOTE: LAST BUGFIX: 3.8.10 / SECURITY: 3.8.20
if _sys.version_info >= (3, 8):
    
    from types import CellType as CellType # 0.3.54
    from typing import (
        # 0.3.26rc1
        Final as Final,
        Protocol as Protocol
    )
    
else:
    
    from typing_extensions import (
        # 0.3.26rc1
        Final as Final,
        Protocol as Protocol
    )
    
if TypingExtensionsVersionInfo >= (4, 8): # Py3.8+
    from typing_extensions import Doc as Doc
    
# ****************** Py3.9: 10/2020 ************************
# NOTE: LAST BUGFIX: 3.9.13 / SECURITY: 3.9.23
#
# / 0.3.42 /: Inspect type subscription with abstract base
# classes from 'collections.abc'
# / 0.3.46 /: Inspect type substription with inbuilt classes
# from 'builtins' in submodule '~._subscript_builtins'
# / 0.3.52 /: Migrate inbuilt classes there; types with AVT
# prefix only have purpose for typing, more specifically,
# subscripting. These change when going since or below Python 3.9.
# Some generic classes can throw errors when inspecting
# them in isinstance() or issubclass(), hence ordinarily classes
# without AVT prefix are exported.
if _sys.version_info >= (3, 9):
    
    from builtins import (
        # 0.3.52
        dict as AVT_Dict,
        frozenset as AVT_FrozenSet,
        list as AVT_List,
        set as AVT_Set,
        tuple as AVT_Tuple,
        type as AVT_Type
    )
    from collections import (
        # 0.3.52
        ChainMap as AVT_ChainMap,
        Counter as AVT_Counter,
        OrderedDict as AVT_OrderedDict,
        defaultdict as AVT_DefaultDict,
        deque as AVT_Deque
    )
    from collections.abc import (
        # 0.3.52
        AsyncGenerator as AVT_AsyncGenerator,
        AsyncIterable as AVT_AsyncIterable,
        AsyncIterator as AVT_AsyncIterator,
        Awaitable as AVT_Awaitable,
        Callable as AVT_Callable,
        Collection as AVT_Collection,
        Container as AVT_Container,
        Coroutine as AVT_Coroutine,
        Generator as AVT_Generator,
        ItemsView as AVT_ItemsView,
        Iterable as AVT_Iterable,
        Iterator as AVT_Iterator,
        KeysView as AVT_KeysView,
        Mapping as AVT_Mapping,
        MappingView as AVT_MappingView,
        MutableMapping as AVT_MutableMapping,
        MutableSequence as AVT_MutableSequence,
        MutableSet as AVT_MutableSet,
        Reversible as AVT_Reversible,
        Sequence as AVT_Sequence,
        Set as AVT_AbstractSet,
        ValuesView as AVT_ValuesView
    )
    from contextlib import (
        # 0.3.53
        AbstractAsyncContextManager as AVT_AsyncContextManager,
        AbstractContextManager as AVT_ContextManager
    )
    from os import PathLike as AVT_PathLike # 0.3.54
    from re import (
        # 0.3.52
        Match as AVT_Match,
        Pattern as AVT_Pattern
    )
    from types import GenericAlias as GenericAlias # 0.3.37
    from typing import Annotated as Annotated # 0.3.26rc1
    
    ByteString = Union[bytes, bytearray, memoryview] # 0.3.37
    
else:
    
    from typing import (
        # 0.3.37
        ByteString as ByteString,
        # builtins, 0.3.52
        Dict as AVT_Dict,
        FrozenSet as AVT_FrozenSet,
        List as AVT_List,
        Set as AVT_Set,
        Tuple as AVT_Tuple,
        Type as AVT_Type, # >=Py3.5.2
        # collections, 0.3.52
        DefaultDict as AVT_DefaultDict, # >=Py3.5.2
        # collections.abc, 0.3.52
        AsyncIterable as AVT_AsyncIterable, # >=Py3.5.2
        AsyncIterator as AVT_AsyncIterator, # >=Py3.5.2
        Awaitable as AVT_Awaitable, # >=Py3.5.2
        Callable as AVT_Callable,
        Collection as AVT_Collection,
        Container as AVT_Container,
        Coroutine as AVT_Coroutine,
        Generator as AVT_Generator,
        ItemsView as AVT_ItemsView,
        Iterable as AVT_Iterable,
        Iterator as AVT_Iterator,
        KeysView as AVT_KeysView,
        Mapping as AVT_Mapping,
        MappingView as AVT_MappingView,
        MutableMapping as AVT_MutableMapping,
        MutableSequence as AVT_MutableSequence,
        MutableSet as AVT_MutableSet,
        Reversible as AVT_Reversible,
        Sequence as AVT_Sequence,
        AbstractSet as AVT_AbstractSet,
        ValuesView as AVT_ValuesView,
        # contextlib, 0.3.53
        ContextManager as AVT_ContextManager, # >=Py3.5.4
        # re, 0.3.52
        Match as AVT_Match, # typing_extensions >= 4.7.0
        Pattern as AVT_Pattern, # typing_extensions >= 4.7.0
        # temporary internal imports for 'AVT_PathLike'
        TypeVar as _TypeVar,
        runtime_checkable as _runtime
    )
    from typing_extensions import Annotated as Annotated # 0.3.26rc1
    
    if _sys.version_info >= (3, 6, 1):
        
        from typing import (
            # collections, 0.3.52
            ChainMap as AVT_ChainMap,
            Counter as AVT_Counter,
            Deque as AVT_Deque,
            # collections.abc, 0.3.52
            AsyncGenerator as AVT_AsyncGenerator
        )
        
    else:
        
        from typing_extensions import (
            # collections, 0.3.52
            ChainMap as AVT_ChainMap,
            Counter as AVT_Counter,
            Deque as AVT_Deque,
            # collections.abc, 0.3.52
            AsyncGenerator as AVT_AsyncGenerator
        )
        
    if _sys.version_info >= (3, 6, 2):
        from typing import AsyncContextManager as AVT_AsyncContextManager # contextlib, 0.3.53
    else:
        from typing_extensions import AsyncContextManager as AVT_AsyncContextManager # contextlib, 0.3.53
        
    if _sys.version_info >= (3, 7, 2):
        from typing import OrderedDict as AVT_OrderedDict # collections, 0.3.52
    else:
        from typing_extensions import OrderedDict as AVT_OrderedDict # collections, 0.3.52
    
    # 'os.PathLike' exists since Python 3.6, but wasn't generic until 3.9.
    @_runtime
    class AVT_PathLike(Protocol[_AnyStr_cov]):
        """Availability: >= 0.3.54"""
        
        def __fspath__(self) -> _AnyStr_cov_pathLikeExclusive: ...
        
    del _runtime

# ****************** Py3.10: 10/2021 ************************
if _sys.version_info >= (3, 10):
    
    # Py3.14+ = 'annotationlib.get_annotations'
    from inspect import (
        # 0.3.37
        get_annotations as get_annotations,
        # 0.3.57
        get_annotations as getAnnotations
    ) 
    from types import (
        # ?
        EllipsisType as EllipsisType,
        # 0.3.26
        NoneType as NoneType,
        # 0.3.37
        UnionType as UnionType, 
        NotImplementedType as NotImplementedType
    )
    from typing import (
        ParamSpecArgs as ParamSpecArgs,
        ParamSpecKwargs as ParamSpecKwargs,
        TypeGuard as TypeGuard,
        TypeAlias as TypeAlias,
        Concatenate as Concatenate,
        get_args as get_args, # >= 0.3.34
        # 0.3.37
        get_origin as get_origin,
        # 0.3.54
        get_args as getArgs, # < 0.3.34
        get_origin as getOrigin
    )
    
else:
    
    from typing_extensions import (
        # 0.3.26rc1
        ParamSpec as ParamSpec, 
        ParamSpecArgs as ParamSpecArgs, 
        ParamSpecKwargs as ParamSpecKwargs,
        TypeGuard as TypeGuard, 
        TypeAlias as TypeAlias,
        Concatenate as Concatenate,
        final as _final,
        get_args as get_args, # >= 0.3.34
        # 0.3.37
        get_origin as get_origin,
        # 0.3.54
        get_origin as getOrigin,
        get_args as getArgs # < 0.3.34
    )
    
    NotImplementedType = type(NotImplemented) # >= 0.3.52
    
    @_final
    class NoneType:
        "Availability: >= 0.3.26"
        def __bool__(self) -> Literal[False]: ...
        
    @_final
    class EllipsisType: ...
    
    del _final
        
    NoneType = cast(NoneType, type(None))
    EllipsisType = cast(EllipsisType, type(Ellipsis))
    
    # backport 0.3.56, Py3.8+
    if TypingExtensionsVersionInfo >= (4, 13):
        from typing_extensions import (
            get_annotations as get_annotations,
            # 0.3.57
            get_annotations as getAnnotations
        )

if _sys.version_info >= (3, 10, 1):
    from typing import Literal as Literal # 0.3.26rc1
else:
    from typing_extensions import Literal as Literal # 0.3.26rc1

# ****************** Py3.11: 10/2022 ************************
# NewType (3.5.2+): the error message for subclassing instances
# of NewType was improved on 3.11
if _sys.version_info >= (3, 11):
    
    from typing import (
        # 0.3.26rc1
        Any as Any,
        LiteralString as LiteralString, 
        Never as Never,
        NewType as NewType,
        NotRequired as NotRequired,
        Required as Required,
        Self as Self,
        overload as overload,
        # 0.3.37
        assert_never as assert_never, 
        assert_type as assert_type,
        clear_overloads as clear_overloads,
        final as final,
        get_overloads as get_overloads,
        reveal_type as reveal_type,
        # 0.3.54
        assert_never as assertNever,
        assert_type as assertType,
        clear_overloads as clearOverloads,
        get_overloads as getOverloads,
        reveal_type as revealType,
    )
    
else:
    
    from typing_extensions import (
        # 0.3.26rc1
        Any as Any,
        LiteralString as LiteralString, 
        Never as Never,
        NewType as NewType,
        NotRequired as NotRequired,
        Required as Required,
        Self as Self,
        overload as overload,
        # 0.3.37
        assert_never as assert_never, 
        reveal_type as reveal_type,
        final as final,
        # 0.3.54
        assert_never as assertNever,
        reveal_type as revealType
    )
        
    if TypingExtensionsVersionInfo >= (4, 2): # Py3.7+
        
        from typing_extensions import (
            # 0.3.37
            assert_type as assert_type, 
            clear_overloads as clear_overloads,
            get_overloads as get_overloads,
            # 0.3.54
            assert_type as assertType,
            clear_overloads as clearOverloads,
            get_overloads as getOverloads
        )

# ****************** Py3.12: 10/2023 ************************
# Unpack (3.11+): see PEP 692 (changed the repr of Unpack[])
# dataclass_transform (3.11+) was lacking frozen_default parameter
if _sys.version_info >= (3, 12):
    
    from collections.abc import Buffer as _Buffer # 0.3.37
    from inspect import BufferFlags as BufferFlags # 0.3.26rc2
    from types import (
        # 0.3.40
        get_original_bases as get_original_bases,
        # 0.3.54
        get_original_bases as getOriginalBases
    )
    from typing import (
        # 0.3.26rc1
        Unpack as Unpack,
        # 0.3.37
        dataclass_transform as dataclass_transform, 
        override as override,
        # 0.3.54
        dataclass_transform as dataclassTransform
    )
    
else:
    
    if TypingExtensionsVersionInfo >= (4, 1): # Py3.6+
        from typing_extensions import (
            
            # 0.3.26rc1
            Unpack as Unpack,
            
            # 0.3.37
            dataclass_transform as dataclass_transform,
            
            # 0.3.54
            dataclass_transform as dataclassTransform
        )
    
    
    if TypingExtensionsVersionInfo >= (4, 4): # Py3.7+
        from typing_extensions import override as override # 0.3.37
    
    if TypingExtensionsVersionInfo >= (4, 6): # Py3.7+
        from typing_extensions import (
            # 0.3.37
            Buffer as _Buffer,
            # 0.3.55a2
            get_original_bases as get_original_bases,
            get_original_bases as getOriginalBases
        )
        
    else:
        
        class Buffer(metaclass=ABCMeta):

            __slots__ = ()

            @abstractmethod
            def __buffer__(self, flags: int) -> memoryview:
                raise NotImplementedError

            @classmethod
            def __subclasshook__(cls, C: type):
                
                if cls is Buffer:
                    return _check_methods(C, "__buffer__")
                return NotImplemented
    
    class BufferFlags(IntegerFlag): # 0.3.26rc2
        SIMPLE = 0x0
        WRITABLE = 0x1
        FORMAT = 0x4
        ND = 0x8
        STRIDES = 0x10 | ND
        C_CONTIGUOUS = 0x20 | STRIDES
        F_CONTIGUOUS = 0x40 | STRIDES
        ANY_CONTIGUOUS = 0x80 | STRIDES
        INDIRECT = 0x100 | STRIDES
        CONTIG = ND | WRITABLE
        CONTIG_RO = ND
        STRIDED = STRIDES | WRITABLE
        STRIDED_RO = STRIDES
        RECORDS = STRIDES | WRITABLE | FORMAT
        RECORDS_RO = STRIDES | FORMAT
        FULL = INDIRECT | WRITABLE | FORMAT
        FULL_RO = INDIRECT | FORMAT
        READ = 0x100
        WRITE = 0x200

# ****************** Py3.13: 10/2024 ************************
# About TypeVar & TypeVarTuple see PEP 696 about 'default'
# parameter. NamedTuple is for backporting updates since its
# existence (3.5.2)

if _sys.version_info >= (3, 13):
    
    from types import CapsuleType as CapsuleType # 0.3.54
    from typing import (
        # 0.3.26rc1
        NamedTuple as NamedTuple, 
        Protocol as Protocol,
        TypeIs as TypeIs,
        NoDefault as NoDefault,
        ReadOnly as ReadOnly,
        runtime_checkable as runtime,
        runtime_checkable as runtime_checkable,
        # 0.3.37
        get_protocol_members as get_protocol_members,
        is_protocol as is_protocol,
        # 0.3.54
        get_protocol_members as getProtocolMembers,
        is_protocol as isProtocol,
    )
    
    
else:
    
    from typing_extensions import (
        # 0.3.26rc1
        NamedTuple as NamedTuple, 
        Protocol as Protocol,
        runtime_checkable as runtime,
        runtime_checkable as runtime_checkable,
    )
        
    if TypingExtensionsVersionInfo >= (4, 7): # Py3.7+
        
        from typing_extensions import (
            # 0.3.37
            is_protocol as is_protocol,
            # 0.3.54
            is_protocol as isProtocol, # pyright: ignore[reportUnusedImport]
            # 0.3.37
            get_protocol_members as get_protocol_members,
            # 0.3.54
            get_protocol_members as getProtocolMembers # pyright: ignore[reportUnusedImport]
        )
        
    else:
        
        def is_protocol(tp: type):
            return isinstance(tp, type) and getattr(tp, "_is_protocol", False) and tp != Protocol
        
        def get_protocol_members(tp: type) -> AVT_FrozenSet[str]:
            if not is_protocol(tp):
                raise TypeError(f"{tp!r} is not a Protocol")
            return frozenset(getattr(tp, "__protocol_attrs__", []))
        
    if TypingExtensionsVersionInfo >= (4, 9): # Py3.8+
        from typing_extensions import ReadOnly as ReadOnly # 0.3.26rc1
    
    if TypingExtensionsVersionInfo >= (4, 10): # Py3.8+
        from typing_extensions import TypeIs as TypeIs # 0.3.26rc1
    
    if TypingExtensionsVersionInfo >= (4, 12): # Py3.8+
        from typing_extensions import (
            # 0.3.26rc1
            NoDefault as NoDefault, # type: ignore
            # 0.3.54
            CapsuleType as CapsuleType # type: ignore
        )                              
    
if _sys.version_info >= (3, 13, 3):
    from warnings import deprecated as deprecated # 0.3.37
else:
    
    if TypingExtensionsVersionInfo >= (4, 5): # Py3.7+
        from typing_extensions import deprecated as deprecated # 0.3.37

# ****************** Py3.14: 07.10.2025 ************************
# Removal of 'collections.abc.ByteString', but we will still
# re-declare it. Update: removal was postponed to 3.17, but
# we will still re-declare it. 'typing.TypeAliasType': star
# unpacking (3.14)
if _sys.version_info >= (3, 14):
    
    from annotationlib import Format as Format # 0.3.54
    from io import (
        Reader as Reader,
        Writer as Writer
    )
    from typing import (
        # 0.3.26rc1
        TypeAliasType as TypeAliasType,
        # 0.3.56
        evaluate_forward_ref as evaluate_forward_ref,
        # 0.3.57
        evaluate_forward_ref as evaluateForwardRef
    )
    
else:
    
    class Format(IntegerEnum): # 0.3.54
        VALUE = 1
        VALUE_WITH_FAKE_GLOBALS = 2
        FORWARDREF = 3
        STRING = 4
    
    if TypingExtensionsVersionInfo >= (4, 6): # Py3.7+
        from typing_extensions import TypeAliasType as TypeAliasType # 0.3.26rc1
        
    elif _sys.version_info >= (3, 12):
        from typing import TypeAliasType as TypeAliasType # 0.3.26rc1
    
    if TypingExtensionsVersionInfo >= (4, 13): # Py3.8+
        from typing_extensions import (
            # 0.3.57
            evaluate_forward_ref as evaluate_forward_ref, # type: ignore
            evaluate_forward_ref as evaluateForwardRef # type: ignore
        )
            
    if TypingExtensionsVersionInfo >= (4, 14): # Py3.9+
        from typing_extensions import (
            Reader as Reader, # type: ignore
            Writer as Writer # type: ignore
        )
        
    else:
        @runtime
        class Reader(Protocol[T_con]):
            """Protocol for simple I/O reader instances.

            This protocol only supports blocking I/O.
            """
            __slots__ = ()
            
            @abstractmethod
            def read(self, size: T_con = ..., /) -> int:
                """Read data from the input stream and return it.

                If *size* is specified, at most *size* items (bytes/characters) will be
                read.
                """

        @runtime
        class Writer(Protocol[T_cov]):
            """Protocol for simple I/O writer instances.

            This protocol only supports blocking I/O.
            """

            __slots__ = ()

            @abstractmethod
            def write(self, data: int, /) -> T_cov:
                """Write *data* to the output stream and return the number of items written."""
                

### ****************** Py3.15: 10/2026 ************************
# If you are unfamiliar of PEP 728 about extra items in
# 'typing.TypedDict', PEP 728 was accepted and is planned for
# Python 3.15. 'typing_extensions' forgot one detail: set their
# internal value for PEP 728 check to 'False'. I will redo this
# statement in latest version, if anything changes with this PEP.
#
# For 'frozendict' check PEP 814
if _sys.version_info >= (3, 15):
    
    from builtins import frozendict
    from typing import (
        # 0.3.37
        TypedDict as TypedDict,
        is_typeddict as is_typeddict,
        # 0.3.54
        is_typeddict as isTypedDict,
        NoExtraItems as NoExtraItems
    ) 
    
else:
    
    if TYPE_CHECKING:
        from _typeshed import SupportsKeysAndGetItem as _KeyItemGetter
    
    class frozendict(AVT_Mapping[KT, VT], _Immutable, _Final):
        """
        Availability: >= 0.3.75 \\
        https://aveyzan.xyz/aveytense#aveytense.extensions.frozendict
        
        Represents an immutable dictionary. Inherits from `collections.abc.Mapping`.
        Since Python 3.15, it equals Python's implementation of this class.
        
        Type hinting note: generic class with 2 type parameters.
        """
        
        __dict: AVT_Dict[KT, VT]
        
        # overloads from 'dict'
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self: frozendict[str, VT], **kwargs: VT) -> None: ...  # pyright: ignore[reportInvalidTypeVarUse]
        @overload
        def __init__(self, map: _KeyItemGetter[KT, VT], /) -> None: ...
        @overload
        def __init__(
            self: frozendict[Union[str, KT], VT],  # pyright: ignore[reportInvalidTypeVarUse]
            map: _KeyItemGetter[str, VT],
            /,
            **kwargs: VT,
        ) -> None: ...
        @overload
        def __init__(self, iterable: AVT_Iterable[AVT_Tuple[KT, VT]], /) -> None: ...
        @overload
        def __init__(
            self: frozendict[Union[str, KT], VT],  # pyright: ignore[reportInvalidTypeVarUse]
            iterable: AVT_Iterable[AVT_Tuple[str, VT]],
            /,
            **kwargs: VT,
        ) -> None: ...
        
        def __init__(self, *args, **kwargs): # >= 0.3.75
            from . import _mangle
            object.__setattr__(self, _mangle(self, "__dict"), type.__call__(dict, *args, **kwargs))
            
        def __str__(self): # >= 0.3.75
            return "{}({})".format(type(self).__name__, self.__dict)
            
        def __repr__(self): # >= 0.3.75
            from . import _ReprStr
            return _ReprStr.format(type(self).__qualname__, id(self))
            
        def get(self, key: KT, default: T = None): # >= 0.3.75
            return self.__dict.get(key, default)
            
        def keys(self): # >= 0.3.75
            return self.__dict.keys()
        
        def items(self): # >= 0.3.75
            return self.__dict.items()
        
        def values(self): # >= 0.3.75
            return self.__dict.values()
        
        def __contains__(self, key: object): # >= 0.3.75
            return key in self.__dict
        
        def __getitem__(self, key: KT): # >= 0.3.75
            return self.__dict.__getitem__(key)
        
        def __eq__(self, other: object): # >= 0.3.75
            return type(other) is type(self) and other.__dict == self.__dict
        
        def __len__(self): # >= 0.3.75
            return len(self.__dict)
        
        def __iter__(self): # >= 0.3.75
            return iter(self.__dict)
        
        # Backporting PEP 584 (Py3.9+, see https://peps.python.org/pep-0584) for Python 3.8.
        # These methods below are provided by 'dict', Mapping ABC doesn't provide these.
        def __or__(self, other: _KeyItemGetter[KT2, VT2]): # >= 0.3.75
            _newdict = cast(
                AVT_Dict[
                    Union[KT, KT2],
                    Union[VT, VT2]
                ],
                self.__dict.copy()
            )
            _newdict.update(other)
            return frozendict(_newdict)
        
        def __ror__(self, other: _KeyItemGetter[KT2, VT2]): # >= 0.3.75
            return self.__or__(other)
        
        # This doesn't exist in Mapping ABC either. 'dict' has it so we re-declare it
        def copy(self): # >= 0.3.75
            return frozendict(self.__dict)
    
    from typing import (
        # ?
        no_type_check_decorator as no_type_check_decorator,
        # 0.3.26rc1
        no_type_check_decorator as noTypeCheckDecorator
    )
    from typing_extensions import (
        # 0.3.37
        TypedDict as TypedDict,
        is_typeddict as is_typeddict, # TE>=4.1
        # 0.3.54
        is_typeddict as isTypedDict
    )
    
    if TypingExtensionsVersionInfo >= (4, 13): # Py3.8+
        from typing_extensions import NoExtraItems as NoExtraItems # type: ignore
    
    _prevent_unused_imports(noTypeCheckDecorator)

if _sys.version_info >= (3, 7):
    
    _prevent_unused_imports(resolveBases)
    
    if TypingExtensionsVersionInfo >= (4, 2): # Py3.7+
        _prevent_unused_imports(assertType, clearOverloads, getOverloads)
    
    if TypingExtensionsVersionInfo >= (4, 6): # Py3.7+
        _prevent_unused_imports(getOriginalBases)

    if TypingExtensionsVersionInfo >= (4, 7): # Py3.7+
        _prevent_unused_imports(getProtocolMembers, isProtocol)
        
    if TypingExtensionsVersionInfo >= (4, 13): # Py3.8+
        _prevent_unused_imports(evaluateForwardRef, getAnnotations) # type: ignore

_prevent_unused_imports(
    T, T1, T2, T3, T4, T5, T6,
    T_con, T1_con, T2_con, T3_con, T4_con, T5_con, T6_con,
    T_cov, T1_cov, T2_cov, T3_cov, T4_cov, T5_cov, T6_cov,
    S, S_con, S_cov, U, U_con, U_cov,
    Ts, P,
    KT, VT, KT_con, KT_cov, VT_con, VT_cov,
    KT1, VT1, KT1_con, KT1_cov, VT1_con, VT1_cov,
    KT2, VT2, KT2_cov, KT2_con, VT2_con, VT2_cov
) # ~._typeparams, 0.3.72

_prevent_unused_imports(AsyncContextManager, ContextManager, MutableSet, AbstractSet)
_prevent_unused_imports(assertNever, dataclassTransform, getArgs, getOrigin, getTypeHints, importModule, isTypedDict, lruCache, noTypeCheck, revealType, singleDispatch, newClass, prepareClass)

import _collections_abc, abc as _abc, _hashlib, hashlib, hmac as _hmac, typing as _typing, typing_extensions as _typing_ext # not for export

# all abstract prefixed decorators: before 0.3.73 in 'aveytense.util'
if hasattr(_abc, "abstractproperty"):
    from abc import abstractproperty as abstractproperty # deprecated since 3.3
    
else:
    class abstractproperty(property):
        """
        Availability: >= 0.3.26rc1

        A decorator class for abstract properties.

        Equivalent invoking decorators `abc.abstractmethod` and in-built `property`.
        """
        __isabstractmethod__ = True

if hasattr(_abc, "abstractstaticmethod"):
    from abc import abstractstaticmethod as abstractstaticmethod # deprecated since 3.3
    
else:
    class abstractstaticmethod(staticmethod):
        """
        Availability: >= 0.3.26rc1

        A decorator class for abstract static methods.

        Equivalent invoking decorators `abc.abstractmethod` and in-built `staticmethod`.
        """
        __isabstractmethod__ = True
        
        def __init__(self, f: AVT_Callable[P, T_cov]):
            f.__isabstractmethod__ = True
            super().__init__(f)

if hasattr(_abc, "abstractclassmethod"):
    from abc import abstractclassmethod as abstractclassmethod # deprecated since 3.3
    
else:
    class abstractclassmethod(classmethod):
        """
        Availability: >= 0.3.26rc1

        A decorator class for abstract class methods.

        Equivalent invoking decorators `abc.abstractmethod` and in-built `classmethod`.
        """
        __isabstractmethod__ = True
        
        def __init__(self, f: AVT_Callable[Concatenate[AVT_Type[T], P], T_cov]):
            f.__isabstractmethod__ = True
            super().__init__(f)
    
class _AsyncNextOperable(Protocol[T_cov]): # >= 0.3.60 // _typeshed.SupportsAnext, see ~.AsyncNextOperable in production code
    def __anext__(self) -> AVT_Awaitable[T_cov]: ...
    
class _AsyncIterOperable(Protocol[T_cov]): # >= 0.3.60 // _typeshed.SupportsAiter, see ~.AsyncIterator in production code
    def __aiter__(self) -> T_cov: ...

_T_anext_cov = TypeVar("_T_anext_cov", covariant = True, bound = _AsyncNextOperable[Any])

if hasattr(_typing_ext, "disjoint_base"): # typing Py3.15+
    from typing_extensions import disjoint_base as disjoint_base

else:
    def disjoint_base(cls: AVT_Type[T]):
        """
        Availability: >= 0.3.56
        
        This decorator marks a class as a disjoint base.

        Child classes of a disjoint base cannot inherit from other disjoint bases that are
        not parent classes of the disjoint base.

        For example:

            @disjoint_base
            class Disjoint1: pass

            @disjoint_base
            class Disjoint2: pass

            class Disjoint3(Disjoint1, Disjoint2): pass  # Type checker error

        Type checkers can use knowledge of disjoint bases to detect unreachable code
        and determine when two types can overlap.

        See PEP 800."""
        cls.__disjoint_base__ = True
        return cls

# 0.3.52
# These both local variables below hold special names that Python uses in lambda and generator expressions.
# We use this way to ensure the change with this attribute's value will happen simultaneously with this project.
_LambdaName = (lambda: None).__name__ # "<lambda>"
_GenExprName = (i for i in (1,)).__qualname__ # "<genexpr>"

class _GenExprTypeMeta(type):
    """Availability: >= 0.3.52"""
    def __instancecheck__(self, obj: object):
        return isinstance(obj, Generator) and obj.__qualname__.endswith(_GenExprName)

class _LambdaTypeMeta(type):
    """Availability: >= 0.3.52"""
    def __instancecheck__(self, obj: object):
        return isinstance(obj, FunctionType) and obj.__name__.endswith(_LambdaName)

class GenExprType(metaclass = _GenExprTypeMeta):
    """
    Availability: >= 0.3.52
    
    Use this class to find, if a generator object is actually created from generator expression, with `isinstance()`.
    """
    __init__ = None
    
class LambdaType(metaclass = _LambdaTypeMeta):
    """
    Availability: >= 0.3.44 \\
    @modified 0.3.52
    
    Use this class to find, if a callable is actually a lambda expression, with `isinstance()`.
    
    NOTE: this class isn't the same as Python's `types.LambdaType`, and it is reserved for `isinstance()` only. `types.LambdaType` is a type alias to `types.FunctionType`
    """
    if False: # projected
        def __new__(
            cls,
            code: CodeType,
            globals: AVT_Dict[str, Any],
            argdefs: Optional[AVT_Tuple[object, ...]] = None,
            closure: Optional[AVT_Tuple[CellType, ...]] = None,
            kwdefaults: Optional[AVT_Dict[str, object]] = None
        ):
            # using assumption 'types.LambdaType' is type alias to 'types.FunctionType',
            # return 'types.FunctionType', just without the 'name' parameter required
            return FunctionType(code, globals, _LambdaName, argdefs, closure, kwdefaults)
    else:
        __init__ = None
    
class _SpecialFormMeta(type):
    """Availability: >= 0.3.52"""
    def __instancecheck__(self, obj: object): # 0.3.53: enhance type checking
        
        from typing import _SpecialForm
        from typing_extensions import _SpecialForm as _ExtSpecialForm
        
        # since 3.13 'typing.Annotated' is instance of 'typing._SpecialForm'
        if _sys.version_info >= (3, 13):
            return isinstance(obj, (_SpecialForm, _ExtSpecialForm))
        else:
            return isinstance(obj, (_SpecialForm, _ExtSpecialForm)) or obj is Annotated
            
class AnnotationForm:
    """
    Availability: >= 0.3.48 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.AnnotationForm
    
    Refer to `_typeshed.AnnotationForm`
    """
    
class ClassInfoType:
    """
    Availability: >= 0.3.60 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.ClassInfoType
    """
    ...
    
class CoroutineWrapperType(AVT_Generator[_T_yield_cov, _T_send_con, _T_return_cov]):
    """
    Availability: >= 0.3.53 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.CoroutineWrapperType
    
    A wrapper object implementing `__await__()` for coroutines
    """
    
class MaybeNone:
    """
    Availability: >= 0.3.57 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.MaybeNone
    
    Refer to `_typeshed.MaybeNone`
    """
    
class Incomplete:
    """
    Availability: >= 0.3.60 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.Incomplete
    
    Refer to `_typeshed.Incomplete`
    """
    
# Let's be honest, I was having trouble re-creating these classes with type annotations.
# In reality none of these are protocols, because these get appropriate values assigned later,
# these definitions are only for correct type hinting
@deprecated("Deprecated since 0.3.75, will be removed in 0.3.78")
class AnyMeta(Protocol):
    """
    Availability: >= 0.3.52
    
    Metaclass of `typing.Any`.
    
    Should be only used as `type(obj) is AnyMeta`
    """
    def __instancecheck__(self, obj: object) -> bool: ...
    def __repr__(self) -> str: ...
    
@final
class DictKeys(AVT_KeysView[KT_cov], Generic[KT_cov, VT_cov]):
    """
    Availability: >= 0.3.53 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.DictKeys
    
    Generic version of class `_collections_abc.dict_keys` (generic only in stub files)
    """
    def __eq__(self, value: object, /) -> bool: ...
    def __reversed__(self) -> AVT_Iterator[KT_cov]: ...
    __hash__: ClassVar[None]  # type: ignore[assignment]
    if _sys.version_info >= (3, 13):
        def isdisjoint(self, other: AVT_Iterable[KT_cov], /) -> bool: ...
    if _sys.version_info >= (3, 10):
        @property
        def mapping(self) -> MappingProxyType[KT_cov, VT_cov]: ...

@final
class DictValues(AVT_ValuesView[VT_cov], Generic[KT_cov, VT_cov]):
    """
    Availability: >= 0.3.53 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.DictValues
    
    Generic version of class `_collections_abc.dict_values` (generic only in stub files)
    """
    def __reversed__(self) -> AVT_Iterator[VT_cov]: ...
    if _sys.version_info >= (3, 10):
        @property
        def mapping(self) -> MappingProxyType[KT_cov, VT_cov]: ...

@final
class DictItems(AVT_ItemsView[KT_cov, VT_cov]):
    """
    Availability: >= 0.3.53 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.DictItems
    
    Generic version of class `_collections_abc.dict_items` (generic only in stub files)
    """
    def __eq__(self, value: object, /) -> bool: ...
    def __reversed__(self) -> AVT_Iterator[AVT_Tuple[KT_cov, VT_cov]]: ...
    __hash__: ClassVar[None]  # type: ignore[assignment]
    if _sys.version_info >= (3, 13):
        def isdisjoint(self, other: AVT_Iterable[AVT_Tuple[KT_cov, VT_cov]], /) -> bool: ...
    if _sys.version_info >= (3, 10):
        @property
        def mapping(self) -> MappingProxyType[KT_cov, VT_cov]: ...

if False: # < 0.3.57
    class ProtocolMeta(Protocol):
        """Availability: >= 0.3.52"""
        __protocol_attrs__: ClassVar[AVT_Set[str]]
        def __init__(cls, *args: Any, **kwargs: Any) -> None: ...
        def __new__(
            mcls: AVT_Type[Self],
            name: str,
            bases: AVT_Tuple[type, ...],
            namespace: AVT_Dict[str, Any],
            /,
            **kwargs: Any
        ) -> Self: ...
        def __subclasscheck__(self, cls: type) -> bool: ...
        def __instancecheck__(self, obj: object) -> bool: ...
    
class SpecialForm(metaclass = _SpecialFormMeta):
    """
    Availability: >= 0.3.52 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.SpecialForm
    
    Use this class to find, if a type is actually a special form from `typing`
    """

if False: # < 0.3.57
    class TypedDictMeta(Protocol):
        """Availability: >= 0.3.52"""
        def __new__(cls, typename: str, fields: AVT_Dict[str, Any] = {}, /, *, total: bool = True) -> Self: ...

class TypingNoDefaultType:
    """Availability: >= 0.3.53"""
    
class TypingTupleType(tuple):
    """
    Availability: >= 0.3.53 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.TypingTupleType
    
    Internal class for deprecated type alias `typing.Tuple`
    """

class TypingGenericType(Protocol):
    """
    Availability: >= 0.3.52 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.TypingGenericType
    
    The base class for almost all internal classes that build special forms in the `typing` library.
    """
    _name: Optional[str] # ?
    _inst: bool # ?
    @property
    def __origin__(self) -> Union[type, TypeAliasType]: ...
    @property
    def __args__(self) -> AVT_Tuple[Any, ...]: ...
    @property
    def __parameters__(self) -> AVT_Tuple[Any, ...]: ...
    if _sys.version_info >= (3, 9):
        __slots__: None
        def __init__(self, origin: type, args: AVT_Tuple[Any, ...], *, inst: bool = True, name: Optional[str] = None) -> None: ...
    else:
        _special: bool # ?
        def __init__(self, origin: type, args: Any, *, inst: bool = True, special: bool = False, name: Optional[str] = None) -> None: ...
    def __eq__(self, other: Self) -> bool: ...
    def __hash__(self) -> int: ...
    if _sys.version_info >= (3, 10):
        def __or__(self, other: type) -> UnionType: ...
        def __ror__(self, other: type) -> UnionType: ...
    else:
        def __or__(self, other: type) -> TypingUnionType: ...
        def __ror__(self, other: type) -> TypingUnionType: ...
    def __getitem__(self, args: Any) -> Self: ...
    def __repr__(self) -> str: ...
    def __iter__(self) -> AVT_Generator[Any, Any, None]: ...
    def __reduce__(self) -> AVT_Tuple[Any, ...]: ...
    def copy_with(self, args: Any) -> Self: ...
    def _determine_new_args(self, args: Any) -> AVT_Tuple[Any, ...]: ...
    def _make_substitution(self, args: AVT_Iterable[type], new_arg_by_param: Any) -> AVT_List[Any]: ...
    ### inherited from typing._BaseGenericAlias ###
    def __dir__(self) -> AVT_List[str]: ...
    def __instancecheck__(self, obj: object) -> bool: ...
    def __subclasscheck__(self, cls: type) -> NoReturn: ...
    def __setattr__(self, attr: str, val: Any) -> None: ...
    def __getattr__(self, attr: str) -> Any: ...
    def __mro_entries__(self, bases: AVT_Iterable[object]) -> AVT_Tuple[type, ...]: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ... 

class TypingAnnotatedType(TypingGenericType, Protocol):
    """
    Availability: >= 0.3.52 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.TypingAnnotatedType
    
    The type of `typing.Annotated`.
    
    This should be used only in inspections, not really in production code.
    """
    __iter__: None
    @property
    def __origin__(self) -> Union[type, TypeAliasType]: ...
    @property
    def __metadata__(self) -> Any: ...
    def __init__(self, origin: type, metadata: Any) -> None: ...
    def __repr__(self) -> str: ...
    def __reduce__(self) -> AVT_Tuple[Any, ...]: ...
    def __eq__(self, other: Self) -> bool: ...
    def __hash__(self) -> int: ...
    def __getattr__(self, attr: str) -> Any: ...
    def __mro_entries__(self, bases: AVT_Iterable[object]) -> AVT_Tuple[type, ...]: ...
    def copy_with(self, args: Any) -> Self: ...
    
class TypingCallableType(TypingGenericType, Protocol):
    """
    Availability: >= 0.3.52 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.TypingCallableType
    
    The type of `typing.Callable`.
    
    This should be used only in inspections, not really in production code.
    """
    __iter__: None
    def __repr__(self) -> str: ...
    def __reduce__(self) -> AVT_Tuple[Any, ...]: ...
    
class TypingConcatenateType(TypingGenericType, Protocol):
    """
    Availability: >= 0.3.52 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.TypingConcatenateType
    
    The type of `typing.Concatenate`.
    
    This should be used only in inspections, not really in production code.
    """
    def copy_with(self, args: Any) -> Self: ...
    
class TypingLiteralType(TypingGenericType, Protocol):
    """
    Availability: >= 0.3.52 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.TypingLiteralType
    
    The type of `typing.Literal`.
    
    This should be used only in inspections, not really in production code.
    """
    def __eq__(self, other: Self) -> bool: ...
    def __hash__(self) -> int: ...

if _sys.version_info >= (3, 9):
    
    class TypingSpecialGenericType(Protocol):
        """
        Availability: >= 0.3.59 \\
        https://aveyzan.xyz/aveytense#aveytense.extensions.TypingSpecialGenericType
        
        The type of the deprecated generic classes from the `typing` library.
    
        This should be used only in inspections, not really in production code.
        """
        __iter__: None
        __slots__: None # undocumented
        @property
        def __origin__(self) -> Union[type, TypeAliasType]: ...
        def __init__(self, origin: type, nparams: int, *, inst: bool = True, name: Optional[str] = None, defaults: AVT_Tuple[type, ...] = ()) -> None: ...
        def __getitem__(self, params: Any) -> TypingGenericType: ...
        def copy_with(self, params: Any) -> TypingGenericType: ...
        def __repr__(self) -> str: ...
        def __subclasscheck__(self, cls: type) -> bool: ...
        def __reduce__(self) -> Optional[str]: ...
        # Parameter names in __or__ and __ror__ are consistent in the code these methods are in 'typing._SpecialGenericAlias'.
        def __or__(self, right: type) -> TypingUnionType: ...
        def __ror__(self, left: type) -> TypingUnionType: ...
        def __call__(self, *args: Any, **kwds: Any) -> Any: ...
        def __mro_entries__(self, bases: AVT_Iterable[object]) -> AVT_Tuple[type, ...]: ...
        def __dir__(self) -> AVT_List[str]: ...
        def __instancecheck__(self, obj: object) -> bool: ...
        def __subclasscheck__(self, cls: type) -> NoReturn: ...
        def __setattr__(self, attr: str, val: Any) -> None: ...
        def __getattr__(self, attr: str) -> Any: ...
        
        
    if _sys.version_info < (3, 13, 0, "beta"):
        
        class TypingExtensionsSpecialGenericType(TypingSpecialGenericType):
            """Availability: >= 0.3.59"""
        
else:
    class TypingSpecialGenericType(TypingGenericType, Protocol):
        """
        Availability: >= 0.3.59 \\
        https://aveyzan.xyz/aveytense#aveytense.extensions.TypingSpecialGenericType
        
        The type of the deprecated generic classes from the `typing` library.
    
        This should be used only in inspections, not really in production code.
        """
        ...
    
class TypingUnionType(TypingGenericType, Protocol):
    """
    Availability: >= 0.3.52 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.TypingUnionType
    
    The type of `typing.Union` before Python 3.14. Since Python 3.14 equivalent to `typing.Union`
    
    This should be used only in inspections, not really in production code.
    
    This allows to use `isinstance()` without any deviations regardless of the used Python version. However,
    in case of `types.UnionType` (Python 3.10+), use `Tense.isUnion()` class method to check for both.
    """
    __iter__: None
    def __eq__(self, other: Self) -> bool: ...
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __reduce__(self) -> AVT_Tuple[Any, ...]: ...
    def __instancecheck__(self, obj: object) -> bool: ...
    def __subclasscheck__(self, cls: type) -> bool: ...
    def copy_with(self, args: Any) -> Self: ...
    
class TypingUnpackType(TypingGenericType, Protocol):
    """
    Availability: >= 0.3.52
    
    Retrieves internal class for the `typing.Unpack` class
    """
    def __repr__(self) -> str: ...
    def __getitem__(self, args: Any) -> Self: ...
    @property
    def __typing_unpacked_tuple_args__(self) -> Optional[AVT_Tuple[Any, ...]]: ...
    @property
    def __typing_is_unpacked_typevartuple__(self) -> bool: ...

### Itertools ###
# 0.3.55a2+

from itertools import (
    # 0.3.55a2
    accumulate as accumulate, 
    chain as chain,
    combinations as combinations,
    combinations_with_replacement as combinations_with_replacement,
    compress as compress,
    count as count,
    cycle as cycle,
    dropwhile as dropwhile,
    filterfalse as filterfalse,
    groupby as groupby,
    islice as islice,
    permutations as permutations,
    product as product,
    repeat as repeat,
    starmap as starmap,
    takewhile as takewhile,
    tee as tee,
    zip_longest as zip_longest
)

if _sys.version_info >= (3, 10):
    from itertools import pairwise as pairwise # 0.3.55a2
    
else:
    
    class pairwise: # 0.3.55a2
        """
        Return an iterator of overlapping pairs taken from the input iterator.

        s -> (s0, s1), (s1, s2), (s2, s3), ...
        """
        
        def __new__(cls, iterable: AVT_Iterable[T]):
            
            if not isinstance(iterable, Iterable):
                error = TypeError("expected an iterable object")
                raise error
            
            _iterator = iter(iterable)
            a = next(_iterator, None)

            for b in _iterator:
                yield a, b
                a = b

# 'itertools.batched' is defined since Python 3.12, but we add the 'strict' parameter before 3.13
if _sys.version_info >= (3, 13):
    from itertools import batched as batched # 0.3.55a2

else:
    class batched: # 0.3.55a2
        """
        Batch data into tuples of length n. The last batch may be shorter than n.

        Loops over the input iterable and accumulates data into tuples up to size n. The input is consumed lazily,
        just enough to fill a batch. The result is yielded as soon as a batch is full or when the input iterable is
        exhausted.
        ```
        >>> for batch in batched('ABCDEFG', 3):
        ...     print(batch)
        ...
        ('A', 'B', 'C')
        ('D', 'E', 'F')
        ('G',)
        ```
        If "strict" is True, raises a ValueError if the final batch is shorter than n.
        """
        
        def __new__(cls, iterable: AVT_Iterable[T], n: int, *, strict: bool = False):
            
            if not isinstance(iterable, Iterable):
                error = TypeError("expected an iterable object")
                raise error
            
            if not isinstance(n, int) or (isinstance(n, int) and n < 1):
                error = ValueError("expected 1 or above in parameter 'n'")
                raise error
            
            i = 0
            _list = []
            _extract_from = tuple(iterable)
            
            if strict and len(_extract_from) % n != 0:
                error = ValueError("on strict mode, length of the iterable object must be divisible by 'n'")
                raise error
            
            while i < len(_extract_from):
                _list.append(_extract_from[i : i + n])
                i += n
                
            for e in _list:
                yield e

### AVT Types ###

# 'array', 'builtins', 'types', 0.3.54+
if _sys.version_info >= (3, 12):
    from array import array as AVT_Array
    
else:
    class AVT_Array(array, Generic[_T_array]):
        """Availability: >= 0.3.54 // Generic version of `array.array`"""
            

if _sys.version_info >= (3, 9):
    from builtins import enumerate as AVT_Enumerate # >= 0.3.55a2
    from types import GenericAlias as AVT_GenericAlias # >= 0.3.55a1
else:
    
    class AVT_Enumerate(enumerate, Generic[T]):
        """Availability: >= 0.3.55a2 // Generic version of `enumerate`"""
    
    AVT_GenericAlias = TypingGenericType # >= 0.3.55a1


class AVT_Filter(filter, Generic[T]):
    """Availability: >= 0.3.55b1 // Generic version of `filter`"""
    
class AVT_Map(map, Generic[T]):
    """
    Availability: >= 0.3.55b1 // Generic version of `map` \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.AVT_Map
    """

if _sys.version_info >= (3, 14):
    from builtins import memoryview as AVT_MemoryView
    
else:
    
    class AVT_MemoryView(AVT_Sequence[_T_memoryview], _Final):
        """
        Availability: >= 0.3.54 // Generic version of `memoryview` \\
        https://aveyzan.xyz/aveytense#aveytense.extensions.AVT_MemoryView
        
        Since Python 3.14 it is a type alias for `memoryview`
        """
        
        __slots__ = ("_AVT_MemoryView__memoryview",)
        
        # 'memoryview' is generic since Python 3.14, but if we only use it in
        # annotations, this shall work fine. better than using 'typing._SpecialGenericAlias'
        # internal class in this case. I will actually need to re-declare this
        # 'typing' class to exclude the deprecation warnings
        __memoryview: memoryview[_T_memoryview]
        
        def __init__(self, obj: ReadableBuffer):
            
            if not isinstance(obj, ReadableBuffer):
                error = TypeError("expected a buffer")
                raise error
            
            self.__memoryview = memoryview(obj)
            
        def __str__(self):
            # mimicking
            h = hex(id(self))[2:]
            if len(h) < 16:
                h = "0" * (16 - len(h)) + h
            
            return "<memory at {}>".format("0x" + h.upper())
            
        @property
        def format(self):
            """
            A string containing the format (in struct module style)
            for each element in the view.
            """
            return self.__memoryview.format
        
        @property
        def itemsize(self):
            """The size in bytes of each element of the memoryview."""
            return self.__memoryview.itemsize
        
        @property
        def shape(self):
            """
            A tuple of ndim integers giving the shape of the memory
            as an N-dimensional array.
            """
            return self.__memoryview.shape
            
        @property
        def strides(self):
            """
            A tuple of ndim integers giving the size in bytes to access
            each element for each dimension of the array.
            """
            return self.__memoryview.strides
        
        @property
        def suboffsets(self):
            """A tuple of integers used internally for PIL-style arrays."""
            return self.__memoryview.suboffsets
        
        
        @property
        def readonly(self):
            """A bool indicating whether the memory is read only."""
            return self.__memoryview.readonly
        
        @property
        def ndim(self):
            """An integer indicating how many dimensions of a multi-dimensional
            array the memory represents."""
            return self.__memoryview.ndim
        
        @property
        def obj(self):
            """The underlying object of the memoryview."""
            return self.__memoryview.obj
        
        @property
        def c_contiguous(self):
            """A bool indicating whether the memory is C contiguous"""
            return self.__memoryview.c_contiguous
        
        @property
        def f_contiguous(self):
            """A bool indicating whether the memory is Fortran contiguous."""
            return self.__memoryview.f_contiguous
        
        @property
        def contiguous(self):
            """A bool indicating whether the memory is contiguous."""
            return self.__memoryview.contiguous
        
        @property
        def nbytes(self):
            """
            The amount of space in bytes that the array would use in
            a contiguous representation.
            """
            return self.__memoryview.nbytes
        
        def __enter__(self):
            return self.__memoryview.__enter__()
        
        def __exit__(
            self,
            exc_type: Optional[AVT_Type[BaseException]],  # noqa: PYI036 # This is the module declaring BaseException
            exc_val: Optional[BaseException],
            exc_tb: Optional[TracebackType],
            /
        ):
            """Release the underlying buffer exposed by the memoryview object."""
            self.__memoryview.__exit__(exc_type, exc_val, exc_tb)
        
        @overload
        def cast(self, format: Literal["c", "@c"], shape: Union[AVT_List[int], AVT_Tuple[int, ...]] = ...) -> _AVT_MemoryView[bytes]: ...
        @overload
        def cast(self, format: Literal["f", "@f", "d", "@d"], shape: Union[AVT_List[int], AVT_Tuple[int, ...]] = ...) -> _AVT_MemoryView[float]: ...
        @overload
        def cast(self, format: Literal["?"], shape: Union[AVT_List[int], AVT_Tuple[int, ...]] = ...) -> _AVT_MemoryView[bool]: ...
        @overload
        def cast(self, format: Literal['b', 'B', '@b', '@B', 'h', 'H', '@h', '@H', 'i', 'I', '@i', '@I', 'l', 'L', '@l', '@L', 'q', 'Q', '@q', '@Q', 'P', '@P'], shape: Union[AVT_List[int], AVT_Tuple[int, ...]] = ...) -> _AVT_MemoryView: ...
        def cast(self, format, shape = _Missing):
            
            if shape is _Missing:
                return _AVT_MemoryView(self.__memoryview.cast(format))
            else:
                return _AVT_MemoryView(self.__memoryview.cast(format, shape))
            
        @overload
        def __getitem__(self, key: Union[Indexable, AVT_Tuple[Indexable, ...]], /) -> _T_memoryview: ...
        @overload
        def __getitem__(self, key: slice, /) -> _AVT_MemoryView[_T_memoryview]: ...
        def __getitem__(self, key, /):
            return self.__memoryview.__getitem__(key)
        
        def __contains__(self, x):
            return x in self.__memoryview
        
        def __iter__(self):
            return iter(self.__memoryview)
        
        def __len__(self):
            return len(self.__memoryview)
        
        def __eq__(self, value: object, /):
            return value == self.__memoryview
        
        def __hash__(self):
            return hash(self.__memoryview)
        
        @overload
        def __setitem__(self, key: slice, value: ReadableBuffer, /) -> None: ...
        @overload
        def __setitem__(self, key: Union[Indexable, AVT_Tuple[Indexable, ...]], value: _T_memoryview, /) -> None: ...
        def __setitem__(self, key, value, /):
            self.__memoryview.__setitem__(key, value)
        
        # Python 3.9 and older had 'None' as 'order' default value
        def tobytes(self, order: Optional[Literal["C", "F", "A"]] = "C"):
            """
            Return the data in the buffer as a byte string.

            Order can be {'C', 'F', 'A'}. When order is 'C' or 'F', the data of the
            original array is converted to C or Fortran order. For contiguous views,
            'A' returns an exact copy of the physical memory. In particular, in-memory
            Fortran order is preserved. For non-contiguous views, the data is converted
            to C first. order=None is the same as order='C'.
            """
            return self.__memoryview.tobytes(order)
        
        def tolist(self):
            """Return the data in the buffer as a list of elements."""
            return self.__memoryview.tolist()
        
        # Python 3.8+
        def toreadonly(self):
            """Return a readonly version of the memoryview."""
            return self.__memoryview.toreadonly()
        
        def release(self):
            """Release the underlying buffer exposed by the memoryview object."""
            return self.__memoryview.release()
        
        def hex(self, sep: Union[str, bytes] = _Missing, bytes_per_sep: Indexable = 1):
            """
            Return the data in the buffer as a str of hexadecimal numbers.

            - `sep` - An optional single character or byte to separate hex bytes.
            - `bytes_per_sep` - How many bytes between separators. Positive values count from the
            right, negative values count from the left.
            """
            
            if sep is _Missing:
                return self.__memoryview.hex(bytes_per_sep=bytes_per_sep)
            else:
                return self.__memoryview.hex(sep, bytes_per_sep)
            
        if _sys.version_info >= (3, 12):
            
            def __buffer__(self, flags: int, /):
                return self.__memoryview.__buffer__(flags)
            def __release_buffer__(self, buffer: AVT_MemoryView, /):
                self.__memoryview.__release_buffer__(self.__memoryview)
        
        # Python 3.14 backported methods
        def index(self, value: object, start: Indexable = 0, stop: Indexable = _sys.maxsize, /):
            """
            Return first index of value.

            Raises ValueError if the value is not present.
            """
            return self.__memoryview.tolist().index(value, start, stop)
        
        def count(self, value: object, /):
            """Return number of occurrences of value."""
            return self.__memoryview.tolist().count(value)

if _sys.version_info >= (3, 10): 
    from types import UnionType as AVT_UnionType # >= 0.3.55a1
else:
    AVT_UnionType = TypingUnionType # >= 0.3.55a1
    
class AVT_Reversed(reversed, Generic[T]):
    """Availability: >= 0.3.55b1 // Generic version of `reversed`"""

# >> https://github.com/python/cpython/issues/128335
if _sys.version_info >= (3, 15): 
    from builtins import slice as AVT_Slice # >= 0.3.55b1
    
else:

    class AVT_Slice(Generic[_T_start_cov, _T_stop_cov, _T_step_cov], _Final):
        """
        Availability: >= 0.3.55b1 // Generic version of `slice` \\
        https://aveyzan.xyz/aveytense#aveytense.extensions.AVT_Slice
        
        Since Python 3.15 it is a type alias for `slice`
        """
        
        __slots__ = ("_AVT_Slice__slice",)
        
        # 'slice' is generic since Python 3.15, but if we only use it in
        # annotations, this shall work fine
        __slice: slice[_T_start_cov, _T_stop_cov, _T_step_cov]
        
        @overload
        def __init__(cls, start: None, stop: None = None, step: None = None, /) -> None: ...
        @overload
        def __init__(cls, stop: _T_stop_cov, /) -> None: ...
        @overload
        def __init__(cls, start: _T_start_cov, stop: None, step: None = None, /) -> None: ...
        @overload
        def __init__(cls, start: None, stop: _T_stop_cov, step: None = None, /) -> None: ...
        @overload
        def __init__(cls, start: _T_start_cov, stop: _T_stop_cov, step: None = None, /) -> None: ...
        @overload
        def __init__(cls, start: None, stop: None, step: _T_step_cov, /) -> None: ...
        @overload
        def __init__(cls, start: _T_start_cov, stop: None, step: _T_step_cov, /) -> None: ...
        @overload
        def __init__(cls, start: None, stop: _T_stop_cov, step: _T_step_cov, /) -> None: ...
        @overload
        def __init__(cls, start: _T_start_cov, stop: _T_stop_cov, step: _T_step_cov, /) -> None: ...
        
        def __init__(self, *args):
            
            if len(args) not in (1, 2, 3):
                error = TypeError("expected 1-3 arguments, got {}".format(len(args)))
                raise error
            
            if len(args) == 1:
                self.__slice = slice(args[0])
            elif len(args) == 2:
                self.__slice = slice(args[0], args[1])
            else:
                self.__slice = slice(args[0], args[1], args[2])
        
        @property
        def start(self) -> _T_start_cov:
            return self.__slice.start

        @property
        def stop(self) -> _T_stop_cov:
            return self.__slice.stop
        
        @property
        def step(self) -> _T_step_cov:
            return self.__slice.step
        
        def __str__(self):
            return "{}({}, {}, {})".format(type(self).__name__, self.start, self.stop, self.step)
                
        def __eq__(self, value: object, /):
            return self.__slice.__eq__(value)
    
        if _sys.version_info >= (3, 12):
            def __hash__(self):
                return hash(self.__slice)

        def indices(self, len: Indexable, /):
            """
            S.indices(len) -> (start, stop, stride)

            Assuming a sequence of length len, calculate the start and stop
            indices, and the stride length of the extended slice described by
            S. Out of bounds indices are clipped in a manner consistent with the
            handling of normal slices.
            """
            return self.__slice.indices(len)
        
if _sys.version_info >= (3, 8): # TE>=4.10, Py3.8+
    from typing_extensions import TypeIs as AVT_TypeIs # 0.3.56
else:
    from typing_extensions import TypeGuard as AVT_TypeIs # 0.3.56
    
class AVT_Zip(zip, Generic[T_cov]):
    """Availability: >= 0.3.55a2 // Generic version of `zip`"""

# 'itertools', 0.3.55a2+
class AVT_Accumulate(accumulate, Generic[T]):
    """Availability: >= 0.3.55a2 // Generic version of `itertools.accumulate`"""
    
class AVT_Batched(batched, Generic[T_cov]):
    """
    Availability: >= 0.3.55a2 // Generic version of `itertools.batched`
    
    `batched` exists since 3.12, and it is backported in-code, to include `strict` \\
    keyword parameter that was added in 3.13. Use `aveytense.extensions.batched` \\
    import to use in versions 3.8 - 3.12!
    """
    
class AVT_Chain(chain, Generic[T]):
    """Availability: >= 0.3.55a2 // Generic version of `itertools.chain`"""
    
class AVT_Combinations(combinations, Generic[T_cov]):
    """Availability: >= 0.3.55a2 // Generic version of `itertools.combinations`"""
    
class AVT_CombinationsReplacement(combinations_with_replacement, Generic[T_cov]):
    """Availability: >= 0.3.55a2 // Generic version of `itertools.combinations_with_replacement`"""
    
class AVT_Compress(compress, Generic[T]):
    """Availability: >= 0.3.55a2 // Generic version of `itertools.compress`"""
    
class AVT_Count(count, Generic[_T_count]):
    """Availability: >= 0.3.55a2 // Generic version of `itertools.count`"""
    
class AVT_Cycle(cycle, Generic[T]):
    """Availability: >= 0.3.55a2 // Generic version of `itertools.cycle`"""
    
class AVT_DropWhile(dropwhile, Generic[T]):
    """Availability: >= 0.3.55a2 // Generic version of `itertools.dropwhile`"""
    
class AVT_FilterFalse(filterfalse, Generic[T]):
    """Availability: >= 0.3.55a2 // Generic version of `itertools.filterfalse`"""
    
class AVT_GroupBy(groupby, Generic[T1_cov, T2_cov]):
    """Availability: >= 0.3.55a2 // Generic version of `itertools.groupby`"""
    
class AVT_Islice(islice, Generic[T]):
    """Availability: >= 0.3.55a2 // Generic version of `itertools.islice`"""
    
class AVT_Pairwise(pairwise, Generic[T_cov]):
    """
    Availability: >= 0.3.55a2 // Generic version of `itertools.pairwise`
    
    `pairwise` exists since 3.10, and it is backported
    """
    
class AVT_Permutations(permutations, Generic[T_cov]):
    """Availability: >= 0.3.55a2 // Generic version of `itertools.permutations`"""
    
class AVT_Product(product, Generic[T_cov]):
    """Availability: >= 0.3.55a2 // Generic version of `itertools.product`"""
    
class AVT_Repeat(repeat, Generic[T]):
    """Availability: >= 0.3.55a2 // Generic version of `itertools.repeat`"""
    
class AVT_StarMap(starmap, Generic[T_cov]):
    """Availability: >= 0.3.55a2 // Generic version of `itertools.starmap`"""
    
class AVT_TakeWhile(takewhile, Generic[T]):
    """Availability: >= 0.3.55a2 // Generic version of `itertools.takewhile`"""
    
class AVT_ZipLongest(zip_longest, Generic[T_cov]):
    """Availability: >= 0.3.55a2 // Generic version of `itertools.zip_longest`"""
    
_prevent_unused_imports(
    AVT_AbstractSet,
    AVT_Accumulate,
    AVT_Array,
    AVT_AsyncContextManager,
    AVT_AsyncGenerator,
    AVT_AsyncIterable,
    AVT_AsyncIterator,
    AVT_Awaitable,
    AVT_Batched,
    AVT_Callable,
    AVT_Chain,
    AVT_ChainMap,
    AVT_Collection,
    AVT_Combinations,
    AVT_CombinationsReplacement,
    AVT_Compress,
    AVT_Container,
    AVT_ContextManager,
    AVT_Coroutine,
    AVT_Count,
    AVT_Counter,
    AVT_Cycle,
    AVT_DefaultDict,
    AVT_Deque,
    AVT_Dict,
    AVT_DropWhile,
    AVT_Enumerate,
    AVT_Filter,
    AVT_FilterFalse,
    AVT_FrozenSet,
    AVT_Generator,
    AVT_GenericAlias,
    AVT_GroupBy,
    AVT_Islice,
    AVT_ItemsView,
    AVT_Iterable,
    AVT_Iterator,
    AVT_KeysView,
    AVT_List,
    AVT_Map,
    AVT_Mapping,
    AVT_MappingView,
    AVT_Match,
    AVT_MemoryView,
    AVT_MutableMapping,
    AVT_MutableSequence,
    AVT_MutableSet,
    AVT_OrderedDict,
    AVT_Pairwise,
    AVT_PathLike,
    AVT_Pattern,
    AVT_Permutations,
    AVT_Product,
    AVT_Repeat,
    AVT_Reversed,
    AVT_Reversible,
    AVT_Sequence,
    AVT_Set,
    AVT_StarMap,
    AVT_TakeWhile,
    AVT_Tuple,
    AVT_Type,
    AVT_TypeIs,
    AVT_UnionType,
    AVT_ValuesView,
    AVT_Zip,
    AVT_ZipLongest
)

### Protocol Classes ###

@runtime
class NextOperable(Protocol[T_cov]):
    """
    Availability: >= 0.3.26b3 // `_typeshed.SupportsNext` \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.NextOperable

    A runtime protocol class with method `__next__()` that equals `next(self)`. \\
    Returned type is addicted to covariant type parameter.
    """
    def __next__(self) -> T_cov: ...

@runtime
class AsyncNextOperable(Protocol[T_cov]):
    """
    Availability: >= 0.3.26b3 // `_typeshed.SupportsAnext` \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.AsyncNextOperable

    A runtime protocol class with method `__anext__()`. Returned type must be an awaitable \\
    of type represented by covariant type parameter.
    
    Similar to `collections.abc.AsyncIterator`, however, no `__aiter__()` method is included.
    """
    def __anext__(self) -> Awaitable[T_cov]: ... # 0.3.60: remove 'async' keyword
    
@runtime
class ExitOperable(Protocol):
    """
    Availability: >= 0.3.26b3 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.ExitOperable

    A runtime protocol class with method `__exit__()`. Returned type is addicted to covariant type parameter.
    """
    def __exit__(
        self,
        exc_type: Optional[AVT_Type[Exception]] = None,
        exc_value: Optional[Exception] = None,
        traceback: Optional[TracebackType] = None
    ) -> bool: ...

@runtime
class AsyncExitOperable(Protocol[T_cov]):
    """
    Availability: >= 0.3.26b3 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.AsyncExitOperable

    A runtime protocol class with method `__aexit__()`. Returned type must be an awaitable \\
    of type represented by covariant type parameter.
    """
    async def __aexit__(
        self,
        exc_type: Optional[AVT_Type[Exception]] = None,
        exc_value: Optional[Exception] = None,
        traceback: Optional[TracebackType] = None
    ) -> Awaitable[T_cov]: ...

@runtime
class EnterOperable(Protocol[T_cov]):
    """
    Availability: >= 0.3.26b3 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.EnterOperable

    A runtime protocol class with method `__enter__()`. Returned type is addicted to covariant type parameter.
    """
    def __enter__(self) -> T_cov: ...

@runtime
class AsyncEnterOperable(Protocol[T_cov]):
    """
    Availability: >= 0.3.26b3 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.AsyncEnterOperable

    A runtime protocol class with method `__aenter__()`. Returned type must be an awaitable \\
    of type represented by covariant type parameter.
    """
    async def __aenter__(self) -> Awaitable[T_cov]: ...
    
@runtime
class ItemGetter(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc3 // `_typeshed.SupportsGetItem` \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.ItemGetter

    A runtime protocol class with method `__getitem__()`. Type parameters:
    - first equals type for `key`
    - second equals returned type

    This method is invoked whether we want to get value \\
    via index notation `self[key]`, as instance of the class.
    """
    def __getitem__(self, key: T_con, /) -> T_cov: ...

if _sys.version_info >= (3, 9):
    
    @runtime
    class ClassItemGetter(Protocol):
        """
        Availability: >= 0.3.26rc3

        A runtime protocol class with method `__class_getitem__()`. \\
        https://aveyzan.xyz/aveytense#aveytense.extensions.ClassItemGetter

        This method is invoked whether we want to get value via index notation `cls[key]`
        """
        def __class_getitem__(cls, args: Any, /) -> GenericAlias: ...

class SizeableItemGetter(Sized, ItemGetter[int, T_cov]):
    """
    Availability: >= 0.3.27a3 // `_typeshed.SupportsLenAndGetItem`

    A runtime protocol class with methods `__len__()` and `__getitem__()`. Type parameters:
    - first equals returned type for `__getitem__()`
    """

@runtime
class ItemSetter(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc3 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.ItemSetter

    A runtime protocol class with method `__setitem__()`. Type parameters:
    - first equals type for `key`
    - second equals type for `value`

    This method is invoked whether we want to set a new value for \\
    specific item accessed by `key`, as `self[key] = value`.
    """
    def __setitem__(self, key: T_con, value: T_cov, /) -> None: ...

@runtime
class ItemDeleter(Protocol[T_con]):
    """
    Availability: >= 0.3.26rc3 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.ItemDeleter

    A runtime protocol class with method `__delitem__()`. Type parameters:
    - first equals type for `key`

    This method is invoked whether we want to delete specific item \\
    using `del` keyword as `del self[key]`.
    """
    def __delitem__(self, key: T_con, /) -> None: ...
    
class ItemManager(
    ItemGetter[T_con, T_cov],
    ItemSetter[T_con, T_cov],
    ItemDeleter[T_con]
):
    """
    Availability: >= 0.3.26rc3 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.ItemManager

    A runtime protocol class with following methods:
    - `__getitem__()` - two type parameters (key type, return type)
    - `__setitem__()` - two type parameters (key type, return type)
    - `__delitem__()` - one type parameter (key type)
    """
    ...

@runtime
class Getter(Protocol[T_cov]):
    """
    Availability: >= 0.3.26 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.Getter

    A runtime protocol class with method `__get__()`. Type parameters:
    - first equals returned type
    """
    def __get__(self, instance: object, owner: Optional[type] = None, /) -> T_cov: ...

@runtime
class Setter(Protocol[T_con]):
    """
    Availability: >= 0.3.27a3 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.Setter

    A runtime protocol class with method `__set__()`. Type parameters:
    - first equals type for `value`
    """
    def __set__(self, instance: object, value: T_con, /) -> None: ...
    
@runtime
class Deleter(Protocol):
    """
    Availability: >= 0.3.44 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.Deleter
    
    A runtime protocol class with method `__delete__()`.
    """
    def __delete__(self, instance: object, /) -> None: ...
    
class Descriptor(
    Setter[T_con],
    Getter[T_cov],
    Deleter
):
    """
    Availability: >= 0.3.44 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.Descriptor
    
    A runtime protocol class with descriptor methods: `__get__()`, `__set__()` and `__delete__()`
    """
    ...

@runtime
@deprecated("Deprecated since 0.3.75, will be removed in 0.3.78.")
class FinalDescriptor(Protocol[T_cov]):
    """
    Availability: >= 0.3.44 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.FinalDescriptor
    
    A runtime protocol class providing descriptor methods, just `__set__()` and `__delete__()` throw an error. \\
    The same as `aveytense.util.finalproperty` works.
    """
    def __get__(self, instance: Optional[object], owner: Optional[type] = None, /) -> T_cov: ...
    def __set__(self, instance: Optional[object], value: Any, /) -> NoReturn: ...
    def __delete__(self, instance: Optional[object], /) -> NoReturn: ...

class KeysProvider(ItemGetter[KT_con, Any]):
    """
    Availability: >= 0.3.26 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.KeysProvider

    A runtime protocol class with method `keys()`. Type parameters:
    - first equals key
    - second equals value
    """
    def keys(self) -> AVT_Iterable[KT_con]: ...

@runtime
class ItemsProvider(Protocol[KT_cov, VT_cov]):
    """
    Availability: >= 0.3.26 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.ItemsProvider

    A runtime protocol class with method `items()`. Type parameters:
    - first equals key
    - second equals value
    """
    def items(self) -> AVT_AbstractSet[AVT_Tuple[KT_cov, VT_cov]]: ...
    
@runtime
class Buffer(Protocol):
    """
    Availability: >= 0.3.44 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.Buffer
    
    A runtime protocol class with method `__buffer__()`.
    """
    def __buffer__(self, flags: int, /) -> memoryview: ...
    
Buffer = _Buffer

@runtime
class BufferReleaser(Protocol):
    """
    Availability: >= 0.3.26 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.BufferReleaser

    A runtime protocol class with method `__release_buffer__()`.
    """
    def __release_buffer__(self, buffer: memoryview, /) -> None: ...
    
# >= 0.3.44; < 0.3.54 as 'BufferManager'
@runtime
class BufferProtocol(Protocol):
    """
    Availability: >= 0.3.54 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.BufferProtocol
    
    This runtime protocol class allows to implement buffer protocol to specific class
    """
    def __buffer__(self, flags: int, /) -> memoryview: ...
    def __release_buffer__(self, buffer: memoryview, /) -> None: ...

@runtime
class NewArgumentsGetter(Protocol[T_cov]):
    """
    Availability: >= 0.3.26

    A runtime protocol class with method `__getnewargs__()`.
    """
    def __getnewargs__(self) -> AVT_Tuple[T_cov]: ...

@runtime
class SubclassHooker(Protocol):
    """
    Availability: >= 0.3.26

    A runtime protocol class with method `__subclasshook__()`.

    Description:
    "Abstract classes can override this to customize `issubclass()`.
    This is invoked early on by `abc.ABCMeta.__subclasscheck__()`.
    It should return `True`, `False` or `NotImplemented`. If it returns
    NotImplemented, the normal algorithm is used. Otherwise, it
    overrides the normal algorithm (and the outcome is cached)."
    """
    def __subclasshook__(cls, subclass: type, /) -> bool: ...

@runtime
class LengthHintProvider(Protocol):
    """
    Availability: >= 0.3.26rc3

    A runtime protocol class with method `__length_hint__()`.

    This method is invoked like in case of `list` built-in, just on behalf of specific class.
    It should equal invoking `len(self)`, as seen for `list`: "Private method returning
    an estimate of `len(list(it))`".
    """
    def __length_hint__(self) -> int: ...

FSPathProvider = AVT_PathLike
"""Availability: >= 0.3.27a3"""

@runtime
class BytearrayConvertible(Protocol):
    """
    Availability: >= 0.3.26rc3 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.BytearrayConvertible

    A runtime protocol class with method `__bytearray__()`.
    """
    def __bytearray__(self) -> bytearray: ...

@runtime
@deprecated("Deprecated since 0.3.75, will be removed in 0.3.78.")
class ListConvertible(Protocol[T_cov]):
    """
    Availability: >= 0.3.26rc3 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.ListConvertible

    A runtime protocol class with method `toList()`. Invoked via the class method `aveytense.Tense.toList()`
    """
    
    # to 0.3.63 as __tlist__, to 0.3.27a3 as __list__
    def toList(self) -> AVT_List[T_cov]: ...


@runtime
@deprecated("Deprecated since 0.3.75, will be removed in 0.3.78.")
class TupleConvertible(Protocol[T_cov]):
    """
    Availability: >= 0.3.26rc3 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.TupleConvertible

    A runtime protocol class with method `toTuple()`.
    """
    
    # to 0.3.63 as __ttuple__, to 0.3.27a3 as __tuple__
    def toTuple(self) -> AVT_Tuple[T_cov, ...]: ...

@runtime
@deprecated("Deprecated since 0.3.75, will be removed in 0.3.78.")
class SetConvertible(Protocol[T_cov]):
    """
    Availability: >= 0.3.26rc3 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.SetConvertible

    A runtime protocol class with method `toSet()`.
    """
    
    # to 0.3.63 as __tset__, to 0.3.27a3 as __set_init__
    def toSet(self) -> AVT_Set[T_cov]: ...

@runtime
class ReckonOperable(Protocol):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.ReckonOperable

    A runtime protocol class with method `__reckon__()`. Invoked via the function `aveytense.reckon()`.
    Returned type is always an integer.
    """
    def __reckon__(self) -> int:
        """
        Availability: >= 0.3.26rc1

        Return `reckon(self)`.
        """
        ...

@runtime
class Absolute(Protocol[T_cov]):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.Absolute

    A runtime protocol class with one method `__abs__()`.
    Returned type is addicted to covariant type parameter.
    """
    def __abs__(self) -> T_cov: ...

@runtime
class Truncable(Protocol[T_cov]):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.Truncable

    A runtime protocol class with one method `__trunc__()`.
    Returned type is addicted to covariant type parameter.
    """
    def __trunc__(self) -> T_cov: ...

@runtime
class BooleanConvertible(Protocol):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.BooleanConvertible

    A runtime protocol class with one method `__bool__()`.
    """
    # >= ^; < 0.3.44; where ^ is version of this class definition, had additional method __nonzero__ (removed since it is for Python 2)
    def __bool__(self) -> bool: ...

@runtime
class IntegerConvertible(Protocol):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.IntegerConvertible

    A runtime protocol class with method `__int__()`.
    """
    def __int__(self) -> int: ...

@runtime
class FloatConvertible(Protocol):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.FloatConvertible

    A runtime protocol class with method `__float__()`.
    """
    def __float__(self) -> float: ...

@runtime
class ComplexConvertible(Protocol):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.ComplexConvertible

    A runtime protocol class with method `__complex__()`.
    """
    def __complex__(self) -> complex: ...

@runtime
class BytesConvertible(Protocol):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.BytesConvertible

    A runtime protocol class with method `__bytes__()`.
    """
    def __bytes__(self) -> bytes: ...

@runtime
class BinaryRepresentable(Protocol):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.BinaryRepresentable

    A runtime protocol class with method `__bin__()`.
    """
    def __bin__(self) -> str: ...

@runtime
class OctalRepresentable(Protocol):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.OctalRepresentable

    A runtime protocol class with method `__oct__()`.
    """
    def __oct__(self) -> str: ...

@runtime
class HexadecimalRepresentable(Protocol):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.HexadecimalRepresentable

    A runtime protocol class with method `__hex__()`.
    """
    def __hex__(self) -> str: ...

@runtime
class StringConvertible(Protocol):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.StringConvertible

    A runtime protocol class with method `__str__()`.
    """
    def __str__(self) -> str: ...

@runtime
class Representable(Protocol):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.Representable

    A runtime protocol class with method `__repr__()`.
    """
    def __repr__(self) -> str: ...

@runtime
class Indexable(Protocol):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.Indexable

    A runtime protocol class with method `__index__()`. 
    """
    def __index__(self) -> int: ...

@runtime
class Positive(Protocol[T_cov]):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.Positive

    A runtime protocol class with method `__pos__()`.
    Returned type is addicted to covariant type parameter.
    """
    def __pos__(self) -> T_cov: ...

@runtime
class Negative(Protocol[T_cov]):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.Negative

    A runtime protocol class with method `__neg__()`.
    Returned type is addicted to covariant type parameter.
    """
    def __neg__(self) -> T_cov: ...

@runtime
class Invertible(Protocol[T_cov]):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.Invertible

    A runtime protocol class with method `__invert__()`.
    Returned type is addicted to covariant type parameter.
    """
    def __invert__(self) -> T_cov: ...

BufferOperable = Buffer
"Availability: >= 0.3.26rc1. *aveytense.extensions.Buffer*"

@runtime
class LeastComparable(Protocol[T_con]):
    """
    Availability: >= 0.3.26b3 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.LeastComparable

    A runtime protocol class with method `__lt__()`, called to be compared with `<`
    """
    def __lt__(self, other: T_con) -> bool: ...

@runtime
class GreaterComparable(Protocol[T_con]):
    """
    Availability: >= 0.3.26b3 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.GreaterComparable

    A runtime protocol class with method `__gt__()`, called to be compared with `>`
    """
    def __gt__(self, other: T_con) -> bool: ...

@runtime
class LeastEqualComparable(Protocol[T_con]):
    """
    Availability: >= 0.3.26b3 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.LeastEqualComparable

    A runtime protocol class with method `__le__()`, called to be compared with `<=`
    """
    def __le__(self, other: T_con) -> bool: ...

@runtime
class GreaterEqualComparable(Protocol[T_con]):
    """
    Availability: >= 0.3.26b3 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.GreaterEqualComparable

    A runtime protocol class with method `__ge__()`, called to be compared with `>=`
    """
    def __ge__(self, other: T_con) -> bool: ...

@runtime
class EqualComparable(Protocol[T_con]):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.EqualComparable

    A runtime protocol class with method `__eq__()`, called to be compared with `==`
    """
    def __eq__(self, other: T_con) -> bool: ...

@runtime
class InequalComparable(Protocol[T_con]):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.InequalComparable

    A runtime protocol class with method `__ne__()`, called to be compared with `!=`
    """
    def __ne__(self, other: T_con) -> bool: ...


class Comparable(
    LeastComparable[Any],
    GreaterComparable[Any],
    LeastEqualComparable[Any],
    GreaterEqualComparable[Any],
    EqualComparable[Any],
    InequalComparable[Any],
    AVT_Container[Any]
):
    """
    Availability: >= 0.3.26b3 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.Comparable

    A runtime protocol class supporting any form of comparison with operators \\
    `>`, `<`, `>=`, `<=`, `==`, `!=`, `in` (last 3 missing before 0.3.26rc1)
    """
    ...

class Comparable2(
    LeastComparable[Any],
    GreaterComparable[Any],
    LeastEqualComparable[Any],
    GreaterEqualComparable[Any],
    EqualComparable[Any]
):
    """
    Availability: >= 0.3.27a2 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.Comparable2

    A runtime protocol class same as `aveytense.extensions.Comparable`, but without the `in` keyword support. To 0.3.72 it was called `ComparableWithoutIn`
    """
    ...

@runtime
class BitwiseAndOperable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.BitwiseAndOperable

    A runtime protocol class with method `__and__()`. First type is contravariant (for value after the `&` operator), second type is covariant and it is the return type.
    """
    def __and__(self, other: T_con) -> T_cov: ...

@runtime
class BitwiseOrOperable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.BitwiseOrOperable

    A runtime protocol class with method `__or__()`. First type is contravariant (for value after the `|` operator), second type is covariant and it is the return type.
    """
    def __or__(self, other: T_con) -> T_cov: ...

@runtime
class BitwiseXorOperable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.BitwiseXorOperable

    A runtime protocol class with method `__xor__()`. First type is contravariant (for value after the `^` operator), second type is covariant and it is the return type.
    """
    def __xor__(self, other: T_con) -> T_cov: ...

@runtime
class BitwiseLeftOperable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.BitwiseLeftOperable

    A runtime protocol class with method `__lshift__()`. First type is contravariant (for value after the `<<` operator), second type is covariant and it is the return type.
    """
    def __lshift__(self, other: T_con) -> T_cov: ...

@runtime
class BitwiseRightOperable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.BitwiseRightOperable

    A runtime protocol class with method `__rshift__()`. First type is contravariant (for value after the `>>` operator), second type is covariant and it is the return type.
    """
    def __rshift__(self, other: T_con) -> T_cov: ...

class BitwiseOperable(
    BitwiseAndOperable[Any, Any],
    BitwiseOrOperable[Any, Any],
    BitwiseXorOperable[Any, Any],
    BitwiseLeftOperable[Any, Any],
    BitwiseRightOperable[Any, Any]
):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.BitwiseOperable

    Can be used with `&`, `|`, `^`, `<<` and `>>` operators (with `other` being the right operand)
    """
    ...
    
@runtime
class ReflectedBitwiseAndOperable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.73 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.ReflectedBitwiseAndOperable
    
    A runtime protocol class with method `__rand__()`. First type is contravariant (for value before the `&` operator), second type is covariant and it is the return type.
    """
    def __rand__(self, other: T_con) -> T_cov: ...
    
@runtime
class ReflectedBitwiseOrOperable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.73 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.ReflectedBitwiseOrOperable
    
    A runtime protocol class with method `__ror__()`. First type is contravariant (for value before the `|` operator), second type is covariant and it is the return type.
    """
    def __ror__(self, other: T_con) -> T_cov: ...
    
@runtime
class ReflectedBitwiseXorOperable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.73 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.ReflectedBitwiseXorOperable
    
    A runtime protocol class with method `__rxor__()`. First type is contravariant (for value before the `^` operator), second type is covariant and it is the return type.
    """
    def __rxor__(self, other: T_con) -> T_cov: ...
    
@runtime
class ReflectedBitwiseLeftOperable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.73 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.ReflectedBitwiseLeftOperable
    
    A runtime protocol class with method `__rlshift__()`. First type is contravariant (for value before the `<<` operator), second type is covariant and it is the return type.
    """
    def __rlshift__(self, other: T_con) -> T_cov: ...
    
@runtime
class ReflectedBitwiseRightOperable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.73 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.ReflectedBitwiseRightOperable
    
    A runtime protocol class with method `__rrshift__()`. First type is contravariant (for value before the `>>` operator), second type is covariant and it is the return type.
    """
    def __rrshift__(self, other: T_con) -> T_cov: ...
    
class ReflectedBitwiseOperable(
    ReflectedBitwiseAndOperable[Any, Any],
    ReflectedBitwiseOrOperable[Any, Any],
    ReflectedBitwiseXorOperable[Any, Any],
    ReflectedBitwiseLeftOperable[Any, Any],
    ReflectedBitwiseRightOperable[Any, Any]
):
    """
    Availability: >= 0.3.73 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.ReflectedBitwiseOperable

    Can be used with `&`, `|`, `^`, `<<` and `>>` operators (with `other` being the left operand)
    """
    ...

@runtime
class BitwiseAndReassignable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.BitwiseAndReassignable

    A runtime protocol class with method `__iand__()`. First type is contravariant (for value after the `&=` operator), second type is covariant and it is the return type.
    """
    def __iand__(self, other: T_con) -> T_cov: ...

@runtime
class BitwiseOrReassignable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.BitwiseOrReassignable

    A runtime protocol class with method `__ior__()`. First type is contravariant (for value after the `|=` operator), second type is covariant and it is the return type.
    """
    def __ior__(self, other: T_con) -> T_cov: ...

@runtime
class BitwiseXorReassignable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.BitwiseXorReassignable

    A runtime protocol class with method `__ixor__()`. First type is contravariant (for value after the `^=` operator), second type is covariant and it is the return type.
    """
    def __ixor__(self, other: T_con) -> T_cov: ...

@runtime
class BitwiseLeftReassignable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.BitwiseLeftReassignable

    A runtime protocol class with method `__ilshift__()`. First type is contravariant (for value after the `<<=` operator), second type is covariant and it is the return type.
    """
    def __ilshift__(self, other: T_con) -> T_cov: ...

@runtime
class BitwiseRightReassignable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.BitwiseRightReassignable

    A runtime protocol class with method `__irshift__()`. First type is contravariant (for value after the `>>=` operator), second type is covariant and it is the return type.
    """
    def __irshift__(self, other: T_con) -> T_cov: ...

class BitwiseReassignable(
    BitwiseAndOperable[Any, Any],
    BitwiseOrOperable[Any, Any],
    BitwiseXorOperable[Any, Any],
    BitwiseLeftReassignable[Any, Any],
    BitwiseRightReassignable[Any, Any]
):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.BitwiseReassignable

    Can be used with `&=`, `|=`, `^=`, `<<=` and `>>=` operators
    """
    ...

class BitwiseCollection(
    BitwiseReassignable,
    BitwiseOperable,
    ReflectedBitwiseOperable
):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.BitwiseCollection

    Can be used with `&`, `|` and `^` operators, including their \\
    augmented forms: `&=`, `|=` and `^=`, with `~` use following::

        class Example(BitwiseCollection, Invertible[T]): ...
    """
    ...

class UnaryOperable(Positive[Any], Negative[Any], Invertible[Any]):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.UnaryOperable

    Can be used with `+`, `-` and `~` operators preceding the type
    """
    ...

class Indexed(ItemGetter[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc2 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.Indexed
    
    A runtime protocol class with method `__getitem__()` that equals `self[key]`. \\
    Returned type is addicted to covariant type parameter as the second \\
    type parameter; first is type for `key` parameter.
    """
    ...

@runtime
class Ceilable(Protocol[T_cov]):
    """
    Availability: >= 0.3.26b3 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.Ceilable

    A runtime protocol class with method `__ceil__()`.
    Returned type is addicted to covariant type parameter.
    """
    def __ceil__(self) -> T_cov: ...

@runtime
class Floorable(Protocol[T_cov]):
    """
    Availability: >= 0.3.26b3 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.Floorable

    A runtime protocol class with method `__floor__()`.
    Returned type is addicted to covariant type parameter.
    """
    def __floor__(self) -> T_cov: ...

@runtime
class Roundable(Protocol[T_cov]):
    """
    Availability: >= 0.3.26b3 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.Roundable

    A runtime protocol class with method `__round__()`.
    Returned type is addicted to covariant type parameter.
    """
    def __round__(self, ndigits: Optional[int] = None) -> T_cov: ...

CeilOperable = Ceilable
FloorOperable = Floorable
RoundOperable = Roundable

@runtime
class AdditionOperable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.AdditionOperable
    
    A runtime protocol class with method `__add__()`. First type is contravariant (for value after the `+` operator), second type is covariant and it is the return type.
    """
    def __add__(self, other: T_con) -> T_cov: ...

@runtime
class SubstractionOperable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.SubstractionOperable
    
    A runtime protocol class with method `__sub__()`. First type is contravariant (for value after the `-` operator), second type is covariant and it is the return type.
    """
    def __sub__(self, other: T_con) -> T_cov: ...

@runtime
class MultiplicationOperable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.MultiplicationOperable
    
    A runtime protocol class with method `__mul__()`. First type is contravariant (for value after the `*` operator), second type is covariant and it is the return type.
    """
    def __mul__(self, other: T_con) -> T_cov: ...

@runtime
class MatrixMultiplicationOperable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.MatrixMultiplicationOperable
    
    A runtime protocol class with method `__matmul__()`. First type is contravariant (for value after the `@` operator), second type is covariant and it is the return type.
    """
    def __matmul__(self, other: T_con) -> T_cov: ...

@runtime
class TrueDivisionOperable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc1
    
    A runtime protocol class with method `__truediv__()`. First type is contravariant (for value after the `/` operator), second type is covariant and it is the return type.
    """
    def __truediv__(self, other: T_con) -> T_cov: ...

@runtime
class FloorDivisionOperable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc1
    
    A runtime protocol class with method `__floordiv__()`. First type is contravariant (for value after the `//` operator), second type is covariant and it is the return type.
    """
    def __floordiv__(self, other: T_con) -> T_cov: ...

@runtime
class DivmodOperable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc1
    
    A runtime protocol class with method `__divmod__()`. First type is contravariant (the second argument for `divmod()`), second type is covariant and it is the return type.
    """
    def __divmod__(self, other: T_con) -> T_cov: ...

@runtime
class ModuloOperable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc1
    
    A runtime protocol class with method `__mod__()`. First type is contravariant (for value after the `%` operator), second type is covariant and it is the return type.
    """
    def __mod__(self, other: T_con) -> T_cov: ...

@runtime
class ExponentiationOperable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc1
    
    A runtime protocol class with method `__pow__()`. First type is contravariant (for value after the `**` operator), second type is covariant and it is the return type.
    """
    def __pow__(self, other: T_con) -> T_cov: ...

@runtime
class ReflectedAdditionOperable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc1
    
    A runtime protocol class with method `__radd__()`. First type is contravariant (for value before the `+` operator), second type is covariant and it is the return type.
    """
    def __radd__(self, other: T_con) -> T_cov: ...

@runtime
class ReflectedSubtractionOperable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc1
    
    A runtime protocol class with method `__rsub__()`. First type is contravariant (for value before the `-` operator), second type is covariant and it is the return type.
    """
    def __rsub__(self, other: T_con) -> T_cov: ...

@runtime
class ReflectedMultiplicationOperable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc1
    
    A runtime protocol class with method `__rmul__()`. First type is contravariant (for value before the `*` operator), second type is covariant and it is the return type.
    """
    def __rmul__(self, other: T_con) -> T_cov: ...

@runtime
class ReflectedMatrixMultiplicationOperable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc1
    
    A runtime protocol class with method `__rmatmul__()`. First type is contravariant (for value before the `@` operator), second type is covariant and it is the return type.
    """
    def __rmatmul__(self, other: T_con) -> T_cov: ...

@runtime
class ReflectedTrueDivisionOperable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc1
    
    A runtime protocol class with method `__rtruediv__()`. First type is contravariant (for value before the `/` operator), second type is covariant and it is the return type.
    """
    def __rtruediv__(self, other: T_con) -> T_cov: ...

@runtime
class ReflectedFloorDivisionOperable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc1
    
    A runtime protocol class with method `__rfloordiv__()`. First type is contravariant (for value before the `//` operator), second type is covariant and it is the return type.
    """
    def __rfloordiv__(self, other: T_con) -> T_cov: ...

@runtime
class ReflectedDivmodOperable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc1
    
    A runtime protocol class with method `__rdivmod__()`. First type is contravariant (the first argument for `divmod()`), second type is covariant and it is the return type.
    """
    def __rdivmod__(self, other: T_con) -> T_cov: ...

@runtime
class ReflectedModuloOperable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc1
    
    A runtime protocol class with method `__rmod__()`. First type is contravariant (for value before the `%` operator), second type is covariant and it is the return type.
    """
    def __rmod__(self, other: T_con) -> T_cov: ...

@runtime
class ReflectedExponentiationOperable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc1
    
    A runtime protocol class with method `__rpow__()`. First type is contravariant (for value before the `**` operator), second type is covariant and it is the return type.
    """
    def __rpow__(self, other: T_con) -> T_cov: ...

@runtime
class AdditionReassignable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc1
    
    A runtime protocol class with method `__iadd__()`. First type is contravariant (for value after the `+=` operator), second type is covariant and it is the return type.
    """
    def __iadd__(self, other: T_con) -> T_cov: ...

@runtime
class SubtractionReassignable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc1
    
    A runtime protocol class with method `__isub__()`. First type is contravariant (for value after the `-=` operator), second type is covariant and it is the return type.
    """
    def __isub__(self, other: T_con) -> T_cov: ...

@runtime
class MultiplicationReassignable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc1
    
    A runtime protocol class with method `__imul__()`. First type is contravariant (for value after the `*=` operator), second type is covariant and it is the return type.
    """
    def __imul__(self, other: T_con) -> T_cov: ...

@runtime
class MatrixMultiplicationReassignable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc1
    
    A runtime protocol class with method `__imatmul__()`. First type is contravariant (for value after the `@=` operator), second type is covariant and it is the return type.
    """
    def __imatmul__(self, other: T_con) -> T_cov: ...

@runtime
class TrueDivisionReassingable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc1
    
    A runtime protocol class with method `__itruediv__()`. First type is contravariant (for value after the `/=` operator), second type is covariant and it is the return type.
    """
    def __itruediv__(self, other: T_con) -> T_cov: ...

@runtime
class FloorDivisionReassignable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc1
    
    A runtime protocol class with method `__ifloordiv__()`. First type is contravariant (for value after the `//=` operator), second type is covariant and it is the return type.
    """
    def __ifloordiv__(self, other: T_con) -> T_cov: ...

@runtime
class ModuloReassignable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc1
    
    A runtime protocol class with method `__imod__()`. First type is contravariant (for value after the `%=` operator), second type is covariant and it is the return type.
    """
    def __imod__(self, other: T_con) -> T_cov: ...

@runtime
class ExponentiationReassignable(Protocol[T_con, T_cov]):
    """
    Availability: >= 0.3.26rc1
    
    A runtime protocol class with method `__ipow__()`. First type is contravariant (for value after the `**=` operator), second type is covariant and it is the return type.
    """
    def __ipow__(self, other: T_con) -> T_cov: ...

class ReflectedArithmeticOperable(
    ReflectedAdditionOperable[Any, Any],
    ReflectedSubtractionOperable[Any, Any],
    ReflectedMultiplicationOperable[Any, Any],
    ReflectedMatrixMultiplicationOperable[Any, Any],
    ReflectedTrueDivisionOperable[Any, Any],
    ReflectedFloorDivisionOperable[Any, Any],
    ReflectedDivmodOperable[Any, Any],
    ReflectedModuloOperable[Any, Any]
):
    """
    Availability: >= 0.3.26rc1

    A protocol class supporting every kind (except bitwise) of reflected arithmetic operations with following operators:
    ```
        + - * @ / // % ** divmod
    ```
    where left operand is `other` and right is `self`
    """
    ...

class ArithmeticOperable(
    AdditionOperable[Any, Any],
    SubstractionOperable[Any, Any],
    MultiplicationOperable[Any, Any],
    MatrixMultiplicationOperable[Any, Any],
    TrueDivisionOperable[Any, Any],
    FloorDivisionOperable[Any, Any],
    DivmodOperable[Any, Any],
    ModuloOperable[Any, Any],
    ExponentiationOperable[Any, Any],
    ReflectedArithmeticOperable
):
    """
    Availability: >= 0.3.26rc1

    A protocol class supporting every kind (except bitwise) of arithmetic operations, including their \\
    reflected equivalents, with following operators:
    ```
        + - * @ / // % ** divmod
    ```
    Both `self` and `other` can be either left or right operands.
    """
    ...

class ArithmeticReassignable(
    AdditionReassignable[Any, Any],
    SubtractionReassignable[Any, Any],
    MultiplicationReassignable[Any, Any],
    MatrixMultiplicationReassignable[Any, Any],
    TrueDivisionReassingable[Any, Any],
    FloorDivisionReassignable[Any, Any],
    ModuloReassignable[Any, Any],
    ExponentiationReassignable[Any, Any]
):
    """
    Availability: >= 0.3.26rc1

    A protocol class supporting every kind (except bitwise) of augmented/re-assigned arithmetic operations \\
    with following operators:
    ```
        += -= *= @= /= //= %= **=
    ```
    """
    ...

class ArithmeticCollection(
    ArithmeticOperable,
    ArithmeticReassignable
):
    """
    Availability: >= 0.3.26rc1

    A protocol class supporting every kind (except bitwise) of augmented/re-assigned and normal arithmetic operations \\
    with following operators:
    ```
        + - * @ / // % ** divmod += -= *= @= /= //= %= **=
    ```
    """
    ...

class OperatorCollection(
    ArithmeticCollection,
    BitwiseCollection,
    UnaryOperable,
    Comparable
):
    """
    Availability: >= 0.3.26rc1

    A protocol class supporting every kind of augmented/re-assigned, reflected and normal arithmetic operations \\
    with following operators:
    ```
        + - * @ / // % ** divmod & | ^ += -= *= @= /= //= %= **= &= |= ^=
    ```
    unary assignment with `+`, `-` and `~`, and comparison with following operators:
    ```
        > < >= <= == != in
    ```
    """
    ...

class LenGetItemOperable(Sized, ItemGetter[int, T_cov]):
    """
    Availability: >= 0.3.26rc2 // `_typeshed.SupportsLenAndGetItem`
    
    A runtime protocol class with `__getitem__()` and `__len__()` methods. Those are typical in sequences.
    """
    ...

@runtime
class Formattable(Protocol):
    """
    Availability: >= 0.3.26rc1

    A runtime protocol class with method `__format__()`.
    """
    def __format__(self, format_spec: str = "") -> str: ...

@runtime
class Flusher(Protocol): # _typeshed.SupportsFlush
    """
    Availability: >= 0.3.27b1

    A runtime protocol class with method `flush()`.
    """
    def flush(self) -> object: ...

@runtime
class Writable(Protocol[T_con]): # _typeshed.SupportsWrite
    """
    Availability: >= 0.3.27b1

    A runtime protocol class with method `write()`.
    """
    def write(self, data: T_con, /) -> int: ...
    
@runtime
class Readable(Protocol[T_cov]):
    """
    Availability: >= 0.3.55b2
    
    A runtime protocol class with method `read()`
    """
    def read(self, size: int = ..., /) -> T_cov: ...
    
@runtime
class FilenoProvider(Protocol):
    """
    Availability: >= 0.3.60
    
    A runtime protocol class with method `fileno()`
    """
    def fileno(self) -> int: ...
    
@runtime
class Copyable(Protocol):
    """
    Availability: >= 0.3.34
    
    A runtime protocol class with method `copy()`.
    """
    # >= 0.3.43; < 0.3.60 it was __copy__ instead; for __copy__ use Copyable2
    def copy(self) -> Self: ... 
    
@runtime
class Copyable2(Protocol):
    """
    Availability: >= 0.3.60
    
    A runtime protocol class with method `__copy__()`
    """
    def __copy__(self) -> Self: ...
    
@runtime
class DeepCopyable(Protocol):
    """
    Availability: >= 0.3.43
    
    A runtime protocol class with method `deepcopy()`.
    """
    # >= 0.3.43; < 0.3.63 it was __deepcopy__ instead; for __deepcopy__ use DeepCopyable2
    def deepcopy(self) -> Self: ...

@runtime
class DeepCopyable2(Protocol):
    """
    Availability: >= 0.3.63
    
    A runtime protocol class with method `__deepcopy__()`.
    """
    def __deepcopy__(self, memo: Optional[AVT_Dict[int, Any]] = None) -> Self: ...
    
### NEGATIONS ###
    
@runtime
class NotIterable(Protocol):
    """
    Availability: >= 0.3.26b3

    A runtime protocol class disallowing iteration with `for` loop
    """
    __iter__ = None

@runtime
class NotCallable(Protocol[T_cov]):
    """
    Availability: >= 0.3.45

    A runtime protocol class disallowing invoking its subclasses (`__call__()` throws an error)
    """
    __call__ = None
            
# NotInvocable = NotCallable # >= 0.3.26rc1; < 0.3.54

@runtime
class NotUnaryOperable(Protocol):
    """
    Availability: >= 0.3.26rc1

    A protocol class indicating that its subclasses' objects cannot use unary operators `+`, `-` and `~`
    """
    def __pos__(self):
        _E(108, "")
        
    def __neg__(self):
        _E(108, "")
        
    def __invert__(self):
        _E(108, "")

@runtime
class NotReassignable(Protocol[T_con]):
    """
    Availability: >= 0.3.26b3

    A protocol class that doesn't support any form of re-assignment, those are augmented assignment
    operators: `+=`, `-=`, `*=`, `**=`, `/=`, `//=`, `%=`, `>>=`, `<<=`, `&=`, `|=`, `^=`. Setting new
    value also is prohibited.
    """
    __slots__ = ("__weakref__",)
    __op = (
        "; used operator '+='", # 0
        "; used operator '-='", # 1
        "; used operator '*='", # 2
        "; used operator '/='", # 3
        "; used operator '//='", # 4
        "; used operator '**='", # 5
        "; used operator '<<='", # 6
        "; used operator '>>='", # 7
        "; used operator '%='", # 8
        "; used operator '&='", # 9
        "; used operator '|='", # 10
        "; used operator '^='", # 11
    )
    
    def __set__(self, i: Self, v: T_con):
        
        s = " variable that isn't assignable and re-assignable"
        _E(102, s)
            
    def __iadd__(self, o: T_con):
        i = 0
        _E(102, self.__op[i])
        
    def __isub__(self, o: T_con):
        i = 1
        _E(102, self.__op[i])
        
    def __imul__(self, o: T_con):
        i = 2
        _E(102, self.__op[i])
        
    def __ifloordiv__(self, o: T_con):
        i = 4
        _E(102, self.__op[i])
        
    def __idiv__(self, o: T_con):
        i = 3
        _E(102, self.__op[i])
        
    def __itruediv__(self, o: T_con):
        i = 3
        _E(102, self.__op[i])
        
    def __imod__(self, o: T_con):
        i = 8
        _E(102, self.__op[i])
        
    def __ipow__(self, o: T_con):
        i = 5
        _E(102, self.__op[i])
        
    def __ilshift__(self, o: T_con):
        i = 6
        _E(102, self.__op[i])
        
    def __irshift__(self, o: T_con):
        i = 7
        _E(102, self.__op[i])
        
    def __iand__(self, o: T_con):
        i = 9
        _E(102, self.__op[i])
        
    def __ior__(self, o: T_con):
        i = 10
        _E(102, self.__op[i])
        
    def __ixor__(self, o: T_con):
        i = 11
        _E(102, self.__op[i])

@runtime
class NotComparable(Protocol[T_con]):
    """
    Availability: >= 0.3.26b3

    A protocol class for subclasses disallowing using comparison operators `==`, `!=`, `>`, `<`, `>=`, `<=`, `in`
    """
    __slots__ = ()
    __op = (
        "; used operator '<'", # 0
        "; used operator '>'", # 1
        "; used operator '<='", # 2
        "; used operator '>='", # 3
        "; used operator '=='", # 4
        "; used operator '!='", # 5
        "; used operator 'in'", # 6
    )
    def __lt__(self, other: T_con):
        i = 0
        _E(102, self.__op[i])
        
    def __gt__(self, other: T_con):
        i = 1
        _E(102, self.__op[i])
        
    def __le__(self, other: T_con):
        i = 2
        _E(102, self.__op[i])
        
    def __ge__(self, other: T_con):
        i = 3
        _E(102, self.__op[i])
        
    def __eq__(self, other: T_con):
        i = 4
        _E(102, self.__op[i])
        
    def __ne__(self, other: T_con):
        i = 5
        _E(102, self.__op[i])
        
    def __contains__(self, other: T_con):
        i = 6
        _E(102, self.__op[i])

@runtime
class TimeClockInfo(Protocol):
    """
    Availability: >= 0.3.71 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.TimeClockInfo
    
    A runtime protocol class equivalent to stub protocol class `time._ClockInfo`
    
    Attributes included: `adjustable` (boolean), `implementation` (string), `monotonic` (boolean), `resolution` (float)
    """
    adjustable: bool
    implementation: str
    monotonic: bool
    resolution: float
    
class Allocator:
    """
    Availability: >= 0.3.27b3 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.Allocator

    An allocator class. Classes extending this class have access to `__alloc__()` magic method, \\
    but it is advisable to use it wisely.
    """
    __a = bytearray()

    def __init__(self, b: Union[bytearray, BytearrayConvertible], /):
        
        if isinstance(b, BytearrayConvertible):
            self.__a = b.__bytearray__()
            
        elif isinstance(b, bytearray):
            self.__a = b
            
        else:
            error = TypeError("Expected a bytearray object or object of class extending 'BytearrayConvertible' class")
            raise error
    
    def __alloc__(self):
        return self.__a.__alloc__()
    
class AwaitableGenerator(
    AVT_Awaitable[_T_return_noDefault_cov],
    AVT_Generator[_T_yield_cov, _T_send_noDefault_con, _T_return_noDefault_cov],
    Generic[_T_yield_cov, _T_send_noDefault_con, _T_return_noDefault_cov, T],
    metaclass = ABCMeta
):
    """
    Availability: >= 0.3.58 // `_typeshed._type_checker.AwaitableGenerator` \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.AwaitableGenerator
    """
    ...

@runtime
class VersionInfo(Protocol):
    """
    Availability: >= 0.3.72 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.VersionInfo
    
    A runtime protocol class for classes that offer the same properties as `sys.version_info`
    """
    
    @property
    def major(self) -> int: ...
    @property
    def minor(self) -> int: ...
    @property
    def micro(self) -> int: ...
    @property
    def releaselevel(self) -> Literal["alpha", "beta", "candidate", "final"]: ...
    @property
    def serial(self) -> int: ...
    
@runtime
class Clearable(Protocol):
    """
    Availability: >= 0.3.73 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.Clearable
    """
    
    def clear(self) -> None: ...
    
@runtime
class Viewable(Protocol[T_cov]):
    """
    Availability: >= 0.3.73 // `_typeshed.Viewable` \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.Viewable
    """
    
    def __len__(self) -> int: ...
    def __iter__(self) -> AVT_Iterator[T_cov]: ...

@runtime
class ViewableItemGetter(Protocol[KT, VT_cov]):
    """
    Availability: >= 0.3.73 // `_typeshed.SupportsGetItemViewable` \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.ViewableItemGetter
    """
    
    def __len__(self) -> int: ...
    def __iter__(self) -> AVT_Iterator[KT]: ...
    def __getitem__(self, key: KT, /) -> VT_cov: ...

### Array Typecode & Memoryview Format Types ###

ArrayIntegerTypecodes: TypeAlias = Literal["b", "B", "h", "H", "i", "I", "l", "L", "q", "Q"] # >= 0.3.60
ArrayFloatTypecodes: TypeAlias = Literal["f", "d"] # >= 0.3.60
if _sys.version_info >= (3, 16): # >= 0.3.60 (all versions)
    ArrayUnicodeTypecodes: TypeAlias = Literal["w"]
elif _sys.version_info >= (3, 13):
    ArrayUnicodeTypecodes: TypeAlias = Literal["u", "w"]
else:
    ArrayUnicodeTypecodes: TypeAlias = Literal["u"]
ArrayTypecodes: TypeAlias = Union[ArrayIntegerTypecodes, ArrayFloatTypecodes, ArrayUnicodeTypecodes] # >= 0.3.60

MemoryViewIntegerFormats: TypeAlias = Literal["b", "B", "@b", "@B", "h", "H", "@h", "@H", "i", "I", "@i", "@I", "l", "L", "@l", "@L", "q", "Q", "@q", "@Q", "P", "@P"] # >= 0.3.60
MemoryViewFloatFormats: TypeAlias = Literal["f", "@f", "d", "@d"] # >= 0.3.60
MemoryViewBytesFormats: TypeAlias = Literal["c", "@c"] # >= 0.3.60
MemoryViewBooleanFormats: TypeAlias = Literal["?"] # >= 0.3.60

### File Types ###

FileBinaryModeUpdating: TypeAlias = Literal[ # >= 0.3.59 // _typeshed.OpenBinaryModeUpdating
    "rb+", "r+b", "+rb", "br+", "b+r", "+br",
    "wb+", "w+b", "+wb", "bw+", "b+w", "+bw",
    "ab+", "a+b", "+ab", "ba+", "b+a", "+ba",
    "xb+", "x+b", "+xb", "bx+", "b+x", "+bx"
]
FileBinaryModeReading: TypeAlias = Literal["rb", "br", "rbU", "rUb", "Urb", "brU", "bUr", "Ubr"] # >= 0.3.59 // _typeshed.OpenBinaryModeReading
FileBinaryModeWriting: TypeAlias = Literal["wb", "bw", "ab", "ba", "xb", "bx"] # >= 0.3.59 // _typeshed.OpenBinaryModeWriting
FileBinaryMode: TypeAlias = Union[FileBinaryModeUpdating, FileBinaryModeReading, FileBinaryModeWriting] # >= 0.3.59 // _typeshed.OpenBinaryMode
FileGenericPath: TypeAlias = Union[AnyStr, AVT_PathLike[AnyStr]] # >= 0.3.59 // _typeshed.GenericPath
FileOpener: TypeAlias = AVT_Callable[[str, int], int] # 0.3.26b3; < 0.3.41; >= 0.3.72 
FilePath: TypeAlias = Union[FileGenericPath[str], FileGenericPath[bytes]] # >= 0.3.59 // _typeshed.StrOrBytesPath
FileTextModeUpdating: TypeAlias = Literal[ # >= 0.3.59 // _typeshed.OpenTextModeUpdating
    "r+", "+r", "rt+", "r+t", "+rt", "tr+", "t+r", "+tr",
    "w+", "+w", "wt+", "w+t", "+wt", "tw+", "t+w", "+tw",
    "a+", "+a", "at+", "a+t", "+at", "ta+", "t+a", "+ta",
    "x+", "+x", "xt+", "x+t", "+xt", "tx+", "t+x", "+tx"
] 
FileTextModeReading: TypeAlias = Literal["w", "wt", "tw", "a", "at", "ta", "x", "xt", "tx"] # >= 0.3.59 // _typeshed.OpenTextModeReading
FileTextModeWriting: TypeAlias = Literal["r", "rt", "tr", "U", "rU", "Ur", "rtU", "rUt", "Urt", "trU", "tUr", "Utr"] # >= 0.3.59 // _typeshed.OpenTextModeWriting
FileTextMode: TypeAlias = Union[FileTextModeUpdating, FileTextModeReading, FileTextModeWriting] # >= 0.3.59 // _typeshed.OpenTextMode
FileMode: TypeAlias = Union[FileBinaryMode, FileTextMode] # 0.3.26b3; < 0.3.41; >= 0.3.72
FileType: TypeAlias = Union[int, FilePath] # >= 0.3.26b3 // _typeshed.StrOrBytesPath

### Buffer Types ###
# All of these 3 are referred from _typeshed stub file. If anything changes, the next version will apply new changes.

ReadableBuffer: TypeAlias = _Buffer # >= 0.3.44 // _typeshed.ReadableBuffer
ReadOnlyBuffer: TypeAlias = _Buffer # >= 0.3.44 // _typeshed.ReadOnlyBuffer
WriteableBuffer: TypeAlias = _Buffer # >= 0.3.44 // _typeshed.WriteableBuffer

### _typeshed Stub File Exclusive ###

AnnotationForm = Any # >= 0.3.48 // _typeshed.AnnotationForm (backport before 3.14)
AnnotateFunc: TypeAlias = AVT_Callable[[Format], AVT_Dict[str, AnnotationForm]] # >= 0.3.57 // _typeshed.AnnotateFunc (backport before 3.14)
EvaluateFunc: TypeAlias = AVT_Callable[[Format], AnnotationForm] # >= 0.3.59 // _typeshed.EvaluateFunc (backport before 3.14)
Incomplete = Any # >= 0.3.60 // _typeshed.Incomplete
MaybeNone = Any # >= 0.3.57 // _typeshed.MaybeNone
Unused: TypeAlias = object # >= 0.3.44 // _typeshed.Unused

### Internal Classes From typing.py ###
# Use these with isinstance() to determine if these are desired special forms.
# Not intended in any other use.

TypingAnnotatedType = type(Annotated[int, "$"]) # >= 0.3.52
TypingCallableType = type(AVT_Callable[..., Any]) # >= 0.3.52
TypingConcatenateType = type(Concatenate[int, P]) # >= 0.3.52 // TypeError occurred until 0.3.53 ('typing.ParamSpec' missing before Py3.11, ellipsis was used instead)
TypingGenericType = type(TypeGuard[int]) # >= 0.3.52
TypingLiteralType = type(Literal[0]) # >= 0.3.52
TypingNoDefaultType = type(NoDefault) # >= 0.3.53
TypingUnionType = type(Union[int, str]) # >= 0.3.52 // 'typing._GenericAlias': < Py3.9 / 'types.UnionType': >= Py3.14
TypingUnpackType = type(Unpack[AVT_Tuple[int, str]]) # >= 0.3.52

# >> TypingSpecialGenericType: >= 0.3.59
# >> TypingExtensionsSpecialGenericType: >= 0.3.59
# NOTE: 'typing.Generator' (with other three) re-implemented in 'typing_extensions' exists for Python versions preceding 3.13 beta, defined as an instance of
# 'typing_extensions._SpecialGenericAlias'. 'typing_extensions' will import 'collections.abc.Generator' with 3 other abstract base classes when 3.13 beta or
# higher is used, meaning aforementioned internal class '_SpecialGenericAlias' won't be defined in 'typing_extensions' (excluding 'typing' that has this class
# since 3.9). 
if _sys.version_info >= (3, 9):
    TypingSpecialGenericType = type(_typing.Generator)
    if _sys.version_info < (3, 13, 0, "beta"):
        TypingExtensionsSpecialGenericType = type(_typing_ext.Generator)
else:
    TypingSpecialGenericType = type(_typing_ext.Generator)

# >> TypingTupleType: >= 0.3.53
# NOTE: Even if 'typing.Tuple' is deprecated since 3.9, it actually has an internal class that implements it. So I decided for version 0.3.54 to copy and paste
# its source code below (different for Py3.8 and Py3.9+ so both versions are included) in case Python removes the 'typing.Tuple' type alias.
if hasattr(_typing, "Tuple"):
    TypingTupleType = type(_typing.Tuple)
    
# (0.3.54)
elif _sys.version_info >= (3, 9):
    
    class TypingTupleType(TypingSpecialGenericType, _root=True):
        """
        Availability: >= 0.3.53
        
        Internal class for tuple type alias `typing.Tuple`
        """
        
        @_typing._tp_cache
        def __getitem__(self, params):
            
            import typing
            
            if not isinstance(params, tuple):
                params = (params,)
            if len(params) >= 2 and params[-1] is ...:
                msg = "Tuple[t, ...]: t must be a type."
                params = tuple(typing._type_check(p, msg) for p in params[:-1])
                return self.copy_with((*params, typing._TypingEllipsis))
            msg = "Tuple[t0, t1, ...]: each t must be a type."
            params = tuple(typing._type_check(p, msg) for p in params)
            return self.copy_with(params)
else:
    class TypingTupleType(TypingGenericType, _root=True):
        """
        Availability: >= 0.3.53
        
        Internal class for tuple type alias `typing.Tuple`
        """
        def __getitem__(self, params):
            if self._name != 'Callable' or not self._special:
                return self.__getitem_inner__(params)
            if not isinstance(params, tuple) or len(params) != 2:
                raise TypeError("Callable must be used as "
                                "Callable[[arg, ...], result].")
            args, result = params
            if args is Ellipsis:
                params = (Ellipsis, result)
            else:
                if not isinstance(args, list):
                    raise TypeError(f"Callable[args, result]: args must be a list."
                                    f" Got {args}")
                params = (tuple(args), result)
            return self.__getitem_inner__(params)

        @_typing._tp_cache
        def __getitem_inner__(self, params):
            
            import typing
            
            if self.__origin__ is tuple and self._special:
                if params == ():
                    return self.copy_with((typing._TypingEmpty,))
                if not isinstance(params, tuple):
                    params = (params,)
                if len(params) == 2 and params[1] is ...:
                    msg = "Tuple[t, ...]: t must be a type."
                    p = typing._type_check(params[0], msg)
                    return self.copy_with((p, typing._TypingEllipsis))
                msg = "Tuple[t0, t1, ...]: each t must be a type."
                params = tuple(typing._type_check(p, msg) for p in params)
                return self.copy_with(params)
            if self.__origin__ is Callable and self._special:
                args, result = params
                msg = "Callable[args, result]: result must be a type."
                result = typing._type_check(result, msg)
                if args is Ellipsis:
                    return self.copy_with((typing._TypingEllipsis, result))
                msg = "Callable[[arg, ...], result]: each arg must be a type."
                args = tuple(typing._type_check(arg, msg) for arg in args)
                params = args + (result,)
                return self.copy_with(params)
            return super().__getitem__(params)
        
### Unions ###
# Not warranted to stay.

StringUnion: TypeAlias = Union[T, str]
"Availability: >= 0.3.26rc3"
IntegerUnion: TypeAlias = Union[T, int]
"Availability: >= 0.3.26rc3"
FloatUnion: TypeAlias = Union[T, float]
"Availability: >= 0.3.26rc3"
ComplexUnion: TypeAlias = Union[T, complex]
"Availability: >= 0.3.26rc3"
IntegerFloatUnion: TypeAlias = Union[T, int, float]
"Availability: >= 0.3.26rc3"
IntegerStringUnion: TypeAlias = Union[T, int, str]
"Availability: >= 0.3.26rc3"
BooleanUnion: TypeAlias = Union[T, bool]
"Availability: >= 0.3.26rc3"
TrueUnion: TypeAlias = Union[T, Literal[True]]
"Availability: >= 0.3.26rc3"
FalseUnion: TypeAlias = Union[T, Literal[False]]
"Availability: >= 0.3.26rc3"

### Uncategorized ###

import time as _time

# *** uppercased

AnyCallable: TypeAlias = AVT_Callable[..., Any] # >= 0.3.26rc3
if _sys.version_info >= (3, 10): # >= 0.3.60 // builtins._ClassInfo
    ClassInfoType = Union[type, UnionType, AVT_Tuple[ClassInfoType, ...]] # type: ignore
else:
    ClassInfoType = Union[type, AVT_Tuple[ClassInfoType, ...]] # type: ignore
ColorType: TypeAlias = Union[int, str, None] # >= 0.3.25 // renamed from SupportsColor (0.3.26b3)
ColourType: TypeAlias = ColorType # >= 0.3.26b3
# CoroutineWrapperType
async def _f(): pass
_coroutine = _f()
# this class as '_collections_abc.coroutine_wrapper' doesn't exist, neither does it exist in 'types'
CoroutineWrapperType = type(_coroutine.__await__()) # >= 0.3.53
_coroutine.close()
del _coroutine
# END CoroutineWrapperType
DecimalComparableType: TypeAlias = Union[Decimal, float, _Rational] # >= 0.3.60
DecimalNewType: TypeAlias = Union[Decimal, float, str, AVT_Tuple[int, AVT_Sequence[int], int]] # >= 0.3.60
DecimalType: TypeAlias = Union[int, Decimal] # >= 0.3.60

FlagsType: TypeAlias = Union[int, RegexFlag] # >= 0.3.60
FloatOrInteger: TypeAlias = Union[int, float] # >= 0.3.25
Hash: TypeAlias = _hashlib.HASH # >= 0.3.44
if _sys.version_info >= (3, 9): # >= 0.3.44 // 0.3.53: '_hashlib.HASHXOF' undefined before Python 3.9 (patched error)
    Hashxof: TypeAlias = _hashlib.HASHXOF
else:
    Hashxof = type(hashlib.shake_128())
HaveCodeType: TypeAlias = Union[MethodType, FunctionType, CodeType, type, AVT_Callable[..., Any]] # >= 0.3.60 // type from dis.dis()
Hmac: TypeAlias = _hmac.HMAC # >= 0.3.44
InComparable: TypeAlias = AVT_Container # >= 0.3.26rc1
Interface = Protocol # >= 0.3.44
LenOperable: TypeAlias = Sized # >= 0.3.26rc1
OptionalCallable: TypeAlias = Optional[AVT_Callable[P, T]] # >= 0.3.26rc3
Pack = Concatenate
PatternType: TypeAlias = Union[AnyStr, AVT_Pattern[AnyStr]] # >= 0.3.60 // type from re.match()
RichComparable: TypeAlias = Union[LeastComparable[Any], GreaterComparable[Any]] # >= ?

# Unfortunately, it is impossible to make this type alias as a class due to the fact
# the Mapping ABC inherits from the Collection ABC. That implementation would look like this:
#
#   class SequenceLike(Protocol[T]):
#       def __len__(self) -> int: ...
#       def __contains__(self, x: object) -> bool: ...
#       def __iter__(self) -> AVT_Iterator[T]: ... 
#
# ...however, it will be correct for Mapping ABC too.
# Another technique in mind was 'class SequenceLike(Sequence[T], AbstractSet[T], ValuesView[T]): ...', but this is
# where it gets anomalous with type hinting, because all the methods from all these ABCs will need to be included.
# If there was a PEP that would cover optional definitions in a protocol runtime, this would be defined as a class
# instead. However, another PEP would be needed to not type hint correctly when an instance of Mapping ABC is used.
# Finally, the last trick was bound with use of an unofficial boolean attribute '__is_sequence_like__'. We will keep
# it like this for now.

SequenceLike: TypeAlias = Union[AVT_Sequence[T], AVT_AbstractSet[T], AVT_ValuesView[T]]
"""Availability: >= 0.3.54 // Renamed 0.3.69 from `TrueSequence` // https://aveyzan.xyz/aveytense#aveytense.extensions.SequenceLike"""

@runtime
@deprecated("Deprecated since 0.3.75, up for removal in 0.3.78")
class Sizeable(Sized, Protocol):
    """
    Availability: >= 0.3.26rc3 \\
    Deprecated: >= 0.3.75
    """

# I was actually thinking to retract from re-defining 'typing.Text' since its from Python 2
# Not doing this in favor of this module purpose.
Text: TypeAlias = str # >= 0.3.58

TimeTable: TypeAlias = AVT_Tuple[int, int, int, int, int, int, int, int, int] # >= 0.3.70 // time._TimeTable
Uuid: TypeAlias = UUID # >= 0.3.54

# *** lowercased
cached_property = cachedproperty
dict_keys = type({}.keys()) # >= 0.3.73
dict_items = type({}.items()) # >= 0.3.73
dict_values = type({}.values()) # >= 0.3.73

# Private types, not for export. This prefix will be removed in 0.3.76, keeping the underscore
if TYPE_CHECKING:
    _PrideMonth2026ReckonType: TypeAlias = Union[IO[Any], AVT_Iterable[Any], ReckonOperable, Sized] # >= 0.3.74
    _PrideMonth2026AbroadStep: TypeAlias = Union[int, float, IntegerConvertible, FloatConvertible, Indexable] # >= 0.3.74
    _PrideMonth2026AbroadStop: TypeAlias = Union[_PrideMonth2026AbroadStep, _PrideMonth2026ReckonType] # >= 0.3.74
    _PrideMonth2026AbroadStart: TypeAlias = _PrideMonth2026AbroadStop # >= 0.3.74
    _PrideMonth2026AbroadConvectType: TypeAlias = _PrideMonth2026AbroadStop # >= 0.3.74
    
    _Bits: TypeAlias = Literal[3, 4, 8, 24] # aveytense.Color
    _Clearable: TypeAlias = Union[str, Clearable, AVT_MutableMapping[Any, Any], AVT_MutableSequence[Any], AVT_MutableSet[Any], IO[Any], FrameType]
    _ProbabilityType: TypeAlias = Union[
        AVT_Tuple[T, int],
        SequenceLike[Union[T, int]], # Sequence => _AVT = 0.3.53, SequenceLike = 0.3.72
        AVT_Mapping[T, int], # Mapping => _AVT = 0.3.53
        T
    ]
    
    _prevent_unused_imports(_PrideMonth2026AbroadStart, _PrideMonth2026AbroadConvectType, _Bits, _Clearable, _ProbabilityType)

del _collections_abc, _abc, _enum, _hashlib, hashlib, _hmac, _time, _typing, _typing_ext # not for export!

### Functions/methods ###

def int_bit_count(i: int, /): # -> int
    """
    Availability: >= 0.3.60 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.int_bit_count
    
    `int.bit_count()` (>=3.10) available for Python 3.8 and 3.9
    """
    
    if not isinstance(i, int):
        error = TypeError("expected an integer")
        raise error
    
    # code highlighted in python documentation
    return bin(i).count("1")

def int_to_bytes(
    i: int,
    /,
    length: Indexable = 1,
    byteorder: Literal["little", "big"] = "big",
    *,
    signed: bool = False
): # -> bytes
    """
    Availability: >= 0.3.60 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.int_to_bytes
    
    `int.to_bytes()` (backporting update for default value of `length` and `byteorder` parameters from Python 3.11)
    """
    
    if not isinstance(i, int):
        error = TypeError("expected an integer")
        raise error
    
    return i.to_bytes(length, byteorder, signed = signed)

def int_from_bytes(
    i: int,
    /,
    bytes: Union[AVT_Iterable[Indexable], BytesConvertible, ReadableBuffer],
    byteorder: Literal["little", "big"] = "big",
    *,
    signed: bool = False
): # -> int
    """
    Availability: >= 0.3.60 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.int_from_bytes
    
    `int.from_bytes()` (backporting update for default value of `byteorder` parameter before Python 3.11)
    """
    
    if not isinstance(i, int):
        error = TypeError("expected an integer")
        raise error
    
    return i.from_bytes(bytes, byteorder, signed = signed)

# NOTE: for int.is_integer() (>= 3.12) use isinstance(o, int) instead.

def str_replace(
    s: str,
    old: str,
    new: str,
    /,
    count: Indexable = -1
): # -> str
    """
    Availability: >= 0.3.60 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.str_replace
    
    `str.replace()` (backporting update for `count` parameter from Python 3.13 - from positional-only to universal parameter)
    """
    
    if not isinstance(s, str):
        error = TypeError("expected a string")
        raise error
    
    return s.replace(old, new, count)

def str_removeprefix(
    s: str,
    prefix: str,
    /
): # -> str
    """
    Availability: >= 0.3.60 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.str_removeprefix
    
    `str.removeprefix()` (backporting the method before Python 3.9; see PEP 616)
    """
    
    if not isinstance(s, str):
        error = TypeError("expected a string")
        raise error
    
    if _sys.version_info >= (3, 9):
        return s.removeprefix(prefix)
    else:
        if not isinstance(prefix, str):
            error = TypeError("expected 'prefix' parameter to have a string value")
            raise error
        return s[len(prefix):] if s.startswith(prefix) else s[:]
    
def str_removesuffix(
    s: str,
    suffix: str,
    /
): # -> str
    """
    Availability: >= 0.3.60 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.str_removesuffix
    
    `str.removesuffix()` (backporting the method before Python 3.9; see PEP 616)
    """
    
    if not isinstance(s, str):
        error = TypeError("expected a string")
        raise error
    
    if _sys.version_info >= (3, 9):
        return s.removesuffix(suffix)
    else: # patch 0.3.73
        if not isinstance(suffix, str):
            error = TypeError("expected 'suffix' parameter to have a string value")
            raise error
        return s[:-len(suffix)] if suffix and s.endswith(suffix) else s[:] 

# Abbreviating to 'bt' to be more consistent for 'bytes' and 'bytearray' simultaneously.
# If 'bytes' prefix replaced 'bt', then users might be confused this function is for
# 'bytes' objects only and not for 'bytearray' ('bytearray' objects also have methods
# 'removesuffix' and 'removeprefix' since Python 3.9), and this will force them to do
# such as:
# -----
# bytearray(<func>(bytes(<bytearray object>)))
# -----
# if they want to focus on 'bytearray' objects.
@overload
def bt_removeprefix(b: bytes, prefix: ReadableBuffer, /) -> bytes: ...
@overload
def bt_removeprefix(b: bytearray, prefix: ReadableBuffer, /) -> bytearray: ...
def bt_removeprefix(b, prefix, /):
    """
    Availability: >= 0.3.60 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.bt_removeprefix
    
    `[bytes|bytearray].removeprefix()` (backporting the method before Python 3.9; see PEP 616)
    """
    
    if not isinstance(b, (bytes, bytearray)):
        error = TypeError("expected a bytes or bytearray object")
        raise error
    
    if _sys.version_info >= (3, 9):
        return b.removeprefix(prefix)
    else:
        if not isinstance(prefix, ReadableBuffer):
            error = TypeError("expected 'prefix' parameter to have a string value")
            raise error
        return b[len(prefix):] if b.startswith(prefix) else b[:]
    
    
@overload
def bt_removesuffix(b: bytes, suffix: ReadableBuffer, /) -> bytes: ...
@overload
def bt_removesuffix(b: bytearray, suffix: ReadableBuffer, /) -> bytearray: ...
def bt_removesuffix(b, suffix, /):
    """
    Availability: >= 0.3.60 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.bt_removesuffix
    
    `[bytes|bytearray].removesuffix()` (backporting the method before Python 3.9; see PEP 616)
    """
    
    if not isinstance(b, (bytes, bytearray)):
        error = TypeError("expected a bytes or bytearray object")
        raise error
    
    if _sys.version_info >= (3, 9):
        return b.removesuffix(suffix)
    else: # patch 0.3.73
        if not isinstance(suffix, ReadableBuffer):
            error = TypeError("expected 'suffix' parameter to have a string value")
            raise error
        return b[:-len(suffix)] if suffix and b.endswith(suffix) else b[:]
    
def aiter(i: _AsyncIterOperable[_T_anext_cov], /):
    """
    Availability: >= 0.3.60 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.aiter
    
    Backported version of the `aiter()` (Python 3.10+) inbuilt function.
    """
    
    if _sys.version_info >= (3, 10):
        import builtins
        return builtins.aiter(i)
    
    else:
        return i.__aiter__()

@overload
def anext(i: AsyncNextOperable[T], /) -> AVT_Awaitable[T]: ...
@overload
async def anext(i: AsyncNextOperable[T1], default: T2, /) -> Union[T1, T2]: ...

def anext(i: AsyncNextOperable[T1], default: T2 = _Missing, /):
    """
    Availability: >= 0.3.60 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.anext
    
    Backported version of the `anext()` (Python 3.10+) inbuilt function.
    
    When `default` is given, no `StopAsyncIteration` exception is raised and `default` is returned instead (coroutine object value).
    """
    
    if _sys.version_info >= (3, 10):
        
        import builtins
        
        # 0.3.73
        if default is _Missing:
            return builtins.anext(i)
        else:
            return builtins.anext(i, default)
        
    else: # 0.3.72
    
        try:
            return i.__anext__()
        except StopAsyncIteration:
            if default is not _Missing:
                async def _re_anext(default: T2, /):
                    return default
                return _re_anext(default)
            raise StopAsyncIteration
    
@overload
def anext2(i: AsyncNextOperable[T], /) -> T: ...
@overload
def anext2(i: AsyncNextOperable[T1], default: T2, /) -> Union[T1, T2]: ...
    
def anext2(i: AsyncNextOperable[T1], default: T2 = _Missing, /):
    """
    Availability: >= 0.3.73 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.anext2
    
    Backported version of the `anext()` (Python 3.10+) inbuilt function, except it extracts actual value from an awaitable object.
    
    When `default` is given, no `StopAsyncIteration` exception is raised and `default` is returned instead.
    """
    
    import asyncio # for asyncio.run() >= Py3.7
    
    async def _re_anext(i: AsyncNextOperable[T1], default: T2, /):
        
        if _sys.version_info >= (3, 10):
            
            import builtins
            
            if default is _Missing:
                return await builtins.anext(i)
            else:
                return await builtins.anext(i, default)
        
        else:
            try:
                return await i.__anext__()
            except StopAsyncIteration:
                if default is not _Missing:
                    return default
                raise StopAsyncIteration
    
    return asyncio.run(_re_anext(i, default))
        
# Re-declaring eval() and exec() with every argument except 'source' as universal arguments before 3.13. Yet I don't know how to re-declare exec() with 'closure' parameter before Python 3.11
def eval(
    source: Union[str, ReadableBuffer, CodeType],
    /,
    globals: Optional[AVT_Dict[str, Any]] = None,
    locals: Optional[AVT_Mapping[str, object]] = None
):
    """
    Availability: >= 0.3.60 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.eval
    
    Equivalent to the `eval()` inbuilt function, just with changed signature: parameters `globals` and `locals` were positional-only prior to Python 3.13
    """
        
    import builtins
    return builtins.eval(source, globals, locals)

if _sys.version_info >= (3, 11):
    
    def exec(
        source: Union[str, ReadableBuffer, CodeType],
        /,
        globals: Optional[AVT_Dict[str, Any]] = None,
        locals: Optional[AVT_Mapping[str, object]] = None,
        *,
        closure: Optional[AVT_Tuple[CellType, ...]] = None
    ):
        """
        Availability: >= 0.3.60 \\
        https://aveyzan.xyz/aveytense#aveytense.extensions.exec

        Equivalent to the `exec()` inbuilt function, just with changed signature: parameters `globals` and `locals` were positional-only prior to Python 3.13
        
        Keyword-only parameter `closure` exists since Python 3.11
        """
            
        import builtins
        builtins.exec(source, globals, locals, closure = closure)
            
else:
    
    def exec(
        source: Union[str, ReadableBuffer, CodeType],
        /,
        globals: Optional[AVT_Dict[str, Any]] = None,
        locals: Optional[AVT_Mapping[str, object]] = None
    ):
        """
        Availability: >= 0.3.60 \\
        https://aveyzan.xyz/aveytense#aveytense.extensions.exec

        Equivalent to the `exec()` inbuilt function, just with changed signature: parameters `globals` and `locals` were positional-only prior to Python 3.13
        
        Keyword-only parameter `closure` exists since Python 3.11
        """
            
        import builtins
        builtins.exec(source, globals, locals)
        
@overload
def reduce(function: AVT_Callable[[T, S], T], iterable: AVT_Iterable[S], /, initial: S) -> T: ...

@overload
def reduce(function: AVT_Callable[[T, T], T], iterable: AVT_Iterable[T], /) -> T: ...
        
def reduce(function, iterable, /, initial = _Missing):
    """
    Availability: >= 0.3.75 \\
    https://aveyzan.xyz/aveytense#aveytense.extensions.reduce
    
    Equivalent to `functools.reduce()`; backported changed from Python 3.14 regarding the `initial` parameter.
    """
    
    import functools
    
    if initial is _Missing:
        return functools.reduce(function, iterable)
    else:
        return functools.reduce(function, iterable, initial)

__all__ = sorted([k for k in globals() if not k.startswith("_")])
__all_deprecated__ = sorted([k for k in range(len(__all__)) if hasattr(__all__[k], "__deprecated__")]) # 0.3.44

if __name__ == "__main__":
    error = RuntimeError("Import-only module")
    raise error