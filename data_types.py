r"""This is documentation of python data types

python data types are also functions which can
parse other appropriate data types to it's own.

Date: 8-Mar-2022 ; Tuesday

|--> Author: Destroid <--|

"""

# List of all data type functions written within this module
# Functions name have been capitalized to prevent conflict.
__all__ = ["Str", "Int", "Float", "Complex", "List",
           "Tuple", "Range", "Dict", "Set", "Frozenset",
           "Bool", "Bytes", "Bytearray", "Memoryview"]

from math import floor
# for checking missing arguments
MISSING = object()

def errorhandler(message, *args):
    "Raises Type error based on arguments passed to it."

    for value, datatype in args:
        if not isinstance(datatype, tuple):
            if not isinstance(value, datatype):
                raise TypeError(f"{message}" % type(value).__name__)
        else:
            IsTrue = False
            for _type in datatype:
                if isinstance(value, _type):
                    IsTrue = False
                    break
                else:
                    IsTrue = True
            if IsTrue:
                raise TypeError(f"{message}" % type(value).__name__)

r"""Python has the following data types built-in by default, in these categories:

null type:
    None

Text Type:
	str

Numeric Types:
	int, float, complex

Sequence Types:
	list, tuple, range

Mapping Type:
	dict

Set Types:
	set, frozenset

Boolean Type:
	bool

Binary Types:
	bytes, bytearray, memoryview

"""


r"""None -> (null type)
Object that denotes the lack of value.

The None keyword is used to define a null value, or no value at all.
None is not the same as 0, False, or an empty string.
None is a data type of its own (NoneType) and only None can be None.

python denotes null values as None.
"""


r"""Strings -> (text type)
Strings are sequences of character data. The string type in Python is called str.

String literals may be delimited using either single or double quotes.
All the characters between the opening delimiter and matching closing delimiter are part of the string:
"""

def Str(self, encoding = 'utf-8', errors = 'strict') -> str:
    """Create a new string object from the given object.
    If encoding or errors is specified, then the object
    must expose a data buffer that will be decoded using the
    given encoding and error handler. Otherwise, returns the
    result of object.__str__() (if defined) or repr(object).
    encoding defaults to sys.getdefaultencoding().
    errors defaults to 'strict'.

    """
    
    return str(self, encoding, errors)

r"""Integer -> (Numeric type)
An integer is colloquially defined as a number that can be written without a fractional component.

In Python 3, there is effectively no limit to how long an integer value can be. Of course,
it is constrained by the amount of memory your system has, as are all things, but beyond
that an integer can be as long as you need it to be:
"""

def Int(x = None, base = 10) -> int:
    """
    Convert a number or string to an integer, or return 0 if no arguments
    are given.  If x is a number, return x.__int__().  For floating point
    numbers, this truncates towards zero.

    If x is not a number or if base is given, then x must be a string,
    bytes, or bytearray instance representing an integer literal in the
    given base.  The literal can be preceded by '+' or '-' and be surrounded
    by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
    Base 0 means to interpret the base from the string as an integer literal.
    >>> int('0b100', base=0)
    4

    """
    # zero is returned for empty argument.
    if not x:
        return 0

    if not isinstance(x, str) and base != 10:
        # base conversion is only allowed for strings.
        raise TypeError("int() can't convert non-string with explicit base")

    if isinstance(x, str):
        # whitespaces are removed
        # from the ends for strings
        result = x.strip()

    elif isinstance(x, float):
        # number is rounded to zero for floats
        result = floor(x)

    elif isinstance(x, int):
        # int is returned
        result = x
    
    elif isinstance(x, bytes):
        # bytes are converted into int
        result = x
    
    else:
        raise TypeError("int() argument must be a string, a bytes-like object or a real number, not %s" % type(x.__name__))

    return int(result, base)

r"""Floating-Point Numbers -> (Numeric type)
The float type in Python designates a floating-point number.
float values are specified with a decimal point. Optionally,
the character e or E followed by a positive or negative integer
may be appended to specify scientific notation:
"""

def Float(x = None) -> float:
    "Converts a string or number to a floating point number, if possible."
    
    # fractional zero is returned for empty argument.
    if not x:
        return 0.0

    if isinstance(x, str):
        # whitespaces are removed
        # from the ends for strings
        result = x.strip()

    elif isinstance(x, float):
        # float is returned
        result = x

    elif isinstance(x, int):
        # int is converted into float
        result = x
    
    elif isinstance(x, bytes):
        raise ValueError("could not convert string to float: %s" % type(x.__name__))
    
    else:
        raise TypeError("float() argument must be a string or a real number, not %s" % type(x.__name__))

    return float(result)

r"""Complex Numbers -> (Numeric type)
Complex numbers are specified as <real part>+<imaginary part>j.

In mathematics, a complex number is an element of a number system that contains
the real numbers and a specific element denoted i, called the imaginary unit,
and satisfying the equation i² = -1. Moreover, every complex number can be
expressed in the form a + bi, where a and b are real numbers.

In python i -> imaginary part is denoted by j.
"""

def Complex(real = 0, imag = 0) -> complex:
    """Create a complex number from a real part and an optional imaginary part.
  
    This is equivalent to (real + imag*1j) where imag defaults to 0."""

    errorhandler("complex() first argument must be a string or a number, not %s", [real, (str, int, float)])
    errorhandler("complex() second argument must be a number, not %s", [imag, (int, float, complex)])
    if isinstance(imag, str):
        raise TypeError("complex() second arg can't be a string")
    if isinstance(real, str) and imag != 0:
        raise TypeError("complex() can't take second arg if first is a string")

    if not isinstance(real, str):
        Complex.real = real
        Complex.imag = imag

        return (real + imag*1j)
    else:
        return complex(real, imag)

r"""list -> (sequence type)
Indexed list of objects. Mutable.

Lists are mutable ordered and indexed collections of objects.
The items of a list are arbitrary Python objects.
Lists are formed by placing a comma-separated list of expressions in square brackets.
(Note that there are no special cases needed to form lists of length 0 or 1.)
""" 

def List(iterable) -> list:
    """If no argument is given, the function creates a new empty list.
    The argument must be an iterable if specified."""

    iter(iterable) # Raises error for non iterables

    _list = []
    for i in iterable:
        _list.append(i)
    return _list

r"""tuple -> (sequence type)
Indexed list of objects. Immutable.

Tuples are immutable ordered and indexed collections of objects.
Tuples of two or more items are formed by comma-separated lists of expressions.
A tuple of one item (a 'singleton') can be formed by affixing a comma to an expression
(an expression by itself does not create a tuple, since parentheses must be usable for grouping of expressions).
An empty tuple can be formed by an empty pair of parentheses.
"""

def Tuple(iterable) -> tuple:
    """If no argument is given, the function returns an empty tuple.
    If iterable is specified the tuple is initialized from iterable's items.
  
    If the argument is a tuple, then the return value is the same object."""
    
    if isinstance(iterable, tuple):
        return iterable
    iter(iterable) # Raises error for non iterables

    tuplatoon = ()
    for i in iterable:
        tuplatoon += (i,)
    return tuplatoon

r"""range -> (sequence type)
Returns a list of arithmetic progressions.

This is a versatile function to create lists containing arithmetic progressions.
It is most often used in for loops. The arguments must be plain integers.
If the step argument is omitted, it defaults to 1. If the start argument is omitted,
it defaults to 0. The full form returns a list of plain integers [start, start + step, start + 2 * step, …]. 
If step is positive, the last element is the largest start + i * step less than stop; if step is negative,
the last element is the smallest start + i * step greater than stop. step must not be zero (or else ValueError is raised).
"""

def Range(start: int = 0, stop: int = 0, step: int = 1):
    """Returns a tuple that produces a sequence of integers from start (inclusive)
    to stop (exclusive) by step.  
    
    range(i, j) produces i, i+1, i+2, ..., j-1
    
    start defaults to 0, and stop is omitted!  
    
    range(4) produces 0, 1, 2, 3
    
    These are exactly the valid indices for a list of 4 elements.
    When step is given, it specifies the increment (or decrement)."""

    errorhandler("%s object cannot be interpreted as an integer", [start, int], [stop, int], [step, int])
    if step == 0:
        raise ValueError("Range() arg 3 must not be zero")
    
    """Note:
        In python range returns a range object not a generator object,
        this function is simpler pythonic implementation of that function.
    """

    if start != 0 and stop == 0:
        start, stop = stop, start

    if step > 0:
        while start < stop:
            yield start
            start += step
    else:
        while start > stop:
            yield start
            start += step

r"""dict -> (Mapping type)
Hash table for storing unordered key-value pairs. Mutable.

Dictionaries are mutable unordered collections (they do not record element position or order of insertion) of key-value pairs.
Keys within the dictionary must be unique and must be hashable. That includes types like numbers, strings and tuples.
Lists and dicts can not be used as keys since they are mutable. Dictionaries in other languages are also called hash tables or associative arrays.

Numeric types used for keys obey the normal rules for numeric comparison: if two numbers compare equal (such as 1 and 1.0)
then they can be used interchangeably to index the same dictionary entry. (Note however, that since computers store
floating-point numbers as approximations it is usually unwise to use them as dictionary keys.)
"""

def Dict(iterable = None, **kwargs) -> dict:
    iter(iterable) # Raises error for non iterables
    if isinstance(iterable, str):
        raise ValueError("dictionary update sequence element #0 has length 1; 2 is required")
    
    d = {}
    if iterable is not None:
        try:
            for k, v in iterable:
                d[k] = v
        except TypeError:
            raise TypeError("cannot convert dictionary update sequence element #0 to a sequence")
    
    for k, v in kwargs.items():
        d[k] = v

    return d

r"""set -> (set type)
Unordered list of unique objects. Mutable.

Sets are mutable unordered collections of unique elements. Common uses include membership testing,
removing duplicates from a sequence, and computing standard math operations on sets such as
intersection, union, difference, and symmetric difference.

Sets do not record element position or order of insertion. Accordingly,
sets do not support indexing, slicing, or other sequence-like behavior.

Sets are implemented using dictionaries. They cannot contain mutable elements such
as lists or dictionaries. However, they can contain immutable collections.
""" 

def Set(iterable) -> set:
    "Builds an unordered collection of unique elements."
    
    iter(iterable) # Raises error for non iterables

    s = set()
    for elem in iterable:
        s.add(elem)
    return s

r"""frozenset -> (set type)
In Python, frozenset is the same as set except the frozensets are immutable
which means that elements from the frozenset cannot be added or removed once created.
This function takes input as any iterable object and converts them into an immutable object.
The order of elements is not guaranteed to be preserved
"""

def Frozenset(iterable) -> frozenset:
    "Build an immutable unordered collection of unique elements."

    iter(iterable) # Raises error for non iterables

    return frozenset(iterable)

r"""bool -> (Boolean type)
True and False Boolean values. Evaluates to 1 and 0 respectively.

These represent the truth values False and True.
The two objects representing the values False and True are the only Boolean objects.
The Boolean type is a subtype of plain integers, and Boolean values behave like the
values 0 and 1, respectively, in almost all contexts, the exception being that when
converted to a string, the strings "False" or "True" are returned, respectively.
"""

def Bool(value) -> bool:
    "Returns True when the argument is true, False otherwise."

    if value is True:
        return True
    elif value is False or value is None:
        return False

    if isinstance(value, int
    ) or isinstance(value, float
    ) or isinstance(value, complex):
        if value != 0:
            return True
    try:
        for _ in value:
            return True
    except TypeError:
        pass # considering non iterables to be False
    return False

r"""bytes -> (Binary type)
Python byte() function converts an object to an
immutable byte-represented object of given size and data.
"""

def Bytes(obj = 0, encoding = MISSING, errors = None) -> bytes:
    """bytes(bytes_or_buffer) -> immutable copy of bytes_or_buffer
    bytes(int) -> bytes object of size given by the parameter initialized with null bytes
    bytes() -> empty bytes object

    Construct an immutable array of bytes from:
      - an iterable yielding integers in range(256)
      - a text string encoded using the specified encoding
      - any object implementing the buffer API.
      - an integer
    
    """

    if errors is not None:
        errorhandler("bytes() argument 'errors' must be str, not %s", [errors, str])
    if encoding is not MISSING:
        errorhandler("bytes() argument 'encoding' must be str, not %s", [encoding, str])
    if errors is not None:
        if not isinstance(errors, str) and not isinstance(obj, str):
            raise TypeError("errors without a string argument")

    if isinstance(obj, str):
        if encoding is MISSING:
            raise TypeError("string argument without an encoding")
        
        if errors is None:
            return bytes(obj, encoding)
        
        return bytes(obj, encoding, errors)
    
    return bytes(obj)

r"""bytearray -> (Binary type)
The bytearray() method returns a bytearray object, which is an array of the given bytes.
The bytearray class is a mutable sequence of integers in the range of 0 to 256
The Python bytearray() function converts strings or collections of integers into a mutable sequence of bytes.
It provides developers the usual methods Python affords to both mutable and byte data types.
Python's bytearray() built-in allows for high-efficiency manipulation of data in several common situations.
"""

def Bytearray(obj = 0, encoding = MISSING, errors = None) -> bytearray:
    """bytearray(bytes_or_buffer) -> mutable copy of bytes_or_buffer
    bytearray(int) -> bytes array of size given by the parameter initialized with null bytes
    bytearray() -> empty bytes array
    
    Construct a mutable bytearray object from:
      - an iterable yielding integers in range(256)
      - a text string encoded using the specified encoding
      - a bytes or a buffer object
      - any object implementing the buffer API.
      - an integer
      
    """

    if errors is not None:
        errorhandler("bytearray() argument 'errors' must be str, not %s", [errors, str])
    if encoding is not MISSING:
        errorhandler("bytearray() argument 'encoding' must be str, not %s", [encoding, str])
    if errors is not None:
        if not isinstance(errors, str) and not isinstance(obj, str):
            raise TypeError("errors without a string argument")

    if isinstance(obj, str):
        if encoding is MISSING:
            raise TypeError("encoding without a string argument")
        
        if errors is None:
            return bytearray(obj, encoding)
        
        return bytearray(obj, encoding, errors)
    
    return bytearray(obj)

r"""Memoryview -> (Binary type)
memoryview objects allow Python code to access the internal data of an object
that supports the buffer protocol without copying. The memoryview() function allows direct
read and write access to an object's byte-oriented data without needing to copy it first.
"""

def Memoryview(obj) -> memoryview:
    "Creates a new memoryview object which references the given object."

    if not isinstance(obj, bytes):
        raise TypeError("memoryview: a bytes-like object is required, not %s" % type(obj.__name__))

    return memoryview(obj)