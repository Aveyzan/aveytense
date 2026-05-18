"""
Availability: >= 0.3.35 \\
© 2024-Present Aveyzan // License: MIT

Core of `aveytense.constants`; use `aveytense.constants` instead
"""

from __future__ import annotations
from . import _extensions as __
    
class ModeSelection(__.Enum):
    "Availability: >= 0.3.36"
    
    AND = 0
    OR = 1
    
if __name__ == "__main__":
    error = RuntimeError("Import-only module")
    raise error