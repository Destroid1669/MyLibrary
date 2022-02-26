r"""This is Re-write of python existing built_in functions on the basis of
functions execution output, I only wrote this to improve my programming skills.
It is written to imitate those function which is not intended to be used in the programs.

Date: 31-Jan-2022 ; Monday

# |--> Author: Destroid <--|

"""

# List of all built_in functions written within this module
# Functions name have been capitalized to prevent conflict.
__all__ = ["Any", "Bool", "All", "Chr", "Ord", "Complex", "Tuple",
           "List", "Divmod", "Min", "Max", "Sum", "Len", "Map",
           "Range", "Enumerate", "Reversed", "Sorted"]

def Merge(self, *args):
    for i in args:
        self.update(i)
    return self

def getkey(dct, value):
    "Returns `dict` value for the key passed to it"

    for key in dct:
        if dct[key] == value:
            return key[0]
    return ''

def errorhandler(message, *args):
    "Raises Type error according to the arguments passed to it."

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
# These are not all unicode characters within python, these are only some general used ones for demonstration only!
all_ascii_characters = Merge(ascii_lowercase, ascii_uppercase, whitespace, digits, punctuation)

def Chr(number):
    "Returns a Unicode string of one character"

    errorhandler("%s object cannot be interpreted as an integer", [number, int])
    
    return all_ascii_characters.get(number)

def Ord(value):
    "Returns the Unicode code point for a one-character string."

    errorhandler("Ord() expected string of length 1, but %s found", [value, str])
    if len(value) > 1:
        raise TypeError("Ord() expected a character, but string of length %s found" % len(value))
    
    return getkey(all_ascii_characters, value)
 
def Any(iterable = None):
    """Returns True if any element of the iterable is true.
    If the iterable is empty, returns False."""
    
    try:
        for _ in iterable:
            return True
    except:
        return False
    return False

def Bool(value):
    "Returns True when the argument is true, False otherwise."

    if value is True:
        return True
    elif value is False or value is None:
        return False

    try:
        iter(value)
        for _ in value:
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

def Complex(real = 0, imag = 0):
    """Create a complex number from a real part and an optional imaginary part.
  
    This is equivalent to (real + imag*1j) where imag defaults to 0."""

    Complex.real = real
    Complex.imag = imag

    return (real + imag*1j)

def Len(obj):
    "Returns the number of items in a container."

    iter(obj) # Raises error for non-iterable object
    count = 0
    for _ in obj:
        count += 1
    return count

def Map(self, *args):
    """Makes an iterator that computes the function using arguments from
    each of the iterables. Stops when the shortest iterable is exhausted."""
    
    """/* 
        Note: In python map returns a iterable object not a tuple sequence,
              this function is simpler pythonic implementation of that function.
    */"""
    tuplatoon = ()
    for i in args:
        tuplatoon += (self(i),)
    return tuplatoon

def Divmod(x, y):
    "Returns the tuple (x//y, x%y).  Invariant: div*y + mod == x."

    return (x//y, x%y)

def Min(*iterable, default = object, key = None):
    """With a single iterable argument, return its smallest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    With two or more arguments, return the smallest argument."""
    
    if len(iterable) == 0:
        raise TypeError("Max expected at least 1 argument, got 0")
    
    if len(iterable) == 1:
        values = iterable[0]
    else:
        values = iterable

    iter(values) # Raises error for non iterables
    if len(values) == 0:
        if default is not object:
            return default
        raise ValueError("Min() arg is an empty sequence")
    
    for small in values:
        break
    if key is None:
        for i in values:
            if i < small:
                small = i
    else:
        for i in values:
            if key(i) < key(small):
                small = i
    return small

def Max(*iterable, default = object, key = None):
    """With a single iterable argument, return its biggest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    With two or more arguments, return the largest argument."""
    
    if len(iterable) == 0:
        raise TypeError("Max expected at least 1 argument, got 0")
    
    if len(iterable) == 1:
        values = iterable[0]
    else:
        values = iterable

    iter(values) # Raises error for non iterables
    if len(values) == 0:
        if default is not object:
            return default
        raise ValueError("Max() arg is an empty sequence")
    
    for big in values:
        break
    if key is None:
        for i in values:
            if i > big:
                big = i
    else:
        for i in values:
            if key(i) > key(big):
                big = i
    return big

def Sum(iterable, start = 0):
    """Returns the sum of a 'start' value (default: 0) plus an iterable of numbers
    When the iterable is empty, return the start value.
    This function is intended specifically for use with numeric values and may
    reject non-numeric types."""

    iter(iterable) # Raises error for non iterables
    if isinstance(iterable, str):
        raise TypeError("Sum() can't sum strings [use ''.join(seq) instead]")
    
    _sum = 0
    for element in iterable:
        _sum += element
    return _sum + start

def Tuple(iterable):
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

def List(iterable):
    """If no argument is given, the function creates a new empty list.
    The argument must be an iterable if specified."""

    iter(iterable) # Raises error for non iterables

    _list = []
    for i in iterable:
        _list.append(i)
    return _list

def Range(start = 0, stop = 0, step = 1):
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
    
    """/* 
        Note: In python range returns a iterable object not a tuple sequence,
              this function is simpler pythonic implementation of that function.
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
              this function is simpler pythonic implementation of that function. 
    */"""

    errorhandler("%s object cannot be interpreted as an integer", [start, int])
    iter(iterable) # Raises error for non iterables

    n = 0 + start
    tuplatoon = ()
    for i in iterable:
        tuplatoon += ((n, i),)
        n += 1
    return tuplatoon

def Reversed(sequence):
    "Return a reverse iterator over the values of the given sequence."
    
    #* Note: In python Reversed returns a iterable object not a list sequence
    iter(sequence) # raises error for non iterables 
    if isinstance(sequence, set):
        raise TypeError("'set' object is not reversible")
    if not isinstance(sequence, list):
        sequence = list(sequence)

    length = len(sequence)
    for i in range(int(length / 2)):
        temp = sequence[i]
        sequence[i] = sequence[length-i-1]
        sequence[length-i-1] = temp
    
    return sequence

def binary_search(array, item, start, end):
    if start == end:
        if array[start] > item:
            return start
        else:
            return start + 1
    if start > end:
        return start

    mid = round((start + end)/ 2)

    if array[mid] < item:
        return binary_search(array, item, mid + 1, end)
    elif array[mid] > item:
        return binary_search(array, item, start, mid - 1)
    else:
        return mid

#* Insertion sort is used by timsort for small array or small runs.
def insertion_sort(array):
    for index in range(1, len(array)):
        value = array[index]
        pos = binary_search(array, value, 0, index - 1)
        array = array[:pos] + [value] + array[pos:index] + array[index+1:]
    return array

#* Returns a single sorted array from two sorted array
def merge(left, right):
    if not left:
        return right
    if not right:
        return left
    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])

def Sorted(iterable, *, key = None, reverse = False):
    """Return a new list containing all items from the iterable in ascending order.

    A custom key function can be supplied to customize the sort order, and the
    reverse flag can be set to request the result in descending order.
    
    /* Note: This is pythonic implementation of timsort algorithm */
    
    """

    if key is not None:
        raise Exception("currently key argument hasn't been implemented !")
    iter(iterable) # Raises error for non iterables
    
    if not isinstance(iterable, list):
        array = list(array)
    else:
        array = iterable

    runs, sorted_runs = [], []
    length = len(array)
    new_run = [array[0]]

    for i in range(1, length):
        # if i is at the last index
        if i == length-1:
            new_run.append(array[i])
            runs.append(new_run)
            break
        if array[i] < array[i-1]:
            # if new_run is None (empty)
            if not new_run:
                runs.append([array[i]])
                new_run.append(array[i])
            else:
                runs.append(new_run)
                new_run = [array[i]]
        else:
            new_run.append(array[i])

    # For every item in runs, append it using insertion sort
    for item in runs:
        sorted_runs.append(insertion_sort(item))
    
    # For every run in sorted_runs, merge them
    sorted_array = []
    for run in sorted_runs:
        sorted_array = merge(sorted_array, run)

    if not reverse:
        return sorted_array
    return Reversed(sorted_array)


__all__.extend(["IS"])
# Note: python `in` is an operator not a function and `IS` isn't any python
# function rather this is `in` implementation of python operator as function.
def IS(self, iterable) -> bool:
    "Performs same operation as `in` operator"

    iter(iterable) # Raises error for non-iterable object
    i, length = 0, len(iterable)
    if isinstance(iterable, str):
        if not isinstance(self, str):
            raise TypeError("'IS <string>' requires string as left operand, not %s" % type(self).__name__)

        s_len = len(self)
        while i < length:
            if self == iterable[i: i+s_len]:
                return True
            i += 1
    else:
        while i < length:
            if self == iterable[i]:
                return True
            i += 1
    return False
