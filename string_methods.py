"""
This module re-implements existing string methods
in python as functions, based on their output
during execution. it's written to Imitate those
methods, it's not intended to be used in programs.

Note: This module doesn't support unicode characters.

"""

from typing import Iterable

from _types import verify_type

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


def getkey(dct: dict[str, str], value: str) -> str:
    "Return key for the value."

    for key, item in dct.items():
        if value == item:
            return key
    raise KeyError(f"key not found for {value}")


def islower(text: str) -> bool:
    """Return True if the string is a lowercase string, False otherwise.

    A string is lowercase if all cased characters in the string are
    lowercase and there is at least one cased character in the string.
    """
    verify_type([text, str])

    is_lowercase = False
    for char in text:
        if char in ascii_letters:
            if char in ascii_uppercase:
                return False
            if not is_lowercase:
                is_lowercase = True
    return is_lowercase


def isupper(text: str) -> bool:
    """Return True if the string is an uppercase string, False otherwise.

    A string is uppercase if all cased characters in the string are
    uppercase and there is at least one cased character in the string.
    """
    verify_type([text, str])

    is_uppercase = False
    for char in text:
        if char in ascii_letters:
            if char in ascii_lowercase:
                return False
            if not is_uppercase:
                is_uppercase = True
    return is_uppercase


def isalpha(text: str) -> bool:
    """Return True if the string is an alphabetic string, False otherwise.

    A string is alphabetic if all characters in the string are
    alphabetic and there is at least one character in the string.
    """
    verify_type([text, str])

    if not text:
        return False

    for char in text:
        if char not in ascii_letters:
            return False
    return True


def isdecimal(text: str) -> bool:
    """Return True if the string is a decimal string, False otherwise.

    A string is a decimal string if all characters in the string
    are decimal and there is at least one character in the string.
    """
    verify_type([text, str])

    if not text:
        return False

    for char in text:
        if char not in digits:
            return False
    return True


def isalnum(text: str) -> bool:
    """Return True if the string is an alphanumeric string, False otherwise.

    A string is alphanumeric if all characters in the string are
    alphanumeric and there is at least one character in the string.
    """
    verify_type([text, str])

    if not text:
        return False

    ascii_alphanumeric = ascii_letters + digits
    for char in text:
        if char not in ascii_alphanumeric:
            return False
    return True


def istitle(text: str) -> bool:
    """Return a version of the string where each word is titlecased.

    More specifically, words start with uppercased characters
    and all remaining cased characters have lower case.
    """
    verify_type([text, str])

    title_cased = False
    check_lowercase = True
    for char in text:
        if char not in ascii_letters:
            check_lowercase = True
            continue
        if check_lowercase:
            if char in ascii_lowercase:
                return False
            if not title_cased:
                title_cased = True
        elif char not in ascii_lowercase:
            return False
        check_lowercase = False
    return title_cased


def isspace(text: str) -> bool:
    """Return True if the string is a whitespace string, False otherwise.

    A string is whitespace if all characters in the string are
    whitespace and there is at least one character in the string.
    """
    verify_type([text, str])

    if not text:
        return False

    for char in text:
        if char not in whitespace:
            return False
    return True


def isprintable(text: str) -> bool:
    """Return True if the string is printable, False otherwise.

    A string is printable if all of its characters are
    considered printable in repr() or if it is empty.
    """
    verify_type([text, str])

    for char in text:
        if char not in printable:
            return False
    return True


def lower(text: str) -> str:
    "Return a copy of the string converted to lowercase."

    verify_type([text, str])

    result = ""
    for char in text:
        if char not in ascii_letters:
            result += char
            continue
        if char in ascii_lowercase:
            result += char
        else:
            result += getkey(ascii_letters_pairs, char)
    return result


def upper(text: str) -> str:
    "Return a copy of the string converted to uppercase."

    verify_type([text, str])

    result = ""
    for char in text:
        if char not in ascii_letters:
            result += char
            continue
        if char in ascii_uppercase:
            result += char
        else:
            result += ascii_letters_pairs[char]
    return result


def swapcase(text: str) -> str:
    "Convert uppercase characters to lowercase and lowercase characters to uppercase."

    verify_type([text, str])

    result = ""
    for char in text:
        if char not in ascii_letters:
            result += char
            continue
        if char in ascii_lowercase:
            result += ascii_letters_pairs[char]
        else:
            result += getkey(ascii_letters_pairs, char)
    return result


def capitalize(text: str) -> str:
    """Return a capitalized version of the string.

    More specifically, make the first character have upper case and the rest lower case.
    """
    verify_type([text, str])

    if not text:
        return text

    result = upper(text[0])
    for char in text[1:]:
        result += lower(char)
    return result


def title(text: str) -> str:
    """Return a version of the string where each word is titlecased.

    More specifically, words start with uppercased characters
    and all remaining cased characters have lower case.
    """
    verify_type([text, str])

    result = ""
    check = True
    for char in text:
        if char not in ascii_letters:
            result += char
            check = True
            continue
        if check:
            if char in ascii_lowercase:
                result += upper(char)
            else:
                result += char
        else:
            result += lower(char)
        check = False
    return result


def ljust(text: str, width: int, fillchar: str = " ") -> str:
    """Return a left-justified string of length width.

    Padding is done using the specified fill character (default is a space).
    """
    verify_type([text, str], [width, int], [fillchar, str])

    n_allign = width - len(text)
    return text + fillchar * n_allign


def rjust(text: str, width: int, fillchar: str = " ") -> str:
    """Return a right-justified string of length width.

    Padding is done using the specified fill character (default is a space).
    """
    verify_type([text, str], [width, int], [fillchar, str])

    n_allign = width - len(text)
    return fillchar * n_allign + text


def center(text: str, width: int, fillchar: str = " ") -> str:
    """Return a centered string of length width.

    Padding is done using the specified fill character (default is a space).
    """
    verify_type([text, str], [width, int], [fillchar, str])

    n_allign = width - len(text)
    return (fillchar * (n_allign if n_allign == 1 else n_allign // 2)) \
        + text + (fillchar * (n_allign // 2))


def zfill(text: str, width: int) -> str:
    """Pad a numeric string with zeros on the left, to fill a field of the given width.

    The string is never truncated.
    """
    verify_type([text, str], [width, int])

    n_zero = width - len(text) if width > 1 else 0
    if text[0] == "+":
        sign = "+"
    elif text[0] == "-":
        sign = "-"
    else:
        sign = ""
    return sign + "0" * n_zero + (text if sign == "" else text[1:])


def expandtabs(text: str, tabsize: int = 8):
    """Return a copy where all tab characters are expanded using spaces.

    If tabsize is not given, a tab size of 8 characters is assumed.
    """
    verify_type([text, str], [tabsize, int])

    result = ""
    for char in text:
        if char == "\t":
            result += " " * tabsize
        else:
            result += char
    return result


def partition(text: str, sep: str) -> tuple[str, str, str]:
    """Partition the string into three parts using the given separator.

    This will search for the separator in the string.  If the separator is found,
    returns a 3-tuple containing the part before the separator, the separator
    itself, and the part after it. If the separator is not found,
    returns a 3-tuple containing the original string and two empty strings.
    """
    verify_type([text, str], [sep, str])

    sep_len = len(sep)
    for i in range(len(text)):
        if sep == text[i: i + sep_len]:
            return (
                text[0: i],
                text[i: i + sep_len],
                text[i + sep_len:]
            )
    return (text, '', '')


def rpartition(text: str, sep: str) -> tuple[str, str, str]:
    """Partition the string into three parts using the given separator.

    This will search for the separator in the string, starting at the end.
    If the separator is found, returns a 3-tuple containing the part before the
    separator, the separator itself, and the part after it. If the separator is not found,
    returns a 3-tuple containing two empty strings and the original string.
    """
    verify_type([text, str], [sep, str])

    sep_len = len(sep)
    for i in range(len(text) - 1, -1, -1):
        if sep == text[i: i + sep_len]:
            return (
                text[0: i],
                text[i: i + sep_len],
                text[i + sep_len:]
            )
    return (text, '', '')


def splitlines(text: str, keepends: bool = False) -> list[str]:
    """Return a list of the lines in the string, breaking at line boundaries.

    Line breaks are not included in the resulting list unless keepends is given and true.
    """
    verify_type([text, str], [keepends, bool])

    line_breaks = "\n\r\v\f"

    res: str = ""
    result: list[str] = []

    for char in text:
        if char not in line_breaks:
            res += char
            continue  # didn't find line break
        if keepends:
            result.append(res + char)
        else:
            result.append(res)
        res = ""  # clear previous strings

    # if last char isn't in line breaks
    if text and char not in line_breaks:  # type: ignore
        result.append(res)
    return result


def removeprefix(text: str, prefix: str) -> str:
    """Return a str with the given prefix string removed if present.

    If the string starts with the prefix string, return string[len(prefix):].
    Otherwise, return a copy of the original string.
    """
    verify_type([text, str], [prefix, str],
                message="removeprefix() argument must be str, not {1}")

    if not prefix or prefix not in text:
        return text

    sep = tuple(prefix)
    i, length = 0, len(text)
    while i < length and startswith(text[i], sep):
        i += 1
    return text[i: length]


def removesuffix(text: str, suffix: str) -> str:
    """Return a str with the given suffix string removed if present.

    If the string ends with the suffix string and that suffix is not empty,
    return string[:-len(suffix)]. Otherwise, return a copy of the original string.
    """
    verify_type([text, str], [suffix, str],
                message="removesuffix() argument must be str, not {1}")

    if not suffix or suffix not in text:
        return text

    sep = tuple(suffix)
    j = len(text) - 1
    while j > 1 and startswith(text[j], sep):
        j -= 1
    return text[0: j + 1]


def startswith(text: str, prefix: str | tuple[str, ...], start: int = 0, end: int | None = None) -> bool:
    """Return True if text starts with the specified prefix, False otherwise.

    With optional start, test text beginning at that position.
    With optional end, stop comparing text at that position.
    Prefix can also be a tuple of strings to try.
    """
    verify_type([text, str], [start, int])
    if end is not None:
        verify_type([end, int])

    if end is None:
        end = len(text)
    text = text[start: end]

    if isinstance(prefix, str):
        return prefix == text[:len(prefix)]

    if not isinstance(prefix, tuple):  # type: ignore
        raise TypeError(  # if prefix argument is not tuple.
            f"startswith second arg must be str or a tuple of str, not {type(prefix).__name__}")

    for char in prefix:
        if char == text[:len(char)]:
            return True
        if not isinstance(char, str):  # type: ignore
            raise TypeError(  # if any char is not str.
                f"tuple for startswith must only contain str, not {type(char).__name__}")
    return False


def endswith(text: str, suffix: str | tuple[str, ...], start: int = 0, end: int | None = None) -> bool:
    """Return True if text ends with the specified suffix, False otherwise.

    With optional start, test text beginning at that position.
    With optional end, stop comparing text at that position.
    suffix can also be a tuple of strings to try.
    """
    verify_type([text, str], [start, int])
    if end is not None:
        verify_type([end, int])

    if end is None:
        end = len(text)
    text = text[start: end]
    length = len(text)
    if isinstance(suffix, str):
        return suffix == text[length - len(suffix): length]

    if not isinstance(suffix, tuple):  # type: ignore
        raise TypeError(  # if suffix argument is not tuple.
            f"endswith second arg must be str or a tuple of str, not {type(suffix).__name__}")

    for char in suffix:
        if char == text[length - len(char): length]:
            return True
        if not isinstance(char, str):  # type: ignore
            raise TypeError(  # if any char isn't not str.
                f"tuple for endswith must only contain str, not {type(char).__name__}")
    return False


def find(text: str, sub: str, start: int = 0, end: int | None = None) -> int:
    """Return the lowest index in text where substring sub is found,
    such that sub is contained within text[start:end].

    Optional arguments start and end are interpreted as in slice notation.

    Return -1 on failure.
    """
    verify_type([text, str], [sub, str], [start, int])
    if end is not None:
        verify_type([end, int])

    s_len = len(sub)
    if end is None:
        end = len(text)

    # special case for empty strings
    if s_len == 0:
        return 0

    for i in range(start, end):
        if sub == text[i: i + s_len]:
            return i
    return -1


def rfind(text: str, sub: str, start: int = 0, end: int | None = None) -> int:
    """Return the highest index in text where substring sub is found,
    such that sub is contained within text[start:end].

    Optional arguments start and end are interpreted as in slice notation.

    Return -1 on failure.
    """
    verify_type([text, str], [sub, str], [start, int])
    if end is not None:
        verify_type([end, int])

    s_len = len(sub)
    if end is None:
        end = len(text)

    # special case for empty strings
    if s_len == 0:
        if text == '':
            return 0
        else:
            return end

    for i in range(end - 1, start - 1, -1):
        if sub == text[i: i + s_len]:
            return i
    return -1


def index(text: str, sub: str, start: int = 0, end: int | None = None) -> int:
    """Return the lowest index in text where substring sub is found,
    such that sub is contained within text[start:end].
    Optional arguments start and end are interpreted as in slice notation.

    Raise ValueError when the substring is not found.
    """
    verify_type([start, int])
    if end is not None:
        verify_type([end, int])

    s_len = len(sub)
    if end is None:
        end = len(text)

    # special case for empty strings
    if s_len == 0:
        return 0

    for i in range(start, end):
        if sub == text[i: i + s_len]:
            return i
    raise ValueError("substring not found")


def rindex(text: str, sub: str, start: int = 0, end: int | None = None) -> int:
    """Return the highest index in text where substring sub is found,
    such that sub is contained within text[start:end].

    Optional arguments start and end are interpreted as in slice notation.

    Raise ValueError when the substring is not found.
    """
    verify_type([text, str], [sub, str], [start, int])
    if end is not None:
        verify_type([end, int])

    len_sub = len(sub)
    if end is None:
        end = len(text)

    # special case for empty strings
    if len_sub == 0:
        if text == '':
            return 0
        else:
            return end

    for i in range(end, start - 1, -1):
        if sub == text[i: i + len_sub]:
            return i
    raise ValueError("substring not found")


def count(text: str, sub: str, start: int = 0, end: int | None = None) -> int:
    """Return the number of non-overlapping occurrences of substring sub in string text[start:end].

    Optional arguments start and end are interpreted as in slice notation.
    """
    verify_type([start, int])
    if end is not None:
        verify_type([end, int])

    s_len = len(sub)
    # special case for empty strings
    if s_len == 0:
        return len(text) + 1

    if end is None:
        end = len(text)

    occurrences = 0
    for i in range(start, end):
        if sub == text[i: i + s_len]:
            occurrences += 1
    return occurrences


def join(text: str, iterable: Iterable[str]) -> str:
    """Concatenate any number of strings.

    The string whose method is called is inserted in between each given string.
    The result is returned as a new string.

    Example: join('.', ['ab', 'pq', 'rs']) -> 'ab.pq.rs
    '"""
    verify_type([text, str])
    try:
        it = iter(iterable)
    except TypeError:
        raise TypeError("can only join an iterable") from None

    result = ""
    try:
        for idx, char in enumerate(it):
            result += char + text
    except TypeError:
        msg = f"sequence item {idx}: expected str instance"  # type: ignore
        raise TypeError(
            f"{msg}, {type(char).__name__} found") from None  # type: ignore
    return result


def replace(text: str, old: str, new: str, count: int = -1) -> str:
    """Return a copy with all occurrences of substring old replaced by new.

    count
       Maximum number of occurrences to replace.
       -1 (the default value) means replace all occurrences.

    If the optional argument count is 
    given, only the first count occurrences are replaced.
    """
    # Checks for valid arguments and raise error if not valid
    verify_type([text, str], [old, str], [new, str], [count, int])

    result: str = ""
    old_len: int = len(old)
    i, length = 0, len(text)
    replace_all = count < 0

    while i < length:
        if old != text[i: i + old_len]:
            result += text[i]
            i += 1
            continue  # match not found
        if count > 0 or replace_all:
            result += new
            i += old_len
            count -= 1
        else:
            result += text[i]
            i += 1
    return result


LEFTSTRIP = 0
RIGHSTRIP = 1
BOTHSTRIP = 2


def do_strip(text: str, striptype: int) -> str:
    i, length = 0, len(text)

    if striptype != RIGHSTRIP:
        while i < length and isspace(text[i]):
            i += 1

    j = length - 1
    if striptype != LEFTSTRIP:
        while (1 < j and isspace(text[j])):
            j -= 1

    return text[i: j + 1]


def do_argstrip(text: str, striptype: int, chars: str) -> str:
    sep = tuple(chars)
    i, length = 0, len(text)

    if striptype != RIGHSTRIP:
        while i < length and startswith(text[i], sep):
            i += 1

    j = length - 1
    if striptype != LEFTSTRIP:
        while 1 < j and startswith(text[j], sep):
            j -= 1

    return text[i: j + 1]


def lstrip(text: str, chars: str | None = None) -> str:
    """Return a copy of the string text with leading whitespace removed.

    If chars is given and not None, remove characters in chars instead.
    """
    verify_type([text, str])
    if chars is not None:
        verify_type([chars, str])

    if chars is None:
        return do_strip(text, LEFTSTRIP)
    else:
        return do_argstrip(text, LEFTSTRIP, chars)


def rstrip(text: str, chars: str | None = None) -> str:
    """Return a copy of the string text with trailing whitespace removed.

    If chars is given and not None, remove characters in chars instead.
    """
    verify_type([text, str])
    if chars is not None:
        verify_type([chars, str])

    if chars is None:
        return do_strip(text, RIGHSTRIP)
    else:
        return do_argstrip(text, RIGHSTRIP, chars)


def strip(text: str, chars: str | None = None) -> str:
    """Return a copy of the string S with leading and trailing whitespace removed.

    If chars is given and not None, remove characters in chars instead.
    """
    verify_type([text, str])
    if chars is not None:
        verify_type([chars, str])

    if chars is None:
        return do_strip(text, BOTHSTRIP)
    else:
        return do_argstrip(text, BOTHSTRIP, chars)


def do_split(text: str, split_type: int, maxsplit: int = -1) -> list[str]:
    if split_type == LEFTSTRIP:
        text = lstrip(text)
    else:
        text = rstrip(text)

    length = len(text)
    indexes: list[int] = []
    do_max_split = maxsplit < 0

    if split_type == LEFTSTRIP:
        for i in range(length - 1):
            if isspace(text[i]) and (maxsplit > 0 or do_max_split):
                indexes.append(i)
                if not isspace(text[i + 1]):
                    maxsplit -= 1
    else:
        for j in range(length - 1, -1, -1):
            if isspace(text[j]) and (maxsplit > 0 or do_max_split):
                indexes.append(j)
                if not isspace(text[j - 1]):
                    maxsplit -= 1

    res: str = ""
    result: list[str] = []
    for idx in range(length):
        if idx in indexes:
            result.append(res)
            res = ""  # clear
        else:
            res += text[idx]
    result.append(res)

    # removing all whitespace
    result = [x for x in result if x != ""]
    # removing extra whitespaces within
    if split_type == LEFTSTRIP:
        return [lstrip(x) for x in result]
    else:
        return [rstrip(x) for x in result]


def do_argsplit(text: str, split_type: int, sep: str, maxsplit: int = -1) -> list[str]:
    sep_len = len(sep)
    length = len(text)
    indexes: list[int] = []
    do_max_split = maxsplit < 0

    if split_type == LEFTSTRIP:
        for i in range(length):
            if sep == text[i: i + sep_len] and (maxsplit > 0 or do_max_split):
                indexes.append(i)
                maxsplit -= 1
    else:
        for j in range(length - 1, -1, -1):
            if sep == text[j - (sep_len - 1): j + 1] and (maxsplit > 0 or do_max_split):
                indexes.append(j - (sep_len - 1))
                maxsplit -= 1

    idx: int = 0
    res: str = ""
    result: list[str] = []
    while idx < length:
        if idx in indexes:
            result.append(res)
            res = ""  # clear
            idx += sep_len
        else:
            res += text[idx]
            idx += 1
    result.append(res)
    return result


def split(text: str, sep: str | None = None, maxsplit: int = -1) -> list[str]:
    """Return a list of the words in the string, using sep as the delimiter string.

    sep
        The delimiter according which to split the string.
        None (the default value) means split according to any whitespace,
        and discard empty strings from the result.
    maxsplit
        Maximum number of splits to do.
        -1 (the default value) means no limit.
    """
    # Checks for valid arguments and raise error if not valid
    verify_type([text, str], [maxsplit, int])
    if sep is not None:
        verify_type([sep, str])

    if sep == '':
        raise ValueError("empty separator")

    if sep is None:
        return do_split(text, LEFTSTRIP, maxsplit)
    else:
        return do_argsplit(text, LEFTSTRIP, sep, maxsplit)


def rsplit(text: str, sep: str | None = None, maxsplit: int = -1) -> list[str]:
    """Return a list of the words in the string, using sep as the delimiter string.

    sep
        The delimiter according which to split the string.
        None (the default value) means split according to any whitespace,
        and discard empty strings from the result.
    maxsplit
        Maximum number of splits to do.
        -1 (the default value) means no limit.
    """
    # Checks for valid arguments and raise error if not valid
    verify_type([text, str], [maxsplit, int])
    if sep is not None:
        verify_type([sep, str])

    if sep == '':
        raise ValueError("empty separator")

    if sep is None:
        return do_split(text, RIGHSTRIP, maxsplit)
    else:
        return do_argsplit(text, RIGHSTRIP, sep, maxsplit)
