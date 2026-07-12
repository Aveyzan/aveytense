"""
**AveyTense Exceptions**

Availability: >= 0.3.27a1 \\
© 2024-Present Aveyzan // License: MIT \\
https://aveyzan.xyz/aveytense#aveytense.exceptions

Exception classes for AveyTense. Used in any scope modules scattered around the project. \\
Globally accessible since 0.3.44.
"""
class MissingValueError(ValueError):
    """
    Availability: >= 0.3.19 \\
    https://aveyzan.xyz/aveytense#aveytense.exceptions.MissingValueError
    
    Missing value (empty parameter).
    
    Usually not thrown at all, common cause is lacking values in probability methods from class `aveytense.Tense`
    """
    ...
class IncorrectValueError(ValueError):
    """
    Availability: >= 0.3.19 \\
    https://aveyzan.xyz/aveytense#aveytense.exceptions.IncorrectValueError
    
    Incorrect value of a parameter, having correct type.
    
    Mostly replaced by `TypeError` inbuilt exception.
    """
    ...
class NotInitializedError(Exception):
    """
    Availability: >= 0.3.25 \\
    https://aveyzan.xyz/aveytense#aveytense.exceptions.NotInitializedError
    
    Class was not instantiated
    """
    ...
class InitializedError(Exception):
    """
    Availability: >= 0.3.26b3 \\
    https://aveyzan.xyz/aveytense#aveytense.exceptions.InitializedError
    
    Class was instantiated.
    
    This exception is thrown by definitions with the 'abstract' word in their names in the `aveytense.util` module.
    """
    ...
class NotReassignableError(Exception):
    """
    Availability: >= 0.3.26b3 \\
    https://aveyzan.xyz/aveytense#aveytense.exceptions.NotReassignableError
    
    Attempt to re-assign a value
    """
    ...
class NotComparableError(Exception):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.exceptions.NotComparableError
    
    Attempt to compare a value with another one.
    """
    ...

class NotIterableError(Exception):
    """
    Availability: >= 0.3.26rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.exceptions.NotIterableError
    
    Attempt to iterate a non-iterable object.
    
    This exception is thrown if an object is object of a class extending class `~.types_collection.NotIterable`
    """
    ...

class NotCallableError(Exception):
    """
    Availability: >= 0.3.45 \\
    https://aveyzan.xyz/aveytense#aveytense.exceptions.NotCallableError
    
    Attempt to call an object.
    
    This exception is thrown to indicate non-callable objects.
    """
    ...
    
NotInvocableError = NotCallableError # >= 0.3.26rc1
    
class SubclassedError(Exception):
    """
    Availability: >= 0.3.27rc1 \\
    https://aveyzan.xyz/aveytense#aveytense.exceptions.SubclassedError
    
    Class has been inherited by the other class.
    
    This exception is thrown by definitions with the 'final' word in their names in the `aveytense.util` module.
    """
    ...

if __name__ == "__main__":
    error = RuntimeError("Import-only module")
    raise error