"""
Availability: >= 0.3.44 \\
© 2024-Present Aveyzan // License: MIT

This module contains definitions accessible via `aveytense` module. Do NOT use it for importing modules; you are also discouraged to import this module itself.

Instead consider:
- `aveytense.constants` instead of `~._constants`
- `aveytense` instead of `~._primal`
- `aveytense.util` instead of `~._util`
- `aveytense.extensions` instead of `~._extensions`
"""

def _prevent_unused_definitions(*_): pass


_ReprStr = "<object of '{}' with id '{}'>" # >= 0.3.74

# Used with object.__setattr__() for frozen dataclasses
_mangle = lambda self, attr = "": "_{}".format(type(self).__name__) + attr # >= 0.3.75


def _is_sequence_like(x): # >= 0.3.76
    
    import collections.abc
    return isinstance(x, (collections.abc.Sequence, collections.abc.Set, collections.abc.ValuesView)) and not isinstance(x, collections.abc.Mapping)

class _SelfInvoke: # >= 0.3.76
    
    def __new__(cls):
        return cls

class _Immutable: # >= 0.3.75
    
    def __init_subclass__(cls, *args, **kwds):
        
        # keep it simple
        def _no_modify(self, name, value):
            if hasattr(self, name):
                error = AttributeError(f"Cannot set a new value to attribute '{name}'")
                raise error
            
        def _no_delete(self, name):
            if hasattr(self, name):
                error = AttributeError(f"Cannot delete attribute '{name}'")
                raise error
            
        cls.__setattr__ = _no_modify
        cls.__delattr__ = _no_delete
        
class _Final: # >= 0.3.75
    
    def __init_subclass__(cls, *args, **kwds):
        
        def _no_subclass(cls, *args, **kwds):
            from ..exceptions import SubclassedError
            
            error = SubclassedError(f"Cannot subclass final class '{cls.__name__}'")
            raise error
        
        cls.__init_subclass__ = _no_subclass
        
def _sentinel(name: str, /, module = ""): # >= 0.3.76
    
    class _(type):
        
        def __str__(self):
            return "<sentinel '{}'>".format(".".join([module, name]).lstrip("."))
        
        def __repr__(self):
            return self.__str__()
        
        def repr(self):
            """Availability: >= 0.3.81"""
            return "<sentinel '{}' id '{}'>".format(".".join([module, name]).lstrip("."), id(self))
    
    # safer to do this way instead of 'exec()'
    # for the 'type' constructor with 3 parameters it does NOT work with metaclasses.
    class Sentinel(_Final, _SelfInvoke, metaclass=_):
        
        __name__ = name
        __module__ = module if module else "__main__"
        __qualname__ = ".".join([module if module else "__main__", name]).lstrip(".")
    
    return Sentinel

# make it more human-readable for 0.3.76
_Missing = _sentinel("_Missing") # >= 0.3.75

_prevent_unused_definitions(_ReprStr, _mangle, _sentinel, _is_sequence_like, _Missing, _Final, _Immutable, _SelfInvoke)