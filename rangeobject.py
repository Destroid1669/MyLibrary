from built_in_functions import Enumerate, errorhandler


class Range:
    """Return a range that produces a sequence of integers from start (inclusive)
    to stop (exclusive) by step.

    range(i, j) produces i, i+1, i+2, ..., j-1

    start defaults to 0, and stop is omitted!

    range(4) produces 0, 1, 2, 3

    These are exactly the valid indices for a list of 4 elements.
    When step is given, it specifies the increment (or decrement)."""

    __slots__ = ['start', 'stop', 'step']

    def __init__(self, /, start: int, stop: int = 0, step: int = 1):
        if start != 0 and stop == 0 and step == 1:
            start, stop = stop, start

        if step == 0:
            raise ValueError("Range() arg 3 must not be zero")

        errorhandler("'%s' object cannot be interpreted as an integer",
                     [start, int], [stop, int], [step, int])

        object.__setattr__(self, 'start', start)
        object.__setattr__(self, 'stop', stop)
        object.__setattr__(self, 'step', step)

    def __getattribute__(self, name, /):
        return object.__getattribute__(self, name)

    def __setattr__(self, name, value, /):
        raise AttributeError("read only attribute")

    def __bool__(self, /):
        return bool(len(self))

    def __eq__(self, value, /):
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

    def __ne__(self, value, /):
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

    def __contains__(self, key, /):
        return key in self

    def __getitem__(self, key, /):
        if key < 0:
            key = len(self) + key

        for idx, num in Enumerate(self):
            if key == idx:
                return num
        raise IndexError("Range object index out of range")

    def __len__(self, /):
        return (self.stop - self.start) // self.step

    def __hash__(self, /):
        if len(self) == 0:
            return id(Range)
        return hash((len(self), self.start, self.step))

    def __getstate__(self, /):
        "Return state information for pickling."

        # Copy the object's state from self.__dict__ which contains
        # all our instance attributes. Always use the dict.copy()
        # method to avoid modifying the original state.
        return self.__dict__.copy()

    def __setstate__(self, state, /):
        "Set state information for unpickling."

        # Restore instance attributes (i.e., filename and lineno).
        self.__dict__.update(state)

    def __iter__(self, /):
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

    def __reversed__(self, /):
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

    def __repr__(self, /):
        if self.step == 1:
            return f"Range({self.start}, {self.stop})"

        return f"Range({self.start}, {self.stop}, {self.step})"

    def count(self, value, /):
        "rangeobject.count(value) -> integer -- return number of occurrences of value"

        counter = 0
        for num in self:
            if value == num:
                counter += 1
        return counter

    def index(self, value, /):
        "rangeobject.index(value) -> integer -- return index of value."

        for idx, num in Enumerate(self):
            if value == num:
                return idx
        raise ValueError(f"{value} is not in Range")
