import sys
from typing import Any, Callable, Generic, Iterable, Self, TypeVar

T = TypeVar('T')

MISSING: tuple[object, ...] = ()


class List(Generic[T]):
    """List a sequence of mutable Python objects.

    If no argument is given, the constructor creates a new empty list.
    The argument must be an iterable if specified.
    """

    def __init__(self, iterable: Iterable[T] = MISSING, /) -> None:
        if iterable is MISSING:
            self.__data: list[T] = []
            return
        if isinstance(iterable, list):
            self.__data = iterable
        elif isinstance(iterable, self.__class__):
            self.__data = iterable.__data
        else:
            self.__data = list(iterable)

    def __eq__(self, value: object, /) -> bool:
        return self.__data == self.__cast(value)  # type: ignore

    def __ne__(self, value: object, /) -> bool:
        return self.__data != self.__cast(value)  # type: ignore

    def __lt__(self, value: Self | list[T], /) -> bool:
        return self.__data < self.__cast(value)

    def __le__(self, value: Self | list[T], /) -> bool:
        return self.__data <= self.__cast(value)

    def __gt__(self, value: Self | list[T], /) -> bool:
        return self.__data > self.__cast(value)

    def __ge__(self, value: Self | list[T], /) -> bool:
        return self.__data >= self.__cast(value)

    def __cast(self, value: Self | list[T], /) -> list[T]:
        if isinstance(value, self.__class__):
            return value.__data
        return value  # type: ignore

    def __add__(self, value: Self | list[T], /) -> Self:
        return self.__class__(self.__data + self.__cast(value))

    def __radd__(self, value: Self | list[T], /) -> Self:
        return self.__class__(self.__cast(value) + self.__data)

    def __iadd__(self, value: Self | list[T], /) -> Self:
        self.__data += self.__cast(value)
        return self

    def __mul__(self, value: Self | list[T], /) -> Self:
        return self.__class__(self.__data * self.__cast(value))  # type: ignore

    def __imul__(self, value: Self | list[T], /) -> Self:
        self.__data *= self.__cast(value)  # type: ignore
        return self

    __rmul__ = __mul__

    def __contains__(self, key: T, /) -> bool:
        return key in self.__data

    def __len__(self, /) -> int:
        return len(self.__data)

    def __sizeof__(self, /) -> int:
        return self.__data.__sizeof__()

    def __getitem__(self, index: int | slice, /) -> T | Self:
        if isinstance(index, int):
            return self.__data[index]
        return self.__class__(self.__data[index])

    def __setitem__(self, index: int, value: T, /) -> None:
        self.__data[index] = value

    def __delitem__(self, key: int, /) -> None:
        del self.__data[key]

    def __copy__(self, /) -> Self:
        inst = self.__class__.__new__(self.__class__)
        inst.__dict__.update(self.__dict__)
        # Create a copy and avoid triggering descriptors
        inst.__dict__[f"_{self.__class__.__name__}__data"] = \
            self.__dict__[f"_{self.__class__.__name__}__data"][:]
        return inst

    def __repr__(self, /) -> str:
        return f"{self.__class__.__name__}({self.__data})"

    def append(self, obj: T, /) -> None:
        "Append object to the end of the list."

        self.__data.append(obj)

    def insert(self, index: int, obj: T, /) -> None:
        "Insert object before index."

        self.__data.insert(index, obj)

    def pop(self, index: int = -1, /) -> T:
        """Remove and return item at index (default last).

        Raise IndexError if list is empty or index is out of range.
        """
        return self.__data.pop(index)

    def remove(self, value: T, /) -> None:
        """Remove first occurrence of value.

        Raise ValueError if the value is not present.
        """
        for idx in range(len(self.__data)):
            if value == self[idx]:
                del self.__data[idx]
                return None

        name = self.__class__.__name__
        raise ValueError(f"{name}.remove(x): x not in {name}")

    def clear(self, /) -> None:
        "Remove all items from list."

        self.__data.clear()

    def copy(self, /) -> Self:
        "Return a shallow copy of the list."

        return self.__class__(self)  # type: ignore

    def count(self, value: T, /) -> int:
        "Return number of occurrences of value."

        occurrences = 0
        for item in self.__data:
            if item == value:
                occurrences += 1
        return occurrences

    def index(self, value: T, start: int = 0, stop: int = sys.maxsize, /) -> int:
        """Return first index of value.

        Raise ValueError if the value is not present.
        """
        length = len(self.__data)
        if length < stop:
            stop = length

        for idx in range(start, stop):
            if value == self[idx]:
                return idx
        raise ValueError(f"{value} is not in {self.__class__.__name__}")

    def reverse(self, /) -> None:
        "Reverse *IN PLACE*."

        self.__data.reverse()

    def sort(self, /, *, key: Callable[[T], Any] | None = None, reverse: bool = False):
        """Sort the list in ascending order and return None.

        The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
        order of two equal elements is maintained).

        If a key function is given, apply it once to each list item and sort them,
        ascending or descending, according to their function values.

        The reverse flag can be set to sort in descending order.
        """
        if key is None:
            self.__data.sort(reverse=reverse)  # type: ignore
        else:
            self.__data.sort(key=key, reverse=reverse)

    def extend(self, iterable: Iterable[T], /) -> None:
        "Extend list by appending elements from the iterable."

        self.__data.extend(iterable)
