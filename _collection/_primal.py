"""
Availability: >= 0.3.24 \\
© 2024-Present Aveyzan // License: MIT

Defines first components for `aveytense` module. Use `aveytense` module instead
"""

from __future__ import annotations # to 0.3.56 it was missing

import sys as _sys

import datetime as _datetime
import decimal as _decimal
import fractions as _fractions
import math as _math
import numbers as _numbers
import warnings as _warnings



from . import _constants as _lc
from . import _version
from .. import constants as _constants
from .. import exceptions as _exceptions
from .. import extensions as _extensions

if _extensions.TYPE_CHECKING:
    from ._extensions import (
        _PrideMonth2026AbroadConvectType,
        _PrideMonth2026AbroadStart,
        _PrideMonth2026AbroadStop,
        _PrideMonth2026AbroadStep,
        _PrideMonth2026ReckonType
    )

from ._typeparams import (
    T1 as _T1,
    T2 as _T2
)

__name__ = "aveytense"

# types
_T_fi = _extensions.TypeVar("_T_fi", int, float) # Bound to float/int

_Ellipsis = _extensions.EllipsisType
_MODE_AND = _lc.ModeSelection.AND
_MODE_OR = _lc.ModeSelection.OR
_Mode = _extensions.Union[_lc.ModeSelection, _extensions.Literal["and", "or"]]
_FloatOrInteger = _extensions.FloatOrInteger
_OptionalFloatOrInteger = _extensions.Union[_FloatOrInteger, _Ellipsis]
_OptionalInteger = _extensions.Union[int, _Ellipsis]

_ReckonNGT = (_extensions.IO, _extensions.Iterable, _extensions.ReckonOperable, _extensions.Sized)

# >= 0.3.55
class _FibGenerator(_extensions.AVT_Generator[_T1, _extensions.Any, _T2]): ...
_FibGenerator = _extensions.AVT_Generator[_T1, _extensions.Any, _T2]

def _figurate_checker(x, cond): # 0.3.55
    
    # alteration 0.3.74
    return isinstance(x, int) and isinstance(cond, _extensions.FunctionType)


def _domain_checker(x: _FloatOrInteger, f: _extensions.Literal["asin", "acos", "asec", "acosec"] = "asin"): # 0.3.38
    
    if f in ("asin", "acos") and (x < -1 or x > 1):
        
        error = ValueError("bad math domain, expected value in range [-1; 1]")
        raise error
    
    elif f in ("asec", "acosec") and abs(x) < 1:
        
        error = ValueError("bad math domain, expected value not in range (-1; 1)")
        raise error
    
    return True

@_extensions.overload
@_extensions.deprecated("Deprecated since 0.3.67, use aveytense.__version__ or Tense.versionInfo instead. Up for removal in 0.3.78")
def aveytenseVersion(asString: _extensions.Literal[True] = True) -> _version.VERSION_TYPE: ...

@_extensions.overload
@_extensions.deprecated("Deprecated since 0.3.67, use aveytense.__version__ or Tense.versionInfo instead. Up for removal in 0.3.78")
def aveytenseVersion(asString: _extensions.Literal[False]) -> _version._VERSION_INFO: ...

def aveytenseVersion(asString = True):
    """
    Availability: >= 0.3.25 \\
    Deprecated: >= 0.3.67
    ```
    # since 0.3.47
    def aveytenseVersion(asString: bool = True): ...
    # for 0.3.24 - 0.3.46
    def tenseVersion(asTuple: bool = False): ...
    # before 0.3.24
    def tenseVersion(): ...
    ```
    Returns AveyTense version installed. Ensure you have version up-to-date to make everything actually working. If optional parameter \\
    is set to `True`, returned is tuple with 3 items, which together compose version of AveyTense. This argument is also responsible for \\
    deletion of global function `tenseVersionAsTuple()` on 0.3.24. Before 0.3.47 it was called `tenseVersion()`
    """
    
    from .._collection import _version
    
    if asString:
        return _version.VERSION
    else:
        return _version.VERSION_INFO


def _int_float_fallback(v, /): # 0.3.71
    
    if isinstance(v, (int, float)):
        return v
    elif isinstance(v, _extensions.FloatConvertible):
        return _extensions.cast(float, v.__float__())
    elif isinstance(v, _extensions.IntegerConvertible):
        return _extensions.cast(int, v.__int__())
    elif isinstance(v, _extensions.Indexable):
        return _extensions.cast(int, v.__index__())
    
# declarations

def _reckon_init(*v: _PrideMonth2026ReckonType):
    
    i = 0
    for e in v:
        
        if isinstance(e, _extensions.IO):
            
            try:
                for _ in e.read():
                    i += 1
            except:
                pass
            
        # elif isinstance(e, _tkinter.StringVar): # < 0.3.39
        #    i += len(e.get())
            
        elif isinstance(e, _extensions.Iterable):
            
            for _ in e:
                i += 1
                
        elif isinstance(e, _extensions.Sizeable):
            i += len(e)
            
        elif isinstance(e, _extensions.ReckonOperable):
            i += e.__reckon__()
            
        else:
            error = TypeError("expected an iterable or file object, or object of a class that has one or more of these methods: __len__(), __reckon__()")
            raise error
        
    return i

def reckon(*v: _PrideMonth2026ReckonType):
    """
    Availability: >= 0.3.7 \\
    Standard: >= 0.3.7 \\
    https://aveyzan.xyz/aveytense#aveytense.reckon
    
    Extension of `len()` built-in function. Supports `IO` and
    its subclasses, classes having either `__len__`, `__iter__`
    or `__reckon__` magic methods.
    """
    i = 0
    
    for e in v:
        i += _reckon_init(e)
        
    return i

def reckonLeast(*v: _PrideMonth2026ReckonType):
    """
    Availability: >= 0.3.25 \\
    Standard: >= 0.3.25
    
    Get the least length from the iterable objects passed.
    """
    n = 0
    for e in v:
        if n > reckon(e):
            n = reckon(e)
    return n

def reckonGreatest(*v: _PrideMonth2026ReckonType):
    """
    Availability: >= 0.3.25 \\
    Standard: >= 0.3.25
    
    Get the greatest length from the iterable objects passed.
    """
    n = 0
    for e in v:
        if n < reckon(e):
            n = reckon(e)
    return n

def reckonIsLeast(v1: _PrideMonth2026ReckonType, v2: _PrideMonth2026ReckonType, /):
    """
    Availability: >= 0.3.25 \\
    Standard: >= 0.3.25
    
    Comparison: Check whether first argument is length-less than the second.
    """
    return reckon(v1) < reckon(v2)


def reckonIsGreater(v1: _PrideMonth2026ReckonType, v2: _PrideMonth2026ReckonType, /):
    """
    Availability: >= 0.3.25 \\
    Standard: >= 0.3.25
    
    Comparison: Check whether first argument is length-greater than the second.
    """
    return reckon(v1) > reckon(v2)

# set all these 3 to False since these are re-declared differently
@_extensions.dataclass(init = False, repr = False, eq = False, frozen = True)
class abroad:
    """
    Availability: >= 0.3.9 \\
    Standard: >= 0.3.10 \\
    https://aveyzan.xyz/aveytense#aveytense.abroad
    """
    
    # These genuinely represent these types
    __start: int
    __stop: int
    __step: int
    __list: _extensions.AVT_List[int]
    
    # 0.3.25: slash update
    # 0.3.74: overloads
    
    @_extensions.overload
    def __init__(self, stop: _PrideMonth2026AbroadStop, /) -> None: ...
    @_extensions.overload
    def __init__(self, start: _PrideMonth2026AbroadStart, stop: _PrideMonth2026AbroadStop, /, step: _PrideMonth2026AbroadStep = 1) -> None: ...
    
    def __init__(self, start: _PrideMonth2026AbroadStart, stop: _PrideMonth2026AbroadStop = ..., /, step: _PrideMonth2026AbroadStep = 1):
        
        error1 = lambda param: TypeError("expected the '{}' argument to be an integer, a floating-point number, an iterable object, a file object," + \
            "or instance of a class that supports one or more of the following methods: __len__(), __reckon__(), __float__(), __int__(), __index__()".format(param))
        error2 = TypeError("expected the 'step' argument to be an integer, a floating-point number, or instance of a class that supports one or more of the following methods: __float__(), __int__(), __index__()")
        
        try:
            _start = _reckon_init(start)
        except TypeError:
            _start = _int_float_fallback(start)
        if _start is None:
            if stop is Ellipsis:
                raise error1("stop")
            else:
                raise error1("start")
        if isinstance(_start, float):
            _start = _math.trunc(_start)
        
        if stop is Ellipsis:
            if _start >= 0:
                _stop = _start
                _start = 0
            else:
                _stop = -1
        else:
            try:
                _stop = _reckon_init(stop)
            except TypeError:
                _stop = _int_float_fallback(stop)
            if _stop is None:
                raise error1("stop")
            if isinstance(_stop, float):
                # fractions above 0.6 and below -0.6
                # re-implementing behavior from the past implementation
                _stop = round(_stop)
            
        _step = _int_float_fallback(step)
        if _step is None:
            raise error2
        if isinstance(_step, float):
            _step = _math.trunc(_step)
        _step = abs(_step)
        if _step == 0:
            _step = 1
            
        _list = [0]
        _list.clear()
        
        i = _start
        
        _statement = lambda x = 0: x > _stop if _start > _stop else x < _stop
        _step = -_step if _start > _stop else _step
        
        while _statement(i):
            _list.append(i)
            i += _step
        
        # normally if we used e.g.: "__start", this means the name is as-is
        # and not mangled
        def _mangle(attr: str):
            return "_{}__{}".format(type(self).__name__, attr)
            
        object.__setattr__(self, _mangle("start"), _start)
        object.__setattr__(self, _mangle("stop"), _stop) 
        object.__setattr__(self, _mangle("step"), _step)
        object.__setattr__(self, _mangle("list"), _list)
        
        del _mangle
        
    @property
    def start(self): # 0.3.74
        return self.__start
    
    @property
    def stop(self): # 0.3.74
        return self.__stop
    
    @property
    def step(self): # 0.3.74
        return self.__step
    
    @property
    def list(self): # 0.3.74
        return self.__list
    
    @property
    def tuple(self): # 0.3.74
        return tuple(self.__list)
        
    def __str__(self):
        return type(self).__name__ + f"{(self.start, self.stop, self.step)}"
    
    def __repr__(self):
        from . import _ReprStr
        return _ReprStr.format(type(self).__qualname__, id(self))
    
    def __iter__(self):
        return iter(self.list)
    
    def __reversed__(self): # 0.3.32
        return reversed(self.list)
    
    def __bytes__(self): # 0.3.74
        return bytes(self.list)
    
    def __hash__(self): # 0.3.74
        return hash(self.tuple)
    
    def __len__(self): # 0.3.74
        return len(self.list)
    
    def __contains__(self, key: int): # 0.3.32
        return key in self.list
    
    def __eq__(self, value): # 0.3.74
        return type(value) == type(self) and value.list == self.list
    
    def __ne__(self, value): # 0.3.74
        return not self.__eq__(value)
    
    def __add__(self, other: _extensions.AVT_Iterable[_extensions.T]): # 0.3.32
        
        if not isinstance(other, _extensions.Iterable):
            error = TypeError("expected an iterable as the right operand")
            raise error
        
        return self.list + list(other)
    
    def __radd__(self, other: _extensions.AVT_Iterable[_extensions.T]): # 0.3.32
        
        if not isinstance(other, _extensions.Iterable):
            error = TypeError("expected an iterable as the left operand")
            raise error
        
        return list(other) + self.list
    
    def __mul__(self, other: _extensions.Indexable): # 0.3.32
        
        if not isinstance(other, _extensions.Indexable) or (isinstance(other, _extensions.Indexable) and other.__index__() < 1):
            error = TypeError("expected a non-negative integer as a right operand")
            raise error
        
        return self.list * other
    
    def __rmul__(self, other: _extensions.Indexable): # 0.3.32
        
        return other * self.list
            
    @_extensions.overload
    def __getitem__(self, key: _extensions.Indexable) -> int: ...
    @_extensions.overload
    def __getitem__(self, key: slice) -> _extensions.AVT_List[int]: ...
    def __getitem__(self, key): # 0.3.29
        return self.__list.__getitem__(key)
    
    @_extensions.deprecated(
        "Pending deprecation since 0.3.78, up for removal in 0.3.84. Consider using the 'abroad.list' property instead.",
        category = PendingDeprecationWarning
    )
    def __pos__(self):
        """
        Availability: >= 0.3.28 \\
        Deprecated: >= 0.3.78
        
        Returns abroad object as a list object. The plus sign means that items can be changed.
        """
        return self.__list
    
    @_extensions.deprecated(
        "Pending deprecation since 0.3.78, up for removal in 0.3.84. Consider using the 'abroad.tuple' property instead.",
        category = PendingDeprecationWarning
    )
    def __neg__(self):
        """
        Availability: >= 0.3.28 \\
        Deprecated: >= 0.3.78
        
        Returns abroad object as a tuple object. The minus sign means that items can be changed.
        """
        return tuple(self.__list)
    
    @_extensions.deprecated(
        "Deprecated since 0.3.74 due to the modified item order of 'set' objects. " +
        "Use of 'reversed(self)' is more encouraged in this case. Moreover, the abroad object content " +
        "is always unique. Up for removal in 0.3.78."
    )
    def __invert__(self):
        """
        Availability: >= 0.3.28 \\
        Deprecated: >= 0.3.74
        
        Returns abroad object as a set object. The bitwise inversion means that all items are unique.
        """
        
        return set(self.__list)
    
    def __mod__(self, other: str): # 0.3.75
        
        if isinstance(other, str):
            
            s = ""
            
            if other.count("{}") == 1:
                
                for e in self.__list:
                    s += other.format(e)
            
            else:
                
                for e in self.__list:
                    s += str(e) + other
                    
            return s
                    
        else:
            error = TypeError("expected a string as a right operand")
            raise error

    def __rmod__(self, other: str): # 0.3.75
        
        if isinstance(other, str):
            
            s = ""
            
            if other.count("{}") == 1:
                
                for e in self.__list:
                    s += other.format(e)
                    
            else:
                
                for e in self.__list:
                    s += other + str(e)
                    
            return s
                    
        else:
            error = TypeError("expected a string as a left operand")
            raise error

    
    def count(self, value: int, /): # 0.3.74
        return self.__list.count(value)
    
    def index(self, value: int, start: _extensions.Indexable = 0, stop: _extensions.Indexable = _sys.maxsize, /): # 0.3.74
        return self.__list.index(value, start, stop)
        
    @staticmethod
    def fromComplex(c: _extensions.Union[complex, _extensions.ComplexConvertible], /, step: _PrideMonth2026AbroadStep = 1):
        """
        Availability: >= 0.3.74 \\
        https://aveyzan.xyz/aveytense#aveytense.abroad.fromComplex
        
        A static method creating instance of class `abroad`, with behavior for `complex` objects improved
        """
        
        # Python 3.11+: 'complex' has the '__complex__()' method
        if not isinstance(c, (complex, _extensions.ComplexConvertible)) or (
            isinstance(c, _extensions.ComplexConvertible) and not isinstance(c.__complex__(), complex)
        ):
            error = TypeError("expected a complex object or object of a class defining the __complex__() method that returns a complex object")
            raise error
        
        if isinstance(c, _extensions.ComplexConvertible):
            c2 = complex(c)
        else:
            c2 = c
        
        return abroad(c2.real, c2.imag, step)
    
    @staticmethod
    @_extensions.overload
    def negative(stop: _PrideMonth2026AbroadStop, /) -> abroad: ...
    
    @staticmethod
    @_extensions.overload
    def negative(start: _PrideMonth2026AbroadStart, stop: _PrideMonth2026AbroadStop, /, step: _PrideMonth2026AbroadStep = 1) -> abroad: ...
    
    @staticmethod
    def negative(start: _PrideMonth2026AbroadStart, stop: _PrideMonth2026AbroadStop = ..., /, step: _PrideMonth2026AbroadStep = 1):
        """
        Availability: >= 0.3.74 \\
        https://aveyzan.xyz/aveytense#aveytense.abroad.negative
        
        A static method creating instance of class `abroad`, converting `start` and `stop` to negative.
        """
        
        a = abroad(start, stop, step)
        _start = -abs(a.start)
        _stop = -abs(a.stop)
        _step = a.step if _start < _stop else -a.step
        del a
        return abroad(_start, _stop, _step)
    
    @staticmethod
    @_extensions.overload
    def positive(stop: _PrideMonth2026AbroadStop, /) -> abroad: ...
    
    @staticmethod
    @_extensions.overload
    def positive(start: _PrideMonth2026AbroadStart, stop: _PrideMonth2026AbroadStop, /, step: _PrideMonth2026AbroadStep = 1) -> abroad: ...
    
    @staticmethod
    def positive(start: _PrideMonth2026AbroadStart, stop: _PrideMonth2026AbroadStop = ..., /, step: _PrideMonth2026AbroadStep = 1):
        """
        Availability: >= 0.3.74 \\
        https://aveyzan.xyz/aveytense#aveytense.abroad.positive
        
        A static method creating instance of class `abroad`, converting `start` and `stop` to positive.
        """
        
        a = abroad(start, stop, step)
        _start = abs(a.start)
        _stop = abs(a.stop)
        _step = a.step if _start < _stop else -a.step
        del a
        return abroad(_start, _stop, _step)
    
    @staticmethod
    def convect(*v: _PrideMonth2026AbroadConvectType):
        """
        Availability: >= 0.3.74 \\
        https://aveyzan.xyz/aveytense#aveytense.abroad.convect
        
        See abroad convection term on https://aveyzan.xyz/aveytense/glossary#abroad_convection
        """
        
        i = 0
        
        if reckon(v) == 0:
            error = _exceptions.MissingValueError("expected at least one item in parameter 'v'")
            raise error
        
        for e in v:
            
            if not isinstance(e, (*_ReckonNGT, int, float, _extensions.IntegerConvertible, _extensions.FloatConvertible, _extensions.Indexable)):
                error = TypeError("at least one argument from parameter 'v' represents unsupported type")
                raise error
            
            elif isinstance(e, _ReckonNGT):
                i += reckon(e)
            
            elif isinstance(e, (float, _extensions.FloatConvertible)):
                
                if isinstance(e, float):
                    i += _math.trunc(e)
                else:
                    i += _math.trunc(float(e))
            
            elif isinstance(e, (int, _extensions.IntegerConvertible)):
                
                if isinstance(e, int):
                    i += e
                else:
                    i += int(e)
                    
            else:
                i += e.__index__()
                
        if i >= 0:
            return abroad(i)
        else:
            return abroad(i, -1)
        

@_extensions.deprecated(
    "Pending deprecation since 0.3.78.",
    category = PendingDeprecationWarning
)
class Time:
    """
    Availability: >= 0.3.25 (4th July 2024)
    
    Access to time. Non-standard and may be removed or remade in the future
    """
    
    __forced_unix_year_range = False
    
    @classmethod
    @_extensions.deprecated("Deprecated since 0.3.74. No longer encouraged to use this method anymore.")
    def forceUnixYearRange(self, option = False, /):
        """
        Availability: >= 0.3.25 (4th July 2024)
        
        Forces year range to 1st Jan 1970 - 19th Jan 2038. \\
        If set to `False`, it is reset.
        """
    
        self.__forced_unix_year_range = option
        return self
    
    @classmethod
    @_extensions.deprecated("Deprecated since 0.3.74. No longer encouraged to use this method anymore.")
    def fencordFormat(self):
        """
        Availability: >= 0.3.25 (4th July 2024)
        
        Returned is present time in `aveytense.fencord.Fencord` former class format as `%Y-%m-%d %H:%M:%S`. Timezone is user's local timezone.
        This format also uses `discord` module.
        """
        
        return _datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    @classmethod
    def isLeapYear(self, year: int):
        """
        Availability: >= 0.3.25 (4th July 2024)
        
        Returned is `True` only when:
        - year is an integer and is positive (above 0)
        - year is divisible by 4 and not divisible by 100 or year is divisible by 400
        - if Unix year range is enforced, only years in range 1970 - 2038

        If none of these requirements are granted, returned is `False`.
        """
        b = ((isinstance(year, int) and year >= 1) and (year % 4 == 0 and year % 100 != 0) or year % 400 == 0)
        if self.__forced_unix_year_range: b = b and (year >= 1970 and year <= 2038)
        return b
    
    @classmethod
    def verifyDate(self, year: int, month: int, day: int):
        """
        Availability: >= 0.3.25 (4th July 2024)
        
        Returned is `True` only when every parameter is an integer and year is from 1 up, \\
        month is from 1 up and day is from 1 up, and one of these statements are granted:
        - day has value 31 for months: 1, 3, 5, 7, 8, 10, 12
        - day has value 30 for every month in range 1-12 excluding 2
        - day has value 29 for every month in range 1-12, for 2 only if year is leap
        - day is in range 1-28 for every month in range 1-12
        - additionally, if Unix year range is enforced, year is in range 1970-2038

        If none of these requirements are granted, returned is `False`.
        """
        return (
                isinstance(year, int) and isinstance(month, int) and isinstance(day, int)) and (year >= 1 and month >= 1 and day >= 1) and (
                (day == 31 and month in (1, 3, 5, 7, 8, 10, 12)) or (day == 30 and month in set(abroad(1, 12.1)).difference({2})) or
                (day == 29 and month in abroad(1, 12.1) and self.isLeapYear(year)) or (day < 29 and month in abroad(1, 12.1))
            )
                
    @classmethod
    def getMillennium(self):
        """
        Availability: >= 0.3.25 (4th July 2024)
        
        Returns current millennium.
        """
        return _math.trunc(int(_datetime.datetime.now().strftime("%Y")) / 1000) + 1
    
    @classmethod
    def getCentury(self):
        """
        Availability: >= 0.3.25 (4th July 2024)
        
        Returns current century.
        """
        return _math.trunc(int(_datetime.datetime.now().strftime("%Y")) / 100) + 1
    
    @classmethod
    def getDecade(self):
        """
        Availability: >= 0.3.25 (4th July 2024)
        
        Returns current decade. Warning: it does not return something like
        3rd decade of 21st century, but decade in overall, which have elapsed
        since Anno Domini time period. So what that means: for 2024 (4th July
        2024, when created this method) returned is 203.

        It does not match 0-to-9 decades, but 1-to-0, so 203 will be returned
        by years in range 2021-2030 (not in 2020-2029), including both points.
        """
        return _math.trunc(int(_datetime.datetime.now().strftime("%Y")) / 10) + 1
    
    @classmethod
    def getYear(self):
        """
        Availability: >= 0.3.25 (4th July 2024)
        
        Returns current year
        """
        return int(_datetime.datetime.now().strftime("%Y"))
    
    @classmethod
    def getMonth(self):
        """
        Availability: >= 0.3.25 (4th July 2024)
        
        Returns current month
        """
        return int(_datetime.datetime.now().strftime("%m"))
    
    @classmethod
    def getDay(self):
        """
        Availability: >= 0.3.25 (4th July 2024)
        
        Returns current day. Basing on local timezone.
        Warning: This doesn't return day of the year \\
        or day of the week, but only day of the month
        """
        return int(_datetime.datetime.now().strftime("%d"))
    
    @classmethod
    def getHour(self):
        """
        Availability: >= 0.3.25 (4th July 2024)
        
        Returns current hour. Basing on local timezone.
        """
        return int(_datetime.datetime.now().strftime("%H"))
    
    @classmethod
    def getMinute(self):
        """
        Availability: >= 0.3.25 (4th July 2024)
        
        Returns current minute. Basing on local timezone.
        """
        return int(_datetime.datetime.now().strftime("%M"))
    
    @classmethod
    def getSecond(self):
        """
        Availability: >= 0.3.25 (4th July 2024)
        
        Returns current second. Basing on local timezone.
        """
        return int(_datetime.datetime.now().strftime("%S"))
    
    __all__ = [n for n in locals() if n[:1] != "_"]
    "Availability: >= 0.3.25"
    
class Math:
    """
    Availability: >= 0.3.25 (4th July 2024) \\
    https://aveyzan.xyz/aveytense#aveytense.Math
    
    Math methods and constants
    """
    
    #################################### Constants extracted from aveytense.constants ####################################

    NAN = float("nan") # >= 0.3.25 (05.07.2024)
    INF = float("inf") # >= 0.3.25 (05.07.2024)
    SQRT2 = 1.4142135623730950488016887242097 # >= 0.3.25 (05.07.2024)
    E = 2.718281828459045235360287471352 # >= 0.3.25 (04.07.2024)
    PI = _decimal.Decimal("3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461") # >= 0.3.25 (04.07.2024)
    TAU = 6.283185307179586476925287 # >= 0.3.25 (05.07.2024)
    THOUSAND           = 10 ** 3   # >= 0.3.47 (07.06.2025)
    MILLION            = 10 ** 6   # >= 0.3.47 (07.06.2025)
    BILLION            = 10 ** 9   # >= 0.3.47 (07.06.2025)
    TRILLION           = 10 ** 12  # >= 0.3.47 (07.06.2025)
    QUADRILLION        = 10 ** 15  # >= 0.3.47 (07.06.2025)
    QUINTILLION        = 10 ** 18  # >= 0.3.47 (07.06.2025)
    SEXTILLION         = 10 ** 21  # >= 0.3.47 (07.06.2025)
    SEPTILLION         = 10 ** 24  # >= 0.3.47 (07.06.2025)
    OCTILLION          = 10 ** 27  # >= 0.3.47 (07.06.2025)
    NONILLION          = 10 ** 30  # >= 0.3.47 (07.06.2025)
    DECILLION          = 10 ** 33  # >= 0.3.47 (07.06.2025)
    UNDECILLION        = 10 ** 36  # >= 0.3.47 (07.06.2025)
    DUODECILLION       = 10 ** 39  # >= 0.3.47 (07.06.2025)
    TREDECILLION       = 10 ** 42  # >= 0.3.47 (07.06.2025)
    QUATTUOR_DECILLION = 10 ** 45  # >= 0.3.47 (07.06.2025)
    QUINDECILLION      = 10 ** 48  # >= 0.3.47 (07.06.2025)
    SEXDECILLION       = 10 ** 51  # >= 0.3.47 (07.06.2025)
    SEPTEN_DECILLION   = 10 ** 54  # >= 0.3.47 (07.06.2025)
    OCTODECILLION      = 10 ** 57  # >= 0.3.47 (07.06.2025)
    NOVEMDECILLION     = 10 ** 60  # >= 0.3.47 (07.06.2025)
    VIGINTILLION       = 10 ** 63  # >= 0.3.47 (07.06.2025)
    GOOGOL             = 10 ** 100 # >= 0.3.47 (07.06.2025)
    CENTILLION         = 10 ** 303 # >= 0.3.25 (19.07.2024)
    
    @classmethod
    def isNegative(self, x: _extensions.Union[_FloatOrInteger, _extensions.AVT_Sequence[_FloatOrInteger]], /):
        """
        Availability: >= 0.3.31 \\
        (no doc yet)
        
        Check whether a number is negative. If provided is a sequence, \\
        each number in it must satisfy this condition.
        """
        
        if not isinstance(x, (int, float, _extensions.Sequence)):
            error = TypeError("expected a number (integer or float) or sequence of numbers")
            raise error
        
        elif isinstance(x, (int, float)):
            return x < 0
        
        else:
            
            for e in x:
                
                if not isinstance(e, (int, float)):
                    error = TypeError("expected a number (integer or float) or sequence of numbers")
                    raise error
            
            _r = [e for e in x if e < 0]
            return reckon(_r) == reckon(x)
                
    
    @classmethod
    def isPositive(self, x: _extensions.Union[_FloatOrInteger, _extensions.AVT_Sequence[_FloatOrInteger]], /):
        """
        Availability: >= 0.3.31 \\
        (no doc yet)
        
        Check whether a number is positive. If provided is a sequence, \\
        each number in it must satisfy this condition.
        """
        
        if not isinstance(x, (int, float, _extensions.Sequence)):
            error = TypeError("expected a number (integer or float) or sequence of numbers")
            raise error
        
        elif isinstance(x, (int, float)):
            return x > 0
        
        else:
            
            for e in x:
                
                if not isinstance(e, (int, float)):
                    error = TypeError("expected a number (integer or float) or sequence of numbers")
                    raise error
            
            _r = [e for e in x if e > 0]
            return _reckon_init(_r) == _reckon_init(x)
    
    @classmethod
    def isPrime(self, x: int, /):
        """
        Availability: >= 0.3.31 \\
        (no doc yet)
        
        Check whether an integer is prime
        """
        if not isinstance(x, int) or (isinstance(x, int) and self.isNegative(x)):
            error = TypeError("expected a positive integer")
            raise error
        
        if x in (0, 1):
            return False
        
        for i in abroad(2, x):
            
            if x % i == 0:
                return False
            
        return True
    
    @classmethod
    def isComposite(self, x: int, /):
        """
        Availability: >= 0.3.31 \\
        (no doc yet)
        
        Check whether an integer is composite
        """
        if not isinstance(x, int) or (isinstance(x, int) and self.isNegative(x)):
            error = TypeError("expected a positive integer")
            raise error
        
        if x in (0, 1):
            return False
        
        return not self.isPrime(x)
    
    @classmethod
    def isScientific(self, x: str, /):
        """
        Availability: >= 0.3.57
        
        Check whether the string contains a number written in scientific notation.
        """
        
        import re
        
        if not isinstance(x, str):
            return False
        
        return re.match(r"^\d+(\.\d+)?[eE][+-]\d+$", x.strip()) is not None
    
    @classmethod
    def isInRange(self, x: _extensions.Union[_FloatOrInteger, _extensions.AVT_Sequence[_FloatOrInteger]], a: _FloatOrInteger, b: _FloatOrInteger, /, mode = "c"):
        """
        Availability: >= 0.3.36 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.isInRange
        
        Returns `True`, if number(s) are in specific range [a; b]. \\
        For empty sequences returned is `False`.
        
        On 0.3.39 added optional parameter `mode` to modify intervals:
        - `"c"` (default value) / `"cc"` = `<a; b>` = `a <= x <= b`
        - `"co"` = `<a; b)` = `a <= x < b`
        - `"o"` / `"oo"` = `(a; b)` = `a < x < b`
        - `"oc"` = `(a; b>` = `a < x <= b`
        """
        
        # 0.3.41: Excluding inf and nan
        if all([type(e) in (int, float) and e not in (self.INF, self.NAN) for e in [a, b]]):
            
            _mode = mode.lower()
            
            # 0.3.41: Brackets
            if _mode not in ("c", "cc", "oc", "co", "o", "oo"):
                error = TypeError("expected an approriate string value in parameter 'mode' from following: 'c', 'cc', 'oc', 'co', 'o', 'oo' (case insensitive), '[]', '[)', '(]', '()'")
                raise error
        
            _range = [a, b]
            
            if a > b:
                _range.reverse()
            
            if isinstance(x, (int, float)):
                
                if _mode in ("c", "cc"):
                    return x >= _range[0] and x <= _range[1]
                
                elif _mode in ("co",):
                    return x >= _range[0] and x < _range[1]
                
                elif _mode in ("oc",):
                    return x > _range[0] and x <= _range[1]
                
                else:
                    return x > _range[0] and x < _range[1]
            
            elif isinstance(x, _extensions.Sequence) and all([type(e) in (int, float) and e not in (self.INF, self.NAN) for e in x]):
                
                if _reckon_init(x) == 0:
                    return False
                
                _placeholder = True
                
                for e in x:
                    
                    if _mode in ("c", "cc",):
                        _placeholder = _placeholder and (e >= _range[0] and e <= _range[1])
                        
                    elif _mode in ("co",):
                        _placeholder = _placeholder and (e >= _range[0] and e < _range[1])
                        
                    elif _mode in ("oc",):
                        _placeholder = _placeholder and (e > _range[0] and e <= _range[1])
                        
                    else:
                        _placeholder = _placeholder and (e > _range[0] and e < _range[1])
                    
                return _placeholder
        
        error = TypeError("expected 'x' as integer/float or sequence of integers and floats, 'a' and 'b' as integers or floats, all excluding infinity and NaN")
        raise error
    
    @classmethod
    def isIncreasing(self, x: _extensions.AVT_Sequence[_FloatOrInteger], /):
        """
        Availability: >= 0.3.38 \\
        (no doc yet)
        
        Returns `True` if sequence has positive difference for consecutive members, \\
        and has at least 3 integer items.
        """
        
        if isinstance(x, _extensions.Sequence) and all([type(e) in (int, float) and e not in (self.INF, self.NAN) for e in x]):
        
            if _reckon_init(x) < 3:
                return False
            
            _placeholder = True
            
            for i in abroad(_reckon_init(x) - 1):
                
                _placeholder = _placeholder and x[i + 1] - x[i] > 0
                
            return _placeholder
            
            
        error = TypeError("expected a number sequence with at least 3 items, without infinity and NaN")
        raise error
    
    @classmethod
    def isDecreasing(self, x: _extensions.AVT_Sequence[_FloatOrInteger], /):
        """
        Availability: >= 0.3.38 \\
        (no doc yet)
        
        Returns `True` if sequence has negative difference for consecutive members, \\
        and has at least 3 number items.
        """
        
        if isinstance(x, _extensions.Sequence) and all([type(e) in (int, float) and e not in (self.INF, self.NAN) for e in x]):
        
            if _reckon_init(x) < 3:
                return False
            
            _placeholder = True
            
            for i in abroad(_reckon_init(x) - 1):
                
                _placeholder = _placeholder and x[i + 1] - x[i] < 0
                
            return _placeholder
            
        error = TypeError("expected a number sequence with at least 3 items, without infinity and NaN")
        raise error
    
    @classmethod
    def isConstant(self, x: _extensions.AVT_Sequence[_FloatOrInteger], /):
        """
        Availability: >= 0.3.38 \\
        (no doc yet)
        
        Returns `True` if sequence has difference equal 0 for consecutive members, \\
        and has at least 3 number items.
        """
        
        if isinstance(x, _extensions.Sequence) and all([type(e) in (int, float) and e not in (self.INF, self.NAN) for e in x]):
        
            if _reckon_init(x) < 3:
                return False
            
            _placeholder = True
            
            for i in abroad(_reckon_init(x) - 1):
                
                _placeholder = _placeholder and x[i + 1] - x[i] == 0
                
            return _placeholder
            
        error = TypeError("expected a number sequence with at least 3 items, without infinity and NaN")
        raise error
    
    @classmethod
    def isNonIncreasing(self, x: _extensions.AVT_Sequence[_FloatOrInteger], /):
        """
        Availability: >= 0.3.38 \\
        (no doc yet)
        
        Returns `True` if sequence has negative difference or equal 0 for consecutive members, \\
        and has at least 3 number items.
        """
        
        if isinstance(x, _extensions.Sequence) and all([type(e) in (int, float) and e not in (self.INF, self.NAN) for e in x]):
        
            if _reckon_init(x) < 3:
                return False
            
            _placeholder = True
            
            for i in abroad(_reckon_init(x) - 1):
                
                _placeholder = _placeholder and x[i + 1] - x[i] <= 0
                
            return _placeholder
            
        error = TypeError("expected a number sequence with at least 3 items, without infinity and NaN")
        raise error
    
    @classmethod
    def isNonDecreasing(self, x: _extensions.AVT_Sequence[_FloatOrInteger], /):
        """
        Availability: >= 0.3.38 \\
        (no doc yet)
        
        Returns `True` if sequence has positive difference or equal 0 for consecutive members, \\
        and has at least 3 number items.
        """
        
        if isinstance(x, _extensions.Sequence) and all([type(e) in (int, float) and e not in (self.INF, self.NAN) for e in x]):
        
            if _reckon_init(x) < 3:
                return False
            
            _placeholder = True
            
            for i in abroad(_reckon_init(x) - 1):
                
                _placeholder = _placeholder and x[i + 1] - x[i] >= 0
                
            return _placeholder
            
        error = TypeError("expected a number sequence with at least 3 items, without infinity and NaN")
        raise error
    
    @classmethod
    def isMonotonous(self, x: _extensions.AVT_Sequence[_FloatOrInteger], /):
        """
        Availability: >= 0.3.38 \\
        (no doc yet)
        
        Returns `True`, if sequence is monotonous (is either increasing, \\
        decreasing, constant, non-decreasing or non-increasing).
        """
        
        if not isinstance(x, _extensions.Sequence) or not all([type(e) in (int, float) and e not in (self.INF, self.NAN) for e in x]):
            error = TypeError("expected a number sequence with at least 3 items, without infinity and NaN")
            raise error
        
        return self.isIncreasing(x) or self.isDecreasing(x) or self.isConstant(x) or self.isNonDecreasing(x) or self.isNonIncreasing(x)
    
    @classmethod
    @_extensions.overload
    def isFraction(self, o: _extensions.Any, /) -> _extensions.TypeIs[_fractions.Fraction]: ...
    
    @classmethod
    @_extensions.overload
    def isFraction(self, o: _extensions.Any, /, *_: _extensions.Any, mode: _Mode = _MODE_AND) -> bool: ...
    
    @classmethod
    def isFraction(self, o, /, *_, mode = _MODE_AND):
        """
        Availability: >= 0.3.41
                
        Returns `True`, if value is instance of class `fractions.Fraction`.
        """
        
        if _reckon_init(_) == 0:
            return type(o) is _fractions.Fraction
        
        else:
            _many = (o,) + _
            
            if mode in (_constants.MODE_OR, "or"):
                return any([type(e) is _fractions.Fraction for e in _many])
            
            elif mode in (_constants.MODE_AND, "and"):
                return all([type(e) is _fractions.Fraction for e in _many])
            
            else:
                return False
            
            
    @classmethod
    @_extensions.overload
    def isDecimal(self, o: _extensions.Any, /) -> _extensions.TypeIs[_decimal.Decimal]: ...
    
    @classmethod
    @_extensions.overload
    def isDecimal(self, o: _extensions.Any, /, *_: _extensions.Any, mode: _Mode = _MODE_AND) -> bool: ...
    
    @classmethod
    def isDecimal(self, o, /, *_, mode = _MODE_AND):
        """
        Availability: >= 0.3.38
                
        Returns `True`, if value is decimal string (since 0.3.41 - `~.Tense.isDecimalString()`).
        - since 0.3.41: -  ^  - is instance of class `decimal.Decimal`.
        """
        
        if _reckon_init(_) == 0:
            return type(o) is _decimal.Decimal
        
        else:
            _many = (o,) + _
            
            if mode in (_constants.MODE_OR, "or"):
                return any([type(e) is _decimal.Decimal for e in _many])
            
            elif mode in (_constants.MODE_AND, "and"):
                return all([type(e) is _decimal.Decimal for e in _many])
            
            else:
                return False
            
            
    @classmethod
    @_extensions.overload
    def isNumber(self, o: _extensions.Any, /) -> _extensions.TypeIs[_numbers.Number]: ...
    
    @classmethod
    @_extensions.overload
    def isNumber(self, o: _extensions.Any, /, *_: _extensions.Any, mode: _Mode = _MODE_AND) -> bool: ...
    
    @classmethod
    def isNumber(self, o, /, *_, mode = _MODE_AND):
        """
        Availability: >= 0.3.41
                
        Returns `True` for any number
        """
        
        # _tuple = (_numbers.Number, _decimal.Decimal, _fractions.Fraction, _tc.Indexable, _tc.IntegerConvertible, _tc.FloatConvertible, _tc.ComplexConvertible, int, float, complex)
        
        if reckon(_) == 0:
            
            return isinstance(o, _numbers.Number)
        
        else:
            
            _many = (o,) + _
            
            if mode in (_constants.MODE_AND, "and"):
                
                return all([isinstance(e, _numbers.Number) for e in _many])
            
            elif mode in (_constants.MODE_OR, "or"):
                
                return any([isinstance(e, _numbers.Number) for e in _many])
            
            else:
                
                return False
    
    class fib(_extensions.NotReassignable):
        """
        Availability: >= 0.3.41 (3rd March 2025) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?miscellaneous_functions
        
        Returns a number from Fibonacci sequence at index `n` before 0.3.54, and since \\
        0.3.54 - generate next Fibonacci sequence numbers up to specified index `n`. If \\
        index not given, generate next numbers endlessly (`itertools`-like).
        
        To retrieve target number at `n` index (if specified), use index `-1` once converting \\
        to a built-in sequence. This number will be at index `n - 1` in Fibonacci sequence, \\
        what means if `n = 13`, then number will be at index 12 in the sequence.
        
        0.3.51: Allow zero. 0 won't appear in the returned generator as first, if `n > 0`. This \\
        is the reason the number at index `-1` is actually at index `n - 1` in Fibonacci \\
        sequence, not at index `n`.
        """
        
        @_extensions.overload
        def __new__(cls, n: None = None, /) -> _FibGenerator[int, _extensions.NoReturn]: ...
        
        @_extensions.overload
        def __new__(cls, n: int, /) -> _FibGenerator[int, None]: ...
        
        def __new__(cls, n = None, /):
            
            if not isinstance(n, (int, _extensions.NoneType)) or (isinstance(n, int) and n < 0):
                error = TypeError("expected integer value above zero or None")
                raise error
            
            if n == 0:
                yield n
                
            n1, n2, _next, i = 0, 1, 1, 1
            
            yield 1
            
            if n is None:
                
                while True:
                    yield _next
                    i += 1
                    n1, n2 = n2, _next
                    _next = n1 + n2
                    
                    
            else:
                
                while i <= n - 2:
                    yield _next
                    i += 1
                    n1, n2 = n2, _next
                    _next = n1 + n2
        
        
    @classmethod
    def fact(self, n: int, /):
        """
        Availability: >= 0.3.26rc3 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?miscellaneous_functions
        ```
        # created 20.08.2024
        ```
        Returns factorial of `n` (`n!`)
        """
        
        # CHANGEOVER 0.3.39
        if not isinstance(n, int) or (isinstance(n, int) and n < 0):
            error = TypeError("expected a non-negative integer")
            raise error
        
        # math.factorial(): since Python 2.6
        if hasattr(_math, "factorial"): 
            return _math.factorial(n)
        
        else:
            
            if n in (0, 1):
                return 1
            
            m, i = 2, 3
            
            # 0.3.41: Do not use 'for' loop in order to bypass limit of 'sys.maxsize'
            while i <= n: 
                m *= i
                i += 1
                
            return m
        
    @classmethod
    def factFalling(self, x: int, n: int, /):
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?miscellaneous_functions
        
        Returns falling factorial of `x` at index `n`
        """
        
        if not isinstance(n, int) or not isinstance(x, int) or (isinstance(n, int) and n < 0):
            error = TypeError("expected a non-negative integer")
            raise error
        
        m, i = x, 1
        
        if n == 0:
            return 1
        
        elif n == 1:
            return x
        
        while i < n:
            m *= (x - i)
            i += 1
        
        return m
        
    @classmethod
    def factRising(self, x: int, n: int, /):
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?miscellaneous_functions
        
        Returns rising factorial of `x` at index `n`
        """
        
        if not isinstance(n, int) or not isinstance(x, int) or (isinstance(n, int) and n < 0):
            error = TypeError("expected a non-negative integer")
            raise error
        
        return int(self.pow(-1, n)) * self.factFalling(-x, n)
    
    if False: # < 0.3.49
        @classmethod
        @_extensions.deprecated("deprecated since 0.3.39, will be removed on 0.3.48")
        def outOfRoot(self, number: int, rootScale: int, /):
            """Since 0.3.?"""
            i = number
            while not isinstance(pow(number, 1/rootScale), int): i -= 1
            return [int(pow(i, 1/rootScale)), number - i]
    
    @classmethod
    def asin(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 (04.07.2024) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?inverse_trigonometric_functions
        
        Returns arc sine of `x` 
        """
        _domain_checker(x, "asin")
        
        return _math.asin(_math.radians(x))
    
    @classmethod
    def acos(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 (04.07.2024) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?inverse_trigonometric_functions
        
        Returns arc cosine of `x`
        """
        _domain_checker(x, "acos")
        
        return _math.acos(_math.radians(x))
    
    @classmethod
    def atan(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 (04.07.2024) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?inverse_trigonometric_functions
        
        Returns arc tangent of `x`. Measured in degrees
        """
        
        return _math.atan(_math.radians(x))
    
    @classmethod
    def acot(self, x: _FloatOrInteger, /):
        """
        @since 0.3.46 (26.05.2025) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?inverse_trigonometric_functions
        
        Returns arc cotangent of `x`, Measured in degrees
        """
        
        return self.PI / 2 - _math.atan(_math.radians(x))
    
    @classmethod
    def asinh(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 (04.07.2024) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?inverse_trigonometric_functions
        
        Returns inverse hyperbolic sine of `x`
        """
        return _math.asinh(_math.radians(x))
    
    @classmethod
    def acosh(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 (04.07.2024) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?inverse_trigonometric_functions
        
        Returns inverse hyperbolic cosine of `x`
        """
        return _math.acosh(_math.radians(x))
    
    @classmethod
    def atanh(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 (04.07.2024) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?inverse_trigonometric_functions
        
        Returns inverse hyperbolic tangent of `x`
        """
        return _math.atanh(_math.radians(x))
    
    @classmethod
    def acoth(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?inverse_trigonometric_functions
        
        Returns inverse hyperbolic cotangent of `x`
        """
        return 1 / self.atanh(x)
    
    @classmethod
    def acosech(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?inverse_trigonometric_functions
        
        Returns inverse hyperbolic cosecant of `x`
        """
        return 1 / self.asinh(x)
    
    @classmethod
    def asech(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?inverse_trigonometric_functions
        
        Returns inverse hyperbolic secant of `x`
        """
        return 1 / self.acosh(x)
    
    @classmethod
    def sin(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 (04.07.2024) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?inverse_trigonometric_functions
        
        Returns sine of `x`
        """
        if not isinstance(x, (int, float)) or x in (self.INF, self.NAN):
            error = TypeError("expected a number")
            raise error
        
        return _math.sin(_math.radians(x))
    
    @classmethod
    def cos(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 (04.07.2024) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?trigonometric_functions
        
        Returns cosine of `x`
        """
        if not isinstance(x, (int, float)) or x in (self.INF, self.NAN):
            error = TypeError("expected a number")
            raise error
        
        return _math.cos(_math.radians(x))
    
    @classmethod
    def tan(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 (04.07.2024) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?trigonometric_functions
        
        Returns tangent of `x`
        """
        if not isinstance(x, (int, float)) or x in (self.INF, self.NAN):
            error = TypeError("expected a number")
            raise error
        
        return _math.tan(_math.radians(x))
    
    @classmethod
    def sinh(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 (04.07.2024) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?hyperbolic_functions
        
        Returns hyperbolic sine of `x`
        """
        if not isinstance(x, (int, float)) or x in (self.INF, self.NAN):
            error = TypeError("expected a number")
            raise error
        
        return _math.sinh(_math.radians(x))
    
    @classmethod
    def cosh(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 (04.07.2024) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?hyperbolic_functions
        
        Returns hyperbolic cosine of `x`
        """
        if not isinstance(x, (int, float)) or x in (self.INF, self.NAN):
            error = TypeError("expected a number")
            raise error
        
        return _math.cosh(_math.radians(x))
    
    @classmethod
    def tanh(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 (04.07.2024) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?hyperbolic_functions
        
        Returns hyperbolic tangent of `x`
        """
        if not isinstance(x, (int, float)) or x in (self.INF, self.NAN):
            error = TypeError("expected a number")
            raise error
        
        return _math.tanh(_math.radians(x))
    
    @classmethod
    def coth(self, x: _FloatOrInteger, /):
        """
        @since 0.3.46 (22.05.2025) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?hyperbolic_functions
        
        Returns hyperbolic cotangent of `x`
        """
        if not isinstance(x, (int, float)) or x in (self.INF, self.NAN):
            error = TypeError("expected a number")
            raise error
        
        return 1 / self.tanh(x)
    
    @classmethod
    def sech(self, x: _FloatOrInteger, /):
        """
        @since 0.3.46 (22.05.2025) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?hyperbolic_functions
        
        Returns hyperbolic secant of `x`
        """
        if not isinstance(x, (int, float)) or x in (self.INF, self.NAN):
            error = TypeError("expected a number")
            raise error
        
        return 1 / self.cosh(x)
    
    @classmethod
    def cosech(self, x: _FloatOrInteger, /):
        """
        @since 0.3.46 (22.05.2025) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?hyperbolic_functions
        
        Returns hyperbolic cosecant of `x`
        """
        if not isinstance(x, (int, float)) or x in (self.INF, self.NAN):
            error = TypeError("expected a number")
            raise error
        
        return 1 / self.sinh(x)
    
    @classmethod
    def cosec(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 (04.07.2024) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?trigonometric_functions
        
        Returns cosecant of `x`. `x` *cannot* be divisible by 90.
        """
        if not isinstance(x, (int, float)) or x in (self.INF, self.NAN) or self.sin(x) == 0:
            error = TypeError("expected a number whose sine isn't equal 0")
            raise error
        
        return 1 / self.sin(x)
    
    @classmethod
    def sec(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 (04.07.2024) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?trigonometric_functions
        
        Returns secant of `x`
        """
        if not isinstance(x, (int, float)) or x in (self.INF, self.NAN) or self.cos(x) == 0:
            error = TypeError("expected a number whose cosine isn't equal 0")
            raise error
        
        return 1 / self.cos(x)
    
    @classmethod
    def acosec(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 (05.07.2024) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?inverse_trigonometric_functions
        
        Returns inverse cosecant of `x`. Equals `asin(1 / x)`.
        """
        _domain_checker(x, "acosec")
        
        return self.asin(1 / x)
    
    @classmethod
    def asec(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 (05.07.2024) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?inverse_trigonometric_functions
        
        Returns inverse secant of `x`. Equals `acos(1 / x)`
        """
        _domain_checker(x, "asec")
        
        return self.acos(1 / x)
    
    @classmethod
    def cot(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 (04.07.2024) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?trigonometric_functions
        
        Returns cotangent of `x`
        """
        if not isinstance(x, (int, float)) or x in (self.INF, self.NAN) or self.tan(x) == 0:
            error = TypeError("expected a number whose tangent isn't equal 0")
            raise error
        
        return 1 / self.tan(x)
    
    @classmethod
    def versin(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 (04.07.2024) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?extended_trigonometric_functions
        
        Returns versed sine of `x`
        """
        return 1 - self.cos(x)
    
    @classmethod
    def coversin(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 (04.07.2024) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?extended_trigonometric_functions
        
        Returns coversed sine of `x`
        """
        return 1 - self.sin(x)
    
    @classmethod
    def vercos(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 (04.07.2024) \\
        @modified 0.3.39 (renamed from `vercosin`) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?extended_trigonometric_functions
        
        Returns versed cosine of `x`
        """
        return 1 + self.cos(x)
    
    @classmethod
    def covercos(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 (04.07.2024) \\
        @modified 0.3.39 (renamed from `covercosin`) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?extended_trigonometric_functions
        
        Returns coversed cosine of `x`
        """
        return 1 + self.sin(x)
    
    @classmethod
    def haversin(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 (04.07.2024) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?extended_trigonometric_functions
        
        Returns haversed sine of `x`
        """
        return self.versin(x) / 2
    
    @classmethod
    def havercos(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 (04.07.2024) \\
        @modified 0.3.39 (renamed from `havercosin`) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?extended_trigonometric_functions
        
        Returns haversed cosine of `x`
        """
        return self.coversin(x) / 2
    
    @classmethod
    def hacoversin(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 (04.07.2024) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?extended_trigonometric_functions
        
        Returns hacoversed sine of `x`
        """
        return self.vercos(x) / 2
    
    @classmethod
    def hacovercos(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 (04.07.2024) \\
        @modified 0.3.39 (renamed from `hacovercos`) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?extended_trigonometric_functions
        
        Returns hacoversed cosine of `x`
        """
        return self.covercos(x) / 2
    
    @classmethod
    def aversin(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 (04.07.2024) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?inverse_trigonometric_functions
        
        Returns inverse versed sine of `x`
        """
        _domain_checker(1 - x, "acos")
        
        return self.acos(1 - x)
    
    @classmethod
    def acoversin(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 (04.07.2024) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?inverse_trigonometric_functions
        
        Returns inverse coversed sine of `x`
        """
        _domain_checker(x - 1, "acos")
        
        return self.acos(x - 1)
    
    @classmethod
    def avercos(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 (04.07.2024) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?inverse_trigonometric_functions
        
        Returns inverse versed cosine of `x`
        """
        if not isinstance(x, (int, float)) or x in (self.INF, self.NAN) and not self.isInRange(x, 0, 2):
            error = TypeError("expected a number in range [0; 2]")
            raise error
        
        return self.asin(1 - x)
    
    @classmethod
    def acovercos(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 (04.07.2025) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?inverse_trigonometric_functions
        
        Returns inverse coversed cosine of `x`
        """
        if not isinstance(x, (int, float)) or x in (self.INF, self.NAN) or not self.isInRange(x, 0, 2):
            error = TypeError("expected a number in range [0; 2]")
            raise error
        
        return self.asin(x - 1)
    
    @classmethod
    def ahaversin(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 (05.07.2024) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?inverse_trigonometric_functions
        
        Returns inverse haversed sine of `x`
        """
        if not isinstance(x, (int, float)) or x in (self.INF, self.NAN) or not self.isInRange(x, 0, 1):
            error = TypeError("expected a number in range [0; 1]")
            raise error
        
        return self.acos(1 - (2 * x))
    
    @classmethod
    def ahavercos(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 (05.07.2024) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?inverse_trigonometric_functions
        
        Returns inverse haversed cosine of `x`
        """
        if not isinstance(x, (int, float)) or x in (self.INF, self.NAN) or not self.isInRange(x, 0, 1):
            error = TypeError("expected a number in range [0; 1]")
            raise error
        
        return self.acos(2 * x - 1)
    
    @classmethod
    def ahacoversin(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 (05.07.2024) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?inverse_trigonometric_functions
        
        Returns inverse hacoversed sine of `x`
        """
        if not isinstance(x, (int, float)) or x in (self.INF, self.NAN) or not self.isInRange(x, 0, 1):
            error = TypeError("expected a number in range [0; 1]")
            raise error
        
        return self.asin(1 - (2 * x))
    
    @classmethod
    def ahacovercos(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 (05.07.2024) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?inverse_trigonometric_functions
        
        Returns inverse hacoversed cosine of `x`
        """
        if not isinstance(x, (int, float)) or x in (self.INF, self.NAN) or not self.isInRange(x, 0, 1):
            error = TypeError("expected a number in range [0; 1]")
            raise error
        
        return self.asin(2 * x - 1)
    
    @classmethod
    def exsec(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 (05.07.2024) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?extended_trigonometric_functions
        
        Returns exsecant (external secant) of `x`
        """
        if not isinstance(x, (int, float)) or x in (self.INF, self.NAN) or self.cos(x) == 0:
            error = TypeError("expected a number whose cosine isn't equal 0")
            raise error
        
        return self.sec(x) - 1
    
    @classmethod
    def excosec(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 (05.07.2024) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?extended_trigonometric_functions
        
        Returns excosecant/coexsecant (external cosecant) of `x`
        """
        if not isinstance(x, (int, float)) or x in (self.INF, self.NAN) or self.sin(x) == 0:
            error = TypeError("expected a number whose sine isn't equal 0")
            raise error
        
        return self.cosec(x) - 1
    
    @classmethod
    def aexsec(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 (05.07.2024) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?inverse_trigonometric_functions
        
        Returns inverse exsecant of `x`
        """
        if not isinstance(x, (int, float)) or x in (self.INF, self.NAN) or self.isInRange(x, -2, 0, "o"):
            error = TypeError("expected a number not in range (-2; 0); values -2 and 0 are allowed")
            raise error
        
        return self.asec(x + 1)
    
    @classmethod
    def aexcosec(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 (05.07.2024) \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?inverse_trigonometric_functions
        
        Returns inverse excosecant of `x`
        """
        if not isinstance(x, (int, float)) or x in (self.INF, self.NAN) or self.isInRange(x, -2, 0, "o"):
            error = TypeError("expected a number not in range (-2; 0); values -2 and 0 are allowed")
            raise error
        
        return self.acosec(x + 1)
    
    @classmethod
    def fma(x: _FloatOrInteger, y: _FloatOrInteger, z: _FloatOrInteger, /):
        """
        Availability: >= 0.3.46
        
        Fused multiply-add operation (support before Python 3.13)
        """
        
        if not all([isinstance(e, (int, float)) for e in [x, y, z]]):
            error = TypeError("expected all parameters integers or floatin-point numbers")
            raise error
        
        if _sys.version_info >= (3, 13):
            return _math.fma(x, y, z)
        else:
            return (x * y) + z
    
    @classmethod
    def log(self, x: _FloatOrInteger, /, base: _OptionalFloatOrInteger = ...): # slash since 0.3.39
        """
        Availability: >= 0.3.25 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.log
        ```
        # created 05.07.2024
        ```
        Logarithm of `x` with specified base. If `base` is omitted, \\
        returned is logarithm of base e.
        """
        if not isinstance(x, (int, float)) or x in (self.INF, self.NAN):
            error = TypeError("expected a number in parameter 'x'")
            raise error
        
        if not isinstance(base, (int, float, _extensions.EllipsisType)):
            error = TypeError("expected a number, 'None' or ellipsis in parameter 'base'")
            raise error
        
        _base = self.E if isinstance(base, _extensions.EllipsisType) else base
        return _math.log(x, _base)
        
    @classmethod
    def log2(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.log
        ```
        # created 05.07.2024
        ```
        Logarithm of `x` with base 2.
        """
        if not isinstance(x, (int, float)) or x in (self.INF, self.NAN):
            error = TypeError("expected a number")
            raise error
        
        return _math.log2(x)
    
    @classmethod
    def log3(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.log
        ```
        # created 05.07.2024
        ```
        Logarithm of `x` with base 3.
        """
        if not isinstance(x, (int, float)) or x in (self.INF, self.NAN):
            error = TypeError("expected a number")
            raise error
        
        return self.log(x, 3)
    
    @classmethod
    def log5(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.log
        ```
        # created 05.07.2024
        ```
        Logarithm of `x` with base 5.
        """
        if not isinstance(x, (int, float)) or x in (self.INF, self.NAN):
            error = TypeError("expected a number")
            raise error
        
        return self.log(x, 5)
    
    @classmethod
    def log7(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.log
        ```
        # created 05.07.2024
        ```
        Logarithm of `x` with base 7.
        """
        if not isinstance(x, (int, float)) or x in (self.INF, self.NAN):
            error = TypeError("expected a number")
            raise error
        
        return self.log(x, 7)
    
    @classmethod
    def ln(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.log
        ```
        # created 05.07.2024
        ```
        Natural logarithm of `x`. That is logarithm with base `e`.
        """
        if not isinstance(x, (int, float)) or x in (self.INF, self.NAN):
            error = TypeError("expected a number")
            raise error
        
        return self.log(x)
    
    @classmethod
    def log10(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.log
        ```
        # created 05.07.2024
        ```
        Logarithm of `x` with base 10.
        """
        if not isinstance(x, (int, float)) or x in (self.INF, self.NAN):
            error = TypeError("expected a number")
            raise error
        
        return _math.log10(x)
    
    @classmethod
    def sqrt(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.sqrt
        ```
        # created 05.07.2024
        ```
        Square root of `x`.
        """
        if not isinstance(x, (int, float)) or x in (self.INF, self.NAN):
            error = TypeError("expected a number not being infinity nor NaN")
            raise error
        
        return _math.sqrt(x)
    
    @classmethod
    def cbrt(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.cbrt
        ```
        # created 05.07.2024
        ```
        Cube root of `x`. To 0.3.26rc2 this method \\
        wouldn't throw an error if used is Python 3.11 \\
        or greater.
        """
        if not isinstance(x, (int, float)) or x in (self.INF, self.NAN):
            error = TypeError("expected a number not being infinity nor NaN")
            raise error
        
        if _sys.version_info >= (3, 11):
            return _math.cbrt(x)
        else:
            return _math.pow(x, (1/3))
        
    @classmethod
    def pow(self, x: _FloatOrInteger, y: _FloatOrInteger, /):
        """
        Availability: >= 0.3.25 \\
        (no doc yet)
        ```
        # created 05.07.2024
        ```
        Equals `x**y`(`x` to the power of `y`).
        """
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)) or any([e in (_math.inf, _math.nan) for e in [x, y]]):
            error = TypeError("both parameters 'x' and 'y' must be numbers not being infinity nor NaN")
            raise error
        
        return _math.pow(x, y)
    
    @classmethod
    def abs(self, x: _extensions.Absolute[_T_fi], /) -> _T_fi:
        """
        https://aveyzan.xyz/aveytense#aveytense.Math.abs
        
        Returns absolute value of a number. \\
        This method is stricter version of `abs()` inbuilt function.
        """
        if not isinstance(x, _extensions.Absolute) or (isinstance(x, _extensions.Absolute) and type(abs(x)) not in (int, float)):
            error = TypeError("expected a number or object of class implementing __abs__ returning either integer or floating-point number")
            raise error
        
        # safety checking, not all __abs__() method implementations return absolute value of a number
        # but it is just in case! abs() function can be manipulated easily with method __abs__()
        return abs(abs(x))

    @classmethod
    def trunc(self, x: _extensions.Truncable[int], /):
        """
        Availability: >= 0.3.25? \\
        (4th March 2025; no doc yet)
        
        Returns an integer from a floating-point number, wiping out the fraction. \\
        This method is stricter version of `math.trunc()` inbuilt function.
        """
        
        if not isinstance(x, _extensions.Truncable) or (isinstance(x, _extensions.Truncable) and type(_math.trunc(x)) is not int):
            error = TypeError("expected a number or object of class implementing __trunc__ returning an integer")
            raise error
        
        # again, safety checking there
        return _math.trunc(_math.trunc(x))
    
    @classmethod
    def triangular(self, n: int, /):
        """
        Availability: >= 0.3.27a4 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Returns triangular number at index `n`
        """
        
        return self.polygonal(n, 3)
    
    @classmethod
    def triangularCentered(self, n: int, /):
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Returns centered triangular number at index `n`
        """
        
        return self.polygonalCentered(n, 3)
    
    @classmethod
    def square(self, n: int, /):
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Returns square number at index `n`
        """
        
        return self.polygonal(n, 4)
    
    @classmethod
    def squareCentered(self, n: int, /):
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Returns centered square number at index `n`
        """
        
        return self.polygonalCentered(n, 4)
    
    @classmethod
    def pentagonal(self, n: int, /):
        """
        Availability: >= 0.3.27a4 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Returns pentagonal number at index `n`
        """
        
        return self.polygonal(n, 5)
    
    @classmethod
    def pentagonalCentered(self, n: int, /):
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Returns centered pentagonal number at index `n`
        """
        
        return self.polygonalCentered(n, 5)
    
    @classmethod
    def hexagonal(self, n: int, /):
        """
        Availability: >= 0.3.27a4 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Returns hexagonal number at index `n`
        """
        
        return self.polygonal(n, 6)
    
    @classmethod
    def hexagonalCentered(self, n: int, /):
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Returns centered hexagonal number at index `n`
        """
        
        return self.polygonalCentered(n, 6)
    
    @classmethod
    def heptagonal(self, n: int, /):
        """
        Availability: >= 0.3.27a4 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Returns heptagonal number at index `n`
        """
        
        return self.polygonal(n, 7)
    
    @classmethod
    def heptagonalCentered(self, n: int, /):
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Returns centered heptagonal number at index `n`
        """
        
        return self.polygonalCentered(n, 7)
    
    @classmethod
    def octagonal(self, n: int, /):
        """
        Availability: >= 0.3.27a4 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Returns octagonal number at index `n`
        """
        
        return self.polygonal(n, 8)
    
    @classmethod
    def octagonalCentered(self, n: int, /):
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Returns centered octagonal number at index `n`
        """
        
        return self.polygonalCentered(n, 8)
    
    @classmethod
    def nonagonal(self, n: int, /):
        """
        Availability: >= 0.3.27a4 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Returns nonagonal number at index `n`
        """
        
        return self.polygonal(n, 9)
    
    @classmethod
    def nonagonalCentered(self, n: int, /):
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Returns centered nonagonal number at index `n`
        """
        
        return self.polygonalCentered(n, 9)
    
    @classmethod
    def decagonal(self, n: int, /):
        """
        Availability: >= 0.3.27a4 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Returns decagonal number at index `n`
        """
        
        return self.polygonal(n, 10)
    
    @classmethod
    def decagonalCentered(self, n: int, /):
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Returns centered decagonal number at index `n`
        """
        
        return self.polygonalCentered(n, 10)
    
    @classmethod
    def hendecagonal(self, n: int, /):
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Returns hendecagonal number at index `n`
        """
        
        return self.polygonal(n, 11)
    
    @classmethod
    def hendecagonalCentered(self, n: int, /):
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Returns centered hendecagonal number at index `n`
        """
        
        return self.polygonalCentered(n, 11)
    
    @classmethod
    def dodecagonal(self, n: int, /):
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Returns dodecagonal number at index `n`
        """
        
        return self.polygonal(n, 12)
    
    @classmethod
    def dodecagonalCentered(self, n: int, /):
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Returns centered dodecagonal number at index `n`
        """
        
        return self.polygonalCentered(n, 12)
    
    @classmethod
    def tridecagonal(self, n: int, /):
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Returns tridecagonal number at index `n`
        """
        
        return self.polygonal(n, 13)
    
    @classmethod
    def tridecagonalCentered(self, n: int, /):
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Returns centered tridecagonal number at index `n`
        """
        
        return self.polygonalCentered(n, 13)
    
    @classmethod
    def star(self, n: int, /):
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Returns star number at index `n`
        """
        if not _figurate_checker(n, n >= 0):
            error = TypeError("expected a positive integer")
            raise error
        
        return 6 * n * (n - 1) + 1
    
    @classmethod
    def pyramidal(self, n: int, s: int, /):
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Return pyramidal number at index `n` of a polygon with `s` sides
        """
        if not _figurate_checker(n, n >= 0) or not _figurate_checker(s, s >= 3):
            error = TypeError("expected a positive integer as first parameter and second parameter equal or greater than 3")
            raise error
        
        return self.triangular(n) * (n * (s - 2) - (s - 5)) // 3
    
    @classmethod
    def polygonal(self, n: int, s: int, /):
        """
        Availability: >= 0.3.27a4 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Returns polygonal number at index `n` with `s` sides
        """
        if not _figurate_checker(n, n >= 0) or not _figurate_checker(s, s >= 3):
            error = TypeError("expected a positive integer as first parameter and second parameter equal or greater than 3")
            raise error
        
        return ((s - 2) * (n ** 2) - (s - 4) * n) // 2
    
    @classmethod
    def polygonalCentered(self, n: int, s: int, /):
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Returns centered polygonal number at index `n` with `s` sides
        """
        
        if not _figurate_checker(n, n >= 0) or not _figurate_checker(s, s >= 3):
            error = TypeError("expected a positive integer as first parameter and second parameter equal or greater than 3")
            raise error
        
        return n if n == 0 else s * n // 2 * (n - 1) + 1
    
    @classmethod
    def tetrahedral(self, n: int, /):
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Returns tetrahedral number at index `n`
        """
        if not _figurate_checker(n, n >= 0):
            error = TypeError("expected a positive integer")
            raise error
        
        return self.factRising(n, 3) // self.fact(3)
    
    @classmethod
    def tetrahedralCentered(self, n: int, /):
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Returns centered tetrahedral number at index `n`
        """
        if not _figurate_checker(n, n >= 0):
            error = TypeError("expected a positive integer")
            raise error
        
        return n if n == 0 else (2 * n - 1) * ((n - 1) ** 2 + n + 2) // 3
    
    @classmethod
    def cube(self, n: int, /):
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Returns cube number at index `n` (equivalent to `n ** 3`)
        """
        
        if not _figurate_checker(n, n >= 0):
            error = TypeError("expected a positive integer")
            raise error
        
        return n ** 3
    
    @classmethod
    def cubeCentered(self, n: int, /):
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Returns centered cube number at index `n`
        """
        if not _figurate_checker(n, n >= 0):
            error = TypeError("expected a positive integer")
            raise error
        
        return n if n == 0 else (2 * n - 1) * ((n - 1) ** 2 + n)
    
    @classmethod
    def pentatope(self, n: int, /):
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Returns pentatope number at index `n`
        """
        if not _figurate_checker(n, n >= 0):
            error = TypeError("expected a positive integer")
            raise error
        
        return self.factRising(n, 4) // self.fact(4)
    
    @classmethod
    def octahedral(self, n: int, /):
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Returns octahedral number at index `n`
        """
        if not _figurate_checker(n, n >= 0):
            error = TypeError("expected a positive integer")
            raise error
        
        return n if n == 0 else n * (2 * (n ** 2) + 1) // 3
    
    @classmethod
    def octahedralCentered(self, n: int, /):
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Returns centered octahedral number at index `n`
        """
        if not _figurate_checker(n, n >= 0):
            error = TypeError("expected a positive integer")
            raise error
        
        return n if n == 0 else (2 * (n - 1) + 1) * (2 * ((n - 1) ** 2) + 2 * (n - 1) + 3) // 3
    
    @classmethod
    def dodecahedral(self, n: int, /):
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Returns centered dodecahedral number at index `n`
        """
        if not _figurate_checker(n, n >= 0):
            error = TypeError("expected a positive integer")
            raise error
        
        return n if n == 0 else n * (3 * n - 1) * (3 * n - 2) // 2
    
    @classmethod
    def dodecahedralCentered(self, n: int, /):
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Returns centered dodecahedral number at index `n`
        """
        if not _figurate_checker(n, n >= 0):
            error = TypeError("expected a positive integer")
            raise error
        
        return n if n == 0 else (2 * (n - 1) + 1) * (5 * ((n - 1) ** 2) + 5 * (n - 1) + 1)
    
    @classmethod
    def icosahedral(self, n: int, /):
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Returns icosahedral number at index `n`
        """
        if not _figurate_checker(n, n >= 0):
            error = TypeError("expected a positive integer")
            raise error
        
        return n if n == 0 else n * (5 * (n ** 2) - 5 * n + 2) // 2
    
    @classmethod
    def icosahedralCentered(self, n: int, /):
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Returns centered icosahedral number at index `n`
        """
        if not _figurate_checker(n, n >= 0):
            error = TypeError("expected a positive integer")
            raise error
        
        return n if n == 0 else (2 * (n - 1) + 1) * (5 * ((n - 1) ** 2) + 5 * (n - 1) + 3) // 3
    
    @classmethod
    def pronic(self, n: int, /):
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Returns pronic number at index `n`
        """
        
        if not _figurate_checker(n, n >= 0):
            error = TypeError("expected a positive integer")
            raise error
        
        return n * (n + 1)
    
    @classmethod
    def stellaOctangula(self, n: int, /):
        """
        Availability: >= 0.3.51 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.?figurate_number_functions
        
        Returns stella octangula number at index `n`
        """
        if not _figurate_checker(n, n >= 0):
            error = TypeError("expected a positive integer")
            raise error
        
        return n * (2 * (n ** 2) - 1)
    
    @classmethod
    def diagonals(self, s: int, /, distinct = False):
        """
        Availability: >= 0.3.41 \\
        (6th March 2025; no doc yet)
        
        Return amount of diagonals in an equilateral polygon with defined amount of sides.
        """
        if not _figurate_checker(s, s >= 3):
            error = TypeError("expected an integer equal or greater than 3")
            raise error
        
        if distinct: # about distinct: https://en.wikipedia.org/wiki/Diagonal
            return (s - 2) // 2
        
        else:
            return (s * (s - 3)) // 2
    
    @classmethod
    def lcm(self, *i: int):
        """
        Availability: >= 0.3.31 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.lcm
        
        Return least common multiple of provided integers
        """
        
        if _reckon_init(i) < 2 or (_reckon_init(i) >= 2 and not all([type(e) is int and not self.isNegative(e) for e in i])):
            error = ValueError("expected at least 2 non-negative integers")
            raise error
        
        if _sys.version_info >= (3, 9):
            return _math.lcm(*i)
        
        else:
            from functools import reduce # >= 2.6
            
            def _gcd(a: int, b: int):
                
                while b:      
                    a, b = b, a % b
                return a
            
            def _lcm(a: int, b: int):
                return a * b // _gcd(a, b)
            
            return reduce(_lcm, i)
        
    @classmethod
    def gcd(self, *i: int):
        """
        Availability: >= 0.3.31 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.gcd
        
        Return greatest common divisor of provided integers
        """
        
        if _reckon_init(i) < 2 or (_reckon_init(i) >= 2 and not all([type(e) is int and not self.isNegative(e) for e in i])):
            error = ValueError("expected at least 2 non-negative integers")
            raise error
        
        if _sys.version_info >= (3, 9):
            return _math.gcd(*i)
        
        else:
            from functools import reduce # >= 2.6
            
            def _gcd(a: int, b: int):
                
                while b:
                    a, b = b, a % b
                return a
            
            return reduce(_gcd, i)
        
    @classmethod
    def toDigits(self, n: int, /):
        """
        Availability: >= 0.3.39 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.toDigits
        
        Splits an integer to a digit list.
        """
        
        if not isinstance(n, int):
            error = TypeError("expected an integer")
            raise error
        
        if self.abs(n) < 10:
            return [self.abs(n)]
        
        return [int(c, base = 10) for c in str(self.abs(n))]
        
    @classmethod
    def minDigit(self, n: int, /):
        """
        Availability: >= 0.3.39 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.minDigit
        
        Returns minimum digit in a number. Sign isn't counted.
        """
        
        if not isinstance(n, int):
            error = TypeError("expected an integer")
            raise error
        
        if self.abs(n) < 10:
            return self.abs(n)
        
        return min(self.toDigits(n))
    
    
    @classmethod
    def maxDigit(self, n: int, /):
        """
        Availability: >= 0.3.39 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.maxDigit
        
        Returns maximum digit in a number. Sign isn't counted.
        """
        
        if not isinstance(n, int):
            error = TypeError("expected an integer")
            raise error
        
        if self.abs(n) < 10:
            return self.abs(n)
        
        return max(self.toDigits(n))
            

    @classmethod
    def lwdp(self, n: int, /):
        """
        Availability: >= 0.3.39 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.lwdp
        
        Return number *least with digit product* of `n`. To be more explanatory, this method returns a number, which \\
        digits create `n` via multiply operation, e.g. for `n` equal 18, method would return 29, because: 2 * 9 = 18.
        
        If this class method cannot find smallest number with digit product of `n`, it will return -1.
        
        """
        if not isinstance(n, int):
            error = TypeError("expected a non-negative integer")
            raise error
        
        r, m, b, i = 0, 1, self.abs(n), 9
        
        while i > 1: # 0.3.41: changed loop
            
            while b % i == 0:
                
                r += m * i
                m *= 10
                b //= i
                
            i -= 1
        
        if m == 10:
            r += 10
            
        return r if b == 1 else -1
    
    @classmethod
    def perm(self, n: int, k: _OptionalInteger = ..., /): # <- slash since 0.3.40
        """
        Availability: >= 0.3.39 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.perm
        
        Formula `n! / (n - k)!`
        """
        
        if not isinstance(n, int):
            error = TypeError("expected an integer in first parameter")
            raise error
        
        if not isinstance(k, (int, _extensions.EllipsisType)):
            error = TypeError("expected an integer, None or ellipsis in second parameter")
            raise error
        
        if isinstance(k, _extensions.EllipsisType):
            return self.fact(n)
        
        else:
            return int(self.fact(n) / (self.fact(k) * self.fact(n - k)) * self.fact(k))
        
    @classmethod
    def mean(self, *n: _FloatOrInteger, mode = "a"):
        """
        Availability: >= 0.3.40 \\
        https://aveyzan.xyz/aveytense#aveytense.Math.mean
        
        - 0.3.41: Floating-point numbers are now allowed
        """
        
        if _reckon_init(n) == 0:
            error = TypeError("expected at least one value")
            raise error
        
        if type(mode) is not str:
            error = TypeError("expected a string in parameter 'mode'")
            raise error
        
        _mode = mode.lower()
        
        if _mode not in ("a", "g", "q", "h"):
            error = TypeError("expected a string value in parameter 'mode' from following: 'a', 'g', 'h' and 'q'")
            raise error
        
        for e in n:
            
            if type(e) not in (int, float) or e in (self.INF, self.NAN) or (_mode == "a" and self.isNegative(e)):
                error = TypeError("expected all values as numbers not being infinity nor NaN; for geometric mean - non-negative numbers only")
                raise error
            
        r = 0
        
        import statistics
        
        if _mode == "a":
            
            if hasattr(statistics, "mean"):
                return statistics.mean(n)
            
            for e in n:
                r += e
                
            return r / _reckon_init(n)
        
        elif _mode == "g":
            
            if hasattr(statistics, "geometric_mean"):
                return statistics.geometric_mean(n)
            
            r = 1
            
            for e in n:
                r *= e
                
            return self.pow(r, (1 / _reckon_init(n)))
        
        # 0.3.41
        elif _mode == "h":
            
            if hasattr(statistics, "harmonic_mean"):
                return statistics.harmonic_mean(n)
            
            r = .0
            
            for e in n:
                
                if e == 0:
                    error = ZeroDivisionError("one of numbers equals zero")
                    raise error
                
                r += 1 / e
                
            return _reckon_init(n) / r
            
        
        else: # root mean square (rms)
            
            for e in n:
                r += e ** 2
                
            return self.sqrt(r / _reckon_init(n))
        
        
    @classmethod
    def stdev(self, *i: int):
        """
        Availability: >= 0.3.41
                
        Returns standard deviation of all given integers.
        """
        
        if _reckon_init(i) == 0:
            error = TypeError("expected at least one value")
            raise error
        
        for e in i:
            
            if type(e) is not int:
                error = TypeError("expected all values as integers")
                raise error
        
        import statistics
        
        if hasattr(statistics, "stdev"):
            return statistics.stdev(i)
        
        _mean = self.mean(*i, mode = "a")
        _res = .0
        
        for e in i:
            _res += (e - _mean) ** 2
            
        return self.sqrt(_res / _reckon_init(i))
    
    @classmethod
    def toScientific(self, x: _FloatOrInteger, /, precision = 20, roundUp = False):
        """
        Availability: >= 0.3.57
        
        Returns scientific notation of a number.
        
        Max value for `precision` is 4284 to comply with 4300 digit integer limit; default value is
        20. Zero removes the fractional part. Minus one refers to amount of digits in fraction of the number minus one.
        
        `roundUp`, if set to `True`, rounds up the rightmost digit specified by `precision`, if digit on the right of it
        was equal or greater than 6. This parameter has no effect, if value for `precision` is equal -1, or equal or greater
        than amount of digits minus one.
        """
        
        if not isinstance(x, (int, float)):
            error = TypeError("expected a numeric string or a number")
            raise error
        
        if not isinstance(precision, int) or (isinstance(precision, int) and not self.isInRange(precision, -1, 4284)):
            error = ValueError("parameter 'precision' can have integer value in range [-1; 4284]")
            raise error
            
        s = str(x).lstrip("-")
        _sign = "-" if str(x) != s else ""
        
        # inbuilt function round() uses rounding up when the digit on the right of a digit is above or equal 6
        _round = lambda x = 0: 1 if roundUp and x >= 6 else 0
        
        if isinstance(x, int):
            
            # Normally, we would...
            ###
            # s = str(x)
            # _max = precision if _reckon_init(s) - 1 > precision else _reckon_init(s) - 1
            # return ("{" + f":.{_max}e" + "}").format(x)
            ###
            # ...but precision isn't fully accurate. We would need to get the first digit
            # from the number manually first.
            
            if _reckon_init(s) == 1:
                return s + "e+0"
            
            a = s.lstrip("-") # remove minus and deduce it later
            l = _reckon_init(a) - 1
            
            if precision == -1 or precision >= l:
                return f"{_sign}{a[0]}.{a[1:]}e+{l}"
            elif precision == 0:
                return _sign + str(int(a[0]) + _round(int(a[1]))).rstrip("0") + f"e+{l}"
            else:
                return f"{_sign}{a[0]}." + str(int(a[1 : precision + 1]) + _round(int(a[precision + 1]))).rstrip("0") + f"e+{l}"
                
        else:
            
            # Floating-point number will be more difficult and will require more developed version of the code with integer.
            # To faciliate work, we will get integral part of the number, and get its fractional part separatedly. Unfortunately
            # in case of precision this will be restricted
            
            i, f = s.split(".") # 'integral', 'fraction'
            z = f.rstrip("0")
            
            if int(i) == 0:
                l = _reckon_init(f) - _reckon_init(z) + 2
            else:
                l = _reckon_init(i) - 1
            
            if self.isScientific(s):
                
                if "e-" in f:
                    e = "e-"
                else:
                    e = "e+"
                    
                e2 = f.split(e)
                
                if precision == 0:
                    return (_sign + str(int(i[0]) + _round(int(f[0])))).rstrip("0") + e + e2[1]
                elif precision == -1 or precision >= l:
                    return (_sign + i[0] + "." + i[1:] + str(int(e2[0][: precision + 1]) + _round(int(e2[0][precision + 1])))).rstrip("0") + e + e2[1]
                else:
                    return (_sign + i[0] + "." + str(int(e2[0][: precision + 1]) + _round(int(e2[0][precision + 1])))).rstrip("0") + e + e2[1]
            
            if int(i) == 0:
                
                # Section with e-N. Fractional part is dominant
                
                z2 = _reckon_init(f) - _reckon_init(z) + 2
                
                if precision == 0:
                    return (_sign + str(int(z[0]) + _round(int(z[1])))).rstrip("0") + f"e-{z2}"
                elif precision == -1 or precision >= l:
                    return (_sign + z[0] + z[1:]).rstrip("0") + f"e-{z2}"
                else:
                    return (_sign + z[0] + "." + str(int(z[1 : precision + 1]) + _round(int(z[precision + 1])))).rstrip("0") + f"e-{z2}"
                    
            else: # > 0
                
                # Section with e+N. There integral part is dominant
                
                _i_exponent_ = _reckon_init(i) - 1
                _d_zeros_ = _reckon_init(f) - _reckon_init(f.lstrip("0"))
                
                if precision == -1 or precision >= l:
                    return f"{_sign}{i[0]}.{i[1:] + f}".rstrip("0") + f"e+{_i_exponent_}"
                elif precision == 0:
                    return (f"{_sign}{i[0]}.{i[1:] + f[:_d_zeros_]}" + str(int(f[_d_zeros_]) + _round(int(f[_d_zeros_ + 1])))).rstrip("0") + f"e+{_i_exponent_}"
                else:
                    return (f"{_sign}{i[0]}.{i[1:] + f[:_d_zeros_]}" + str(int(f[_d_zeros_ : precision + 1]) + _round(int(f[precision + 1])))).rstrip("0") + f"e+{_i_exponent_}"
        
    @classmethod
    def toRadians(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.41
                
        Returns angle in radians notation. Formula: `x*(π/180)`
        """
        
        if type(x) not in (int, float) or x in (self.NAN, self.INF):
            error = TypeError("expected a number not being infinity nor NaN")
            raise error
        
        if hasattr(_math, "radians"):
            return _math.radians(x)
        
        return x * (float(self.PI) / 180)
        
    @classmethod
    def toDegrees(self, x: _FloatOrInteger, /):
        """
        Availability: >= 0.3.41
                
        Returns radians to angle notation. Formula: `x*(180/π)`
        """
        
        if type(x) not in (int, float) or x in (self.NAN, self.INF):
            error = TypeError("expected a number not being infinity nor NaN")
            raise error
        
        if hasattr(_math, "degrees"):
            return _math.degrees(x)
        
        return x * (180 / float(self.PI))
    
    @classmethod
    def toGradians(cls, x: _FloatOrInteger, /, n = "r"):
        """
        Availability: >= 0.3.41
                
        Returns radians/degrees to gradians notation.
        """
        if type(x) not in (int, float) or x in (cls.NAN, cls.INF):
            error = TypeError("expected a number not being infinity nor NaN")
            raise error
        
        if n.lower() not in ("r", "d"):
            error = TypeError("expected 'r' or 'd' in parameter 'n'")
            raise error
        
        if n.lower() == "r":
            return x * (float(cls.PI) / 200)
        
        else:
            return x * (9 / 10)
        
    @classmethod
    def addPercentage(cls, x: _FloatOrInteger, percentage: str, /):
        """
        Availability: >= 0.3.68
        
        Adds `x` and its `percentage` together and returns the result.
        
        - `x` - any integer or floating-point number.
        - `percentage` - a numeric string with ending percentage character. Examples: `"18％"`, `"-23％"`, `"62.4％"`, `"-189.36％"`
        
        ```
        Math.addPercentage(20, "15%") # 23.0
        ```
        """
        
        # NOTE: ignore the VSC note about percent character confusion, because sometimes '%' can entirely
        # disappear from the documentation when hovering on an object to review it. Using '％' (U+FF05) to
        # prevent this from happening. Despite the 'help()' function displays the docstring correctly, the
        # '%' sign may not appear in VSC upon hovering.
        
        cls.toGradians(x)
        
        import re
        
        # only one match needed, otherwise it will bind with more lines of the code
        # without 're', the lines of the code will differ, it would be like:
        # -----
        # allowed = "- . % 0 1 2 3 4 5 6 7 8 9".split(" ") ## avoid re-invocation
        # ...
        # isinstance(percentage, str) and (
        #   any([c not in allowed for c in percentage]) or
        #   ("-" in percentage and (not percentage.startswith("-") or percentage.count("-") > 1)) or
        #   ("." in percentage and ((percentage.startswith(".") or percentage.endswith(".") or percentage.index(".") + 1 == percentage.index("%")) or percentage.count(".") > 1)) or
        #   ("%" in percentage and (not percentage.endswith("%") or percentage.count("%") != 0))
        # )
        # -----
        # 'str.isnumeric()' would work here instead of the 'not in' statement in the list comprehension
        # notation, but we also need to impose another requirement bound with ASCII compatibility, that is
        # 'str.isascii()'
        # 21.03.2026
        if not isinstance(percentage, str) or (isinstance(percentage, str) and re.match(r"(-?[0-9]+(\.[0-9]+)?%){1}", percentage) is None):
            error = TypeError("invalid string literal, expected a number string ending with '%'")
            raise error
        
        # remove all whitespaces around then remove the percent sign to properly convert
        # it to a float object, then divide the value by 100 (because 1 = 100%), minus sign
        # allowed and will reverse the plus sign
        return x + (x * (float(percentage.strip().strip("%")) / 100))
        
    __all__ = sorted([n for n in locals() if n[:1] != "_"]) # 0.3.41: sorted()
    "Availability: >= 0.3.25"
    __dir__ = lambda self: __all__
    "Availability: >= 0.3.25"

__all__ = sorted([n for n in globals() if n[:1] != "_"])
__dir__ = __all__

if __name__ == "__main__":
    error = RuntimeError("Import-only module")
    raise error