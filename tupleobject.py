import sys
from typing import Generic, Iterable, Self, TypeVar

T = TypeVar('T')


class Tuple(Generic[T]):
    """Tuple a sequence of immutable Python objects.

    If no argument is given, the constructor returns an empty tuple.
    If iterable is specified the tuple is initialized from iterable's items.

    If the argument is a tuple, the return value is the same object.
    """

    def __init__(self, iterable: Iterable[T] = (), /) -> None:
        self.__data: tuple[T, ...] = ()
        if iterable == ():
            return
        if isinstance(iterable, type(self.__data)):
            self.__data = iterable
        elif isinstance(iterable, self.__class__):
            self.__data = iterable.__data
        else:
            self.__data = tuple(iterable)

    def __eq__(self, value: object, /) -> bool:
        return self.__data == self.__cast(value)  # type: ignore

    def __ne__(self, value: object, /) -> bool:
        return self.__data != self.__cast(value)  # type: ignore

    def __lt__(self, value: Self | tuple[T, ...], /) -> bool:
        return self.__data < self.__cast(value)

    def __le__(self, value: Self | tuple[T, ...], /) -> bool:
        return self.__data <= self.__cast(value)

    def __gt__(self, value: Self | tuple[T, ...], /) -> bool:
        return self.__data > self.__cast(value)

    def __ge__(self, value: Self | tuple[T, ...], /) -> bool:
        return self.__data >= self.__cast(value)

    def __cast(self, value: Self | tuple[T, ...], /) -> tuple[T, ...]:
        if isinstance(value, self.__class__):
            return value.__data
        return value  # type: ignore

    def __add__(self, value: Self | tuple[T, ...], /) -> Self:
        return self.__class__(self.__data + self.__cast(value))

    def __radd__(self, value: Self | tuple[T, ...], /) -> Self:
        return self.__class__(self.__cast(value) + self.__data)

    def __iadd__(self, value: Self | tuple[T, ...], /) -> Self:
        self.__data += self.__cast(value)
        return self

    def __mul__(self, value: Self | tuple[T, ...], /) -> Self:
        return self.__class__(self.__data * self.__cast(value))  # type: ignore

    def __imul__(self, value: Self | tuple[T, ...], /) -> Self:
        self.__data *= self.__cast(value)  # type: ignore
        return self

    __rmul__ = __mul__

    def __contains__(self, key: T, /) -> bool:
        return key in self.__data

    def __len__(self, /) -> int:
        return len(self.__data)

    def __hash__(self, /) -> int:
        return hash(self.__data)

    def __getitem__(self, index: int | slice, /) -> T | Self:
        if isinstance(index, int):
            return self.__data[index]
        return self.__class__(self.__data[index])

    def __repr__(self, /) -> str:
        return f"{self.__class__.__name__}[{self.__data}]"

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

        name = self.__class__.__name__
        raise ValueError(f"{name}.index(x): x not in {name}")
