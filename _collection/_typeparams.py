"""
Availability: >= 0.3.72 \\
© 2024-Present Aveyzan // License: MIT

Type parameters. Not in use in public scope; use these accessible via the `aveytense.extensions` module instead.
"""

from __future__ import annotations
import subprocess
import sys

# These lines of the code below must be invoked everytime when next AveyTense versions are being
# uploaded due to an error stating that there is no 'pip' module. This is apparently due to 'build'
# PyPi project creating a temporary venv which only gets 'setuptools' (>= 40.8.0; for instance I had
# 80.9.0 while writing this), and AveyTense uses 'typing_extensions' as well. Looks like the only way
# to get 'pip' for this venv is running 'py -m ensurepip', since this tool is inbuilt and doesn't
# require 'pip'. This error occurred while preparing to upload version 0.3.64. The scrap of the code
# below will be kept unless 'build' PyPi project contributors manage to mend this issue.
#
# These lines of the code are placeholders and designed to be never invoked by users normally, this
# scrap of the code is only for sending next project releases to PyPi.
# - 24.01.2026
try:
    import pip # this must throw an error
    del pip
except ModuleNotFoundError:
    subprocess.run([sys.executable] + "-m ensurepip".split(" "))
    subprocess.run([sys.executable] + "-m pip install --upgrade pip".split(" ")) 
    subprocess.run([sys.executable] + "-m pip install typing_extensions".split(" "))

import typing_extensions
from typing_extensions import (
    # 'default' parameter availability...
    ParamSpec, # TE>=4.4.0, AV>=0.3.26rc1
    TypeVar, # TE>=4.4.0, AV>=0.3.26b3
    TypeVarTuple # TE>=4.4.0, AV>=0.3.26rc3
)

# You might want to actually make your own TypeVar/ParamSpec/TypeVarTuple instances.
# Use these below at your own risk as these aren't intentionally made for export. However,
# one thing is certain that 'T', 'Ts' and 'P' will be cemented as public exports, so feel
# free to use these three!
S = TypeVar("S")
S_con = TypeVar("S_con", contravariant = True)
S_cov = TypeVar("S_cov", covariant = True)
T = TypeVar("T") # public, stable
T_con = TypeVar("T_con", contravariant = True)
T_cov = TypeVar("T_cov", covariant = True)
U = TypeVar("U")
U_con = TypeVar("U_con", contravariant = True)
U_cov = TypeVar("U_cov", covariant = True)

KT = TypeVar("KT")
KT_con = TypeVar("KT_con", contravariant = True)
KT_cov = TypeVar("KT_cov", covariant = True)
VT = TypeVar("VT")
VT_con = TypeVar("VT_con", contravariant = True)
VT_cov = TypeVar("VT_cov", covariant = True)

KT1 = TypeVar("KT1")
KT1_con = TypeVar("KT1_con", contravariant = True)
KT1_cov = TypeVar("KT1_cov", covariant = True)
KT2 = TypeVar("KT2")
KT2_con = TypeVar("KT2_con", contravariant = True)
KT2_cov = TypeVar("KT2_cov", covariant = True)
VT1 = TypeVar("VT1")
VT1_con = TypeVar("VT1_con", contravariant = True)
VT1_cov = TypeVar("VT1_cov", covariant = True)
VT2 = TypeVar("VT2")
VT2_con = TypeVar("VT2_con", contravariant = True)
VT2_cov = TypeVar("VT2_cov", covariant = True)

T1 = TypeVar("T1")
T1_con = TypeVar("T1_con", contravariant = True)
T1_cov = TypeVar("T1_cov", covariant = True)
T2 = TypeVar("T2")
T2_con = TypeVar("T2_con", contravariant = True)
T2_cov = TypeVar("T2_cov", covariant = True)
T3 = TypeVar("T3")
T3_con = TypeVar("T3_con", contravariant = True)
T3_cov = TypeVar("T3_cov", covariant = True)
T4 = TypeVar("T4")
T4_con = TypeVar("T4_con", contravariant = True)
T4_cov = TypeVar("T4_cov", covariant = True)
T5 = TypeVar("T5")
T5_con = TypeVar("T5_con", contravariant = True)
T5_cov = TypeVar("T5_cov", covariant = True)
T6 = TypeVar("T6")
T6_con = TypeVar("T6_con", contravariant = True)
T6_cov = TypeVar("T6_cov", covariant = True)
# ...
Ts = TypeVarTuple("Ts") # public, stable
P = ParamSpec("P") # public, stable

AnyStr = TypeVar("AnyStr", str, bytes) # public, stable
"""Availability: >= ? // https://aveyzan.xyz/aveytense#aveytense.extensions.AnyStr"""

AnyStr_cov = TypeVar("AnyStr_cov", str, bytes, covariant = True)

# definitely NOT for export.
T_array = TypeVar("T_array", int, float, str) # array.array
T_memoryview = TypeVar("T_memoryview", default = int) # memoryview
T_count = TypeVar("T_count", int, float, typing_extensions.SupportsFloat, typing_extensions.SupportsInt, typing_extensions.SupportsIndex, typing_extensions.SupportsComplex) # itertools.count
T_yield_cov = TypeVar("T_yield_cov", covariant = True) # Generator, Coroutine
T_send_con = TypeVar("T_send_cov", contravariant = True, default = None) # Generator -> CoroutineWrapperType
T_return_cov = TypeVar("T_return_cov", covariant = True, default = None) # Generator -> CoroutineWrapperType
T_send_noDefault_con = TypeVar("T_send_noDefault_con", contravariant = True) # Coroutine
T_return_noDefault_cov = TypeVar("T_return_noDefault_cov", covariant = True) # Coroutine
T_start_cov = TypeVar("T_start_cov", covariant = True, default = typing_extensions.Any) # slice
T_stop_cov = TypeVar("T_stop_cov", covariant = True, default = T_start_cov) # slice
T_step_cov = TypeVar("T_step_cov", covariant = True, default = typing_extensions.Union[T_start_cov, T_stop_cov]) # slice