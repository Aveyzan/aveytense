"""
Availability: >= 0.3.34 \\
© 2024-Present Aveyzan // License: MIT

Core of `aveytense.util`; use `aveytense.util` instead
"""
from __future__ import annotations

import abc as _abc
import sys as _sys

from . import _extensions
from ._exceptions import _ErrorHandler as _E
from ._typeparams import (
    T as _T,
    T_cov as _T_cov,
    P as _P,
    KT as _KT,
    VT as _VT,
    KT2 as _KT2,
    VT2 as _VT2
)

if _extensions.TYPE_CHECKING:
    from _typeshed import SupportsKeysAndGetItem as _KeyItemGetter

__name__ = "aveytense.util"

_ch = _extensions.eval # checker

_T_func = _extensions.TypeVar("_T_func", bound = _extensions.AVT_Callable[..., _extensions.Any])
_T_enum = _extensions.TypeVar("_T_enum", bound = _extensions.Enum)

# That's 'None' at runtime. 'typing.Any' for type hinting purposes while not wanting to type hint with ':' or 'typing.cast()'.
# I would also use other alternatives, but this seems creative enough
_AnyObjectHinter = StopIteration().value

_RichComparable: _extensions.TypeAlias = _extensions.RichComparable
_OptionSelection: _extensions.TypeAlias = _extensions.Literal["frozen", "final", "abstract", "no_reassign", "forced_abstract"] # 0.3.27rc2
_AllMode: _extensions.TypeAlias = _extensions.Literal[
    "clear",
    "lowercased",
    "lowercased_clear",
    "uppercased",
    "uppercased_clear",
    "sunder",
    "lowercased_sunder",
    "uppercased_sunder",
    "dunder",
    "lowercased_dunder",
    "uppercased_dunder",
    "protected",
    "lowercased_protected",
    "uppercased_protected",
    "private",
    "lowercased_private",
    "uppercased_private",
    "all"
] # 0.3.53

def _reckon(i: _extensions.AVT_Iterable[_T], /):
    
    _i = 0
    
    for _ in i:
        _i += 1
        
    return _i

def _ih(id: int, /): # internal helper
    
    _m = "eval"
    _c = _i = ""
    
    if id == 10:
        
        _c, _i = "_E(113, t.__name__)", "<final-class inspect>"
        
    elif id == 11:
        
        _c, _i = "_E(116, type(self).__name__)", "<final-class inspect>"
        
    elif id == 12:
        
        _c, _i = "_E(116, t.__name__)", "<final-class inspect>"
        
    elif id == 20:
        
        _c, _i = "_E(104, type(self).__name__)", "<abstract-class inspect>"
    
    elif id == 21:
        
        _c, _i = "_E(115, type(self).__name__)", "<abstract-class inspect>"
        
    elif id == 22:
        
        _c, _i = "_E(115, t.__name__)", "<abstract-class inspect>"
        
    return compile(_c, _i, _m)
    
def _return_param(f = object(), s = ""): # 0.3.47
    """
    Availability: >= 0.3.47
    
    Used to remove private method notation on pre-PEP 570 positional-only parameters in a method. \\
    Not intended to be shared globally; this function is reserved for `~.util.ParamVar` class only.
    ```
        _return_param(Class().method, "__1") # -> __1 instead of _Class__1
        _return_param(Class().method, "__1_") # -> __1_ instead of _Class__1_
        _return_param(Class().method, "__1__") # -> __1__ (no change)
    ```
    """
    
    # 0.3.50: callable(...) and __name__ != __qualname__
    if isinstance(f, _extensions.MethodType) or (callable(f) and f.__name__ != f.__qualname__):
        
        _class_ = "_" +  _extensions.str_removesuffix(f.__qualname__, "." + f.__name__)
        
        if s.startswith(_class_ + "__") and not s.endswith("__"):
            return _extensions.str_removeprefix(s, _class_)
            
    return s

def _check_if_callable(f): # 0.3.51
    
    return callable(f) or isinstance(f, _extensions.partial)

def _check_if_builtin(f): # 0.3.51
    
    return isinstance(f, (
        _extensions.BuiltinFunctionType,
        _extensions.ClassMethodDescriptorType,
        _extensions.MethodDescriptorType,
        _extensions.MethodWrapperType,
        _extensions.WrapperDescriptorType
    ))

def _param_sanitize(param = "", includeEqualSign = False): # 0.3.51
    """Used in internal class `~.util._BuiltinParamVar`"""
            
    s = ""
    
    for c in param:
        
        if c == "=":
            
            if includeEqualSign:
                s += c
            
            break
        
        s += c
        
    return s.lstrip("*")


class _Immutable:
    """
    Availability: >= 0.3.53 (`_FlagsType` < 0.3.57)
    
    Subclasses of this class cannot have attributes modified. This doesn't fully work and shouldn't be used in production code.
    """
    
    def __init_subclass__(cls):
        
        cls._members = [""]
        
        def __setattr__(self: _extensions.Self, name: str, value: _extensions.Any):
            
            if hasattr(self, "__qualname__"):
                
                if (
                    (self.__qualname__ in ("Tense",) and name in ("_Tense__frame",))
                ):
                    return
            
            if name in (*self._members[1:], "_members"):
                _E(102, "'{}'".format(name))
                
            else:
                self._members.append(name)
                setattr(self, name, value)
            
        def __delattr__(self: _extensions.Self, name: str):
            
            if name in (*self._members[1:], "_members"):
                error = TypeError("cannot delete member '{}'".format(name))
                raise error
            
            else:
                delattr(self, name)
                
        cls.__setattr__ = __setattr__
        cls.__delattr__ = __delattr__
        
class _TenseImmutableMeta(type, _Immutable):
    """Availability: >= 0.3.58"""
    
_extensions._prevent_unused_imports(_TenseImmutableMeta) # used in aveytense.Tense
            
class _TypeFlags:
    """Availability: >= 0.3.53"""
    
    # https://github.com/python/cpython/blob/31a8393cf6a74c870c3484dd68500619f6232c6d/Include/object.h#L598
    # In C notation '1UL' ('unsigned long long') is used to get wider positive value range. In Python this notation doesn't exist,
    # but we can use '1' instead
    # exception is 'mapping' property: see _collections_abc.Mapping.__abc_tpflags__ from _collections_abc.py
    
    @property
    def haveFinalize(self):
        """Type flag for types having attribute `tp_finalize`"""
        return 1
    
    @property 
    def mapping(self):
        return 1 << 6
    
    @property
    def heapType(self):
        """Type flag for types dynamically allocated"""
        return 1 << 9
    
    @property
    def baseType(self):
        """Type flag for inheritable types"""
        return 1 << 10
    
    @property
    def ready(self):
        """Type flag for fully initialized ("ready") types"""
        return 1 << 12
    
    @property
    def readying(self):
        """Type flag for types preparing to be fully initialized ("readying")"""
        return 1 << 13
    
    @property
    def haveGc(self):
        """Type flag for types supporting garbage collection"""
        return 1 << 14
    
    @property
    def haveStacklessExtension(self):
        """Type flag for Stackless Python (< 3.10). Value is `0` if Stackless isn't used, either way it is `32768`"""
        
        import os
        
        if os.getenv("STACKLESS", False) and _sys.version_info < (3, 10):
            return 1 << 15
        else:
            return 0
    
    @property
    def haveVersionTag(self):
        """Type flag for types supporting attribute cache"""
        return 1 << 18
    
    @property
    def validVersionTag(self):
        """Type flag for types supporting attribute cache"""
        return 1 << 19
    
    @property
    def abstract(self):
        """Type flag for abstract types"""
        return 1 << 20
    
    @property
    def longSubclass(self):
        """Type flag for subclasses of `long` (for Python 3 that's `int`)"""
        return 1 << 24
    
    @property
    def listSubclass(self):
        """Type flag for subclasses of `list`"""
        return 1 << 25
    
    @property
    def tupleSubclass(self):
        """Type flag for subclasses of `tuple`"""
        return 1 << 26
    
    @property
    def bytesSubclass(self):
        """Type flag for subclasses of `bytes`"""
        return 1 << 27
    
    @property
    def unicodeSubclass(self):
        """Type flag for subclasses of `unicode` (for Python 3 that's `str`)"""
        return 1 << 28
    
    @property
    def dictSubclass(self):
        """Type flag for subclasses of `dict`"""
        return 1 << 29
    
    @property
    def baseExcSubclass(self):
        """Type flag for subclasses"""
        return 1 << 30
    
    @property
    def typeSubclass(self):
        """Type flag for subclasses of `type`"""
        return 1 << 31
    
    @property
    def default(self):
        """Type flag equivalent to `Py_TPFLAGS_HAVE_STACKLESS_EXTENSION | Py_TPFLAGS_HAVE_VERSION_TAG | 0`"""
        return self.haveStacklessExtension | self.haveVersionTag
    
class _CodeFlags:
    """Availability: >= 0.3.53"""
    
    # https://github.com/python/cpython/blob/31a8393cf6a74c870c3484dd68500619f6232c6d/Include/code.h#L54
    @property
    def optimized(self):
        """Code flag for optimized objects"""
        return 1
    
    @property
    def newlocals(self):
        """Code flag for frame objects returning a new dictionary from `f_locals` upon execution"""
        return 1 << 1
    
    @property
    def varargs(self):
        """Code flag for callable objects having variable positional argument (`*<param-name>`)"""
        return 1 << 2
    
    @property
    def varkeywords(self):
        """Code flag for callable objects having variable keyword argument (`**<param-name>`)"""
        return 1 << 3
    
    @property
    def nested(self):
        """Code flag for nested functions"""
        return 1 << 4
    
    @property
    def generator(self):
        """Code flag for generator objects"""
        return 1 << 5
    
    @property
    def noFree(self):
        return 1 << 6
    
    @property
    def coroutine(self):
        """Code flag for coroutine objects"""
        return 1 << 7
    
    @property
    def iterableCoroutine(self):
        """Code flag for generator-based coroutine objects"""
        return 1 << 8
    
    @property
    def asyncGenerator(self):
        """Code flag for asynchronous generator objects"""
        return 1 << 9
    
    if _sys.version_info >= (3, 14):
        
        @property
        def hasDocString(self): # 0.3.57
            """Code flag for objects having docstring in their source code"""
            return 0x4000000
        
        @property
        def method(self): # 0.3.57
            """Code flag for functions defined in a class"""
            return 0x8000000
    
class _BufferFlags:
    """Availability: >= 0.3.53"""
    
    # retrieved via 'inspect.BufferFlags' source code for Python 3.13.5
    @property
    def contiguous(self):
        return 0x9
    
    @property
    def contiguousAny(self):
        return 0x98
    
    @property
    def contiguousC(self):
        """C-contiguous"""
        return 0x38
    
    @property
    def contiguousF(self):
        """Fortran contiguous"""
        return 0x58
    
    @property
    def contiguousReadOnly(self):
        return 0x18
    
    @property
    def format(self):
        return 0x4
    
    @property
    def full(self):
        return 0x11d
    
    @property
    def fullReadOnly(self):
        return 0x11c
    
    @property
    def indirect(self):
        return 0x118
    
    @property
    def nd(self):
        return 0x8
    
    @property
    def read(self):
        return 0x100
    
    @property
    def records(self):
        return 0x1d
    
    @property
    def recordsReadOnly(self):
        return 0x1c
    
    @property
    def simple(self):
        return 0x0
    
    @property
    def strided(self):
        return 0x19
    
    @property
    def stridedReadOnly(self):
        return 0x18
    
    @property
    def strides(self):
        return 0x18
    
    @property
    def writable(self):
        return 0x1
    
    @property
    def write(self):
        return 0x200

class _InternalHelper:
    """
    Availability: >= 0.3.27rc2
    
    Class responsible to shorten code for several classes such as `Final` and `Abstract`
    """
    
    def __new__(cls, t: _extensions.AVT_Type[_T], o: _OptionSelection, /):
        
        _reassignment_operators = {
            "__iadd__": "+=",
            "__isub__": "-=",
            "__imul__": "*=",
            "__itruediv__": "/=",
            "__ifloordiv__": "//=",
            "__imod__": "",
            "__imatmul__": "@=",
            "__iand__": "&=",
            "__ior__": "|=",
            "__ixor__": "^=",
            "__ilshift__": "<<=",
            "__irshift__": ">>=",
            "__ipow__": "**="
        }
        
        _cannot_redo = {"": ""}
        
        # assuming empty string-string dictionary
        _cannot_redo.clear()
        
        def _no_sa(self: _T, name: str, value): # no setattr
            
            if name in type(self).__dict__:
                _E(118, name)
            
            self.__dict__[name] = value
            
        def _no_da(self: _T, name: str): # no delattr
            
            if name in type(self).__dict__:
                _E(117, name)
                
        def _no_inst(self: _T, *args, **kwds): # no initialize
            _ch(_ih(20))
            
        def _no_cinst(o: object): # no check instance
            nonlocal t
            _ch(_ih(22))
            
        def _no_sub(*args, **kwds): # no subclass
            nonlocal t
            _ch(_ih(10))
            
        def _no_csub(cls: type): # no check subclass
            nonlocal t
            _ch(_ih(12))
            
        def _no_re(op: str): # no reassignment; must return callback so assigned attributes can be methods
            
            def _no_re_internal(self: _extensions.Self, other: _T):
                
                _op = "with operator {}".format(op)
                _E(102, _op)
                
            return _no_re_internal
        
        def _empty_mro(self: _T): # empty method resolution order; peculiar for final classes
            return None
        
        if o in ("frozen", "no_reassign"):
            
            t.__slots__ = ("__weakref__",)
            t.__setattr__ = _no_sa
            t.__delattr__ = _no_da
            
            _cannot_redo["__setattr__"] = _no_sa.__name__
            _cannot_redo["__delattr__"] = _no_da.__name__
            
            if o == "no_reassign":
                
                for key in _reassignment_operators:
                    
                    exec("t.{} = _no_re(\"{}\")".format(key, _reassignment_operators[key])) # f-strings since python 3.6
                    exec("_cannot_redo[\"{}\"] = _no_re(\"{}\").__name__".format(key, _reassignment_operators[key]))
                    
        elif o == "final":
            
            t.__slots__ = ("__weakref__",)
            t.__init_subclass__ = _no_sub
            t.__subclasscheck__ = _no_csub
            t.__mro_entries__ = _empty_mro
            
            _cannot_redo["__init_subclass__"] = _no_sub.__name__
            _cannot_redo["__subclasscheck__"] = _no_csub.__name__
            _cannot_redo["__mro_entries__"] = _empty_mro.__name__
            
        else:
            
            if o == "forced_abstract":
                t.__call__ = _no_inst
                
                _cannot_redo["__call__"] = _no_inst.__name__
            
            else:
                t.__init__ = _no_inst
                t.__instancecheck__ = _no_cinst
                
                _cannot_redo["__init__"] = _no_inst.__name__
                _cannot_redo["__instancecheck__"] = _no_cinst.__name__
            
        for key in _cannot_redo:
            if _cannot_redo[key] != "_no_re_internal" and eval("t.{}.__code__".format(key)) != eval("{}.__code__".format(_cannot_redo[key])):
                _E(120, key)    
        
        return t
    
class Abstract:
    """
    Availability: >= 0.3.26b3 \\
    https://aveyzan.xyz/aveytense#aveytense.util.Abstract
    
    Creates an abstract class. This type of class forbids class initialization.
    
    To promote a class abstract, it needs to be inherited, as shown::
        
        from aveytense.util import Abstract
        
        class A(Abstract): ...
        print(A()) # InitializedError
        
    This is done by overriding `__init__` method. Worth noticing the class doesn't work the same as
    `abc.ABC`. Class object construction from `abc.ABC` is allowed only, if there aren't any abstract
    methods, meanwhile `aveytense.util.Abstract` doesn't require any abstract methods to throw an error upon
    object initialization.
    """
    
    def __init__(self):
        _ch(_ih(20))
        
    def __init_subclass__(cls):
        cls = _InternalHelper(cls, "abstract")
    
    def __instancecheck__(self, instance: object):
        "Availability: >= 0.3.27b1. Error is thrown, because class may not be instantiated"
        _ch(_ih(21))
    
    def __subclasscheck__(self, cls: type):
        "Availability: >= 0.3.27b1. Check whether a class is a subclass of this class"
        return issubclass(cls, type(self))
    
    if False: # 0.3.28 (use abstractmethod instead)
        @staticmethod
        def method(f: _T_func):
            """Availability: >= 0.3.27rc2"""
            from abc import abstractmethod as _a
            return _a(f)

def abstract(t: _extensions.AVT_Type[_T], /): # <- 0.3.41 slash
    """
    Availability: >= 0.3.27a5 (formally)
    
    Decorator for abstract classes. To 0.3.27rc2 same as `abc.abstractmethod()`
    """
    t = _InternalHelper(t, "abstract")
    return t

class Final:
    """
    Availability: >= 0.3.26b3 (experimental; to 0.3.27b3 `FinalClass`, experiments ended 0.3.27rc1) \\
    https://aveyzan.xyz/aveytense#aveytense.util.Final
    
    Create a final class. Subclasses of this class disallow further inheritance. Example::
    
        from aveytense.util import Final
        
        class F1(Final): ...
        class F2(F1): ... # SubclassedError
    
    This class is a reference to local class `typing._Final`, with lack of necessity
    providing the `_root` keyword to inheritance section.
    """
    __slots__ = ("__weakref__",)

    def __init_subclass__(cls):
        cls = _InternalHelper(cls, "final")
       
    def __instancecheck__(self, instance: object):
        "Availability: >= 0.3.27rc1. Check whether an object is instance to this class"
        return isinstance(instance, type(self))
    
    def __subclasscheck__(self, cls: type):
        "Availability: >= 0.3.27rc1. Error is thrown, because this class may not be subclassed"
        _ch(_ih(11))
       
    def __mro_entries__(self):
        return None
    
    @property
    def __mro__(self):
        return None
    
    if False: # 0.3.28 (use finalmethod instead)
        @staticmethod
        def method(f: _T_func):
            """Availability: >= 0.3.27rc2"""
            
            if _sys.version_info >= (3, 11):
                from typing import final as _f
                
            else:
                from typing_extensions import final as _f
                
            return _f(f)
    
def final(t: _extensions.AVT_Type[_T], /): # <- 0.3.41 slash
    """
    Availability: >= 0.3.26b3 \\
    https://aveyzan.xyz/aveytense#aveytense.util.final
    """
    t = _InternalHelper(t, "final")
    return t

def finalmethod(f: _T_func, /): # <- 0.3.41 slash
    """
    Availability: >= 0.3.27rc2 \\
    https://aveyzan.xyz/aveytense#aveytense.util.finalmethod
    """
    if False:
        return Final.method(f)
    
    else:
        
        if isinstance(f, _extensions.MethodType):
            return _extensions.cast(_T_func, _extensions.final(f))
        
        else:
            error = TypeError("expected a method")
            raise error

# it is worth noticing that even if 'finalproperty' class doesn't formally inherit
# from 'property' builtin, it is considered a 'property' builtin anyway. reason it
# does is because of descriptor methods __get__, __set__ and __delete__
# 18.03.2025

@_extensions.deprecated("Deprecated since 0.3.75, will be removed in 0.3.78. Use '@property' instead")
class finalproperty(_extensions.Generic[_T]):
    """
    Availability: >= 0.3.37 \\
    https://aveyzan.xyz/aveytense#aveytense.util.finalproperty
    
    A decorator which creates a final (constant) property. 
    This property cannot receive new values nor be deleted, what makes 
    this property read-only. This class doesn't inherit from `property`, 
    however, it returns a new property - just classified as final. It is
    worth noticing this is *instance* final property, not like
    `jaraco.classes.properties.classproperty`.
    
    Usage of `~.finalproperty` is as simple as `property` inbuilt decorator::
    
        from aveytense.util import finalproperty
        
        class R:
            
            @property
            def val(self):
                return 42
        
        print(R.val) # <finalproperty 'R.val'>
        print(R().val) # 42
    """
    
    def __init__(self, f: _extensions.AVT_Callable[[_extensions.Any], _T], /):
        
        if isinstance(f, staticmethod):
            f = f.__func__
        
        if not callable(f) or (callable(f) and (f.__code__.co_argcount != 1 or f.__code__.co_kwonlyargcount != 0)):
            error = TypeError("expected callable with one parameter, or attempt to create final static property with no parameters")
            raise error
        
        self.__func = f
        self.__doc__ = f.__doc__
        
    def __str__(self):
        
        return "<final-property '{}'>".format(self.__func.__qualname__) # < 0.3.44; >= 0.3.69
        
    @_extensions.overload
    def __get__(self, instance: None, owner: _extensions.Optional[type] = None) -> finalproperty[_T]: ...
    
    @_extensions.overload
    def __get__(self, instance: _extensions.Any, owner: _extensions.Optional[type] = None) -> _T: ...
        
    def __get__(self, instance, owner = None):
        
        if instance is None:
            return self
        
        a = self.__func(instance)
        return a
    
    def __set__(self, instance, value):
        
        v = self.__func.__name__
        _E(122, v)
        
    def __delete__(self, instance):
        
        v = self.__func.__name__
        _E(122, v)
        
    @property
    def __func__(self): # >= 0.3.69
        return self.__func

if False: # >= 0.3.43
    
    class finalstaticproperty(_extensions.Generic[_T]):
        
        def __init__(self, f: _extensions.Callable[[], _T], /):
            
            if isinstance(f, staticmethod):
                f = f.__func__
            
            if not callable(f) or (f.__code_extensions.co_argcount != 0 or f.__code_extensions.co_kwonlyargcount != 0):
                error = TypeError("expected callable with no parameters")
                raise error
            
            self.func = f
            self.__name__ = f.__name__
            self.__doc__ = f.__doc__
            
        def __get__(self, instance, owner = None):
            
            if owner is not None and isinstance(owner, type(self)):
                return owner.func.__func__()
            
            return self.func.__func__()
        
        def __set__(self, instance, value):
            
            v = self.func.__name__
            _E(122, v)
            
        def __delete__(self, instance):
            
            v = self.func.__name__
            _E(122, v)

if False: # < 0.3.52
    @final
    class ClassLike(_extensions.Generic[_P, _T]):
        """
        Availability: >= 0.3.27a3
        
        To 0.3.35 this class was in `aveytense.types_collection`. \\
        A class decorator for functions, transforming them to declarations \\
        similar to classes. Example::
        
            @ClassLike
            def test():
                return 42

            a = test() # returns 42

        """
        def __init__(self, f: _extensions.AVT_Callable[_P, _T]):
            self.f = f
            
        def __call__(self, *args: _P.args, **kwds: _P.kwargs):
            return self.f(*args, **kwds)
        
    classlike = ClassLike # since 0.3.27a3
        
AbstractMeta = _abc.ABCMeta
"""
Availability: >= 0.3.27b1. Use it as::
```
class AbstractClass(metaclass = AbstractMeta): ...
```
"""

class AbstractFinal:
    """
    Availability: >= 0.3.27rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.util.AbstractFinal
    
    Creates an abstract-final class. Blend of `Abstract` and `Final` classes
    within submodule `aveytense.util`. Classes extending this class are
    only restricted to modify fields (as in `TenseOptions`) or invoke static methods,
    because these classes cannot be neither initialized nor inherited.
    """
    __slots__ = ("__weakref__",)
    
    def __init__(self):
        _ch(_ih(20))
    
    def __init_subclass__(cls):
        cls = _InternalHelper(cls, "abstract")
        cls = _InternalHelper(cls, "final")
       
    def __mro_entries__(self):
        return None
    
    @property
    def __mro__(self):
        return None
    
    def __instancecheck__(self, instance: object):
        "Availability: >= 0.3.27rc1. Error is thrown, because class may not be instantiated"
        _ch(_ih(21))
    
    def __subclasscheck__(self, cls: type):
        "Availability: >= 0.3.27rc1. Error is thrown, because class may not be subclassed"
        _ch(_ih(11))

@_extensions.dataclass(init = False, repr = False, eq = False, frozen = True) # 0.3.74
class SortedList(_extensions.Generic[_T]):
    """
    Availability: >= 0.3.35
    
    Creates a sorted list. Note this class doesn't inherit from the `list` builtin itself.
    """
    
    # The types are genuine and these attributes exist actually.
    __list: _extensions.AVT_List[_T]
    __sorted: _extensions.AVT_List[_T]
    
    def __init__(self, i: _extensions.AVT_Iterable[_T], /, key: _extensions.Optional[_extensions.AVT_Callable[[_T], _RichComparable]] = None, reverse = False): # 0.3.35

        if not isinstance(i, _extensions.Iterable):
            error = ValueError("expected an iterable object")
            raise error
        
        _mangle = lambda attr = "": "_" + type(self).__name__ + attr
        
        object.__setattr__(self, _mangle("__list"), list(i))
        object.__setattr__(self, _mangle("__sorted"), sorted(i, key = key, reverse = reverse))
        
        del _mangle
    
    def __iter__(self): # 0.3.35
        return iter(self.__sorted)
    
    def __len__(self): # 0.3.35
        return len(self.__sorted)
    
    @_extensions.overload
    def __getitem__(self, index: int, /) -> _T: ...
    @_extensions.overload
    def __getitem__(self, index: slice, /) -> _extensions.AVT_List[_T]: ...
    
    def __getitem__(self, index: _extensions.Union[int, slice], /): # 0.3.35
        return self.__sorted[index]
    
    def __contains__(self, item: _T, /): # 0.3.35
        return item in self.__sorted
    
    def __eq__(self, other, /): # 0.3.35
        return type(other) == type(self) and list(self) == list(other)
    
    def __ne__(self, other, /): # 0.3.35
        return not self.__eq__(other)
        
    def __str__(self): # 0.3.35
        return "{}({})".format(type(self).__name__, len(self.__list))
    
    def __repr__(self): # 0.3.35
        from . import _ReprStr
        return _ReprStr.format(type(self).__qualname__, id(self))
        
    def reverse(self, v = False, /):
        """Availability: >= 0.3.35"""
        if v:
            self.__sorted.reverse()
            
    def setKey(self, v: _extensions.Optional[_extensions.AVT_Callable[[_T], _RichComparable]] = None, /):
        """Availability: >= 0.3.35"""
        
        self.__sorted = self.__list
        if v is not None:
            self.__sorted.sort(key = v)
            
def all(name: str = "all", mode: _extensions.Union[_AllMode, _extensions.AVT_Callable[[str], bool]] = "clear", deprecatedInclude: bool = False, deprecatedName: _extensions.Optional[str] = None):
    """
    Availability: >= 0.3.53
    
    Creates `__all__` or user named attribute for target class as a decorator to store its names in a string list. \\
    This decorator is unrealized concept from 0.3.41
    
    Parameters
    
    - `name`: The name of the attribute that will store the names. Whitespaces around it then underscores around it \\
        are removed from the given name, and `name` becomes a dunder attribute for the type, that is: `__<name>__`
    - `mode`: Either a name of a mode as a string or a callable object with one parameter. Default value is `"clear"` \\
        that retrieves all names without even single underscore preceding
    - `deprecatedInclude`: If set to `True`, given type will receive a dunder attribute for deprecated definitions no \\
        matter the letter case or presence of underscores before or/and after.
    - `deprecatedName`: Only takes place when `deprecatedInclude` is set to `True`. If `None` or empty string, then \\
        attribute for deprecated definitions is `__<name>_deprecated__`, otherwise it is `__<deprecatedName>__`. Same
        actions about the name are performed as with `name` parameter
    """
        
    def _internals(t: _extensions.AVT_Type[_T], /):
        
        if not isinstance(t, type):
            error = TypeError("expected a class")
            raise error
        
        nonlocal name, mode, deprecatedInclude, deprecatedName
        
        if not isinstance(name, str):
            error = TypeError("the 'name' parameter must be a string")
            raise error
        
        if not isinstance(deprecatedInclude, bool):
            error = TypeError("the 'name' parameter must be a boolean value")
            raise error
        
        if not isinstance(deprecatedName, (str, _extensions.NoneType)):
            error = TypeError("the 'deprecatedName' parameter must be a string or 'None'")
            raise error
    
        _dict_ = dict(t.__dict__) # 'mappingproxy', hence we convert to 'dict'
        
        if name.strip().strip("_"):
            _name_ = "__{}__".format(name.strip().strip("_"))
        else:
            error = TypeError("expected at least one char not being underscore and whitespace")
            raise error
        
        if mode == "clear":
            _dict_.update({ _name_: sorted([k for k in t.__dict__ if not k.startswith("_")]) })
            
        elif mode == "lowercased":
            _dict_.update({ _name_: sorted([k for k in t.__dict__ if k.islower()]) })
            
        elif mode == "lowercased_clear":
            _dict_.update({ _name_: sorted([k for k in t.__dict__ if k.islower() and not k.startswith("_")]) }) 
            
        elif mode == "uppercased":
            _dict_.update({ _name_: sorted([k for k in t.__dict__ if k.isupper()]) })
            
        elif mode == "uppercased_clear":
            _dict_.update({ _name_: sorted([k for k in t.__dict__ if k.isupper() and not k.startswith("_")]) })
            
        elif mode == "sunder":
            _dict_.update({ _name_: sorted([k for k in t.__dict__ if (k.startswith("_") and not k.startswith("__")) and (k.endswith("_") and not k.endswith("__"))]) })
            
        elif mode == "lowercased_sunder":
            _dict_.update({ _name_: sorted([k for k in t.__dict__ if k.islower() and (k.startswith("_") and not k.startswith("__")) and (k.endswith("_") and not k.endswith("__"))]) })
            
        elif mode == "uppercased_sunder":
            _dict_.update({ _name_: sorted([k for k in t.__dict__ if k.isupper() and (k.startswith("_") and not k.startswith("__")) and (k.endswith("_") and not k.endswith("__"))]) })
            
        elif mode == "dunder":
            _dict_.update({ _name_: sorted([k for k in t.__dict__ if k.startswith("__") and k.endswith("__")]) })
            
        elif mode == "lowercased_dunder":
            _dict_.update({ _name_: sorted([k for k in t.__dict__ if k.islower() and k.startswith("__") and k.endswith("__")]) })
            
        elif mode == "uppercased_dunder":
            _dict_.update({ _name_: sorted([k for k in t.__dict__ if k.isupper() and k.startswith("__") and k.endswith("__")]) })
            
        elif mode == "protected":
            _dict_.update({ _name_: sorted([k for k in t.__dict__ if k.startswith("_") and not k.endswith("_")]) })
            
        elif mode == "lowercased_protected":
            _dict_.update({ _name_: sorted([k for k in t.__dict__ if k.islower() and k.startswith("_") and not k.endswith("_")]) })
            
        elif mode == "uppercased_protected":
            _dict_.update({ _name_: sorted([k for k in t.__dict__ if k.isupper() and k.startswith("_") and not k.endswith("_")]) })
            
        elif mode == "private":
            _dict_.update({ _name_: sorted([k for k in t.__dict__ if k.startswith("__") and not k.endswith("__")]) })
            
        elif mode == "lowercased_private":
            _dict_.update({ _name_: sorted([k for k in t.__dict__ if k.islower() and k.startswith("__") and not k.endswith("__")]) })
            
        elif mode == "uppercased_private":
            _dict_.update({ _name_: sorted([k for k in t.__dict__ if k.isupper() and k.startswith("__") and not k.endswith("__")]) })
            
        elif callable(mode) and mode.__code_extensions.co_argcount == 1 and mode.__defaults__ is None:
            _dict_.update({ _name_: sorted([k for k in t.__dict__ if mode(k) ]) })
            
        else:
            error = TypeError("invalid mode, expected callable object with one parameter or a string value from the following: " + str(_AllMode.__args__[0].__args__)[1:-1])
            raise error
        
        if deprecatedInclude:
            
            if deprecatedName and deprecatedName.strip().strip("_"):
                _deprecated_name_ = "__{}__".format(deprecatedName.strip().strip("_"))
                
                if _deprecated_name_ == _name_: # 0.3.54
                    _deprecated_name_ = "__{}_deprecated__".format(_name_.strip().strip("_"))
                
            else:
                _deprecated_name_ = "__{}_deprecated__".format(_name_.strip().strip("_"))
            
            _dict_.update({ _deprecated_name_: sorted([k for k in t.__dict__ if hasattr(t.__dict__[k], "__deprecated__") or isinstance(t.__dict__[k], _extensions.deprecated)]) })
        
        return _extensions.cast(_extensions.AVT_Type[_T], type(t.__name__, t.__bases__, _dict_))
    
    return _internals
    
_builtin_classes = (int, float, complex, filter, memoryview, bytearray, bytes, str, slice, map, range, bool, list, tuple, set, frozenset, dict, object, reversed, enumerate, zip)

class ParamNoDefault(Abstract):
    """
    Availability: >= 0.3.51 \\
    https://aveyzan.xyz/aveytense#aveytense.util.ParamNoDefault
    
    Used to denote parameters without default value with final \\
    properties ending with `withDefaults` suffix, in `aveytense.util.ParamVar`.
    
    Public since 0.3.74
    """
    
class _BuiltinParamVar:
    """
    Availability: >= 0.3.51
    
    Used in `aveytense.util.ParamVar` to receive parameters from inbuilt functions. Note: none of these have annotations.
    """
    
    def __init__(self, f):
        
        if not isinstance(f, ( # these are defined since Python 3.7 (except 'BuiltinFunctionType')
            _extensions.BuiltinFunctionType,
            _extensions.ClassMethodDescriptorType,
            _extensions.MethodDescriptorType,
            _extensions.MethodWrapperType,
            _extensions.WrapperDescriptorType 
        )):
            error = TypeError("provided object is not a builtin")
            raise error
        
        # 0.3.51
        # If only we were able to do much...
        # Inbuilt functions are supported, but a question beg inbuilt methods, which in most
        # cases return signature (*args, **kwargs) with no useful signature information.
        _unsanitized_signature_ = getattr(f, "__text_signature__", None)
        _SPACES_ = [" " * 0b111][0]
        
        if type(_unsanitized_signature_) is str:
            
            def _await_comma(s = ""):
                
                s2 = ""
                
                for c in s:
                    
                    s2 += c
                    
                    if c == ",":
                        break
                    
                return _reckon(s2)  
            
            _revoke_first_ = _unsanitized_signature_[: _await_comma(_unsanitized_signature_) + 1]
            
            _signature_ = _extensions.str_removeprefix(_extensions.str_removeprefix(_unsanitized_signature_,  _revoke_first_), "/, ").replace("\n" + _SPACES_, "")
            _signature2_ = _extensions.str_removesuffix(_signature_, ")").split(", ")
            
            self.__signature = _signature_ 
            self.__gleaned_params = list(filter(lambda x: _reckon(x) > 0, _signature2_))
            
        else:
            error = TypeError("unable to retrieve signature")
            raise error
        
    @property
    def signature(self): # 0.3.51
        
        return "(" + self.__signature.replace("=", " = ")
        
    @property
    def all(self): # 0.3.51
        
        return tuple([_param_sanitize(p) for p in self.__gleaned_params if p not in ("/", "*")])
        
    @property
    def allDefaults(self): # 0.3.51
        
        _return_ = [("", StopIteration.value)]
        _return_.clear()
        _return_.extend([(_param_sanitize(p), p[_reckon(_param_sanitize(p, True)):]) for p in self.__gleaned_params if _param_sanitize(p, True).endswith("=")])
        return tuple(_return_)
    
    @property
    def allWithDefaults(self): # 0.3.51
        
        return tuple([(p, ParamNoDefault if p not in dict(self.allDefaults) else dict(self.allDefaults)[p]) for p in self.all])
    
    @property
    def allNoDefaults(self): # 0.3.51
        
        return tuple([p for p in self.all if p not in dict(self.allDefaults)])
    
    @property
    def positional(self): # 0.3.51
        
        _return_ = [""]
        _return_.clear()
        
        for p in self.__gleaned_params:
            
            # pre-pep 570 (statement after 'or')
            if p == "/" or ("/" not in self.__gleaned_params and not p.endswith("__")):
                break
            
            _return_.append(p)
            
        return tuple(_return_)
    
    @property
    def positionalDefaults(self): # 0.3.51
        
        return tuple([p for p in self.allDefaults if p[0] in self.positional])
    
    @property
    def positionalWithDefaults(self): # 0.3.51
        
        return tuple([(p, ParamNoDefault if p not in dict(self.positionalDefaults) else dict(self.positionalDefaults)[p]) for p in self.positional])
    
    @property
    def positionalNoDefaults(self): # 0.3.51
        
        return tuple([p for p in self.positional if p not in dict(self.positionalDefaults)])
    
    @property
    def keyword(self): # 0.3.51
        
        _marker_ = 0
        
        for p in self.__gleaned_params:
            
            # either * or *<param-name>
            if p.startswith("*"):
                break
            
            _marker_ += 1
            
        return tuple([_param_sanitize(p) for p in self.__gleaned_params[_marker_:] if not p.startswith("**")])
    
    @property
    def keywordDefaults(self): # 0.3.51
        
        return tuple([p for p in self.allDefaults if p[0] in self.keyword])
    
    @property
    def keywordWithDefaults(self): # 0.3.51
        
        return tuple([(p, ParamNoDefault if p not in dict(self.keywordDefaults) else dict(self.keywordDefaults)[p]) for p in self.keyword])
    
    @property
    def keywordNoDefaults(self): # 0.3.51
        
        return tuple([p for p in self.keyword if p not in dict(self.keywordDefaults)])
    
    @property
    def universal(self): # 0.3.51
        
        return tuple([p for p in self.all if p not in (*self.positional, *self.keyword) and not p.startswith(("*", "/"))])
    
    @property
    def universalDefaults(self): # 0.3.51
        
        return tuple([p for p in self.allDefaults if p[0] in self.universal])
    
    @property
    def universalWithDefaults(self): # 0.3.51
        
        return tuple([(p, ParamNoDefault if p not in dict(self.universalDefaults) else dict(self.universalDefaults)[p]) for p in self.universal])
    
    @property
    def universalNoDefaults(self): # 0.3.51
        
        return tuple([p for p in self.universal if p not in dict(self.universalDefaults)])
    
    @property
    def variable(self): # 0.3.51
        
        _return_ = [("", "")]
        _return_.clear()
        
        for p in self.__gleaned_params:
            
            if p.startswith("**"):
                _return_.append((_param_sanitize(p), "<args>"))
                
            elif p.startswith("*") and p != "*":
                _return_.append((_param_sanitize(p), "<kwargs>"))
                
        return tuple(_return_)

class ParamVar:
    """
    Availability: >= 0.3.42 \\
    In projection: >= 0.3.33; < 0.3.42 \\
    https://aveyzan.xyz/aveytense#aveytense.util.ParamVar
    
    Allows to obtain positional, universal,
    keyword (and their default values) and variable (`*<param>`
    and `**<param>`) arguments, and signature of a callable
    object.
    
    *Constructor general information*
    
    If `f` is overloaded function, used is `i` index to denote
    specific signature. `f` must be any callable object
    """
    
    __builtin: _extensions.Optional[_BuiltinParamVar]
    __func: _extensions.AVT_Callable[..., _extensions.Any]
    __no_first: _extensions.Literal[0, 1]
    __vartype: str
    
    def __init__(self, f: _extensions.AVT_Callable[..., _extensions.Any], i = 0, /): # 0.3.42
        
        _mangle = lambda x = "": "_{}".format(type(self).__name__) + x
        
        # Revamp 0.3.51. Sadly, inbuilt functions do not feature the __code__ attribute, what would be easier.
        _overloads_ = None
        
        if _check_if_callable(f) or isinstance(getattr(f, "__code__", None), _extensions.CodeType):
            
            # AttributeError is thrown when trying to access non-overloaded functions, or overloaded, but without the __module__ attribute
            try:
                _overloads_ = _extensions.get_overloads(f)
            except AttributeError:
                _overloads_ = None
            if not isinstance(i, int) or (_overloads_ is not None and _reckon(_overloads_) > 0 and i not in range(_reckon(_overloads_))):
                error = TypeError("expected an integer in second parameter. keep this parameter as-is, when function isn't overloaded." + \
                                "otherwise, ensure the parameter value is in range <0; overloads_length>. " + \
                                "this does not apply to inbuilt functions")
                raise error
            
            if _check_if_builtin(f) or not isinstance(getattr(f, "__code__", None), _extensions.CodeType):
                
                try:
                    object.__setattr__(self, _mangle("__builtin"), _BuiltinParamVar(f))
                    
                except TypeError:
                    error = TypeError("expected a callable object with a proper implementation. with type as value use '~.util.ParamVar.fromType()' static method")
                    raise error
                
            else:
                object.__setattr__(self, _mangle("__builtin"), None)
                
        else:
            error = TypeError("expected a callable object with a proper implementation")
            raise error
        
        object.__setattr__(self, _mangle("__vartype"), "")
        
        if isinstance(f, _extensions.partial):
            object.__setattr__(self, _mangle("__func"), f.func)
        elif _overloads_ is not None and _reckon(_overloads_) > 0:
            object.__setattr__(self, _mangle("__func"), _overloads_[i])
        else:
            object.__setattr__(self, _mangle("__func"), f)
        
        func = f.func if isinstance(f, _extensions.partial) else f
        
        # 0.3.51: Less complexity in this statement. __name__ != __qualname__ is required to deduce if a function belongs to a class as an instance method,
        # passed to the constructor via class reference. If __name__ equals __qualname__, then function doesn't belong to a class and is in globally scope.
        if (isinstance(func, _extensions.MethodType) and not isinstance(func, staticmethod)) or \
            isinstance(func, _extensions.MethodDescriptorType) or (
            isinstance(func, _extensions.FunctionType) and func.__name__ != func.__qualname__
            ):
            object.__setattr__(self, _mangle("__no_first"), 1)
        else:
            object.__setattr__(self, _mangle("__no_first"), 0)
        
    def __str__(self): # 0.3.42
        
        # 0.3.51
        if self.__builtin is not None:
            _annotated_ = ("?", "?")
        else:
            _annotated_ = (str(self.annotatedCount), str(self.annotatedDefaultsCount)) # >= 0.3.44
        
        return "{}(positional: {}, positionalDefaults: {}, universal: {}, universalDefaults: {}, keyword: {}, keywordDefaults: {}, annotated: {}, annotatedDefaults: {}, variable: {}, all: {}, allDefaults: {})".format(
            type(self).__name__,
            self.positionalCount,
            self.positionalDefaultsCount,
            self.universalCount,
            self.universalDefaultsCount,
            self.keywordCount,
            self.keywordDefaultsCount,
            _annotated_[0],
            _annotated_[1], 
            str(self.variableCount) + self.__vartype,
            self.allCount,
            self.allDefaultsCount
        )
        
    def __repr__(self): # 0.3.42
        
        return "<{}.{} object :: {} :: Inspected function -> {}>".format(self.__module__, type(self).__name__, self.__str__(), self.func.__qualname__)
    
    @staticmethod
    def fromType(t, i = 0, /):
        """
        Availability: >= 0.3.51
        
        Alternative constructor for `~.util.ParamVar`
        """
        
        if isinstance(t, _builtin_classes) or (type(t) is type and hasattr(t, "__new__")):
            return ParamVar(t.__new__, i)
        
        elif type(t) is type and hasattr(t, "__init__"):
            return ParamVar(t.__init__, i)
        
        else:
            error = TypeError("unable to retrieve a function from desired type")
            raise error
    
    @property
    def func(self): # 0.3.42
        """
        Availability: >= 0.3.42
        
        Represents the function passed to the constructor
        """
        
        return self.__func
    
    @func.setter
    def func(self, v): # 0.3.42
        
        type(self).__init__(self, v)
        
    @func.deleter
    def func(self): # 0.3.43
        
        error = TypeError("unable to delete property {}".format(self.func.__name__))
        raise error
    
    @property
    def builtin(self):
        """
        Availability: >= 0.3.52 \\
        https://aveyzan.xyz/aveytense#aveytense.util.ParamVar.builtin
        
        Returns `True` if function is inbuilt.
        """
        return self.__builtin is not None
    
    @property
    def signature(self): # 0.3.42
        """
        Availability: >= 0.3.42 \\
        https://aveyzan.xyz/aveytense#aveytense.util.ParamVar.signature
        
        Returns function's signature
        """
            
        # 0.3.51
        if self.__builtin is not None:
            return self.__builtin.signature
        
        _signature_ = "("
        
        # inverting keys and values pairs, because <args> and <kwargs> are normally values (not keys) in dictionary (in tuples: second item)
        # trick with indexes may be needed - whether ~.variable is empty, indexes aren't accessed
        _variable_ = {e[1]: e[0] for e in self.variable}
        
        # on terminals quotes are omitted, so we will be including them to indicate these values are strings
        # 0.3.45: + present ellipsis as '...'
        _quote_ = lambda x: "..." if x is ... else str(x) if type(x) is not str else "\"{}\"".format(x)
        
        # 0.3.47, 0.3.49
        # doing it with __future__.annotations and values of globals() is not preferred idea
        # better catch the error when subscripting
        _quoted_annotations_ = False
        
        if _sys.version_info < (3, 9):
            
            from collections.abc import Sequence
            
            try:
                _e_ = Sequence[str] # type: ignore
                _e_ = _e_
                
            except:
                _quoted_annotations_ = True
        
        # 0.3.47: Faster to do it than do the same with dict(~.annotations). 'True' and 'False' cannot be deduced in type annotation, they need use with
        # typing.Literal, hence ... if self...get(x, False)
        # 0.3.52: Un-stringify type annotations
        # 0.3.53: Check whether 'globals' in eval() can be passed as a keyword
        if not _quoted_annotations_:
            _receive_annotation_ = lambda x = "": ": " + str(_extensions.eval(self.func.__annotations__[x], globals = self.func.__globals__)) if self.func.__annotations_extensions.get(x, False) is not False else ""
        else:
            _receive_annotation_ = lambda x = "": ": \"{}\"".format(str(_extensions.eval(self.func.__annotations__[x], globals = self.func.__globals__))) if self.func.__annotations_extensions.get(x, False) is not False else ""
                
        # 0.3.48
        # Fixed annotations (these only applied to parameters with default value)
        
        # pep 570, Py>=3.8
        if self.positionalCount > 0:
            
            _positional_defaults = dict(self.positionalDefaults)
            _annotations_ = [e + _receive_annotation_(e) + (" = " + _quote_(_positional_defaults[e]) if e in _positional_defaults else "") for e in self.positional]
            
            _signature_ += ", ".join(_annotations_) + ", /, "
            
        if self.universalCount > 0:
            
            _universal_defaults = dict(self.universalDefaults)
            _annotations_ = [e + _receive_annotation_(e) + (" = " + _quote_(_universal_defaults[e]) if e in _universal_defaults else "") for e in self.universal]
            
            _signature_ += ", ".join(_annotations_) + ", "
            
        if "<args>" in _variable_:
            
            if not _signature_.endswith(", ") and self.positionalCount > 0: # >= 0.3.45
                _signature_ += ", "
            
            _signature_ += "*{}, ".format(_variable_["<args>"] + _receive_annotation_(_variable_["<args>"]))
        
        # pep 3102, Py>=3.0
        if self.keywordCount > 0:
            
            _keyword_defaults = dict(self.keywordDefaults)
            _annotations_ = [e + _receive_annotation_(e) + (" = " + _quote_(_keyword_defaults[e]) if e in _keyword_defaults else "") for e in self.keyword]
            
            if "<args>" not in _variable_:
                _signature_ += "*, "
                
            _signature_ += ", ".join(_annotations_)
            
        if "<kwargs>" in _variable_:
            
            if not _signature_.endswith(", ") and (any([e > 0 for e in (self.positionalCount, self.universalCount, self.keywordCount)]) or "<args>" in _variable_):
                _signature_ += ", "
            
            _signature_ += "**{}, ".format(_variable_["<kwargs>"] + _receive_annotation_(_variable_["<kwargs>"]))
        
        if _signature_.endswith(", "):
            _signature_ = _signature_[: _reckon(_signature_) - 2]
            
        _signature_ += ")"
        
        # 0.3.48
        # Return type annotation
        _return_ = dict(self.annotations).get("return", False)
        
        # if not that, 'None' would be excluded too
        if _return_ is not False:
            _signature_ += " -> {}".format(_return_)
            
        return _signature_
    
    @property
    def firstParam(self): # 0.3.61
        """
        Availability: >= 0.3.61
        
        If function is actually a non-static method, returns first parameter bound to either class instance or class itself (like `self` and `cls`).
        Returns `None` otherwise
        """
        
        if self.__no_first == 1:
            return self.func.__code__.co_varnames[0]
        
    @property
    def all(self): # 0.3.42
        """
        Availability: >= 0.3.42 \\
        https://aveyzan.xyz/aveytense#aveytense.util.ParamVar.all
        
        Returns a tuple with all arguments, positioned as they appear in the signature.
        Earlier, this property returned arguments in the following way: positional-only,
        universal, keyword-only, variable argument, variable keyword argument.
        
        Empty if the function doesn't have any parameters (first parameter in non-static
        method isn't counted). Examples::
        
            def f1(p1, p2, /, p3, p4 = 75, *, p5, p6, **p7): ...
            # ("p1", "p2", "p3", "p4", "p5", "p6", "p7")
            def f2(p1, p2, *p3, p4 = 75, p5, **p6): ...
            # ("p1", "p2", "p3", "p4", "p5", "p6")
        """
        
        # 0.3.51
        if self.__builtin is not None:
            return self.__builtin.all 
        
        c = self.func.__code__
        n = c.co_argcount + c.co_kwonlyargcount
        f = _CodeFlags()
        _if_varargs = c.co_flags & f.varargs
        _if_varkeywords = c.co_flags & f.varkeywords

        # Include variable arguments in correct places
        if _if_varargs and _if_varkeywords:
            _all_ = (*self.positional, *self.universal, _return_param(self.func, c.co_varnames[n]), *self.keyword, _return_param(self.func, c.co_varnames[n + 1]))
        elif _if_varargs:
            _all_ = self.positional + (*self.universal, _return_param(self.func, c.co_varnames[n])) + self.keyword
        elif _if_varkeywords:
            _all_ = self.positional + self.universal + (*self.keyword, _return_param(self.func, c.co_varnames[n]))
        else:
            _all_ = self.positional + self.universal + self.keyword
            
        return _all_
    
    @property
    def allDefaults(self): # 0.3.42
        """
        Availability: >= 0.3.42 \\
        https://aveyzan.xyz/aveytense#aveytense.util.ParamVar.allDefaults
        
        Returns a tuple holding tuples with pair of items with content, respectively:
        - all arguments
        - their default values
        
        Empty whether there are none. It does not apply to variable arguments. Examples::
        
            def f1(p1, p2, /, p3, p4 = 75, *, p5, p6, **p7): ...
            def f2(p1, p2, *p3, p4 = 75, p5, **p6): ...
            # (("p4", "75"),) (both)
        
        Convertible to `dict`
        """
        
        # 0.3.51
        if self.__builtin is not None:
            return self.__builtin.allDefaults
        
        return self.positionalDefaults + self.universalDefaults + self.keywordDefaults
    
    @property
    def allWithDefaults(self): # 0.3.51
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.util.ParamVar.allWithDefaults
        
        Returns a tuple holding tuples with pair of items with content, respectively:
        - all arguments
        - their default values (internal class if default value in some is not present)
        
        Empty whether there are none. It does apply to variable arguments. Examples::
        
            def f1(p1, p2, /, p3, p4 = 75, *, p5, p6): ...
            def f2(p1, p2, *p3, p4 = 75, p5, **p6): ...
            # (("p1", <paramNoDefault>), ("p2", <paramNoDefault>),
            # ("p3", <paramNoDefault>), ("p4", 75), ("p5", <paramNoDefault>),
            # ("p6", <paramNoDefault>)) (both)
        
        Convertible to `dict`
        """
        
        return tuple([(p, ParamNoDefault if p not in dict(self.allDefaults) else dict(self.allDefaults)[p]) for p in self.all])
        
    
    @property
    def allNoDefaults(self): # 0.3.44
        """
        Availability: >= 0.3.44 \\
        https://aveyzan.xyz/aveytense#aveytense.util.ParamVar.allNoDefaults
        
        Returns a tuple holding all kind of parameters whose don't have a default value.
        Empty whether there are none. Examples::
        
            def f1(p1, p2, /, p3, p4 = 75, *, p5, p6, **p7): ...
            # ("p1", "p2", "p3", "p5", "p6", "p7")
            def f2(p1, p2, *p3, p4 = 75, p5, **p6): ...
            # ("p1", "p2", "p3", "p5", "p6")
        """
        
        return tuple([e for e in self.all if e not in dict(self.allDefaults)])
    
    @property
    def positional(self): # 0.3.42
        """
        Availability: >= 0.3.42 \\
        https://aveyzan.xyz/aveytense#aveytense.util.ParamVar.positional
        
        Returns a tuple holding all positional-only arguments. Empty whether there are none. Examples::
        
            def f1(p1, p2, p3, p4 = 54, p5 = "", /): ...
            # ("p1", "p2", "p3", "p4", "p5")
            def f2(__p1, __p2, __p3, __p4 = 54, __p5 = ""): ... # pre-PEP 570
            # ("__p1", "__p2", "__p3", "__p4", "__p5")
            def f3(__p1, __p2, __p3, __p4 = 54, /, __p5 = ""): ... # mixed
            # ("__p1", "__p2", "__p3", "__p4")
            
        See PEP 570 for positional-only operator `/`. Variable parameter (`*<param>`) isn't counted.
        """
        
        # 0.3.51
        if self.__builtin is not None:
            return self.__builtin.positional
        
        c = self.func.__code__
        
        # Code revamp 0.3.47
        if c.co_posonlyargcount > 0:
            # Before 0.3.47, this was only returned, and no doubly underscored arguments
            # as the only way to create positional arguments before PEP 570 were included.
            return tuple([_return_param(self.func, e) for e in c.co_varnames[self.__no_first : c.co_posonlyargcount]])
        
        _tuple_ = c.co_varnames[: c.co_argcount]
        
        if _reckon(_tuple_) == 0:
            a = [""]
            a.clear()
            return tuple(a)
        
        # Parameters in a method have following syntax, as in private methods: _<class-name>__<param-name>.
        # Functions do not use this naming syntax
        if isinstance(self.func, _extensions.MethodType):
            _tuple_ = _tuple_[self.__no_first :]
            _gen_ = (e for e in _tuple_)
            _list_ = [""]
            _list_.clear()
            e = "__a_" # loop statement satisfaction; changed after first iteration
            
            while e.startswith("__") and not e.endswith("__"):
                e = next(_gen_, "")
                
                if e == "":
                    break
                
                _list_.append(_return_param(self.func, e))
                
            return tuple(_list_)
        
        _tuple_end_marker_ = 0
        
        # If argument is completely encased by 2 (or more) underscores at the beginning and ending, then
        # it ISN'T considered positional! Also, we are catching IndexError, as it may occur.
        # Examples for non-positional-only parameters: _1, _1_, _1__, __1__, __1___, ___1__, etc. 
        try:
            while _tuple_[_tuple_end_marker_].startswith("__") and not _tuple_[_tuple_end_marker_].endswith("__"):
                _tuple_end_marker_ += 1
                
        except IndexError:
            pass
            
        return _tuple_[: _tuple_end_marker_]
    
    @property
    def positionalDefaults(self): # 0.3.42
        """
        Availability: >= 0.3.42 \\
        https://aveyzan.xyz/aveytense#aveytense.util.ParamVar.positionalDefaults
        
        Returns a tuple holding tuples with pair of items with content, respectively:
        - positional-only arguments
        - their default values
        
        Empty whether there are none. Examples::
        
            def f1(p1, p2, p3, p4 = 54, p5 = "", /): ...
            # (("p4", 65), ("p5", ""))
            def f2(__p1, __p2, __p3, __p4 = 54, __p5 = ""): ... # pre-PEP 570
            # (("__p4", 65), ("__p5", ""))
            def f3(__p1, __p2, __p3, __p4 = 54, /, __p5 = ""): ... # mixed
            # (("__p4", 54),)
            
        Convertible to `dict`
        """
        
        # 0.3.51
        if self.__builtin is not None:
            return self.__builtin.positionalDefaults
        
        # Code revamp 0.3.47
        if self.positionalCount > 0 and self.func.__defaults__ is not None:
            
            _defaults_ = self.func.__defaults__[::-1][self.universalCount:]
            _positional_ = self.positional[::-1]
            
            return tuple([(_positional_[i], _defaults_[i]) for i in range(min(_reckon(_positional_), _reckon(_defaults_)))])[::-1]
                
        a = [("", _AnyObjectHinter)]
        a.clear()
        return tuple(a)
    
    @property
    def positionalWithDefaults(self): # 0.3.51
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.util.ParamVar.positionalWithDefaults
        
        Returns a tuple holding tuples with pair of items with content, respectively:
        - positional-only arguments
        - their default values (internal class if default value in some is not present)
        
        Empty whether there are none. Examples::
        
            def f1(p1, p2, p3, p4 = 54, p5 = "", /): ...
            # (("p1", <paramNoDefault>), ("p2", <paramNoDefault>),
            # ("p3", <paramNoDefault>), ("p4", 65), ("p5", ""))
            def f2(__p1, __p2, __p3, __p4 = 54, __p5 = ""): ... # pre-PEP 570
            # (("__p1", <paramNoDefault>), ("__p2", <paramNoDefault>),
            # ("__p3", <paramNoDefault>), ("__p4", 54), ("__p5", ""))
            def f3(__p1, __p2, __p3, __p4 = 54, /, __p5 = ""): ... # mixed
            # (("__p1", <paramNoDefault>), ("__p2", <paramNoDefault>),
            # ("__p3", <paramNoDefault>), ("__p4", 54)
            
        Convertible to `dict`
        """
        
        return tuple([(p, ParamNoDefault if p not in dict(self.positionalDefaults) else dict(self.positionalDefaults)[p]) for p in self.positional])
    
    @property
    def positionalNoDefaults(self): # 0.3.44
        """
        Availability: >= 0.3.44 \\
        https://aveyzan.xyz/aveytense#aveytense.util.ParamVar.positionalNoDefaults
        
        Returns a tuple holding all positional-only arguments whose don't have a default value. \\
        Empty whether there are none. Examples::
        
            def f1(p1, p2, p3, p4 = 54, p5 = "", /): ...
            # ("p1", "p2", "p3")
            def f2(__p1, __p2, __p3, __p4 = 54, __p5 = ""): ... # pre-PEP 570
            # ("__p1", "__p2", "__p3")
            def f3(__p1, __p2, __p3, __p4 = 54, /, __p5 = ""): ... # mixed
            # ("__p1", "__p2", "__p3")
        """
        
        return tuple([e for e in self.positional if e not in dict(self.positionalDefaults)]) 
    
    @property
    def keyword(self): # 0.3.42
        """
        Availability: >= 0.3.42 \\
        https://aveyzan.xyz/aveytense#aveytense.util.ParamVar.keyword
        
        Returns a tuple holding all keyword-only arguments.
        Empty whether there are none. Example::
        
            def f(p1, *, p2 = 66, p3 = "", p4, **p5): ...
            # ("p2", "p3", "p4")
        
        See PEP 3102 for keyword-only operator `*`. Variable
        keyword parameter (`**<param>`) isn't counted.
        """
        
        # 0.3.51
        if self.__builtin is not None:
            return self.__builtin.keyword
        
        c = self.func.__code__
        return tuple([_return_param(self.func, e) for e in c.co_varnames[c.co_argcount : c.co_argcount + c.co_kwonlyargcount]])
    
    @property
    def keywordDefaults(self): # 0.3.42
        """
        Availability: >= 0.3.42 \\
        https://aveyzan.xyz/aveytense#aveytense.util.ParamVar.keywordDefaults
        
        Returns tuple holding tuples with pair of items with content, respectively:
        - keyword-only arguments
        - their default values
        
        Empty if there are none. Example::
        
            def f(p1, *, p2 = 66, p3 = "", p4, **p5): ...
            # (("p2", 72), ("p3", ""))
            
        Convertible to `dict`
        """
        
        # 0.3.51
        if self.__builtin is not None:
            return self.__builtin.keywordDefaults
        
        if self.func.__kwdefaults__ is None:
            
            a = [("", _AnyObjectHinter)]
            a.clear()
            return tuple(a)
    
        return tuple([(_return_param(self.func, k), self.func.__kwdefaults__[k]) for k in self.func.__kwdefaults__])
    
    @property
    def keywordWithDefaults(self): # 0.3.51
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.util.ParamVar.keywordWithDefaults
        
        Returns tuple holding tuples with pair of items with content, respectively:
        - keyword-only arguments
        - their default values (internal class if default value in some is not present)
        
        Empty if there are none. Example::
        
            def f(p1, *, p2 = 66, p3 = "", p4, **p5): ...
            # >= 0.3.52: (("p2", 72), ("p3", ""), ("p4", <paramNoDefault>))
            # <  0.3.52: None
            
        Convertible to `dict`
        """
        return tuple([(p, ParamNoDefault if p not in dict(self.keywordDefaults) else dict(self.keywordDefaults)[p]) for p in self.keyword]) # >= 0.3.52: missing return statement
        
    
    @property
    def keywordNoDefaults(self): # 0.3.44
        """
        Availability: >= 0.3.44 \\
        https://aveyzan.xyz/aveytense#aveytense.util.ParamVar.keywordNoDefaults
        
        Returns tuple holding all keyword arguments whose don't have a default value.
        Empty if there are none. Example::
        
            def f(p1, *, p2 = 72, p3 = "", p4, **p5): ...
            # ("p4",)
        """
        return tuple([e for e in self.keyword if e not in dict(self.keywordDefaults)])
    
    @property
    def universal(self): # 0.3.42
        """
        Availability: >= 0.3.42 \\
        https://aveyzan.xyz/aveytense#aveytense.util.ParamVar.universal
        
        Returns tuple holding all universal arguments. *Universal* arguments are
        arguments that can have their values assigned either by position or their
        names (keywords).
        
        Empty if there are none. Examples::
        
            def f1(p1, /, p2, p3, p4 = 96, p5 = True, *, p6 = 12): ...
            # ("p2", "p3", "p4", "p5")
            def f2(__p1, /, __p2, __p3, __p4 = 65, __p5 = "", *, __p6 = 12): ...
            # ("__p2", "__p3", "__p4", "__p5")
        """
        
        # 0.3.51
        if self.__builtin is not None:
            return self.__builtin.universal
        
        c = self.func.__code__
        
        # Code revamp 0.3.47; see self.positional
        if isinstance(self.func, _extensions.MethodType):
            _tuple_ = c.co_varnames[self.__no_first : c.co_argcount]
            return tuple([_return_param(self.func, e) for e in _tuple_ if _return_param(self.func, e) not in self.positional])
            
        else:
            
            # Prevent negative integer slice arguments
            _left = self.__no_first if c.co_posonlyargcount - self.__no_first <= 0 else c.co_posonlyargcount - self.__no_first
            return tuple([e for e in c.co_varnames[_left : c.co_argcount] if e not in self.positional])
    
    @property
    def universalDefaults(self): # 0.3.42
        """
        Availability: >= 0.3.42 \\
        https://aveyzan.xyz/aveytense#aveytense.util.ParamVar.universalDefaults
        
        Returns tuple holding tuples with pair of items with content, respectively:
        - universal arguments
        - their default values
        
        Empty if there are none. Examples::
        
            def f1(p1, /, p2, p3, p4 = 96, p5 = True, *, p6 = 12): ...
            # (("p4", 96), ("p5", True))
            def f2(__p1, /, __p2, __p3, __p4 = 65, __p5 = "", *, __p6 = 12): ...
            # (("__p4", 96), ("__p5", True))
        
        Convertible to `dict`
        """
        
        # 0.3.51
        if self.__builtin is not None:
            return self.__builtin.universalDefaults
        
        # Code revamp 0.3.47
        if self.positionalCount > 0 and self.func.__defaults__ is not None:
            
            _defaults_ = self.func.__defaults__[self.positionalDefaultsCount:][::-1]
            _universal_ = self.universal[::-1]
            
            return tuple([(_universal_[i], _defaults_[i]) for i in range(min(_reckon(_universal_), _reckon(_defaults_))) if (_universal_[i], _defaults_[i]) not in self.positionalDefaults])[::-1]
        
        a = [("", _AnyObjectHinter)]
        a.clear()
        return tuple(a)
    
    @property
    def universalWithDefaults(self): # 0.3.51
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.util.ParamVar.universalWithDefaults
        
        Returns tuple holding tuples with pair of items with content, respectively:
        - universal arguments
        - their default values (internal class if default value in some is not present)
        
        Empty if there are none. Examples::
        
            def f1(p1, /, p2, p3, p4 = 96, p5 = True, *, p6 = 12): ...
            # (("p2", <paramNoDefault>), ("p3", <paramNoDefault>),
            # ("p4", 96), ("p5", True))
            def f2(__p1, /, __p2, __p3, __p4 = 65, __p5 = "", *, __p6 = 12): ...
            # (("__p2", <paramNoDefault>), ("__p3", <paramNoDefault>),
            # ("__p4", 96), ("__p5", True))
        
        Convertible to `dict`
        """
        
        return tuple([(p, ParamNoDefault if p not in dict(self.universalDefaults) else dict(self.universalDefaults)[p]) for p in self.universal])
                
    @property
    def universalNoDefaults(self): # 0.3.44
        """
        Availability: >= 0.3.44 \\
        https://aveyzan.xyz/aveytense#aveytense.util.ParamVar.universalNoDefaults
        
        Returns tuple holding all universal arguments whose don't have a default value.
        Empty if there are none. Examples::
        
            def f1(p1, /, p2, p3, p4 = 96, p5 = True, *, p6 = 12): ...
            # ("p2", "p3")
            def f2(__p1, /, __p2, __p3, __p4 = 65, __p5 = "", *, __p6 = 12): ...
            # ("__p2", "__p3")
        """
        return tuple([e for e in self.universal if e not in dict(self.universalDefaults)])
    
    @property
    def annotated(self): # 0.3.42
        """
        Availability: >= 0.3.42 \\
        https://aveyzan.xyz/aveytense#aveytense.util.ParamVar.annotated
        
        Returns tuple holding names of arguments whose have been annotated a type. Such
        parameter can be type annotated since Python 3.5. Example::
        
            def f(p1: bool, p2: int = 90, p3: str = "f", p4 = False): ...
            # ("p1", "p2", "p3")
        
        See PEP 484 for type annotations. Note variable argument and variable keyword
        argument are counted too.
        """
        
        # 0.3.51
        if self.__builtin is not None:
            a = [""]
            a.clear()
            return tuple(a)
        
        return tuple([_return_param(self.func, k) for k in self.all if k in self.func.__annotations__ and k != "return"])
    
    @property
    def annotatedDefaults(self): # 0.3.44
        """
        Availability: >= 0.3.44 \\
        https://aveyzan.xyz/aveytense#aveytense.util.ParamVar.annotatedDefaults
        
        Returns tuple holding tuples with pair of items with content, respectively:
        - type-annotated arguments
        - their annotated type and default values (respectively in a 2-item tuple since 0.3.47)
        
        Empty if there are none. Example::
        
            def f(p1: bool, p2: int = 90, p3: str = "f", p4 = False): ...
            # >= 0.3.52:           (("p2", (int, 90)), ("p3", (str, "f")))
            # >= 0.3.47; < 0.3.52: (("p2", ("int", 90)), ("p3", ("str", "f")))
            # <  0.3.47:           (("p2", 90), ("p3", "f"))
        
        Convertible to `dict`
        """
            
        _list_ = [("", (_AnyObjectHinter, _AnyObjectHinter))]
        _list_.clear()
        
        # 0.3.51
        if self.__builtin is not None:
            return tuple(_list_)
        
        _defaults_ = dict(self.allDefaults)
        
        for e in self.annotated:
            if e in _defaults_:
                _list_.append((e, (_extensions.eval(self.func.__annotations__[e], globals = self.func.__globals__), _defaults_[e])))
                
        return tuple(_list_)
        
    @property
    def annotatedWithDefaults(self): # 0.3.51
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.util.ParamVar.annotatedWithDefaults
        
        Returns tuple holding tuples with pair of items with content, respectively:
        - type-annotated arguments
        - their annotated type and default values (respectively in a 2-item tuple)
            or internal class if default value in some is not present
        
        Empty if there are none. Example::
        
            def f(p1: bool, p2: int = 90, p3: str = "f", p4 = False): ...
            # (("p1", <paramNoDefault>), ("p2", ("int", 90)), ("p3", ("str", "f")))
        
        Convertible to `dict`
        """
        
        return tuple([(p, ParamNoDefault if p not in dict(self.annotatedDefaults) else dict(self.annotatedDefaults)[p]) for p in self.annotated])
    
    @property
    def annotatedNoDefaults(self): # 0.3.44
        """
        Availability: >= 0.3.44 \\
        https://aveyzan.xyz/aveytense#aveytense.util.ParamVar.annotatedNoDefaults
        
        Returns tuple holding names of arguments whose have been annotated a type,
        but do not have a default value. Empty if there are none. Example::
        
            def f(p1: bool, p2: int = 90, p3: str = "f", p4 = False): ...
            # ("p1",)
        """
        
        # 0.3.51
        if self.__builtin is not None:
            return self.annotated
        
        _defaults_ = dict(self.annotatedDefaults)
        return tuple([e for e in self.annotated if e not in _defaults_])
    
    @property
    def annotations(self): # 0.3.42
        """
        Availability: >= 0.3.42 \\
        https://aveyzan.xyz/aveytense#aveytense.util.ParamVar.annotations
        
        Same as invocation `self.func.__annotations__`, just sorted as parameters appear in the signature,
        and with `return` annotation returned (changeover 0.3.47). Convertible to `dict`
        
        Since 0.3.52 annotations no longer are returned as strings.
        """
        
        # Code revamp 0.3.47
        _list_: _extensions.AVT_List[_extensions.AVT_Tuple[str, _extensions.AnnotationForm]] = []
        
        # 0.3.51
        if self.__builtin is not None:
            return tuple(_list_)
        
        _annotated_ = (*self.all, "return")
        
        for e in _annotated_:
            if e in self.func.__annotations__:
                _list_.append((_return_param(self.func, e), _extensions.eval(self.func.__annotations__[e], globals = self.func.__globals__)))
                
        return tuple(_list_)
        
    @property
    def variable(self): # 0.3.42 
        """
        Availability: >= 0.3.42 \\
        https://aveyzan.xyz/aveytense#aveytense.util.ParamVar.variable
        
        Returns tuple holding variable argument and variable keyword argument - both in separate
        internal 2-item tuples (second item being one of keywords: `"<args>"` and `"<kwargs>"`).
        Empty if there are none. Examples::
        
            def f1(*args, **kwds): ...
            # (("args", "<args>"), ("kwds", "<kwargs>"))
            def f2(*args): ...
            # (("args", "<args>"))
            def f3(**kwds): ...
            # (("kwds", "<kwargs>"))
        
        Convertible to `dict`. Sometimes preferred to use dictionary comprehension in the following
        way: `{e[1]: e[0] for e in self.variable}`, to refer by keyword `"<args>"`
        or `"<kwargs>"`. The same can be done with `~.Tense.invert()` class method (>= 0.3.46).
        """
        
        # 0.3.51
        if self.__builtin is not None:
            return self.__builtin.variable
        
        c = self.func.__code__
        f = _CodeFlags()
        
        _filter_ = tuple([e for e in self.all if e not in (self.positional + self.universal + self.keyword)]) # 0.3.46
        
        if c.co_flags & f.varargs and c.co_flags & f.varkeywords:
            
            self.__vartype = " <args, kwargs>"
            # < 0.3.45: self.allCount, self.allCount + 1
            # < 0.3.46: self.allCount - 2, self.allCount - 1
            # >= 0.3.46
            return _extensions.cast(_extensions.AVT_Tuple[_extensions.AVT_Tuple[str, str], ...], ((_filter_[0], "<args>"), (_filter_[1], "<kwargs>")))
        
        else:
            
            if c.co_flags & f.varargs:
                self.__vartype = " <args>"
                
            elif c.co_flags & f.varkeywords:
                self.__vartype = " <kwargs>"
                
            else:
                return _extensions.cast(_extensions.AVT_Tuple[_extensions.AVT_Tuple[str, str], ...], ())
            
            # < 0.3.45: self.allCount
            # >= 0.3.46
            return _extensions.cast(_extensions.AVT_Tuple[_extensions.AVT_Tuple[str, str], ...], (_filter_[0], self.__vartype.lstrip()))
        
    @property
    def positionalCount(self): # 0.3.44
        """
        Availability: >= 0.3.44
        
        Returns count of all positional-only parameters"""
        
        return _reckon(self.positional)
    
    @property
    def positionalDefaultsCount(self): # 0.3.44
        """
        Availability: >= 0.3.44
        
        Returns count of all positional-only parameters with default values"""
        
        return _reckon(self.positionalDefaults)
    
    @property
    def positionalNoDefaultsCount(self): # 0.3.44
        """
        Availability: >= 0.3.44
        
        Returns count of all positional-only parameters without default values"""
        
        return _reckon(self.positionalNoDefaults)
    
    @property
    def universalCount(self): # 0.3.44
        """
        Availability: >= 0.3.44
        
        Returns count of all universal parameters"""
        
        return _reckon(self.universal)
    
    @property
    def universalDefaultsCount(self): # 0.3.44
        """
        Availability: >= 0.3.44
        
        Returns count of all universal parameters with default values"""
        
        return _reckon(self.universalDefaults)
    
    @property
    def universalNoDefaultsCount(self): # 0.3.44
        """
        Availability: >= 0.3.44
        
        Returns count of all universal parameters without default values"""
        
        return _reckon(self.universalNoDefaults)
    
    @property
    def keywordCount(self): # 0.3.44
        """
        Availability: >= 0.3.44
        
        Returns count of all keyword-only parameters"""
        
        return _reckon(self.keyword)
    
    @property
    def keywordDefaultsCount(self): # 0.3.44
        """
        Availability: >= 0.3.44
        
        Returns count of all keyword-only parameters with default values"""
        
        return _reckon(self.keywordDefaults)
    
    @property
    def keywordNoDefaultsCount(self): # 0.3.44
        """
        Availability: >= 0.3.44
        
        Returns count of all keyword parameters without default values"""
        
        return _reckon(self.keywordNoDefaults)
    
    @property
    def allCount(self): # 0.3.44
        """
        Availability: >= 0.3.44
        
        Returns count of all parameters"""
        
        return _reckon(self.all)
    
    @property
    def allDefaultsCount(self): # 0.3.44
        """
        Availability: >= 0.3.44
        
        Returns count of all parameters with default values"""
        
        return _reckon(self.allDefaults)
    
    @property
    def allNoDefaultsCount(self): # 0.3.44
        """
        Availability: >= 0.3.44
        
        Returns count of all parameters without default value"""
        
        return _reckon(self.allNoDefaults)
    
    @property
    def annotatedCount(self): # 0.3.44
        """
        Availability: >= 0.3.44
        
        Returns count of all parameters which have been annotated a type"""
        
        return _reckon(self.annotated)
    
    @property
    def annotatedDefaultsCount(self): # 0.3.44
        """
        Availability: >= 0.3.44
        
        Returns count of all parameters which have been annotated a type, and a default value"""
        
        return _reckon(self.annotatedDefaults)
    
    @property
    def annotatedNoDefaultsCount(self): # 0.3.44
        """
        Availability: >= 0.3.44
        
        Returns count of all parameters which have been annotated a type, however, don't have default value"""
        
        return _reckon(self.annotatedNoDefaults)
    
    @property
    def variableCount(self): # 0.3.44
        """
        Availability: >= 0.3.44
        
        Returns count of all variable parameters (0-2)"""
        
        return _reckon(self.variable)
    
    __all__ = sorted([k for k in locals() if not k.startswith("_")])
    """Availability: >= 0.3.51"""
        
class MutableString:
    """
    Availability: >= 0.3.42 \\
    https://aveyzan.xyz/aveytense#aveytense.util.MutableString
    
    Represents a string, which can be mutated.
    """
    
    ### Initializer ###
    def __init__(self, string, /): # 0.3.42
        
        # 0.3.45: allow instances of the class to be used in the constructor
        if not isinstance(string, (str, type(self))):
            error = TypeError("expected a string or instance of the same class")
            raise error
        
        if isinstance(string, str):
            self.__str = list(string)
            
        else:
            self.__str = list(str(string))
    
    ### Conversions ###
    def __str__(self): # 0.3.42
        
        if not all([isinstance(e, str) for e in self.__str]):
            error = TypeError("internal variable isn't a string")
            raise error
        
        else:
            return "".join(self.__str)
    
    def __repr__(self): # 0.3.42
        
        return "<{}.{} object :: {}(\"{}\")> ".format(self.__module__, type(self).__name__, type(self).__name__, self.__str__())
    
    def __hash__(self): # 0.3.42
        
        return hash(str(self))
    
    def __format__(self, format_spec): # 0.3.42
        
        if type(format_spec) is not str:
            error = TypeError("expected a string")
            raise error
        
        return format_spec.format(str(self))  
    
    ### Length ###
    def __len__(self): # 0.3.42
        
        return _reckon(self.__str__())
    
    def __reckon__(self): # 0.3.42
        
        return _reckon(self.__str__())
    
    ### Indexes ###
    @_extensions.overload
    def __getitem__(self, value: _extensions.Union[int, slice]) -> str: ...
    
    @_extensions.overload
    def __getitem__(self, value: str) -> int: ...
    
    def __getitem__(self, value): # 0.3.42
        
        if type(value) is int or type(value) is slice:
            
            if type(value) is int and -(_reckon(self.__str) + 1) >= value >= _reckon(self.__str):
                error = IndexError("index out of range")
                raise error
            
            return str(self)[value]
        
        elif type(value) is str:
            
            return str(self).count(value)
        
        else:
            error = TypeError("expected a slice, substring or integer")
            raise error
        
    def __setitem__(self, name, value):
        
        if type(name) is int or type(name) is slice:
                
            if type(name) is int and -(_reckon(self.__str) + 1) >= name >= _reckon(self.__str):
                error = IndexError("index out of range")
                raise error
            
            self.__str[name] = value
            
        elif type(name) is str:
            
            if type(value) is str:
                self.__str = list(self.__str__().replace(name, value))
                
            else:
                error = TypeError("expected string for string indexes")
                raise error
            
        else:
            error = TypeError("expected a slice, substring or integer")
            raise error
        
    def __delitem__(self, name): # 0.3.42
        
        if type(name) is not int and type(name) is not slice:
            error = TypeError("expected a slice or integer")
            raise error
        
        if type(name) is int and -(_reckon(self.__str) + 1) >= name >= _reckon(self.__str):
            error = IndexError("index out of range")
            raise error
        
        del self.__str[name]
        
    ### Other ###
        
    def __add__(self, other): # 0.3.42
        
        if type(other) is type(self):
            
            return type(self)(str(self) + str(other))
        
        elif type(other) is str:
            
            return type(self)(str(self) + other)
        
        else:
            
            error = TypeError("operation with unsupported type of right operand: '{}'".format(type(other).__name__))
            raise error
        
    def __radd__(self, other): # 0.3.42
        
        try:
            
            return self.__add__(other)
        
        except TypeError:
            
            error = TypeError("operation with unsupported type of left operand: '{}'".format(type(other).__name__))
            raise error
        
    def __iadd__(self, other): # 0.3.42
        
        if type(other) is type(self):
            
            self.__str += list(str(other))
        
        elif type(other) is str:
            
            self.__str += list(other)
        
        else:
            
            error = TypeError("operation with unsupported type of right operand: '{}'".format(type(other).__name__))
            raise error
        
        return self
        
    def __mul__(self, other): # 0.3.42
        
        if type(other) is int:
            
            if other > 0:
                return type(self)(str(self) * other)
            
            elif other == 0: # >= 0.3.43
                return type(self)("")
            
            else:
                error = IndexError("expected an integer above zero")
                raise error
            
        else:
            error = TypeError("expected an integer")
            raise error
        
    def __rmul__(self, other): # 0.3.42
        
        try:
            
            return self.__mul__(other)
        
        except TypeError:
            
            error = TypeError("operation with unsupported type of left operand: '{}'".format(type(other).__name__))
            raise error
        
    def __imul__(self, other): # 0.3.42
        
        if type(other) is int:
            
            if other > 0:
                s = str(self)
                self.__str = list(s * other)
            
            else:
                error = IndexError("expected an integer above zero")
                raise error
            
        else:
            error = TypeError("expected an integer")
            raise error
        
        return self
    
    def __mod__(self, other): # 0.3.42
        
        return str(self.__str__() % other)
    
    def __getnewargs__(self): # 0.3.42
        
        return self.__str__().__getnewargs__()
      
    ### Checking ###
    def __contains__(self, key): # 0.3.42
        
        return key in self.__str__() if type(key) is str else str(key) in self.__str__() if type(key) is type(self) else False
    
    def __lt__(self, other): # 0.3.42
        
        return self.__str__() < other if type(other) is str else self.__str__() < str(other) if type(other) is type(self) else False
    
    def __gt__(self, other): # 0.3.42
        
        return self.__str__() > other if type(other) is str else self.__str__() > str(other) if type(other) is type(self) else False
    
    def __le__(self, other): # 0.3.42
        
        return self.__str__() <= other if type(other) is str else self.__str__() <= str(other) if type(other) is type(self) else False
    
    def __ge__(self, other): # 0.3.42
        
        return self.__str__() >= other if type(other) is str else self.__str__() >= str(other) if type(other) is type(self) else False
    
    def __eq__(self, other): # 0.3.42
        
        return self.__str__() == other if type(other) is str else self.__str__() == str(other) if type(other) is type(self) else False
    
    def __ne__(self, other): # 0.3.42
        
        return self.__str__() != other if type(other) is str else self.__str__() != str(other) if type(other) is type(self) else False
    
    ### Other ###
    def clear(self): # 0.3.42
        """Clear the mutable string."""
        
        a = [""]
        del a[0]
        self.__str = a
        
    def join(self, i: _extensions.AVT_Iterable[_extensions.Any], /, useRepr = False): # 0.3.45
        """
        Extension of `str.join()`, which accepts every iterable's type (unlike for mentioned method it is string iterable only), \\
        with setting `useRepr` that allows to use `repr()` instead of `str()` when set to `True`.
        """
        
        if not isinstance(i, _extensions.Iterable):
            error = TypeError("expected an iterable")
            raise error
        
        if _reckon(i) == 0:
            return "".join(self.__str)
        
        try:
            [str(e) for e in i]
            
        except:
            
            try:
                [repr(e) for e in i]
                
            except:
                
                error = TypeError("couldn't convert all items to strings")
                raise error
        
        _invoke = lambda x: str(x) if not useRepr else repr(x)
        
        return "".join(self.__str).join([_invoke(e) for e in i])
    
    def reverse(self): # 0.3.45
        """
        Reverse the mutable string.
        """
        self.__str = self.__str[::-1]
        
    @property
    def value(self): # 0.3.42
        return self.__str__()
    
    @value.setter
    def value(self, value): # 0.3.42
        
        if type(value) is type(self):
            self.__str = list(str(value))
            
        elif type(value) is str:
            self.__str = list(value)
            
        else:
            error = TypeError("expected a string or instance of '{}.MutableString'".format(self.__module__))
            raise error
        
    @value.deleter
    def value(self):
        
        error = TypeError("unable to delete property '" + type(self).value.fget.__name__ + "'")
        raise error
    
        
def simpleEnum(etype: type[_T_enum] = _extensions.Enum, boundary: _extensions.Optional[_extensions.FlagBoundary] = None, useArgs = False):
    """
    Availability: >= 0.3.42
    
    Globally scoped version of `enum._simple_enum()`
    """
    
    import enum
    return _extensions.cast(_extensions.AVT_Callable[[type[_extensions.Any]], type[_T_enum]], enum._simple_enum(etype, boundary = boundary, use_args = useArgs))
            

def uniquelist(iterable: _extensions.AVT_Iterable[_T] = ..., /):
    """
    Availability: >= 0.3.48 \\
    https://aveyzan.xyz/aveytense#aveytense.util.uniquelist
    
    Returns version of an iterable object without duplicate items and changing order, as a list object
    """
        
    if iterable is Ellipsis:
        return _extensions.cast(_extensions.AVT_List[_T], [])
    
    if not isinstance(iterable, _extensions.Iterable):
        error = TypeError("expected an iterable object")
        raise error
    
    _list_ = list(iterable)
    _new_list_: _extensions.AVT_List[_T] = []
    
    for e in _list_:
        
        if e not in _new_list_:
            _new_list_.append(e)
            
    return _new_list_
    
def uniquetuple(iterable: _extensions.AVT_Iterable[_T_cov] = ..., /):
    """
    Availability: >= 0.3.48 \\
    https://aveyzan.xyz/aveytense#aveytense.util.uniquetuple
    
    Returns version of an iterable object without duplicate items and changing order, as a tuple object
    
    Alias to `tuple(~.uniquelist(i))`
    """
        
    return tuple(uniquelist(iterable))

def uniquedict(mapping: _extensions.AVT_Mapping[_KT, _VT] = ..., /):
    """
    Availability: >= 0.3.74 \\
    https://aveyzan.xyz/aveytense#aveytense.util.uniquedict
    
    Returns version of a mapping object without duplicate values and changing order, as a dict object
    """
    
    if mapping is Ellipsis:
        return _extensions.cast(_extensions.AVT_Dict[_KT, _VT], {})
    
    if not isinstance(mapping, _extensions.Mapping):
        error = TypeError("expected a mapping object")
        raise error
    
    _items_ = list(mapping.items())
    _new_dict_: _extensions.AVT_Dict[_KT, _VT] = {}
    
    for e in _items_:
        
        if e[1] not in _new_dict_.values():
            _new_dict_.update([e])
    
    return _new_dict_

def uniquestr(string: str, /):
    """
    Availability: >= 0.3.74 \\
    https://aveyzan.xyz/aveytense#aveytense.util.uniquestr
    
    Returns version of a string without duplicate characters and changing order as another string.
    
    NOTE: this is not the same as `"".join(set(string))`
    """
    
    if not isinstance(string, str):
        error = TypeError("expected a string")
        raise error
    
    return "".join(uniquelist(string))

def indexeddict(i: _extensions.Iterable[_T], /, negative = False):
    """
    Availability: >= 0.3.74 \\
    https://aveyzan.xyz/aveytense#aveytense.util.indexeddict
    
    Returns a new dictionary object with every item indexes being keys, and every item from an iterable object being values
    """
    
    d: _extensions.AVT_Dict[int, _T] = {}
    l = len(list(i))
    
    for index, item in enumerate(i):
        
        if negative:
            d.update({-l + index: item})
        else:
            d.update({index: item})
        
    return d

@_extensions.overload
def flexiblelist(o: _extensions.Iterable[_T], /) -> _extensions.AVT_List[_T]: ...
@_extensions.overload
def flexiblelist(o: _T) -> _extensions.AVT_List[_T]: ...

def flexiblelist(o: object, /):
    """
    Availability: >= 0.3.75 \\
    https://aveyzan.xyz/aveytense#aveytense.util.flexiblelist
    
    Returns a new list object. Unlike for the `list` constructor, if the argument isn't an iterable object, then
    a new list object is returned with this argument as the first item, preventing any exceptions thrown.
    """
    
    if not isinstance(o, _extensions.Iterable):
        return [o]
    else:
        return list(o)
    
@_extensions.overload
def flexibletuple(o: _extensions.Iterable[_T], /) -> _extensions.AVT_Tuple[_T, ...]: ...
@_extensions.overload # that's actually tuple[_T] not tuple[_T, ...]
def flexibletuple(o: _T) -> _extensions.AVT_Tuple[_T, ...]: ... 

def flexibletuple(o: object, /):
    """
    Availability: >= 0.3.75 \\
    https://aveyzan.xyz/aveytense#aveytense.util.flexibletuple
    
    Returns a new tuple object. Unlike for the `tuple` constructor, if the argument isn't an iterable object, then
    a new tuple object is returned with this argument as the first item, preventing any exceptions thrown.
    """
    
    if not isinstance(o, _extensions.Iterable):
        return (o,)
    else:
        return tuple(o)
    
@_extensions.overload
def flexibleset(o: _extensions.Iterable[_T], /) -> _extensions.AVT_Set[_T]: ...
@_extensions.overload 
def flexibleset(o: _T) -> _extensions.AVT_Set[_T]: ... 

def flexibleset(o: object, /):
    """
    Availability: >= 0.3.75 \\
    https://aveyzan.xyz/aveytense#aveytense.util.flexibleset
    
    Returns a new set object. Unlike for the `set` constructor, if the argument isn't an iterable object, then
    a new set object is returned with this argument as the first item, preventing any exceptions thrown.
    """
    
    if not isinstance(o, _extensions.Iterable):
        return {o,}
    else:
        return set(o)
    
@_extensions.overload
def flexiblefrozenset(o: _extensions.Iterable[_T], /) -> _extensions.AVT_FrozenSet[_T]: ...
@_extensions.overload 
def flexiblefrozenset(o: _T) -> _extensions.AVT_FrozenSet[_T]: ... 

def flexiblefrozenset(o: object, /):
    """
    Availability: >= 0.3.75 \\
    https://aveyzan.xyz/aveytense#aveytense.util.flexiblefrozenset
    
    Returns a new set object. Unlike for the `set` constructor, if the argument isn't an iterable object, then
    a new set object is returned with this argument as the first item, preventing any exceptions thrown.
    """
    
    return frozenset(flexiblelist(o))

@_extensions.dataclass(init = False, eq = False, frozen = True)
class pair(_extensions.Generic[_KT, _VT]):
    """
    Availability: >= 0.3.75 \\
    https://aveyzan.xyz/aveytense#aveytense.util.pair
    
    An auxiliary class that creates pairs for dictionaries. It is *not* a dictionary
    
    New appended pairs cannot be deleted or re-set, unless it has the same *key*, its *value* is changed
    
    Type hinting note: generic class with 2 type parameters.
    """
    
    __pairs: _extensions.AVT_List[_extensions.AVT_Tuple[_KT, _VT]]
    
    def __init__(self, key: _KT, value: _VT, /): # >= 0.3.75
        
        from . import _mangle
        
        object.__setattr__(self, _mangle(self, "__pairs"), [(key, value)])
        
    def __str__(self): # >= 0.3.75
        return type(self).__name__ + str(tuple(self.__pairs))
    
    def __repr__(self): # >= 0.3.75
        from . import _ReprStr
        return _ReprStr.format(type(self).__qualname__, id(self))
    
    def __iter__(self): # >= 0.3.75
        return iter(self.__pairs)
    
    def copy(self): # >= 0.3.75
        c = type(self)(self.__pairs[0][0], self.__pairs[0][1])
        c.__pairs.extend(self.__pairs[1:])
        return c
    
    def __or__(self, other: _extensions.Union[pair[_KT2, _VT2], _extensions.AVT_Tuple[_KT2, _VT2]]): # >= 0.3.75
        
        def _override_last(l: _extensions.AVT_List[_extensions.AVT_Tuple[_KT, _VT]]):
            l2 = l.copy()
            l2.reverse()
            k = [x[0] for x in l2]
            v = [x[1] for x in l2]
            l2.clear()
            
            for i, e in enumerate(k):
                if e not in l2:
                    l2.extend([e, v[i]]) 
                
            l2 = list(_extensions.batched(l2, 2))
            l2.reverse()
            return _extensions.cast(_extensions.AVT_List[_extensions.AVT_Tuple[_KT, _VT]], l2)
        
        if isinstance(other, tuple):
            if _reckon(other) == 2:
                p = pair(other[0], other[1])
            else:
                error = ValueError("expected 2-item tuple")
                raise error
        elif isinstance(other, pair):
            p = other.copy()
        else:
            error = TypeError("expected a 'pair' instance or 2-item tuple")
            raise error
        
        p = _extensions.cast(
            pair[
                _extensions.Union[_KT, _KT2],
                _extensions.Union[_VT, _VT2]
            ],
            p
        )
        
        l = _override_last(self.__pairs + p.__pairs)
        p.__pairs.clear()
        p.__pairs.extend(l)
        return p
    
    def __ror__(self, other: _extensions.Union[pair[_KT2, _VT2], _extensions.AVT_Tuple[_KT2, _VT2]]): # >= 0.3.75
        
        def _override_last(l: _extensions.AVT_List[_extensions.AVT_Tuple[_KT, _VT]]):
            l2 = l.copy()
            l2.reverse()
            k = [x[0] for x in l2]
            v = [x[1] for x in l2]
            l2.clear()
            
            for i, e in enumerate(k):
                if e not in l2:
                    l2.extend([e, v[i]]) 
                
            l2 = list(_extensions.batched(l2, 2))
            l2.reverse()
            return _extensions.cast(_extensions.AVT_List[_extensions.AVT_Tuple[_KT, _VT]], l2)
        
        if isinstance(other, tuple):
            if _reckon(other) == 2:
                p = pair(other[0], other[1])
            else:
                error = ValueError("expected 2-item tuple")
                raise error
        elif isinstance(other, pair):
            p = other.copy()
        else:
            error = TypeError("expected a 'pair' instance or 2-item tuple")
            raise error
        p = _extensions.cast(
            pair[
                _extensions.Union[_KT, _KT2],
                _extensions.Union[_VT, _VT2]
            ],
            p
        )
        
        l = _override_last(p.__pairs + self.__pairs)
        p.__pairs.clear()
        p.__pairs.extend(l) 
        return p
    
    @property
    def pairs(self):
        return self.__pairs

@_extensions.dataclass(init = False, eq = False, repr = False, frozen = True)
class simpledict(_extensions.AVT_Mapping[_KT, _VT]):
    """
    Availability: >= 0.3.75 \\
    https://aveyzan.xyz/aveytense#aveytense.util.simpledict
    
    A mutable dictionary that doesn't require *keys* to be hashable objects.
    Inherits from `collections.abc.Mapping` (doesn't fully follow all methods
    from `collections.abc.MutableMapping`).
    
    This class itself does not create a dictionary object, it just
    mimicks its behavior.
    
    Type hinting note: generic class with 2 type parameters.
    """
    
    __keys: _extensions.AVT_List[_KT]
    __values: _extensions.AVT_List[_VT]
    __items: _extensions.AVT_List[_extensions.AVT_Tuple[_KT, _VT]]
    
    @_extensions.overload
    def __init__(self) -> None: ...
    @_extensions.overload
    def __init__(self: simpledict[str, _VT], **kwargs: _VT) -> None: ...  # pyright: ignore[reportInvalidTypeVarUse]
    @_extensions.overload
    def __init__(self, map: _KeyItemGetter[_KT, _VT], /) -> None: ...
    @_extensions.overload
    def __init__(
        self: simpledict[_extensions.Union[str, _KT], _VT],  # pyright: ignore[reportInvalidTypeVarUse]
        map: _KeyItemGetter[str, _VT],
        /,
        **kwargs: _VT,
    ) -> None: ...
    @_extensions.overload
    def __init__(
        self,
        iterable: _extensions.AVT_Iterable[_extensions.Union[
            pair[_KT, _VT],
            _extensions.AVT_Tuple[_KT, _VT]
        ]],
        /
    ) -> None: ...
    @_extensions.overload
    def __init__(
        self: simpledict[_extensions.Union[str, _KT], _VT],  # pyright: ignore[reportInvalidTypeVarUse]
        iterable: _extensions.AVT_Iterable[_extensions.Union[
            pair[_KT, _VT],
            _extensions.AVT_Tuple[_KT, _VT]
        ]],
        /,
        **kwargs: _VT,
    ) -> None: ...
    
    # alright, there we go, we re-implement the constructor of 'dict'...
    def __init__(self, i = None, **kwargs): # >= 0.3.75
        
        from . import _mangle
        
        keys, values, items = ([], [], [])
        
        if isinstance(i, _extensions.Iterable) and all(isinstance(x, pair) or (isinstance(x, tuple) and _reckon(x) == 2) for x in i):
            
            for x in i:
                keys.append(x.pairs[0] if isinstance(x, pair) else x[0])
                values.append(x.pairs[1] if isinstance(x, pair) else x[1])
                
        elif hasattr(i, "keys") and hasattr(i, "__getitem__"):
            
            keys = list(getattr(i, "keys", lambda: None)())
            values = [i[k2] for k2 in i]
            
        elif i is None:
            pass
        
        else:
            raise TypeError
            
        if _reckon(kwargs) > 0:
            
            for k2 in kwargs:
                keys.append(k2)
                values.append(kwargs[k2])
                
        for i2, k2 in enumerate(keys):
            items.append((k2, values[i2]))
            
        object.__setattr__(self, _mangle(self, "__keys"), keys)
        object.__setattr__(self, _mangle(self, "__values"), values)
        object.__setattr__(self, _mangle(self, "__items"), items)
        
    def __str__(self): # >= 0.3.75
        
        s = ""
        
        # mimicking the existence of 'dict'
        if _reckon(self.__keys) == 0:
            s = "{}"
        
        pattern = "{}: {}"
        i = 0
        
        while _reckon(self.__items) > i:
            
            s += pattern.format(self.__keys[i], self.__values[i]) + ", "
            i += 1
            
        s = "{" + _extensions.str_removesuffix(s, ", ") + "}"
        
        return "{}({})".format(type(self).__name__, s)
    
    def __repr__(self): # >= 0.3.75
        from . import _ReprStr
        return _ReprStr.format(type(self).__qualname__, id(self))
    
    def keys(self): # >= 0.3.75
        return self.__keys
    
    def items(self): # >= 0.3.75
        return self.__items
    
    def values(self): # >= 0.3.75
        return self.__values
    
    def clear(self): # >= 0.3.75
        self.__keys.clear()
        self.__values.clear()
        self.__items.clear()
    
    def __contains__(self, key: object): # >= 0.3.75
        return key in self.__keys
    
    def __getitem__(self, key: _KT): # >= 0.3.75
        if key in self:
            return self.__values[self.__keys.index(key)]
        else:
            raise KeyError
        
    def __setitem__(self, key: _KT2, value: _VT2): # >= 0.3.75
        
        # rewrite and append when missing
        if key in self:
            self.__values[self.__keys.index(key)] = value
            self.__items[self.__keys.index(key)] = (key, value)
        else:
            self.__keys.append(key)
            self.__values.append(value)
            self.__items.append((key, value))
        
    def __delitem__(self, key: _KT): # >= 0.3.75
        if key in self:
            del self.__keys[self.__keys.index(key)]
            del self.__values[self.__keys.index(key)]
            del self.__items[self.__keys.index(key)]
        else:
            raise KeyError
        
    def get(self, key: _KT, default: _T = None): # >= 0.3.75
        
        if key in self.__keys:
            return self[key]
        else:
            return default
    
    def __eq__(self, other: object): # >= 0.3.75
        return type(other) is type(self) and other.__items == self.__items
    
    def __len__(self): # >= 0.3.75
        return len(self.__keys)
    
    def __iter__(self): # >= 0.3.75
        return iter(self.__keys)
    
    # Backporting PEP 584 (Py3.9+, see https://peps.python.org/pep-0584) for Python 3.8.
    # These methods below are provided by 'dict', MutableMapping ABC doesn't provide these.
    def __or__(self, other: _KeyItemGetter[_KT2, _VT2]): # >= 0.3.75
        
        if hasattr(other, "keys") and hasattr(other, "__getitem__"):
            
            keys = self.__keys.copy()
            values = self.__values.copy()
            
            for k in other.keys():
                if k in self.__keys:
                    values[self.__keys.index(k)] = other[k]
                
            items = [(keys[i], values[i]) for i in range(_reckon(keys))]
            
            return simpledict(items)
        
        else:
            raise TypeError
    
    def __ror__(self, other: _KeyItemGetter[_KT2, _VT2]): # >= 0.3.75
        return self.__or__(other)
    
    # This doesn't exist in MutableMapping ABC either. 'dict' has it so we re-declare it
    def copy(self): # >= 0.3.75
        return simpledict(self.__items)

class Flags(_Immutable):
    """
    Availability: >= 0.3.53 \\
    https://aveyzan.xyz/aveytense#aveytense.util.Flags
    
    Returns buffer, code and type flags
    """
    
    buffer = _BufferFlags()
    """
    Availability: >= 0.3.53
    
    Receive buffer flags
    """
    
    code = _CodeFlags()
    """
    Availability: >= 0.3.53
    
    Receive code flags defined as in `dis.COMPILER_FLAG`
    """
    
    type = _TypeFlags()
    """
    Availability: >= 0.3.53
    
    Receive type flags
    """
    
    __all__ = sorted(list(_extensions.frozendict(vars(_BufferFlags)) | vars(_CodeFlags) | vars(_TypeFlags)))
    """
    Availability: >= 0.3.53
    
    Returns all flag names
    """

Flags = Flags()
BufferFlags = Flags.buffer
"""Availability: >= 0.3.53"""
CodeFlags = Flags.code
"""Availability: >= 0.3.53"""
TypeFlags = Flags.type
"""Availability: >= 0.3.53"""
    
__all__ = sorted([k for k in globals() if not k.startswith("_")]) # 0.3.41: sorted()
__all_deprecated__ = sorted([k for k in globals() if hasattr(globals()[k], "__deprecated__")])
"""
Availability: >= 0.3.41

Returns all deprecated declarations within this module.
"""

if __name__ == "__main__":
    error = RuntimeError("Import-only module")
    raise error