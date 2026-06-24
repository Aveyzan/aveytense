"""
Availability: >= 0.3.44 \\
© 2024-Present Aveyzan // License: MIT

This module contains definitions accessible via `aveytense` module. Do NOT use it for importing modules!

Instead consider:
- `aveytense.constants` instead of `~._constants`
- `aveytense` instead of `~._abroad` and `~._primal`
- `aveytense.util` instead of `~._util`
- `aveytense.extensions` instead of `~._extensions`
"""

def _prevent_unused_definitions(*_): pass

# >= 0.3.74
_ReprStr = "<object of '{}' with id '{}'>"

# >= 0.3.75
# Used with object.__setattr__() for frozen dataclasses
_mangle = lambda self, attr = "": "_{}".format(type(self).__name__) + attr

class _Missing: ... # >= 0.3.75

class _Immutable: # >= 0.3.75
    
    def __init_subclass__(cls, *args, **kwds):
        
        # keep it simple
        def _no_modify(self, name, value):
            if name in self.__dict__:
                error = AttributeError(f"Cannot set a new value to attribute '{name}'")
                raise error
            
        def _no_delete(self, name):
            if name in self.__dict__:
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

_prevent_unused_definitions(_ReprStr, _mangle, _Missing, _Final, _Immutable)