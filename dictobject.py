from typing import Generic, Iterable, Iterator, Self, TypeVar, Union

from _types import SupportsKeysAndGetItem
from functions import MISSING, Reversed

K = TypeVar('K')
T = TypeVar('T')
R = TypeVar('R')


class Dict_keys(Generic[K, T]):
    def __init__(self, value: dict[K, T]):
        self.__data: list[K] = []
        for key in value:
            self.__data.append(key)

    def __len__(self, /) -> int:
        return len(self.__data)

    def __iter__(self, /) -> Iterator[K]:
        return iter(self.__data)

    def __reversed__(self, /) -> Reversed[K]:
        class Reverse(Reversed[R]):
            def __repr__(self, /):
                return "<dict_reversekeyiterator object at %s>" % \
                    str(hex(id(self))).replace('x', 'x00000').upper()
        return Reverse(self.__data)

    def __repr__(self, /) -> str:
        return f"{self.__class__.__name__}({self.__data})"


class Dict_values(Generic[K, T]):
    def __init__(self, value: dict[K, T], /) -> None:
        self.__data: list[T] = []
        for key in value:
            self.__data.append(value[key])

    def __len__(self, /) -> int:
        return len(self.__data)

    def __iter__(self, /) -> Iterator[T]:
        return iter(self.__data)

    def __reversed__(self, /) -> Reversed[T]:
        class Reverse(Reversed[R]):
            def __repr__(self, /):
                return "<dict_reversevalueiterator object at %s>" % \
                    str(hex(id(self))).replace('x', 'x00000').upper()

        return Reverse(self.__data)

    def __repr__(self, /) -> str:
        return f"{self.__class__.__name__}({self.__data})"


class Dict_items(Generic[K, T]):
    def __init__(self, value: dict[K, T], /) -> None:
        self.__data: list[tuple[K, T]] = []
        for key in value:
            self.__data.append((key, value[key]))

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, self.__class__):
            return False
        return self.__data == value.__data

    def __ne__(self, value: object, /) -> bool:
        if not isinstance(value, self.__class__):
            return True
        return self.__data != value.__data

    def __lt__(self, value: Self, /) -> bool:
        return self.__data < self.__cast(value, '<')

    def __le__(self, value: Self, /) -> bool:
        return self.__data <= self.__cast(value, '<=')

    def __gt__(self, value: Self, /) -> bool:
        return self.__data > self.__cast(value, '>')

    def __ge__(self, value: Self, /) -> bool:
        return self.__data >= self.__cast(value, '>=')

    def __cast(self, value: Self, symbol: str, /) -> list[tuple[K, T]]:
        if isinstance(value, self.__class__):
            return value.__data
        raise TypeError(
            "unsupported operand type(s) for %s: '%s' and '%s'" % (
                symbol, self.__class__.__name__, type(value).__name__))

    def __and__(self, value: Self, /) -> set[tuple[K, T]]:
        res: set[tuple[K, T]] = set()
        for x in self:
            if x in value:
                res.add(x)
        return res

    __rand__ = __and__

    def __or__(self, value: Self, /) -> set[tuple[K, T]]:
        res = set(self.__data)
        for x in value:
            if x not in res:
                res.add(x)
        return res

    __ror__ = __or__

    def __xor__(self, value: Self, /) -> set[tuple[K, T]]:
        res = set(self.__data)
        for x in value:
            if x in self:
                res.remove(x)
            else:
                res.add(x)
        return res

    __rxor__ = __xor__

    def __sub__(self, value: Self, /) -> set[tuple[K, T]]:
        res = set(self.__data)
        for x in value:
            if x in self:
                res.remove(x)
        return res

    __rsub__ = __sub__

    def __len__(self, /) -> int:
        return len(self.__data)

    def __iter__(self, /) -> Iterator[tuple[K, T]]:
        return iter(self.__data)

    def __repr__(self, /) -> str:
        return f"{self.__class__.__name__}({self.__data})"

    def __reversed__(self, /) -> Reversed[tuple[K, T]]:
        class Reverse(Reversed[R]):
            "Return a reverse iterator over the dict items."

            def __repr__(self, /) -> str:
                return "<dict_reverseitemiterator object at %s>" % \
                    str(hex(id(self))).replace('x', 'x00000').upper()

        return Reverse(self.__data)

    def isdisjoint(self, value: Self, /) -> bool:
        "Return True if the view and the given iterable have a null intersection."

        for x in value:
            if x in self:
                return False
        return True


class Dict(Generic[K, T]):
    """Dict() -> new empty dictionary
    Dict(mapping) -> new dictionary initialized from a mapping object's
        (key, value) pairs
    Dict(iterable) -> new dictionary initialized as if via:
        d = {}
        for k, v in iterable:
            d[k] = v
    Dict(**kwargs) -> new dictionary initialized with the name=value pairs
        in the keyword argument list.  For example:  Dict(one=1, two=2)
    """

    def __init__(self,
                 value: Union[
                     SupportsKeysAndGetItem[K, T],
                     Iterable[tuple[K, T]],
                 ] | object = MISSING, /,
                 **kwargs: T) -> None:

        self.__data: dict[K, T] = {}
        if isinstance(value, type(self.__data)):
            self.__data = value  # type: ignore
        elif isinstance(value, self.__class__):
            self.__data = value.__data  # type: ignore
        else:
            self.update(value)  # type: ignore
        if kwargs:
            self.update(kwargs)  # type: ignore

    def __eq__(self, value: object, /) -> bool:
        return self.__data == self.__cast(value)  # type: ignore

    def __ne__(self, value: object, /) -> bool:
        return self.__data != self.__cast(value)  # type: ignore

    def __or__(self, value: Self | dict[K, T], /) -> Self:
        return self.__class__(self.__data | self.__cast(value))

    def __ror__(self, value: Self | dict[K, T], /) -> Self:
        return self.__class__(self.__cast(value) | self.__data)

    def __ior__(self, value: Self | dict[K, T], /) -> Self:
        self.__data |= self.__cast(value)
        return self

    def __cast(self, value: Self | dict[K, T], /) -> dict[K, T]:
        if isinstance(value, self.__class__):
            return value.__data
        return value  # type: ignore

    def __getitem__(self, key: K, /) -> T:
        return self.__data[key]

    def __setitem__(self, key: K, value: T, /) -> None:
        self.__data[key] = value

    def __delitem__(self, key: K, /) -> None:
        del self.__data[key]

    def __iter__(self, /) -> Iterator[K]:
        return iter(self.__data)

    def __contains__(self, key: K, /) -> bool:
        return key in self.__data

    def __len__(self, /) -> int:
        return len(self.__data)

    def __sizeof__(self, /) -> int:
        return self.__data.__sizeof__()

    def __repr__(self, /) -> str:
        return f"{self.__class__.__name__}({repr(self.__data)})"

    def __copy__(self, /) -> Self:
        inst = self.__class__.__new__(self.__class__)
        inst.__dict__.update(self.__dict__)
        # Create a copy and avoid triggering descriptors
        inst.__dict__[f"_{self.__class__.__name__}__data"] = \
            self.__dict__[f"_{self.__class__.__name__}__data"].copy()
        return inst

    def copy(self, /) -> Self:
        "D.copy() -> a shallow copy of D"

        return self.__class__(self)

    def clear(self, /) -> None:
        "D.clear() -> None.  Remove all items from D."

        self.__data.clear()

    def pop(self, key: K, default: T | None = None, /) -> T:
        """D.pop(k[,d]) -> v, remove specified key and return the corresponding value.

        If the key is not found, return the default if given; otherwise,
        raise a KeyError.
        """
        if key in self.__data:
            return self.__data.pop(key)

        if default is not None:
            return default
        raise KeyError(key)

    def popitem(self, /) -> tuple[K, T]:
        """Remove and return a (key, value) pair as a 2-tuple.

        Pairs are returned in LIFO (last-in, first-out) order.
        Raises KeyError if the dict is empty.
        """
        if not self.__data:
            raise KeyError("'popitem(): dictionary is empty'")

        return self.__data.popitem()

    def setdefault(self, key: K, default: T | None = None, /) -> T:
        """Insert key with a value of default if key is not in the dictionary.

        Return the value for key if key is in the dictionary, else default.
        """
        if key in self.__data:
            return self.__data[key]
        self.__data[key] = default  # type: ignore
        return default  # type: ignore

    def update(self, value: Union[SupportsKeysAndGetItem[K, T], Iterable[tuple[K, T]], ] | object = MISSING, /, **kwargs: T) -> None:
        """D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
        If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
        If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
        In either case, this is followed by: for k in F:  D[k] = F[k]
        """
        def copy(iterable: Iterable[tuple[K, T]], /) -> None:
            idx = 0
            try:
                for k, v in iterable:
                    self.__data[k] = v
                    idx += 1
            except TypeError:
                raise TypeError(
                    f"cannot convert dictionary update sequence element #{idx} to a sequence") from None

        if value is MISSING:
            if kwargs:
                copy(kwargs.items())  # type: ignore
            return

        try:
            if hasattr(value, 'keys'):
                kvs = ((k, value[k]) for k in value.keys())  # type: ignore
            elif hasattr(value, 'items'):
                kvs = value.items()  # type: ignore
            elif isinstance(value, str):
                raise ValueError
            elif iter(value):  # type: ignore
                kvs = value
            else:
                raise TypeError
        except TypeError:
            raise TypeError(
                f"{type(value).__name__!r} object is not iterable") from None
        except ValueError:
            raise ValueError(
                "dictionary update sequence element #0 has length 1; 2 is required") from None
        copy(kvs)  # type: ignore

        if kwargs:
            copy(kwargs.items())  # type: ignore

    def get(self, key: K, default: T | None = None, /) -> T | None:
        "Return the value for key if key is in the dictionary, else default."

        if key in self.__data:
            return self.__data[key]
        return default

    @classmethod
    def fromkeys(cls, iterable: Iterable[K], value: T | None = None, /) -> Self:
        "Create a new dictionary with keys from iterable and values set to value."

        d = cls()
        for key in iterable:
            d[key] = value  # type: ignore
        return d

    def keys(self, /) -> Dict_keys[K, T]:
        "D.keys() -> a set-like object providing a view on D's keys"

        return Dict_keys(self.__data)

    def values(self, /) -> Dict_values[K, T]:
        "D.values() -> an object providing a view on D's values"

        return Dict_values(self.__data)

    def items(self, /) -> Dict_items[K, T]:
        "D.items() -> a set-like object providing a view on D's items"

        return Dict_items(self.__data)
