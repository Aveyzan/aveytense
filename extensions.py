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
from ._collection._extensions import *
from ._collection._extensions import __all__

def __getattr__(attr):
    
    import warnings
    
    if attr in "AST Expression Module Interactive".split(" "):
        warnings.warn(f"Importing '{attr}' from 'aveytense.extensions' is deprecated since 0.3.81, and this definition will be removed in 0.3.84. " +
                      "Consider importing it from inbuilt Python library 'ast' instead", DeprecationWarning)
    
    elif attr in "ArgInfo Arguments Attribute BlockFinder BoundArguments ClosureVars FrameInfo FullArgSpec Parameter Signature Traceback".split(" "):
        warnings.warn(f"Importing '{attr}' from 'aveytense.extensions' is deprecated since 0.3.81, and this definition will be removed in 0.3.84. " +
                      "Consider importing it from inbuilt Python library 'inspect' instead", DeprecationWarning)
        
    elif attr in ("AsyncExitOperable AsyncEnterOperable AsyncNextOperable ExitOperable EnterOperable NextOperable ItemGetter ClassItemGetter SizeableItemGetter " +
                  "ItemSetter ItemDeleter ItemManager Getter Setter Deleter Descriptor KeysProvider ItemsProvider BufferReleaser SubclassHooker LengthHintProvider " +
                  "BytearrayConvertible Absolute Truncable BooleanConvertible IntegerConvertible FloatConvertible ComplexConvertible BytesConvertible " +
                  "BinaryRepresentable OctalRepresentable HexadecimalRepresentable Indexable Positive Negative Invertible LeastComparable GreaterComparable " +
                  "LeastEqualComparable GreaterEqualComparable BitwiseAndOperable BitwiseOrOperable BitwiseXorOperable BitwiseLeftOperable BitwiseRightOperable " +
                  "BitwiseOperable ReflectedBitwiseAndOperable ReflectedBitwiseOrOperable ReflectedBitwiseXorOperable ReflectedBitwiseLeftOperable " +
                  "ReflectedBitwiseRightOperable ReflectedBitwiseOperable BitwiseAndReassignable BitwiseOrReassignable BitwiseXorReassignable " +
                  "BitwiseLeftReassignable BitwiseRightReassignable BitwiseReassignable BitwiseCollection UnaryOperable Ceilable CeilOperable " +
                  "Floorable FloorOperable Roundable RoundOperable AdditionOperable SubstractionOperable MultiplicationOperable MatrixMultiplicationOperable " +
                  "TrueDivisionOperable FloorDivisionOperable DivmodOperable ModuleOperable ExponentationOperable ReflectedAdditionOperable " +
                  "ReflectedSubtractionOperable ReflectedMultiplicationOperable ReflectedMatrixMultiplicationOperable ReflectedTrueDivisionOperable " +
                  "ReflectedFloorDivisionOperable ReflectedDivmodOperable ReflectedModuloOperable ReflectedExponentationOperable AdditionReassignable " +
                  "SubtractionReassignable MultiplicationReassignable MatrixMultiplicationReassignable TrueDivisionReassignable FloorDivisionReassignable " +
                  "ModuloReassignable ExponentationReassignable ReflectedArithmeticOperable ArithmeticOperable ArithmeticReassignable ArithmeticCollection " +
                  "LenGetItemOperable FilenoProvider Copyable Copyable2 DeepCopyable DeepCopyable2 Allocator Clearable ViewableItemGetter").split(" "):
        warnings.warn(f"Importing '{attr}' from 'aveytense.extensions' is deprecated since 0.3.81, and this definitions will be removed in 0.3.84. " +
                      "Consider importing its equivalent with the 'Supports-' prefix on its name.", DeprecationWarning)

if __name__ == "__main__":
    error = RuntimeError("Import-only module")
    raise error
