r"""This is Re-write of python existing built_in functions on the basis of
functions execution output, I only wrote this to improve my programming skills.
It is written to imitate those functions, not intended to be used in the programs.

Date: 31-Jan-2022 ; Monday

|--> Author: Destroid <--|

"""

# List of all built_in functions written within this module
# Functions name have been capitalized to prevent conflict.
__all__ = ["Any", "All", "Bool", "Chr", "Ord", "Bin", "Divmod",
           "Min", "Max", "Sum", "Len", "Map", "Filter", "Range",
           "Enumerate", "Reversed", "Sorted"]

# variable for checking missing arguments
missing_value = object()

def Merge(self, *args):
    for i in args:
        self.update(i)
    return self

def getkey(dct, value):
    "Returns `dict` value for the key passed to it"

    for key in dct:
        if dct[key] == value:
            return key[0]
    raise ValueError("Key not found for Ascii value !")

def errorhandler(message, *args):
    "Raises Type error based on arguments passed to it."

    for value, datatype in args:
        if not isinstance(value, datatype):
            raise TypeError(f"{message}" % type(value).__name__)

"""A collection of unicode constants.

Public module variables:

whitespace -- a dict containing all unicode whitespace
ascii_lowercase -- a dict containing all unicode lowercase letters
ascii_uppercase -- a dict containing all unicode uppercase letters
ascii_letters -- a dict containing all unicode letters
digits -- a dict containing all unicode decimal digits
punctuation -- a dict containing all unicode punctuation characters

"""

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
# These are not all unicode characters within python, these are some general used ones for demonstration only!
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
    except:
        if isinstance(value, str):
            value = eval(value)

        if abs(value) > 0:
            return True
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

def Bin(number: int):
  """Returns the binary representation of an integer.

  >>> bin(2796202)
  '0b1010101010101010101010'
  
  """

  errorhandler("%s object cannot be interpreted as an integer", [number, int])
  
  if number == 0:
    return "0b0"
  num = abs(number)

  binary = ''
  while num != 0:
    num, remainder = Divmod(num, 2)
    binary += str(remainder)

  if number > -1:
    return f"0b{binary[::-1]}"
  else:
    return f"-0b{binary[::-1]}"

def Len(obj):
    "Returns the number of items in a container."

    iterable = iter(obj) # Raises error for non iterables
    count = 0
    for _ in iterable:
        count += 1
    return count

def Divmod(x, y):
    "Returns the tuple (x//y, x%y).  Invariant: div*y + mod == x."

    return (x//y, x%y)

def Min(*iterable, default = missing_value, key = None):
    """With a single iterable argument, return its smallest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    With two or more arguments, return the smallest argument."""

    it = iter(iterable)
    try:
        values = next(it)
    except StopIteration:
        raise TypeError("Min expected at least 1 argument, got 0")

    try:
        small = next(iter(values))
    except StopIteration:
        if default is not missing_value:
            return default
        raise ValueError("Min() arg is an empty sequence")
    
    if key is None:
        for i in values:
            if i < small:
                small = i
    else:
        for i in values:
            if key(i) < key(small):
                small = i
    return small

def Max(*iterable, default = missing_value, key = None):
    """With a single iterable argument, return its biggest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    With two or more arguments, return the largest argument."""
    
    it = iter(iterable)
    try:
        values = next(it)
    except StopIteration:
        raise TypeError("Max expected at least 1 argument, got 0")

    try:
        big = next(iter(values))
    except StopIteration:
        if default is not missing_value:
            return default
        raise ValueError("Max() arg is an empty sequence")

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

    it = iter(iterable) # Raises error for non iterables
    if isinstance(start, str):
        raise TypeError("Sum() can't sum strings [use ''.join(seq) instead]")
    
    _sum = 0
    for element in it:
        _sum += element
    return _sum + start

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
    
    """Note:
        In python range returns a range object not a tuple sequence,
        this function is simpler pythonic implementation of that function.
    """

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

    """Note:
        In python enumerate returns a enumerate object not a tuple sequence,
        this function is simpler pythonic implementation of that function. 
    """

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
    
    """Note:
        In python reversed returns a reversed object not a tuple sequence,
        this function is simpler pythonic implementation of that function. 
    """

    iter(sequence) # raises error for non iterables 
    if isinstance(sequence, set):
        raise TypeError("'set' object is not reversible")
    sequence = sequence.copy() if isinstance(
    sequence, list) else list(sequence)

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

def timsort(array):
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
    # for every item in runs, append it using insertion sort
    for item in runs:
        sorted_runs.append(insertion_sort(item))
    # for every run in sorted_runs, merge them
    sorted_array = []
    for run in sorted_runs:
        sorted_array = merge(sorted_array, run)
    return sorted_array

def Sorted(iterable, *, key = None, reverse = False):
    """Return a new list containing all items from the iterable in ascending order.

    A custom key function can be supplied to customize the sort order, and the
    reverse flag can be set to request the result in descending order.
    
    /* Note: This is pythonic implementation of timsort algorithm */
    
    """

    iter(iterable) # Raises error for non iterables
    
    Array = iterable.copy() if isinstance(
    iterable, list) else list(iterable)
    array = Array if not reverse else Reversed(Array)
    import sys; sys.setrecursionlimit(len(array))
    
    if key is None:
        sorted_array = timsort(array)
    else:
        # sorting array elements using key
        key_sorted = timsort([key(k) for k in array])
        # sorting array using sorted key elements
        sorted_array = []
        for k_elem in key_sorted:
            for elem in array:
                if k_elem == key(elem):
                    sorted_array.append(elem)
                    array.remove(elem)

    return sorted_array if not reverse else Reversed(sorted_array)

def Map(function, *args):
    """Makes an iterator that computes the function using arguments from
    each of the iterables. Stops when the shortest iterable is exhausted."""
    
    """Note:
        In python map returns a map object not a tuple sequence,
        this function is simpler pythonic implementation of that function.
    """

    it = iter(args)
    try:
        initial = next(it)
    except StopIteration:
        raise TypeError("Map() must have at least two arguments.")

    iter(initial) # raises error for non iterables.
    #! issue: doesn't support multi *args.
    tuplatoon = ()
    for element in initial:
        tuplatoon += (function(element),)
    return tuplatoon

def Filter(function, iterable):
    """filter(function or None, iterable) --> filter object
 
   Return an iterator yielding those items of iterable for which function(item)
   is true. If function is None, return the items that are true."""
    
    """Note:
        In python filter returns a filter object not a tuple sequence,
        this function is simpler pythonic implementation of that function.
    """

    it = iter(iterable)
    tuplatoon = ()
    if function is None:
        return tuple(iterable)
    
    for element in it:
        if function(element):
            tuplatoon += (element,)
    return tuplatoon

__all__.extend(["Reduce"])
#* Note: `reduce` is functools library function not a python built-in function.
def Reduce(function, sequence, initial = missing_value):
    """
    reduce(function, iterable[, initial]) -> value

    Apply a function of two arguments cumulatively to the items of a sequence
    or iterable, from left to right, so as to reduce the iterable to a single
    value.  For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
    of the iterable in the calculation, and serves as a default when the
    iterable is empty.
    """

    it = iter(sequence)
    if initial is missing_value:
        try:
            value = next(it)
        except StopIteration:
            raise TypeError(
                "reduce() of empty iterable with no initial value") from None
    else:
        value = initial
    
    for element in it:
        value = function(value, element)

    return value


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