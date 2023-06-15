from typing import Any, Iterator

from functions import check_type


class Range:
    """Return a range that produces a sequence of integers from start (inclusive)
    to stop (exclusive) by step.

    range(i, j) produces i, i+1, i+2, ..., j-1

    start defaults to 0, and stop is omitted!

    range(4) produces 0, 1, 2, 3

    These are exactly the valid indices for a list of 4 elements.
    When step is given, it specifies the increment (or decrement).
    """

    __slots__ = ['start', 'stop', 'step']

    def __init__(self, /, start: int, stop: int = 0, step: int = 1) -> None:
        if start != 0 and stop == 0 and step == 1:
            start, stop = stop, start

        if step == 0:
            raise ValueError(
                f"{self.__class__.__name__}() arg 3 must not be zero")

        check_type("'%s' object cannot be interpreted as an integer",
                   [start, int], [stop, int], [step, int])

        # for type hints
        self.start: int
        self.stop: int
        self.step: int

        # hack to avoid calling __setattr__
        object.__setattr__(self, 'start', start)
        object.__setattr__(self, 'stop', stop)
        object.__setattr__(self, 'step', step)

    def __getattribute__(self, name: str, /) -> Any:
        return object.__getattribute__(self, name)

    def __setattr__(self, name: str, value: int, /) -> None:
        raise AttributeError("read only attribute")

    def __bool__(self, /) -> bool:
        return bool(len(self))

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, self.__class__):
            return False
        if len(self) != len(value):
            return False
        if self.start != value.start:
            return False
        if self.stop != value.stop:
            return False
        if self.step == value.step:
            return True
        return False

    def __ne__(self, value: object, /) -> bool:
        if not isinstance(value, self.__class__):
            return True
        if len(self) != len(value):
            return True
        if self.start != value.start:
            return True
        if self.stop != value.stop:
            return True
        if self.step == value.step:
            return False
        return True

    def __contains__(self, key: int, /) -> bool:
        return key in self

    def __getitem__(self, key: int, /) -> int:
        if key < 0:
            key = len(self) + key

        idx: int = 0
        for num in self:
            if idx == key:
                return num
            idx += 1
        raise IndexError("Range object index out of range")

    def __len__(self, /) -> int:
        return (self.stop - self.start) // self.step

    def __hash__(self, /) -> int:
        if len(self) == 0:
            return id(self.__class__)
        return hash((len(self), self.start, self.step))

    def __getstate__(self, /) -> dict[str, Any]:
        "Return state information for pickling."

        # Copy the object's state from self.__dict__ which contains
        # all our instance attributes. Always use the dict.copy()
        # method to avoid modifying the original state.
        return self.__dict__.copy()

    def __setstate__(self, state: dict[str, Any], /) -> None:
        "Set state information for unpickling."

        # Restore instance attributes (i.e., filename and lineno).
        self.__dict__.update(state)

    def __iter__(self, /) -> Iterator[int]:
        start = self.start
        stop = self.stop
        step = self.step

        if step > 0:
            while start < stop:
                yield start
                start += step
        else:
            while start > stop:
                yield start
                start += step

    def __reversed__(self, /) -> Iterator[int]:
        start = self.start
        stop = self.stop
        step = self.step
        # To reverse
        if step > 0:
            start -= 1
            stop -= 1
        else:
            start += 1
            stop += 1
        return iter(Range(stop, start, -step))

    def __repr__(self, /) -> str:
        name = self.__class__.__name__
        if self.step == 1:
            return f"{name}({self.start}, {self.stop})"
        return f"{name}({self.start}, {self.stop}, {self.step})"

    def count(self, value: int, /) -> int:
        "rangeobject.count(value) -> integer -- return number of occurrences of value"

        occurrences = 0
        for num in self:
            if num == value:
                occurrences += 1
        return occurrences

    def index(self, value: int, /) -> int:
        "rangeobject.index(value) -> integer -- return index of value."

        idx: int = 0
        for num in self:
            if num == value:
                return idx
            idx += 1
        raise ValueError(f"{value} is not in Range")
