from typing import Generic, Iterable, Iterator, Self, TypeVar

T = TypeVar('T')

MISSING = object()


class Set(Generic[T]):
    """Set() -> new empty set object
    Set(iterable) -> new set object

    Build an unordered collection of unique elements.
    """

    def __init__(self, iterable: Iterable[T] | object = MISSING, /) -> None:
        if iterable is MISSING:
            self.__data: set[T] = set()
            return
        if isinstance(iterable, set):
            self.__data = iterable
        elif isinstance(iterable, self.__class__):
            self.__data = iterable.__data
        else:
            self.__data = set(iterable)  # type: ignore

    def __eq__(self, value: object, /) -> bool:
        return self.__data == self.__cast(value)  # type: ignore

    def __ne__(self, value: object, /) -> bool:
        return self.__data != self.__cast(value)  # type: ignore

    def __lt__(self, value: Self | set[T], /) -> bool:
        return self.__data < self.__cast(value)

    def __le__(self, value: Self | set[T], /) -> bool:
        return self.__data <= self.__cast(value)

    def __gt__(self, value: Self | set[T], /) -> bool:
        return self.__data > self.__cast(value)

    def __ge__(self, value: Self | set[T], /) -> bool:
        return self.__data >= self.__cast(value)

    def __cast(self, value: Self | set[T], /) -> set[T]:
        if isinstance(value, self.__class__):
            return value.__data
        return value  # type: ignore

    def __sub__(self, value: Self | set[T], /) -> Self:
        return self.difference(value)

    def __xor__(self, value: Self | set[T], /) -> Self:
        return self.symmetric_difference(value)

    def __ixor__(self, value: Self | set[T], /) -> Self:
        self.symmetric_difference_update(value)
        return self

    __rxor__ = __xor__

    def __and__(self, value: Self | set[T], /) -> Self:
        return self.intersection(value)

    def __iand__(self, value: Self | set[T], /) -> Self:
        self.intersection_update(value)
        return self

    __rand__ = __and__

    def __or__(self, value: Self | set[T], /) -> Self:
        return self.union(value)

    def __ior__(self, value: Self | set[T], /) -> Self:
        self.update(value)
        return self

    __ror__ = __or__

    def __iter__(self, /) -> Iterator[T]:
        return iter(self.__data)

    def __contains__(self, key: T, /) -> bool:
        return key in self.__data

    def __len__(self, /) -> int:
        return len(self.__data)

    def __sizeof__(self, /) -> int:
        return self.__data.__sizeof__()

    def __repr__(self, /) -> str:
        return f"{self.__class__.__name__}({str(self.__data)})"

    def __copy__(self, /) -> Self:
        inst = self.__class__.__new__(self.__class__)
        inst.__dict__.update(self.__dict__)
        # Create a copy and avoid triggering descriptors
        inst.__dict__[f"_{self.__class__.__name__}__data"] = self.__dict__[
            f"_{self.__class__.__name__}__data"].copy()
        return inst

    def add(self, obj: T, /) -> None:
        """Add an element to a set.

        This has no effect if the element is already present.
        """
        self.__data.add(obj)

    def update(self, value: Iterable[T], /) -> None:
        "Update a set with the union of itself and others."

        for elem in value:
            self.add(elem)

    def copy(self, /) -> Self:
        "Return a shallow copy of a Set."

        return self.__class__(self)

    def clear(self, /) -> None:
        "Remove all elements from this Set."

        self.__data.clear()

    def pop(self, /) -> T:
        """Remove and return an arbitrary set element.

        Raise KeyError if the set is empty.
        """
        if self.__data:
            return self.__data.pop()
        raise KeyError("pop from empty Set")

    def remove(self, key: T, /) -> None:
        """Remove an element from a set; it must be a member.

        If the element is not a member, raise a KeyError.
        """
        if key not in self.__data:
            raise KeyError(key)
        self.__data.remove(key)

    def discard(self, key: T, /) -> None:
        """Remove an element from a set if it is a member.

        If the element is not a member, do nothing.
        """
        if key in self.__data:
            self.__data.remove(key)

    def union(self, value: Iterable[T], /) -> Self:
        """Return the union of sets as a new set.

        (i.e. all elements that are in either set.)
        """
        res = self.copy()
        for x in value:
            if x not in res:
                res.add(x)
        return res

    def intersection(self, value: Iterable[T], /) -> Self:
        """Return the intersection of two sets as a new set.

       (i.e. all elements that are in both sets.)
       """
        res = self.__class__()
        for x in self:
            if x in value:
                res.add(x)
        return res

    def intersection_update(self, value: Iterable[T], /) -> None:
        "Update a set with the intersection of itself and another."

        res: set[T] = set()
        for x in self:
            if x in value:
                res.add(x)
        self.__data = res

    def difference(self, value: Iterable[T], /) -> Self:
        """Return the difference of two or more sets as a new set.

        (i.e. all elements that are in this set but not the others.)
        """
        res = self.copy()
        for x in value:
            if x in self:
                res.remove(x)
        return res

    def difference_update(self, value: Iterable[T], /) -> None:
        "Remove all elements of another set from this set."

        for x in value:
            if x in self:
                self.remove(x)

    def symmetric_difference(self, value: Iterable[T], /) -> Self:
        """Return the symmetric difference of two sets as a new set.

        (i.e. all elements that are in exactly one of the sets.)
        """
        res = self.copy()
        for x in value:
            if x in self:
                res.remove(x)
            else:
                res.add(x)
        return res

    def symmetric_difference_update(self, value: Iterable[T], /) -> None:
        "Update a set with the symmetric difference of itself and another."

        for x in value:
            if x in self:
                self.remove(x)
            else:
                self.add(x)

    def isdisjoint(self, value: Iterable[T], /) -> bool:
        "Return True if two sets have a null intersection."

        for x in value:
            if x in self:
                return False
        return True

    def issubset(self, value: Iterable[T], /) -> bool:
        "Report whether another set contains this set."

        for x in self:
            if x not in value:
                return False
        return True

    def issuperset(self, value: Iterable[T], /) -> bool:
        "Report whether this set contains another set."

        for x in value:
            if x not in self:
                return False
        return True
