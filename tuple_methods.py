r"This is Re-write of tuple methods"

# These are two tuple methods in Python.
__all__ = ["count", "index"]

def errorhandler(*args):
    "Raises Type error based on arguments passed to it"

    for value, datatype in args:
        if not isinstance(value, datatype):
            raise TypeError("expected {} found {}".format(datatype.__name__, type(value).__name__))

"""/*
# A sort note about these methods:

count, index methods are same for string,
tuple and list for these iterable data types.

These functions compares each element to substring passed
to it for iterable data types, only for strings this case change
whereas substring is compared with same length of string slice iterations.

*/"""

def count(self, sub, start = 0, end = None):
    """Returns the number of non-overlapping occurrences of substring sub in string self[start:end].
    Optional arguments start and end are interpreted as in slice notation."""

    errorhandler([start, int])
    if end is not None:
        errorhandler([end, int])
    iter(self) # Raises error for non iterables
    
    iterable = self[start: end]
    if isinstance(self, str):
        #! Issue with counting empty string
        #! Returns wrong result for this case
        _count, len_sub = 0, len(sub)
        for i in range(len(iterable)):
            if sub == iterable[i: i+len_sub]:
                _count += 1
        return _count if sub != "" else _count+1
    else:
        # Expecting for iterable object
        _count = 0
        for i in iterable:
            if sub == i:
                _count += 1
        return _count

def index(self, sub, start = 0, end = None):
    """Returns the lowest index in self where substring sub is found,
    such that sub is contained within self[start:end].  Optional
    arguments start and end are interpreted as in slice notation.
    Raises ValueError when the substring is not found."""

    errorhandler([start, int])
    if end is not None:
        errorhandler([end, int])
    if sub == "":
        return 0
    iter(self) # Raises error for non iterables

    iterable = self[start: end]
    if isinstance(self, str):
        len_sub = len(sub)
        for i in range(len(self)):
            if sub == iterable[i: i+len_sub]:
                return i
    else:
        # Expecting for iterable object
        for i in range(len(iterable)):
            if sub == iterable[i]:
                return i
    raise ValueError("%s substring not found" % sub)