from built_in_functions import Reversed, errorhandler


class Range:
    """Return a range that produces a sequence of integers from start (inclusive)
    to stop (exclusive) by step.

    range(i, j) produces i, i+1, i+2, ..., j-1

    start defaults to 0, and stop is omitted!

    range(4) produces 0, 1, 2, 3

    These are exactly the valid indices for a list of 4 elements.
    When step is given, it specifies the increment (or decrement)."""

    __slots__ = ['start', 'stop', 'step'] + ['_Range__data']

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

        sequence = ()
        if step > 0:
            while start < stop:
                sequence += (start,)
                start += step
        else:
            while start > stop:
                sequence += (start,)
                start += step

        object.__setattr__(self, '_Range__data', sequence)

    def __getattribute__(self, name, /):
        return object.__getattribute__(self, name)

    def __setattr__(self, name, value, /):
        raise AttributeError("read only attribute")

    def __bool__(self, /):
        return True if self._Range__data else False

    def __eq__(self, value, /):
        if not isinstance(value, self.__class__):
            return False
        if len(self._Range__data) != len(value):
            return False
        if len(self._Range__data) == 0:
            return True
        if self.start != value.start:
            return False
        if self._Range__data[-1] == value[-1]:
            return True
        return False

    def __ne__(self, value, /):
        if not isinstance(value, self.__class__):
            return True
        if len(self._Range__data) != len(value):
            return True
        if len(self._Range__data) == 0:
            return False
        if self.start != value.start:
            return True
        if self._Range__data[-1] == value[-1]:
            return False
        return True

    def __contains__(self, key, /):
        return key in self._Range__data

    def __getitem__(self, key, /):
        length = len(self)
        if key >= length or ~key >= length:
            raise IndexError("Range object index out of range")

        return self._Range__data[key]

    def __len__(self, /):
        return (self.stop - self.start) // self.step

    def __hash__(self, /):
        if len(self) == 0:
            return id(Range)
        return hash((len(self), self.start, self[-1]))

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
        class Iterator:
            def __init__(self, sequence, /):
                self.__iters = iter(sequence)

            def __iter__(self, /):
                return self

            def __next__(self, /):
                return next(self.__iters)

            def __repr__(self, /):
                return "<Range_iterator object at %s>" % str(
                    hex(id(self))).replace('x', 'x00000').upper()

        return Iterator(self._Range__data)

    def __reversed__(self, /):
        class Reverse(Reversed):
            def __repr__(self, /):
                return "<Range_iterator object at %s>" % str(
                    hex(id(self))).replace('x', 'x00000').upper()

        return Reverse(self._Range__data)

    def __repr__(self, /):
        if self.step == 1:
            return f"Range({self.start}, {self.stop})"

        return f"Range({self.start}, {self.stop}, {self.step})"

    def count(self, value, /):
        "rangeobject.count(value) -> integer -- return number of occurrences of value"

        i, _count = 0, 0
        length = len(self)
        while i < length:
            if value == self._Range__data[i]:
                _count += 1
            i += 1
        return _count

    def index(self, value, /):
        "rangeobject.index(value) -> integer -- return index of value."

        i = 0; length = len(self)
        while i < length:
            if value == self._Range__data[i]:
                return i
            i += 1

        raise ValueError(f"{value} is not in Range")