"""This Module is re-implementation of python existing string methods
as functions on the basis of their execution output it's written
to Imitate those methods, it's not intended to be used in programs.

# Note: This module doesn't support unicode characters.
# Note: This module is a support file for stringobject.py

"""

# List of all string methods written within this module.
__all__ = ["isupper", "islower", "isalpha", "isdecimal", "isalnum", "isspace", "istitle",
           "isprintable", "startswith", "endswith", "removeprefix", "removesuffix", "upper",
           "lower", "swapcase", "title", "capitalize", "zfill", "ljust", "rjust", "center",
           "expandtabs", "partition", "rpartition", "splitlines", "find", "rfind", "index",
           "rindex", "count", "join", "replace", "strip", "lstrip", "rstrip", "split", "rsplit"]

"""A collection of string constants.

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

"""

whitespace = ' \t\n\r\v\f'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_letters = ascii_lowercase + ascii_uppercase
digits = '0123456789'
hexdigits = digits + 'abcdef' + 'ABCDEF'
octdigits = '01234567'
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
printable = digits + ascii_letters + punctuation + ' '
ascii_letters_pairs = dict(zip(ascii_lowercase, ascii_uppercase))


def getkey(dct: dict, value: str) -> str:
    "Return key for the value."

    for key, item in dct.items():
        if value == item:
            return key
    raise KeyError(f"key not found for {value}")


def errorhandler(*args, message=None) -> None:
    "Raise Type Error based on the arguments passed to it."

    if message is None:
        message = "expected {} found {}"
    for value, datatype in args:
        if not isinstance(value, datatype):
            raise TypeError(
                message.format(datatype.__name__, type(value).__name__))


def islower(text):
    """Return True if the string is a lowercase string, False otherwise.

    A string is lowercase if all cased characters in the string are lowercase and there is at least one cased character in the string."""

    errorhandler([text, str])

    is_true = False
    for char in text:
        if char in ascii_letters:
            if char in ascii_uppercase:
                return False
            if not is_true:
                is_true = True
    return is_true


def isupper(text):
    """Return True if the string is an uppercase string, False otherwise.

    A string is uppercase if all cased characters in the string are uppercase and there is at least one cased character in the string."""

    errorhandler([text, str])

    is_true = False
    for char in text:
        if char in ascii_letters:
            if char in ascii_lowercase:
                return False
            if not is_true:
                is_true = True
    return is_true


def isalpha(text):
    """Return True if the string is an alphabetic string, False otherwise.

    A string is alphabetic if all characters in the string are alphabetic and there is at least one character in the string."""

    errorhandler([text, str])

    if len(text) == 0:
        return False

    for char in text:
        if char not in ascii_letters:
            return False
    return True


def isdecimal(text):
    """Return True if the string is a decimal string, False otherwise.

    A string is a decimal string if all characters in the string are decimal and there is at least one character in the string."""

    errorhandler([text, str])

    if len(text) == 0:
        return False

    for char in text:
        if char not in digits:
            return False
    return True


def isalnum(text):
    """Return True if the string is an alphanumeric string, False otherwise.

    A string is alphanumeric if all characters in the string are alphanumeric and there is at least one character in the string."""

    errorhandler([text, str])

    if len(text) == 0:
        return False

    ascii_alphanumeric = ascii_letters + digits
    for char in text:
        if char not in ascii_alphanumeric:
            return False
    return True


def istitle(text):
    """Return a version of the string where each word is titlecased.

    More specifically, words start with uppercased characters and all remaining cased characters have lower case."""

    errorhandler([text, str])

    is_true = True
    is_title = False
    for char in text:
        if char in ascii_letters:
            if is_true:
                if char in ascii_lowercase:
                    return False
                if not is_title:
                    is_title = True
            elif char not in ascii_lowercase:
                return False
            is_true = False
        else:
            is_true = True
    return is_title


def isspace(text):
    """Return True if the string is a whitespace string, False otherwise.

    A string is whitespace if all characters in the string are whitespace and there is at least one character in the string."""

    errorhandler([text, str])

    if len(text) == 0:
        return False

    for char in text:
        if char not in whitespace:
            return False
    return True


def isprintable(text):
    """Return True if the string is printable, False otherwise.

    A string is printable if all of its characters are considered printable in repr() or if it is empty."""

    errorhandler([text, str])

    for char in text:
        if char not in printable:
            return False
    return True


def lower(text):
    "Return a copy of the string converted to lowercase."

    errorhandler([text, str])

    letters = ""
    for char in text:
        if char in ascii_letters:
            if char in ascii_lowercase:
                letters += char
            else:
                letters += getkey(ascii_letters_pairs, char)
        else:
            letters += char
    return letters


def upper(text):
    "Return a copy of the string converted to uppercase."

    errorhandler([text, str])

    letters = ""
    for char in text:
        if char in ascii_letters:
            if char in ascii_uppercase:
                letters += char
            else:
                letters += ascii_letters_pairs[char]
        else:
            letters += char
    return letters


def swapcase(text):
    "Convert uppercase characters to lowercase and lowercase characters to uppercase."

    errorhandler([text, str])

    letters = ""
    for char in text:
        if char in ascii_letters:
            if char in ascii_lowercase:
                letters += ascii_letters_pairs[char]
            else:
                letters += getkey(ascii_letters_pairs, char)
        else:
            letters += char
    return letters


def capitalize(text):
    """Return a capitalized version of the string.

    More specifically, make the first character have upper case and the rest lower case."""

    errorhandler([text, str])

    letters = upper(text[0])
    for char in text[1:]:
        letters += lower(char)
    return letters


def title(text):
    """Return a version of the string where each word is titlecased.

    More specifically, words start with uppercased characters and all remaining cased characters have lower case."""

    errorhandler([text, str])

    letters, is_true = "", True
    for char in text:
        if char in ascii_letters:
            if is_true:
                if char in ascii_lowercase:
                    letters += upper(char)
                else:
                    letters += char
            else:
                letters += lower(char)
            is_true = False
        else:
            is_true = True
            letters += char
    return letters


def ljust(text, width, fillchar=" "):
    """Return a left-justified string of length width.

    Padding is done using the specified fill character (default is a space)."""

    errorhandler([text, str], [width, int], [fillchar, str])

    n_allign = width - len(text)
    return text + fillchar * n_allign


def rjust(text, width, fillchar=" "):
    """Return a right-justified string of length width.

    Padding is done using the specified fill character (default is a space)."""

    errorhandler([text, str], [width, int], [fillchar, str])

    n_allign = width - len(text)
    return fillchar * n_allign + text


def center(text, width, fillchar=" "):
    """Return a centered string of length width.

    Padding is done using the specified fill character (default is a space)."""

    errorhandler([text, str], [width, int], [fillchar, str])

    n_allign = width - len(text)
    return (fillchar * (n_allign if n_allign == 1 else n_allign // 2)) + text + (fillchar * (n_allign // 2))


def zfill(text, width):
    """Pad a numeric string with zeros on the left, to fill a field of the given width.

    The string is never truncated."""

    errorhandler([text, str], [width, int])

    n_zero = width - len(text) if width > 1 else 0
    if text[0] == "+":
        sign = "+"
    elif text[0] == "-":
        sign = "-"
    else:
        sign = ""

    return sign + "0" * n_zero + (text if sign == "" else text[1:])


def expandtabs(text, tabsize=8):
    """Return a copy where all tab characters are expanded using spaces.

    If tabsize is not given, a tab size of 8 characters is assumed."""

    errorhandler([text, str], [tabsize, int])

    letters = ""
    for char in text:
        if char == "\t":
            letters += " " * tabsize
        else:
            letters += char
    return letters


def partition(text, sep):
    """Partition the string into three parts using the given separator.
    This will search for the separator in the string.  If the separator is found,
    returns a 3-tuple containing the part before the separator, the separator
    itself, and the part after it. If the separator is not found,
    returns a 3-tuple containing the original string and two empty strings."""

    errorhandler([text, str], [sep, str])

    len_sep = len(sep)
    for i in range(len(text)):
        if sep == text[i: i+len_sep]:
            return (text[0: i], text[i: i+len_sep], text[i+len_sep:])

    return (text, '', '')


def rpartition(text, sep):
    """Partition the string into three parts using the given separator.
    This will search for the separator in the string, starting at the end.
    If the separator is found, returns a 3-tuple containing the part before the
    separator, the separator itself, and the part after it. If the separator is not found,
    returns a 3-tuple containing two empty strings and the original string."""

    errorhandler([text, str], [sep, str])

    len_sep = len(sep)
    for i in range(len(text)-1, -1, -1):
        if sep == text[i: i+len_sep]:
            return (text[0: i], text[i: i+len_sep], text[i+len_sep:])

    return (text, '', '')


def splitlines(text, keepends=False):
    """Return a list of the lines in the string, breaking at line boundaries.

    Line breaks are not included in the resulting list unless keepends is given and true."""

    errorhandler([text, str], [keepends, bool])

    line_breaks = "\n\r\v\f"
    letters, output = "", []
    for char in text:
        if char in line_breaks:
            if keepends:
                output.append(letters+char)
            else:
                output.append(letters)
            # re-assigning empty string
            # to clear previous strings
            letters = ""
        else:
            letters += char

    if text and char not in line_breaks:
        output.append(letters)
    return output


def removeprefix(text, prefix):
    """Return a str with the given prefix string removed if present.

    If the string starts with the prefix string, return string[len(prefix):].
    Otherwise, return a copy of the original string."""

    errorhandler([text, str], [prefix, str],
                 message="removeprefix() argument must be str, not {1}")

    if prefix not in text:
        return text

    sep = tuple(prefix)
    i, length = 0, len(text)
    while i < length and startswith(text[i], sep):
        i += 1

    return text[i: length]


def removesuffix(text, suffix):
    """Return a str with the given suffix string removed if present.

    If the string ends with the suffix string and that suffix is not empty,
    return string[:-len(suffix)]. Otherwise, return a copy of the original string."""

    errorhandler([text, str], [suffix, str],
                 message="removesuffix() argument must be str, not {1}")

    if suffix not in text:
        return text

    sep = tuple(suffix)
    j = len(text)-1
    while j > 1 and startswith(text[j], sep):
        j -= 1

    return text[0: j+1]


def startswith(text, prefix, start=0, end=None):
    """Return True if text starts with the specified prefix, False otherwise.

    With optional start, test text beginning at that position.
    With optional end, stop comparing text at that position.
    Prefix can also be a tuple of strings to try."""

    errorhandler([text, str], [start, int])
    if end is not None: errorhandler([end, int])

    if end is None: end = len(text)
    text = text[start: end]
    if isinstance(prefix, str):
        return prefix == text[:len(prefix)]

    if not isinstance(prefix, tuple):
        raise TypeError(
            f"startswith second arg must be str or a tuple of str, not {type(prefix).__name__}")

    for char in prefix:
        if char == text[:len(char)]:
            return True
        if not isinstance(char, str):
            raise TypeError(
                f"tuple for startswith must only contain str, not {type(char).__name__}")
    return False


def endswith(text, suffix, start=0, end=None):
    """Return True if text ends with the specified suffix, False otherwise.
    With optional start, test text beginning at that position.
    With optional end, stop comparing text at that position.
    suffix can also be a tuple of strings to try."""

    errorhandler([text, str], [start, int])
    if end is not None: errorhandler([end, int])

    if end is None: end = len(text)
    text = text[start: end]
    length = len(text)
    if isinstance(suffix, str):
        return suffix == text[length-len(suffix): length]

    if not isinstance(suffix, tuple):
        raise TypeError(
            f"endswith second arg must be str or a tuple of str, not {type(suffix).__name__}")

    for char in suffix:
        if char == text[length-len(char): length]:
            return True
        if not isinstance(char, str):
            raise TypeError(
                f"tuple for endswith must only contain str, not {type(char).__name__}")
    return False


def find(text, sub, start=0, end=None):
    """Return the lowest index in text where substring sub is found,
    such that sub is contained within text[start:end].
    Optional arguments start and end are interpreted as in slice notation.
    Returns -1 on failure."""

    errorhandler([text, str], [sub, str], [start, int])
    if end is not None: errorhandler([end, int])
    # special case for empty strings
    if sub == '':
        return 0

    if end is None:
        end = len(text)
    s_len = len(sub)
    for i in range(start, end):
        if sub == text[i: i+s_len]:
            return i
    return -1


def rfind(text, sub, start=0, end=None):
    """Return the highest index in text where substring sub is found,
    such that sub is contained within text[start:end].
    Optional arguments start and end are interpreted
    as in slice notation. Returns -1 on failure."""

    errorhandler([text, str], [sub, str], [start, int])
    if end is not None: errorhandler([end, int])
    if end is None: end = len(text)
    # special case for empty strings
    if sub == text == '':
        return 0

    if sub == '' and text != '':
        if start == end:
            return end

    s_len = len(sub)
    for i in range(end-1, start-1, -1):
        if sub == text[i: i+s_len]:
            if sub == '':
                return i + 1
            return i
    return -1


def index(text, sub, start=0, end=None):
    """Return the lowest index in text where substring sub is found,
    such that sub is contained within text[start:end].
    Optional arguments start and end are interpreted as in slice notation.
    Raises ValueError when the substring is not found."""

    errorhandler([start, int])
    if end is not None: errorhandler([end, int])

    if end is None: end = len(text)
    if isinstance(text, str):
        # special case for empty strings
        if sub == '':
            return 0

        s_len = len(sub)
        for i in range(start, end):
            if sub == text[i: i+s_len]:
                return i

        raise ValueError("substring not found")

    if not hasattr(text, '__getitem__'):
        raise TypeError(
            f"{type(text).__name__!r} object is not subscriptable")

    for i in range(start, end):
        if sub == text[i]:
            return i

    raise ValueError(f"{sub!r} is not in {type(text).__name__}")


def rindex(text, sub, start=0, end=None):
    """Return the highest index in text where substring sub is found,
    such that sub is contained within text[start:end].
    Optional arguments start and end are interpreted as in slice notation.
    Raises ValueError when the substring is not found."""

    errorhandler([text, str], [sub, str], [start, int])
    if end is not None: errorhandler([end, int])
    # special case for empty strings
    if sub == text == '':
        return 0

    if sub == '' and text != '':
        if start == end:
            return end

    len_sub = len(sub)
    if end is None: end = len(text)
    for i in range(end, start-1, -1):
        if sub == text[i: i+len_sub]:
            if sub == '':
                return i + 1
            return i

    raise ValueError("substring not found")


def count(text, sub, start=0, end=None):
    """Return the number of non-overlapping occurrences of substring sub in string text[start:end].

    Optional arguments start and end are interpreted as in slice notation."""

    errorhandler([start, int])
    if end is not None: errorhandler([end, int])

    if end is None: end = len(text)
    _count = 0  # holds substring occurrences
    if isinstance(text, str):
        #! issue with counting empty string
        #! returns wrong result for this case
        s_len = len(sub)
        for i in range(start, end):
            if sub == text[i: i+s_len]:
                _count += 1

        if s_len == 0:
            return _count + 1
        return _count

    if not hasattr(text, '__getitem__'):
        raise TypeError(
            f"{type(text).__name__!r} object is not subscriptable")

    for i in range(start, end):
        if sub == text[i]:
            _count += 1
    return _count


def join(text, iterable):
    """Concatenate any number of strings.

    The string whose method is called is inserted in between each given string.
    The result is returned as a new string.

    Example: join('.', ['ab', 'pq', 'rs']) -> 'ab.pq.rs'"""

    errorhandler([text, str])
    try:
        it = iter(iterable)
    except TypeError:
        raise TypeError("can only join an iterable") from None

    letters = ""
    try:
        for idx, char in enumerate(it):
            letters += char + text
    except TypeError:
        raise TypeError(
            f"sequence item {idx}: expected str instance, {type(char).__name__} found") from None
    return letters


def replace(text, old, new, count=-1):
    """Returns a copy with all occurrences of substring old replaced by new.
    count
       Maximum number of occurrences to replace.
       -1 (the default value) means replace all occurrences.
    If the optional argument count is given, only the first count occurrences are replaced."""

    # Checks for valid arguments and raises error if not valid
    errorhandler([text, str], [old, str], [new, str], [count, int])

    c = float('-inf') if count < 0 else 0
    letters, old_len = "", len(old)
    i = 0; length = len(text)
    while i < length:
        if old == text[i: i+old_len]:
            if c < count:
                letters += new
                i += old_len-1
                count -= 1
            else:
                letters += text[i]
        else:
            letters += text[i]
        i += 1
    return letters


LEFTSTRIP = 0
RIGHSTRIP = 1
BOTHSTRIP = 2


def do_strip(text, striptype):
    i = 0; length = len(text)
    if striptype != RIGHSTRIP:
        while i < length and isspace(text[i]):
            i += 1

    j = length-1
    if striptype != LEFTSTRIP:
        while (1 < j and isspace(text[j])):
            j -= 1

    return text[i: j+1]


def do_argstrip(text, striptype, chars):
    sep = tuple(chars)
    i = 0; length = len(text)
    if striptype != RIGHSTRIP:
        while i < length and startswith(text[i], sep):
            i += 1

    j = length-1
    if striptype != LEFTSTRIP:
        while 1 < j and startswith(text[j], sep):
            j -= 1

    return text[i: j+1]


def strip(text, chars=None):
    """Return a copy of the string S with leading and trailing whitespace removed.

    If chars is given and not None, remove characters in chars instead."""

    errorhandler([text, str])
    if chars is not None:
        errorhandler([chars, str])

    if chars is None:
        return do_strip(text, BOTHSTRIP)
    else:
        return do_argstrip(text, BOTHSTRIP, chars)


def lstrip(text, chars=None):
    """Return a copy of the string text with leading whitespace removed.

    If chars is given and not None, remove characters in chars instead."""

    errorhandler([text, str])
    if chars is not None:
        errorhandler([chars, str])

    if chars is None:
        return do_strip(text, LEFTSTRIP)
    else:
        return do_argstrip(text, LEFTSTRIP, chars)


def rstrip(text, chars=None):
    """Return a copy of the string text with trailing whitespace removed.

    If chars is given and not None, remove characters in chars instead."""

    errorhandler([text, str])
    if chars is not None:
        errorhandler([chars, str])

    if chars is None:
        return do_strip(text, RIGHSTRIP)
    else:
        return do_argstrip(text, RIGHSTRIP, chars)


def do_split(text, split_type, maxsplit=-1):
    c = float('-inf') if maxsplit < 0 else 0
    letters, indexes, output = "", (), []

    length = len(text)
    j = length-1
    if split_type == LEFTSTRIP:
        i = 0; text = lstrip(text)
        while i < length:
            if isspace(text[i]):
                if c < maxsplit:
                    indexes += (i,)
                    if i < j and not isspace(text[i+1]):
                        maxsplit -= 1
            i += 1
    else:
        text = rstrip(text)
        while j > -1:
            if isspace(text[j]):
                if c < maxsplit:
                    indexes += (j,)
                    if j > 0 and not isspace(text[j-1]):
                        maxsplit -= 1
            j -= 1
    idx = 0
    while idx < length:
        if idx in indexes:
            output.append(letters)
            # re-assigning to clear
            # pervious stored strings
            letters = ""
        else:
            letters += text[idx]
        idx += 1
    output.append(letters)
    # removing all whitespace elements
    out = [x for x in output if x != ""]
    # removing extra whitespaces of the elements
    if split_type == LEFTSTRIP:
        return [lstrip(x) for x in out]
    else:
        return [rstrip(x) for x in out]


def do_argsplit(text, split_type, sep, maxsplit=-1):
    c = float('-inf') if maxsplit < 0 else 0
    letters, indexes, output = "", (), []

    sep_len = len(sep)
    length = len(text)
    if split_type == LEFTSTRIP:
        i = 0
        while i < length:
            if sep == text[i: i+sep_len]:
                if c < maxsplit:
                    indexes += (i,)
                    maxsplit -= 1
            i += 1
    else:
        j = length-1
        while j > -1:
            if sep == text[j-(sep_len-1): j+1]:
                if c < maxsplit:
                    indexes += (j-(sep_len-1),)
                    maxsplit -= 1
            j -= 1
    idx = 0
    while idx < length:
        if idx in indexes:
            output.append(letters)
            # re-assigning empty string
            # to clear previous strings
            letters = ""
            idx += sep_len-1
        else:
            letters += text[idx]
        idx += 1
    output.append(letters)
    return output


def split(text, sep=None, maxsplit=-1):
    """Return a list of the words in the string, using sep as the delimiter string.
    sep
        The delimiter according which to split the string.
        None (the default value) means split according to any whitespace,
        and discard empty strings from the result.
    maxsplit
        Maximum number of splits to do.
        -1 (the default value) means no limit.
    """

    # Checks for valid arguments and raises error if not valid
    errorhandler([text, str], [maxsplit, int])
    if sep is not None: errorhandler([sep, str])
    if sep == '':
        raise ValueError("empty separator")

    if sep is None:
        return do_split(text, LEFTSTRIP, maxsplit)
    else:
        return do_argsplit(text, LEFTSTRIP, sep, maxsplit)


def rsplit(text, sep=None, maxsplit=-1):
    """Return a list of the words in the string, using sep as the delimiter string.
    sep
        The delimiter according which to split the string.
        None (the default value) means split according to any whitespace,
        and discard empty strings from the result.
    maxsplit
        Maximum number of splits to do.
        -1 (the default value) means no limit.
    """

    # Checks for valid arguments and raises error if not valid
    errorhandler([text, str], [maxsplit, int])
    if sep is not None: errorhandler([sep, str])
    if sep == '':
        raise ValueError("empty separator")

    if sep is None:
        return do_split(text, RIGHSTRIP, maxsplit)
    else:
        return do_argsplit(text, RIGHSTRIP, sep, maxsplit)