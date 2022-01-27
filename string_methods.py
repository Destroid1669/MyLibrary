r"""This is Re-write of python existing string methods as functions on the basis
of method's execution output, I only wrote this to improve my programming skills
its is written to Imitate those methods, not intended to be used in programs.

-->  No Unicode implementation  <--
Please note: no unicode implementation was done
within this module meaning using this module for
checking unicode characters is meaningless.

Date: 25-jan-2022 ; tuesday

# |--> Author: Destroid <--|

"""

# List of all string methods written within this module
__all__ = ["isupper", "islower", "isalpha", "isdecimal", "isalnum", "isspace", "istitle",
           "isprintable", "startswith", "endswith", "upper", "lower", "swapcase", "title",
           "capitalize", "zfill", "ljust", "rjust", "center", "expandtabs", "partition",
           "rpartition", "splitlines", "find", "rfind", "index", "rindex", "count", "join",
           "replace", "strip", "lstrip", "rstrip", "split", "rsplit"]

"""/*A collection of string constants.

Public module variables:

whitespace -- a string containing all ASCII whitespace
ascii_lowercase -- a string containing all ASCII lowercase letters
ascii_uppercase -- a string containing all ASCII uppercase letters
ascii_letters -- a string containing all ASCII letters
digits -- a string containing all ASCII decimal digits
hexdigits -- a string containing all ASCII hexadecimal digits
octdigits -- a string containing all ASCII octal digits
punctuation -- a string containing all ASCII punctuation characters
printable -- a string containing all ASCII characters considered printable

*/"""

whitespace = ' \t\n\r\v\f'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_letters = ascii_lowercase + ascii_uppercase
digits = '0123456789'
hexdigits = digits + 'abcdef' + 'ABCDEF'
octdigits = '01234567'
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
printable = digits + ascii_letters + punctuation + ' '

def get_ascii_letters_pairs():
    ascii_letters_pairs = {}
    for i in range(len(ascii_uppercase)):
        ascii_letters_pairs[ascii_lowercase[i]] = ascii_uppercase[i]
    return ascii_letters_pairs

ascii_letters_pairs = get_ascii_letters_pairs()

def getkey(dct, value):
    "Returns `dict` value for the key passed to it"

    for key in dct:
        if dct[key] == value:
            return key[0]
    return ''

def errorhandler(self):
    """Raises Type error according to the arguments passed to it"""

    for i in self:
        if not isinstance(self[i], i):
            raise TypeError("expected {} found {}".format(i.__name__, type(self[i]).__name__,))

def isupper(self):
    """Returns True if the string is an uppercase string, False otherwise.

    A string is uppercase if all cased characters in the string are uppercase and there is at least one cased character in the string."""

    errorhandler({str: self})

    for letters in self:
        if letters in ascii_letters:
            if letters in ascii_lowercase:
                return False

    return True if self != "" else False

def islower(self):
    """Returns True if the string is a lowercase string, False otherwise.

    A string is lowercase if all cased characters in the string are lowercase and there is at least one cased character in the string."""

    errorhandler({str: self})

    for letters in self:
        if letters in ascii_letters:
            if letters in ascii_uppercase:
                return False

    return True if self != "" else False

def isalpha(self):
    """Returns True if the string is an alphabetic string, False otherwise.

    A string is alphabetic if all characters in the string are alphabetic and there is at least one character in the string."""

    errorhandler({str: self})

    for i in self:
        if not i in ascii_letters:
            return False

    return True if self != "" else False

def isdecimal(self):
    """Return True if the string is a decimal string, False otherwise.

    A string is a decimal string if all characters in the string are decimal and there is at least one character in the string"""

    errorhandler({str: self})

    for i in self:
        if i not in digits:
            return False

    return True if self != "" else False

def isalnum(self):
    """Returns True if the string is an alpha-numeric string, False otherwise.
    
    A string is alpha-numeric if all characters in the string are alpha-numeric and there is at least one character in the string."""

    errorhandler({str: self})

    ascii_alphanumeric = ascii_letters + digits
    for i in self:
        if i not in ascii_alphanumeric:
            return False

    return True if self != "" else False

def isspace(self):
    """Returns True if the string is a whitespace string, False otherwise.
    
    A string is whitespace if all characters in the string are whitespace and there is at least one character in the string."""

    errorhandler({str: self})
    
    for i in self:
        if i not in whitespace:
            return False

    return True if self != "" else False

def istitle(self):
    """Returns a version of the string where each word is titlecased.

    More specifically, words start with uppercased characters and all remaining cased characters have lower case."""

    errorhandler({str: self})
    
    ISTitle = False
    IsTrue = True
    for i in self:
        if i in ascii_letters:
            if IsTrue:
                if i in ascii_lowercase:
                    return False
                else:
                    ISTitle = True
            elif not i in ascii_lowercase:
                return False
            IsTrue = False
        else:
            IsTrue = True
   
    return True if ISTitle else False
    
def isprintable(self):
    """Returns True if the string is printable, False otherwise.
    
    A string is printable if all of its characters are considered printable in repr() or if it is empty."""

    errorhandler({str: self})
    
    for i in self:
        if i not in printable:
            return False
    return True

def startswith(self, prefix, start = 0, end = None):
    """Returns True if self starts with the specified prefix, False otherwise.
    
    With optional start, test self beginning at that position.
    With optional end, stop comparing self at that position.
    prefix can also be a tuple of strings to try."""

    errorhandler({str: self, int: start})
    if end is not None and not isinstance(end, int):
        errorhandler({int: end})
    if not isinstance(prefix, str):
        if isinstance(prefix, tuple):
            for _p in prefix:
                if not isinstance(_p, str):
                    raise TypeError("tuple for startswith must only contain str, not %s" % type(_p).__name__)
        else:
            raise TypeError("startswith second arg must be str or a tuple of str, not %s" % type(prefix).__name__)
    
    iterable = self[start: end]
    if isinstance(prefix, str):
        len_p = len(prefix)
        for i in range(len(iterable)):
            if prefix == iterable[i: i+len_p]:
                return True
            else:
                return False
    else:
        for p in prefix:
            if p in iterable:
                return True
        return False
        
def endswith(self, suffix, start = 0, end = None):
    """Returns True if self ends with the specified suffix, False otherwise.
    With optional start, test self beginning at that position.
    With optional end, stop comparing self at that position.
    suffix can also be a tuple of strings to try."""

    errorhandler({str: self, int: start})
    if end is not None and not isinstance(end, int):
        errorhandler({int: end})
    if not isinstance(suffix, str):
        if isinstance(suffix, tuple):
            for _s in suffix:
                if not isinstance(_s, str):
                    raise TypeError("tuple for endswith must only contain str, not %s" % type(_s).__name__)
        else:
            raise TypeError("endswith second arg must be str or a tuple of str, not %s" % type(suffix).__name__)
    
    iterable = self[start: end]
    if isinstance(suffix, str):
        len_s = len(suffix)
        for i in reversed(range(len(iterable)+1)):
            if suffix == iterable[i-len_s: i]:
                return True
            else:
                return False
    else:
        for s in suffix:
            if s in iterable:
                return True
        return False
        
def upper(self):
    "Returns a copy of the string converted to uppercase."

    errorhandler({str: self})
    
    string = ""
    for i in self:
        if i in ascii_letters:
            if i in ascii_uppercase:
                string += i
            else:
                string += ascii_letters_pairs.get(i)
        else:
            string += i
    return string

def lower(self):
    "Returns a copy of the string converted to lowercase."

    errorhandler({str: self})
    
    string = ""
    for i in self:
        if i in ascii_letters:
            if i in ascii_lowercase:
                string += i
            else:
                string += getkey(ascii_letters_pairs, i)
        else:
            string += i
    return string

def swapcase(self):
    "Converts uppercase characters to lowercase and lowercase characters to uppercase."

    errorhandler({str: self})
    
    string = ""
    for i in self:
        if i in ascii_letters:
            if i in ascii_lowercase:
                string += ascii_letters_pairs.get(i)
            else:
                string += getkey(ascii_letters_pairs, i)
        else:
            string += i
    return string

def title(self):
    """Returns a version of the string where each word is titlecased.

    More specifically, words start with uppercased characters and all remaining cased characters have lower case."""

    errorhandler({str: self})
    
    string, IsTrue = "", True
    for i in self:
        if i in ascii_letters:
            if IsTrue:
                if i in ascii_lowercase:
                    string += upper(i)
                else:
                    string += i
            else:
                string += lower(i)
            IsTrue = False
        else:
            IsTrue = True
            string += i
    return string

def capitalize(self):
    """Returns a capitalized version of the string.

    More specifically, make the first character have upper case and the rest lower case."""

    errorhandler({str: self})
    
    string = ""
    for n,i in enumerate(self):
        if n == 0:
            string += upper(i)
        else:
            string += lower(i)
    return string

def zfill(self, width):
    """Pad a numeric string with zeros on the left, to fill a field of the given width.

    The string is never truncated."""

    errorhandler({str: self, int: width})

    n_zero = width - len(self) if width > 1 else 0
    if self[0] == "+":
        sign = "+"
    elif self[0] == "-":
        sign = "-"
    else:
        sign = ""

    return sign + "0" * n_zero + (self if sign == "" else self[1: ])

def ljust(self, width, fillchar = " "):
    """Returns a left-justified string of length width.

    Padding is done using the specified fill character (default is a space)."""
    
    errorhandler({str: self, int: width, str: fillchar})
    
    n_allign = width - len(self)
    return self + fillchar * n_allign

def rjust(self, width, fillchar = " "):
    """Returns a right-justified string of length width.

    Padding is done using the specified fill character (default is a space)."""
    
    errorhandler({str: self, int: width, str: fillchar})

    n_allign = width - len(self)
    return fillchar * n_allign + self

def center(self, width, fillchar = " "):
    """Returns a centered string of length width.

    Padding is done using the specified fill character (default is a space)."""
    
    errorhandler({str: self, int: width, str: fillchar})

    n_allign = width - len(self)
    return (fillchar * (n_allign if n_allign == 1 else n_allign // 2)) + self + (fillchar * (n_allign // 2))

def expandtabs(self, tabsize = 8):
    """Returns a copy where all tab characters are expanded using spaces.

    If tabsize is not given, a tab size of 8 characters is assumed."""

    errorhandler({str: self, int: tabsize})

    string = ""
    for i in self:
        if i == "\t":
            string += " " * tabsize
        else:
            string += i
    return string

def partition(self, sep):
    """Partition the string into three parts using the given separator.

    This will search for the separator in the string.  If the separator is found,
    returns a 3-tuple containing the part before the separator, the separator
    itself, and the part after it.

    If the separator is not found, returns a 3-tuple containing the original string and two empty strings."""

    errorhandler({str: self, str: sep})

    len_sep = len(sep)
    for i in range(len(self)):
        if sep == self[i: i+len_sep]:
            return (self[0: i], self[i: i+len_sep], self[i+len_sep: ])

    return (self, '', '')

def rpartition(self, sep):
    """Partition the string into three parts using the given separator.

    This will search for the separator in the string, starting at the end.
    If the separator is found, returns a 3-tuple containing the part before the
    separator, the separator itself, and the part after it.

    If the separator is not found, returns a 3-tuple containing two empty strings and the original string."""

    errorhandler({str: self, str: sep})

    len_sep = len(sep)
    for i in reversed(range(len(self))):
        if sep == self[i: i+len_sep]:
            return (self[0: i], self[i: i+len_sep], self[i+len_sep: ])

    return (self, '', '')

def splitlines(self, keepends = False):
    """Returns a list of the lines in the string, breaking at line boundaries.

    Line breaks are not included in the resulting list unless keepends is given and true."""

    errorhandler({str: self, bool: keepends})

    line_breaks = "\n\r\v\f"
    string, output = "", []
    for i in self:
        if i in line_breaks:
            if keepends:
                output.append(string+i)
            else:
                output.append(string)
            # emptying the `string` variable 
            # to clear previous stored strings
            string = ""
        else:
            string += i
    else:
        if i not in line_breaks:
            output.append(string)
    return output

def find(self, sub, start = 0, end = None):
    """find(self, sub[, start[, end]]) -> int

    Returns the lowest index in self where substring sub is found,
    such that sub is contained within self[start:end].  Optional
    arguments start and end are interpreted as in slice notation.

    Returns -1 on failure."""

    errorhandler({str: self, str: sub, int: start})
    if end is not None and not isinstance(end, int):
        errorhandler({int: end})

    string = self[start: end]
    len_sub = len(sub)
    for i in range(len(self)):
        if sub == string[i: i+len_sub]:
            return i
    return -1

def rfind(self, sub, start = 0, end = None):
    """rfind(self, sub[, start[, end]]) -> int

    Returns the highest index in self where substring sub is found,
    such that sub is contained within self[start:end].  Optional
    arguments start and end are interpreted as in slice notation.

    Returns -1 on failure."""

    errorhandler({str: self, str: sub, int: start})
    if end is not None and not isinstance(end, int):
        errorhandler({int: end})

    string = self[start: end]
    len_sub = len(sub)
    for i in reversed(range(len(self))):
        if sub == string[i: i+len_sub]:
            return i
    return -1

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

def rindex(self, sub, start = 0, end = None):
    """rindex(self, sub[, start[, end]]) -> int
    Returns the highest index in self where substring sub is found,
    such that sub is contained within self[start:end].  Optional
    arguments start and end are interpreted as in slice notation.
    Raises ValueError when the substring is not found."""

    errorhandler({str: self, str: sub, int: start})
    if end is not None and not isinstance(end, int):
        errorhandler({int: end})
    if sub == "" and self == "":
        return 0
    
    string = self[start: end]
    len_sub = len(sub)
    for i in reversed(range(len(self))):
        if sub == string[i: i+len_sub]:
            return i
    
    raise ValueError("%s substring not found" % sub)

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

def join(self, iterable):
    """Concatenate any number of strings.

    The string whose method is called is inserted in between each given string.
    The result is returned as a new string.

    Example: join('.', ['ab', 'pq', 'rs']) -> 'ab.pq.rs'"""

    errorhandler({str: self})
    try:
        # checking for iterable object
        iter(iterable)
        output = ""
        for i in iterable:
            output += i + self
        return output
    except:
        raise # Raising exception if not found iterable

def replace(self, old, new, count = -1):
    """Returns a copy with all occurrences of substring old replaced by new.
    count
       Maximum number of occurrences to replace.
       -1 (the default value) means replace all occurrences.

    If the optional argument count is given, only the first count occurrences are replaced."""

    # Checking for invalid arguments and raising error if not valid
    errorhandler({str: self, str: old, str: new, int: count})

    IsTrue = True if count <= -1 else False
    i, string, old_len = 0, "", len(old)
    while i < len(self):
        if old == self[i: i+old_len]:
            if 0 < count or IsTrue: 
                string += new
                i += old_len-1
                count -= 1
            else:
                string += self[i]
        else:
            string += self[i]
        i += 1
    return string

LEFTSTRIP = 0
RIGHSTRIP = 1
BOTHSTRIP = 2

def do_strip(self, striptype):
    i = 0
    if striptype != RIGHSTRIP:
        while i < len(self) and isspace(self[i]):
            i += 1

    j = len(self) - 1
    if striptype != LEFTSTRIP:
        while (1 < j and isspace(self[j])):
            j -= 1

    return self[i: j+1]

def do_argstrip(self, striptype, chars):
    sep = tuple(i for i in chars)
    i = 0
    if striptype != RIGHSTRIP:
        while i < len(self) and startswith(self[i], sep):
            i += 1

    j = len(self) -1
    if striptype != LEFTSTRIP:
        while 1 < j and startswith(self[j], sep):
            j -= 1
    
    return self[i: j+1]

def strip(self, chars = None):
    """"strip(self, [chars]) -> string

    Returns a copy of the string S with leading and trailing whitespace removed.
    If chars is given and not None, remove characters in chars instead."""

    errorhandler({str: self})
    if chars is not None and not isinstance(chars, str):
        errorhandler({str: chars})

    if chars is None:
        return do_strip(self, BOTHSTRIP)
    else:
        return do_argstrip(self, BOTHSTRIP, chars)

def lstrip(self, chars = None):
    """lstrip(self, [chars]) -> string
    
    Returns a copy of the string self with leading whitespace removed.
    If chars is given and not None, remove characters in chars instead."""

    errorhandler({str: self})
    if chars is not None and not isinstance(chars, str):
        errorhandler({str: chars})

    if chars is None:
        return do_strip(self, LEFTSTRIP)
    else:
        return do_argstrip(self, LEFTSTRIP, chars)

def rstrip(self, chars = None):
    """rstrip(self, [chars]) -> string
    
    Returns a copy of the string self with trailing whitespace removed.
    If chars is given and not None, remove characters in chars instead."""

    errorhandler({str: self})
    if chars is not None and not isinstance(chars, str):
        errorhandler({str: chars})

    if chars is None:
        return do_strip(self, RIGHSTRIP)
    else:
        return do_argstrip(self, RIGHSTRIP, chars)

def do_split(self, split_type, maxsplit = -1):
    IsTrue = True if maxsplit <= -1 else False
    string, indexes, output = "", (), []

    i = 0
    if split_type == LEFTSTRIP:
        self = lstrip(self)
        j = len(self)-1
        while i < len(self):
            if isspace(self[i]):
                if 0 < maxsplit or IsTrue:
                    indexes += (i,)
                    if i < j and not isspace(self[i+1]):
                        maxsplit -= 1
            i += 1
    else:
        self = rstrip(self)
        j = len(self)-1
        while j > -1:
            if isspace(self[j]):
                if 0 < maxsplit or IsTrue:
                    indexes += (j,)
                    if j > 0 and not isspace(self[j-1]):
                        maxsplit -= 1
            j -= 1
    I = 0
    while I < len(self):
        if I in indexes:
            output.append(string)
            # emptying the `string` variable 
            # to clear pervious stored strings
            string = ""
        else: 
            string += self[I]
        I += 1
    output.append(string)
    out = [x for x in output if x != ""]
    # Returning a new output with all whitespaces elements removed
    if split_type == LEFTSTRIP:
        return [lstrip(x) for x in out]
    else:
        return [rstrip(x) for x in out]

def do_argsplit(self, split_type, sep, maxsplit =-1):
    IsTrue = True if maxsplit <= -1 else False
    string, indexes, output = "", (), []
    sep_len = len(sep)

    i, j = 0, len(self)-1
    if split_type == LEFTSTRIP:
        while i < len(self):
            if sep == self[i: i+sep_len]:
                if 0 < maxsplit or IsTrue:
                    indexes += (i,)
                    maxsplit -= 1
            i += 1
    else:
        while j > -1:
            if sep == self[j-(sep_len-1): j+1]:
                if 0 < maxsplit or IsTrue:
                    indexes += (j-(sep_len-1),)
                    maxsplit -= 1
            j -= 1
    I = 0
    while I < len(self):
        if I in indexes:
            output.append(string)
            string = ""
            # emptying the `string` variable 
            # to clear previous stored strings
            I += sep_len-1
        else: 
            string += self[I]
        I += 1
    output.append(string)
    return output

def split(self, sep = None, maxsplit = -1):
    """Returns a list of the words in the string, using sep as the delimiter string.
    sep
        The delimiter according which to split the string.
        None (the default value) means split according to any whitespace,
        and discard empty strings from the result.
    maxsplit
        Maximum number of splits to do.
        -1 (the default value) means no limit.
    """

    # Checking for string and raising error if not found
    errorhandler({str: self, int: maxsplit})
    if sep is not None and not isinstance(sep, str):
        errorhandler({str: sep})
    if sep == "":
        raise ValueError("empty separator")

    if sep is None:
        return do_split(self, LEFTSTRIP, maxsplit)
    else:
        return do_argsplit(self, LEFTSTRIP, sep, maxsplit)

def rsplit(self, sep = None, maxsplit = -1):
    """Returns a list of the words in the string, using sep as the delimiter string.
    sep
        The delimiter according which to split the string.
        None (the default value) means split according to any whitespace,
        and discard empty strings from the result.
    maxsplit
        Maximum number of splits to do.
        -1 (the default value) means no limit.
    """

    # Checking for string and raising error if not found
    errorhandler({str: self, int: maxsplit})
    if sep is not None and not isinstance(sep, str):
        errorhandler({str: sep})
    if sep == "":
        raise ValueError("empty separator")
    
    if sep is None:
        return do_split(self, RIGHSTRIP, maxsplit)
    else:
        return do_argsplit(self, RIGHSTRIP, sep, maxsplit)
