r"""This is Re-write of tuple methods """

# there are two tuple methods in python
__all__ = ["count", "index"]

def errorhandler(self):
    """Raises Type error according to the arguments passed to it"""

    for i in self:
        if not isinstance(self[i], i):
            raise TypeError("expected {} found {}".format(i.__name__, type(self[i]).__name__,))

"""/*
# A sort Note about these methods.

count, index methods are same for string,
tuple and list for these iterable data types.

these functions compares each element to substring passed
to it for iterable data types, only with for string this case changes
whereas substring is compared with same length of string slice iterations.

*/"""

def count(self, sub, start = 0, end = None):
    """count(self, sub[, start[, end]]) -> int
    Returns the number of non-overlapping occurrences of substring sub in string self[start:end].
    Optional arguments start and end are interpreted as in slice notation."""

    errorhandler({int: start})
    if end is not None and not isinstance(end, int):
        errorhandler({int: end})
    
    iterable = self[start: end]
    try:
        iter(self) # checking for iterable object
        # raising `AssertionError` if not found `str`
        assert isinstance(self, str)
        # issue with counting empty string
        # returns wrong result for this case
        Count, len_sub = 0, len(sub)
        for i in range(len(iterable)):
            if sub == iterable[i: i+len_sub]:
                Count += 1
        return Count if sub != "" else Count+1
    except AssertionError:
        # expecting for iterable object
        Count = 0
        for i in iterable:
            if sub == i:
                Count += 1
        return Count
    except:
        raise # Raising exception if not found iterable

def index(self, sub, start = 0, end = None):
    """index(self, sub[, start[, end]]) -> int
    Returns the lowest index in self where substring sub is found,
    such that sub is contained within self[start:end].  Optional
    arguments start and end are interpreted as in slice notation.
    Raises ValueError when the substring is not found."""

    errorhandler({int: start})
    if end is not None and not isinstance(end, int):
        errorhandler({int: end})
    if sub == "":
        return 0

    iterable = self[start: end]
    try:
        iter(self) # checking for iterable object
        # raising `AssertionError` if not found `str`
        assert isinstance(self, str)
        len_sub = len(sub)
        for i in range(len(self)):
            if sub == iterable[i: i+len_sub]:
                return i
    except AssertionError:
        # expecting for iterable object
        for i in range(len(iterable)):
            if sub == iterable[i]:
                return i
    except:
        raise # Raising exception if not found iterable
    raise ValueError("%s substring not found" % sub)