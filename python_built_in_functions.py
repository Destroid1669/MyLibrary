r"""This is Re-write of python existing built_in functions on the basis of
functions execution output, I only wrote this to improve my programming skills
its is written to Imitate those functions, not intended to be used in programs.

Date: 31-jan-2022 ; Monday

# |--> Author: Destroid <--|

"""
# ! INCOMPLETE STATE NEED SUGGESTIONS TO FIX ISSUES !

# List of all built_in functions written within this module
# functions name have been capitalized to prevent conflict.
"""
__all__ = ["Abs", "Any", "Bool", "All", "Chr", "Ord", "Tuple", "List",
           "Divmod","Min", "Max", "Sum", "Sorted", "Pow", "Round",
           "IS", "Len", "Map", "Range", "Emumerate"]
"""

def Merge(self, *args):
    DICT = self
    for i in args:
        DICT.update(i)
    return DICT

def getkey(dct, value):
    "Returns `dict` value for the key passed to it"

    for key in dct:
        if dct[key] == value:
            return key[0]
    return ''

def errorhandler(message, *args):
    """Raises Type error accordingly to the arguments passed to it"""

    for value, datatype in args:
        if not isinstance(value, datatype):
            raise TypeError(f"{message}" % type(value).__name__)

"""/*A collection of unicode constants.

Public module variables:

whitespace -- a dict containing all unicode whitespace
ascii_lowercase -- a dict containing all unicode lowercase letters
ascii_uppercase -- a dict containing all unicode uppercase letters
ascii_letters -- a dict containing all unicode letters
digits -- a dict containing all unicode decimal digits
punctuation -- a dict containing all unicode punctuation characters

*/"""

whitespace = {32: ' ', 9: '\t', 10: '\n', 13: '\r', 11: '\x0b', 12: '\x0c'}

ascii_lowercase = {97: 'a', 98: 'b', 99: 'c', 100: 'd', 101: 'e', 102: 'f', 103: 'g',
                   104: 'h', 105: 'i', 106: 'j', 107: 'k', 108: 'l', 109: 'm', 110: 'n',
                   111: 'o', 112: 'p', 113: 'q', 114: 'r', 115: 's', 116: 't', 117: 'u',
                   118: 'v', 119: 'w', 120: 'x', 121: 'y', 122: 'z'}

ascii_uppercase = {65: 'A', 66: 'B', 67: 'C', 68: 'D', 69: 'E', 70: 'F', 71: 'G',
                   72: 'H', 73: 'I', 74: 'J', 75: 'K', 76: 'L', 77: 'M', 78: 'N',
                   79: 'O', 80: 'P', 81: 'Q', 82: 'R', 83: 'S', 84: 'T', 85: 'U',
                   86: 'V', 87: 'W', 88: 'X', 89: 'Y', 90: 'Z'}

punctuation = {33: '!', 34: '"', 35: '#', 36: '$', 37: '%', 38: '&', 39: "'", 40: '(', 41: ')',
               42: '*', 43: '+', 44: ',', 45: '-', 46: '.', 47: '/', 58: ':', 59: ';', 60: '<',
               61: '=', 62: '>', 63: '?', 64: '@', 91: '[', 92: '\\', 93: ']', 94: '^', 95: '_',
               96: '`', 123: '{', 124: '|', 125: '}', 126: '~'}

digits = {48: '0', 49: '1', 50: '2', 51: '3', 52: '4', 53: '5', 54: '6', 55: '7', 56: '8', 57: '9'}
# These aren't all unicode characters within python it's only some general used ones for demenestration!
all_ascii_characters = Merge(ascii_lowercase, ascii_uppercase, whitespace, digits, punctuation)

def Chr(number):
    "Returns a Unicode string of one character"

    errorhandler("%s object cannot be interpreted as an integer", (number, int))
    
    return all_ascii_characters.get(number)

def Ord(value):
    "Returns the Unicode code point for a one-character string."

    errorhandler("Ord() expected string of length 1, but %s found", (value, str))
    if len(value) > 1:
        raise TypeError("Ord() expected a character, but string of length %s found" % len(value))
    
    return getkey(all_ascii_characters, value)
 
def Abs(value):
    "Returns the absolute value of the argument."

    # TODO: implement complex numbers
    if value < 0:
        value = -value
    return value

def Any(iterable = None):
    """Returns True if any element of the iterable is true.
    If the iterable is empty, returns False."""
    
    try:
        for x in iterable:
            return True
    except:
        return False
    return False

def Bool(value):
    """Returns True when the argument is true, False otherwise."""

    if value is True:
        return True
    elif value is False or value is None:
        return False

    try:
        iter(value)
        for x in value:
                return True
        return False
    
    except:
        if isinstance(value, str):
            value = eval(value)

        if abs(value) > 0:
            return True
        else:
            return False

def All(iterable):
    """Returns True if Bool(x) is True for all values x in the iterable.

    If the iterable is empty, returns True."""

    for x in iterable:
        if iter(x):
            continue

        if not Bool(x):
            return False
    return True

def Len(obj):
    "Returns the number of items in a container."

    Count = 0
    for x in obj:
        Count += 1
    return Count

def Map(self, *args):
    """Makes an iterator that computes the function using arguments from
    each of the iterables. Stops when the shortest iterable is exhausted."""

    tuplatoon = ()
    for i in args:
        tuplatoon += (self(i),)
    return tuplatoon

def Divmod(x, y):
    "Returns the tuple (x//y, x%y).  Invariant: div*y + mod == x."

    return (x//y, x%y)

def Pow(base, exp, mod = None):
    """Equivalent to base**exp with 2 arguments or base**exp % mod with 3 arguments

    Some types, such as ints, are able to use a more efficient algorithm when
    invoked using the three argument form."""
    
    # TODO: implement float numbers
    # TODO: as well as mod argument
    i, number = 0, 1
    if exp > 0:
        while i < abs(exp):
            number *= base
            i += 1
    else:
        while i < abs(exp):
            number /= base
            i += 1

    return number if base > 0 else -number

def Min(*iterable, default = False, key = None):
    """With a single iterable argument, return its smallest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    With two or more arguments, return the smallest argument."""
    
    try:
        # cheking for iterable data type
        iter(iterable)
        if len(iterable) == 0:
            if default != False:
                return default
            raise ValueError("Max() arg is an empty sequence")
        
        if key is None:
            for x in iterable:
                small = x[0]
                for i in x:
                    if small > i:
                        small = i
        else:
            for x in iterable:
                small = x[0]
                for i in x:
                    if key(small) > key(i):
                        small = i
        return small
    except:
        raise # Raising error if not found iterable

def Max(*iterable, default = False, key = None):
    """With a single iterable argument, return its biggest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    With two or more arguments, return the largest argument."""
    
    try:
        # cheking for iterable data type
        iter(iterable)
        if len(iterable) == 0:
            if default != False:
                return default
            raise ValueError("Max() arg is an empty sequence")
        
        if key is None:
            for x in iterable:
                Big = x[0]
                for i in x:
                    if Big < i:
                        Big = i
        else:
            for x in iterable:
                Big = x[0]
                for i in x:
                    if key(Big) < key(i):
                        Big = i
        return Big
    except:
        raise # Raising error if not found iterable

def Sum(iterable, start = 0):
    """Returns the sum of a 'start' value (default: 0) plus an iterable of numbers

    When the iterable is empty, return the start value.
    This function is intended specifically for use with numeric values and may
    reject non-numeric types."""

    try:
        iter(iterable)
        if isinstance(iterable, str):
            raise TypeError("Sum() can't sum strings [use ''.join(seq) instead]")
        
        SUM = 0
        for element in iterable:
            SUM += element
        return SUM + start
    except:
        raise

def Tuple(iterable):
    """If no argument is given, the function returns an empty tuple.
    If iterable is specified the tuple is initialized from iterable's items.
  
    If the argument is a tuple, the return value is the same object."""
    
    if isinstance(iterable, tuple):
        return iterable

    tuplatoon = ()
    for i in iterable:
        tuplatoon += (i,)
    return tuplatoon

def List(iterable):
    """If no argument is given, the function creates a new empty list.
    The argument must be an iterable if specified."""
    
    LIST = []
    for i in iterable:
        LIST.append(i)
    return LIST

def Round(number, ndigits = None):
    """Rounds a number to a given precision in decimal digits.

    The return value is an integer if ndigits is omitted or None.  Otherwise
    the return value has the same type as the number.  ndigits may be negative."""

    if not isinstance(number, int) and not isinstance(number, float):
        raise TypeError("expected int or float but found %s" % type(number).__name__)

    # ! int() unexpected value issue: it converts floats more than 17 digits to incorrect int values

    import math
    fnum, inum = math.modf(number)

    if fnum > 0.5:
        return int(inum) + 1
    else:
        return int(inum)

def Range(start = 0, stop = 0, step = 1):
    """Returns a tuple that produces a sequence of integers from start (inclusive)
    to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
    start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
    These are exactly the valid indices for a list of 4 elements.
    When step is given, it specifies the increment (or decrement)."""

    errorhandler("%s object cannot be interpreted as an integer", (start, int), (stop, int), (step, int))
    if step == 0:
        raise ValueError("Range() arg 3 must not be zero")
    
    """/* 
        Note: In python range returns a iterable object not a tuple sequence,
              This function is simpler pythonic implementation of that function.
    */"""

    if start != 0 and stop == 0:
        start, stop = stop, start

    tuplatoon = ()
    if step > 0:
        while start < stop:
            tuplatoon += (start,)
            start += step
    else:
        while start > stop:
            tuplatoon += (start,)
            start += step

    return tuplatoon

def Enumerate(iterable, start = 0):
    """Returns a tuple sequence.
  
    iterable
        an object supporting iteration
  
    The enumerate function yields pairs containing a count (from start, which
    defaults to zero) and a value yielded by the iterable argument.
  
    enumerate is useful for obtaining an indexed list:
        (0, seq[0]), (1, seq[1]), (2, seq[2]), ..."""

    """/* 
        Note: In python enumerate returns a iterable object not a tuple sequence,
              This function is simpler pythonic implementation of that function. 
    */"""

    errorhandler("%s object cannot be interpreted as an integer", (start, int))
    try:
        # checking for iterable object
        iter(iterable)
        n = 0 + start
        tuplatoon = ()
        for i in iterable:
            tuplatoon += ((n, i),)
            n += 1
        return tuplatoon
    except:
        raise # Raising error for non-iterable object

def IS(self, iterable) -> bool:
    "Performs same operation as `in`"

    # Note: python `in` isn't a function nor `IS` is any python function
    # rather this function is `in` implementation of python as function

    try:
        # checking for iterable object
        iter(iterable)
        # raising error if not found string object
        assert isinstance(iterable, str)
        if not isinstance(self, str):
            raise TypeError("'IS <string>' requires string as left operand, not %s" % type(self).__name__)

        len_self = len(self)
        i = 0
        while i < len(iterable):
            if self == iterable[i: i+len_self]:
                return True
            i += 1
        return False

    except AssertionError:
        # expecting for iterable object
        i = 0
        while i < len(iterable):
            if self == iterable[i]:
                return True
            i += 1
        return False

    except:
        raise # Raising error for non-iterable object
