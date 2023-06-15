from sys import getdefaultencoding
from typing import Iterable, LiteralString, Self

from _types import FormatMapMapping, ReadableBuffer, TranslateTable
from string_methods import *


class Str:
    """Str(bytes_or_buffer[, encoding[, errors]]) -> Str

    Create a new string object from the given object. If encoding or
    errors is specified, then the object must expose a data buffer
    that will be decoded using the given encoding and error handler.
    Otherwise, returns the result of object.__str__() (if defined)
    or repr(object).
    encoding defaults to sys.getdefaultencoding().
    errors defaults to 'strict'.
    """

    def __init__(self, obj: ReadableBuffer = '', /, *,
                 encoding: str = getdefaultencoding(), errors: str = 'strict') -> None:

        is_default = encoding == getdefaultencoding() and errors == 'strict'
        if isinstance(obj, str) and is_default:
            self.__data = obj
        elif isinstance(obj, self.__class__) and is_default:
            self.__data = obj.__data[:]
        elif is_default:
            self.__data = str(obj)
        else:
            self.__data = str(obj, encoding, errors)  # type: ignore

    def __str__(self, /) -> str:
        return self.__data

    def __repr__(self, /) -> str:
        return f"{self.__class__.__name__}({self.__data!r})"

    def __int__(self, /) -> int:
        return int(self.__data)

    def __float__(self, /) -> float:
        return float(self.__data)

    def __complex__(self, /) -> complex:
        return complex(self.__data)

    def __hash__(self, /) -> int:
        return hash(self.__data)

    def __getnewargs__(self, /) -> tuple[str]:
        return (self.__data[:],)

    def __len__(self, /) -> int:
        return len(self.__data)

    def __sizeof__(self, /) -> int:
        return self.__data.__sizeof__()

    def __getitem__(self, key: int | slice, /) -> Self:
        return self.__class__(self.__data[key])

    def __eq__(self, value: object, /) -> bool:
        return self.__data == self.__cast(value)  # type: ignore

    def __ne__(self, value: object, /) -> bool:
        return self.__data != self.__cast(value)  # type: ignore

    def __lt__(self, value: Self | str, /) -> bool:
        return self.__data < self.__cast(value)

    def __le__(self, value: Self | str, /) -> bool:
        return self.__data <= self.__cast(value)

    def __gt__(self, value: Self | str, /) -> bool:
        return self.__data > self.__cast(value)

    def __ge__(self, value: Self | str, /) -> bool:
        return self.__data >= self.__cast(value)

    def __cast(self, value: Self | str, /) -> str:
        if isinstance(value, self.__class__):
            return value.__data
        return value  # type: ignore

    def __contains__(self, value: Self | str, /) -> bool:
        return self.__cast(value) in self.__data

    def __add__(self, value: Self | str, /) -> Self:
        return self.__class__(self.__data + self.__cast(value))

    def __radd__(self, value: Self | str, /) -> Self:
        return self.__class__(self.__cast(value) + self.__data)

    def __mul__(self, value: int, /) -> Self:
        return self.__class__(self.__data * value)

    def __rmul__(self, value: int, /) -> Self:
        return self.__class__(value * self.__data)

    def __mod__(self, value: Self | str, /) -> Self:
        return self.__class__(self.__data % self.__cast(value))

    def __format__(self, format_spec: str, /) -> str:
        return self.__data.__format__(format_spec)

    maketrans = str.maketrans

    def translate(self, /, _table: TranslateTable) -> Self:
        """Replace each character in the string using the given translation table.

        table
          Translation table, which must be a mapping of Unicode ordinals to
          Unicode ordinals, strings, or None.

        The table must implement lookup/indexing via __getitem__, for instance a
        dictionary or list.  If this operation raises LookupError, the character is
        left untouched.  Characters mapped to None are deleted.
        """
        return self.__class__(self.__data.translate(_table))

    def encode(self, /, encoding: str = 'utf-8', errors: str = 'strict') -> bytes:
        """Encode the string using the codec registered for encoding.

        encoding
            The encoding in which to encode the string.
        errors
            The error handling scheme to use for encoding errors.
            The default is 'strict' meaning that encoding errors raise a
            UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
            'xmlcharrefreplace' as well as any other name registered with
            codecs.register_error that can handle UnicodeEncodeErrors.
        """
        return self.__data.encode(encoding, errors)

    def format(self, /, *args: LiteralString, **kwds: LiteralString) -> str:
        """Return a formatted version of S, using substitutions from args and kwargs.

        The substitutions are identified by braces ('{' and '}').
        """
        return self.__data.format(*args, **kwds)

    def format_map(self, /, mapping: FormatMapMapping) -> str:
        """Return a formatted version of S, using substitutions from mapping.

        The substitutions are identified by braces ('{' and '}').
        """
        return self.__data.format_map(mapping)

    def isdigit(self, /) ->bool:
        """Return True if the string is a digit string, False otherwise.

        A string is a digit string if all characters in the string are digits and there
        """
        return self.__data.isdigit()

    def isascii(self, /) ->bool:
        """Return True if all characters in the string are ASCII, False otherwise.

        ASCII characters have code points in the range U+0000-U+007F.
        Empty string is ASCII too.
        """
        return self.__data.isascii()

    def isnumeric(self, /) ->bool:
        """Return True if the string is a numeric string, False otherwise.

        A string is numeric if all characters in the string are numeric and there is at
        least one character in the string.
        """
        return self.__data.isnumeric()

    def isidentifier(self, /) ->bool:
        """Return True if the string is a valid Python identifier, False otherwise.

        Call keyword.iskeyword(s) to test whether string s is a reserved identifier,
        such as "def" or "class".
        """
        return self.__data.isidentifier()

    def casefold(self, /) -> Self:
        "Return a version of the string suitable for caseless comparisons."

        return self.__class__(self.__data.casefold())

    def isdecimal(self, /) -> bool:
        """Return True if the string is a decimal string, False otherwise.

        A string is a decimal string if all characters in the string are
        decimal and there is at least one character in the string.
        """
        return isdecimal(self.__data)

    def isalpha(self, /) -> bool:
        """Return True if the string is an alphabetic string, False otherwise.

        A string is alphabetic if all characters in the string are
        alphabetic and there is at least one character in the string.
        """
        return isalpha(self.__data)

    def isalnum(self, /) -> bool:
        """Return True if the string is an alphanumeric string, False otherwise.

        A string is alphanumeric if all characters in the string are
        alphanumeric and there is at least one character in the string.
        """
        return isalnum(self.__data)

    def islower(self, /) -> bool:
        """Return True if the string is a lowercase string, False otherwise.

        A string is lowercase if all cased characters in the string are
        lowercase and there is at least one cased character in the string.
        """
        return islower(self.__data)

    def isupper(self, /) -> bool:
        """Return True if the string is an uppercase string, False otherwise.

        A string is uppercase if all cased characters in the string are
        uppercase and there is at least one cased character in the string.
        """
        return isupper(self.__data)

    def istitle(self, /) -> bool:
        """Return a version of the string where each word is titlecased.

        More specifically, words start with uppercased characters
        and all remaining cased characters have lower case.
        """
        return istitle(self.__data)

    def isspace(self, /) -> bool:
        """Return True if the string is a whitespace string, False otherwise.

        A string is whitespace if all characters in the string are
        whitespace and there is at least one character in the string.
        """
        return isspace(self.__data)

    def isprintable(self, /) -> bool:
        """Return True if the string is printable, False otherwise.

        A string is printable if all of its characters are
        considered printable in repr() or if it is empty.
        """
        return isprintable(self.__data)

    def lower(self, /) -> Self:
        "Return a copy of the string converted to lowercase."

        return self.__class__(lower(self.__data))

    def upper(self, /) -> Self:
        "Return a copy of the string converted to uppercase."

        return self.__class__(upper(self.__data))

    def swapcase(self, /) -> Self:
        "Converts uppercase characters to lowercase and lowercase characters to uppercase."

        return self.__class__(swapcase(self.__data))

    def capitalize(self, /) -> Self:
        """Return a capitalized version of the string.

        More specifically, make the first character have upper case and the rest lower case.
        """
        return self.__class__(capitalize(self.__data))

    def title(self, /) -> Self:
        """Return a version of the string where each word is titlecased.

        More specifically, words start with uppercased characters
        and all remaining cased characters have lower case.
        """
        return self.__class__(title(self.__data))

    def center(self, /, width: int, fillchar: Self | str = " ") -> Self:
        """Return a centered string of length width.

        Padding is done using the specified fill character (default is a space).
        """
        return self.__class__(center(self.__data, width, self.__cast(fillchar)))

    def ljust(self, /, width: int, fillchar: Self | str = " ") -> Self:
        """Return a left-justified string of length width.

        Padding is done using the specified fill character (default is a space).
        """
        return self.__class__(ljust(self.__data, width, self.__cast(fillchar)))

    def rjust(self, /, width: int, fillchar: str = " ") -> Self:
        """Return a right-justified string of length width.

        Padding is done using the specified fill character (default is a space).
        """
        return self.__class__(rjust(self.__data, width, self.__cast(fillchar)))

    def zfill(self, /, width: int) -> Self:
        """Pad a numeric string with zeros on the left, to fill a field of the given width.

        The string is never truncated.
        """
        return self.__class__(zfill(self.__data, width))

    def expandtabs(self, /, tabsize: int = 8) -> Self:
        """Returns a copy where all tab characters are expanded using spaces.

        If tabsize is not given, a tab size of 8 characters is assumed.
        """
        return self.__class__(expandtabs(self.__data, tabsize))

    def partition(self, /, sep: Self | str) -> tuple[str, str, str]:
        """Partition the string into three parts using the given separator.

        This will search for the separator in the string.  If the separator is found,
        returns a 3-tuple containing the part before the separator, the separator
        itself, and the part after it. If the separator is not found,

        Return a 3-tuple containing the original string and two empty strings.
        """
        return partition(self.__data, self.__cast(sep))

    def rpartition(self, /, sep: Self | str) -> tuple[str, str, str]:
        """Partition the string into three parts using the given separator.

        This will search for the separator in the string, starting at the end.
        If the separator is found, returns a 3-tuple containing the part before the
        separator, the separator itself, and the part after it. If the separator is not found,

        Return a 3-tuple containing two empty strings and the original string.
        """
        return rpartition(self.__data, self.__cast(sep))

    def splitlines(self, /, keepends: bool = False) -> list[str]:
        """Return a list of the lines in the string, breaking at line boundaries.

        Line breaks are not included in the resulting list unless keepends is given and true.
        """
        return splitlines(self.__data, keepends)

    def removeprefix(self, /, prefix: Self | str) -> Self:
        """Return a str with the given prefix string removed if present.

        If the string starts with the prefix string, return string[len(prefix):].
        Otherwise, return a copy of the original string.
        """
        return self.__class__(removeprefix(self.__data, self.__cast(prefix)))

    def removesuffix(self, /, suffix: Self | str) -> Self:
        """Return a str with the given suffix string removed if present.

        If the string ends with the suffix string and that suffix is not empty,
        return string[:-len(suffix)]. Otherwise, return a copy of the original string.
        """
        return self.__class__(removesuffix(self.__data, self.__cast(suffix)))

    def startswith(self, /, prefix: Self | str, start: int = 0, end: int | None = None) -> bool:
        """Return True if self starts with the specified prefix, False otherwise.

        With optional start, test self beginning at that position.
        With optional end, stop comparing self at that position.
        Prefix can also be a tuple of strings to try.
        """
        return startswith(self.__data, self.__cast(prefix), start, end)

    def endswith(self, /, suffix: Self | str, start: int = 0, end: int | None = None) -> bool:
        """Return True if self ends with the specified suffix, False otherwise.

        With optional start, test self beginning at that position.
        With optional end, stop comparing self at that position.
        suffix can also be a tuple of strings to try.
        """
        return endswith(self.__data, self.__cast(suffix), start, end)

    def find(self, /, sub: Self | str, start: int = 0, end: int | None = None) -> int:
        """Return the lowest index in self where substring sub is found,
        such that sub is contained within self[start:end].
        Optional arguments start and end are interpreted as in slice notation.

        Return -1 on failure.
        """
        return find(self.__data, self.__cast(sub), start, end)

    def rfind(self, /, sub: Self | str, start: int = 0, end: int | None = None) -> int:
        """Return the highest index in self where substring sub is found,
        such that sub is contained within self[start:end].

        Optional arguments start and end are interpreted as in slice notation.

        Return -1 on failure.
        """
        return rfind(self.__data, self.__cast(sub), start, end)

    def index(self, /, sub: Self | str, start: int = 0, end: int | None = None) -> int:
        """Return the lowest index in self where substring sub is found,
        such that sub is contained within self[start:end].

        Optional arguments start and end are interpreted as in slice notation.

        Raise ValueError when the substring is not found.
        """
        return index(self.__data, self.__cast(sub), start, end)

    def rindex(self, /, sub: Self | str, start: int = 0, end: int | None = None) -> int:
        """Return the highest index in self where substring sub is found,
        such that sub is contained within self[start:end].

        Optional arguments start and end are interpreted as in slice notation.

        Raise ValueError when the substring is not found.
        """
        return rindex(self.__data, self.__cast(sub), start, end)

    def count(self, /, sub: Self | str, start: int = 0, end: int | None = None) -> int:
        """Return the number of non-overlapping occurrences of substring sub in string self[start:end].

        Optional arguments start and end are interpreted as in slice notation.
        """
        return count(self.__data, self.__cast(sub), start, end)

    def join(self, /, iterable: Iterable[str]) -> Self:
        """Concatenate any number of strings.

        The string whose method is called is inserted in between each given string.
        The result is returned as a new string.

        Example: join('.', ['ab', 'pq', 'rs']) -> 'ab.pq.rs'
        """
        return self.__class__(join(self.__data, iterable))

    def replace(self, /, old: Self | str, new: Self | str, maxsplit: int = -1) -> Self:
        """Return a copy with all occurrences of substring old replaced by new.

        count
            Maximum number of occurrences to replace.
            -1 (the default value) means replace all occurrences.

        If the optional argument count is given, only the first count occurrences are replaced.
        """
        return self.__class__(replace(self.__data, self.__cast(old), self.__cast(new), maxsplit))

    def strip(self, /, chars: Self | str | None = None) -> Self:
        """Return a copy of the string S with leading and trailing whitespace removed.

        If chars is given and not None, remove characters in chars instead.
        """
        return self.__class__(strip(self.__data, self.__cast(chars)))  # type: ignore

    def lstrip(self, /, chars: Self | str | None = None) -> Self:
        """Return a copy of the string self with leading whitespace removed.

        If chars is given and not None, remove characters in chars instead.
        """
        return self.__class__(lstrip(self.__data, self.__cast(chars)))  # type: ignore

    def rstrip(self, /, chars: Self | str | None = None) -> Self:
        """Return a copy of the string self with trailing whitespace removed.

        If chars is given and not None, remove characters in chars instead.
        """
        return self.__class__(rstrip(self.__data, self.__cast(chars)))  # type: ignore

    def split(self, /, sep: Self | str | None = None, maxsplit: int = -1) -> list[str]:
        """Return a list of the words in the string, using sep as the delimiter string.

        sep
            The delimiter according which to split the string.
            None (the default value) means split according to any whitespace,
            and discard empty strings from the result.
        maxsplit
            Maximum number of splits to do.
            -1 (the default value) means no limit.
        """
        return split(self.__data, self.__cast(sep), maxsplit)  # type: ignore

    def rsplit(self, /, sep: str | Self | None = None, maxsplit: int = -1) -> list[str]:
        """Return a list of the words in the string, using sep as the delimiter string.

        sep
            The delimiter according which to split the string.
            None (the default value) means split according to any whitespace,
            and discard empty strings from the result.
        maxsplit
            Maximum number of splits to do.
            -1 (the default value) means no limit.
        """
        return rsplit(self.__data, self.__cast(sep), maxsplit)  # type: ignore
