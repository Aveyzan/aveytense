"""
**AveyTense Extensions**

Availability: >= 0.3.26b3 \\
© 2024-Present Aveyzan // License: MIT \\
https://aveyzan.xyz/aveytense#aveytense.extensions

Similarly as `typing_extensions`, this module provides backports for Python types,
functions, classes and ABCs (especially generic).

This module occurred in many names:

- `aveytense.tcs` to 0.3.26rc2
- `aveytense.types_collection` during 0.3.26rc3 - 0.3.51
- `aveytense.types` during 0.3.52 - 0.3.56

Constants have been moved to separate submodule `aveytense.constants`.
"""

from __future__ import annotations
from ._collection import _extensions
from ._collection._extensions import *
from ._collection._extensions import __all__

def __getattr__(attr):
    
    import warnings
    
    if attr in "UUID Uuid".split(" "):
        warnings.warn(f"Importing '{attr}' from 'aveytense.extensions' is deprecated since 0.3.85, and this definition will be removed in 0.3.90. " +
                      "Consider importing it from inbuilt Python library 'uuid' instead", DeprecationWarning)

if __name__ == "__main__":
    error = RuntimeError("Import-only module")
    raise error
