from typing import Generic, Iterable, Iterator, Self, TypeVar

T = TypeVar('T')

MISSING = object()


class Frozenset(Generic[T]):
    """Frozenset() -> empty Frozenset object
    Frozenset(iterable) -> Frozenset object

    Build an immutable unordered collection of unique elements.
    """

    def __init__(self, iterable: Iterable[T] | object = MISSING, /) -> None:
        if iterable is MISSING:
            self.__data: frozenset[T] = frozenset()
            return
        if isinstance(iterable, frozenset):
            self.__data = iterable
        elif isinstance(iterable, self.__class__):
            self.__data = iterable.__data
        else:
            self.__data = frozenset(iterable)  # type: ignore

    def __eq__(self, value: object, /) -> bool:
        return self.__data == self.__cast(value)  # type: ignore

    def __ne__(self, value: object, /) -> bool:
        return self.__data != self.__cast(value)  # type: ignore

    def __lt__(self, value: Self | frozenset[T], /) -> bool:
        return self.__data < self.__cast(value)

    def __le__(self, value: Self | frozenset[T], /) -> bool:
        return self.__data <= self.__cast(value)

    def __gt__(self, value: Self | frozenset[T], /) -> bool:
        return self.__data > self.__cast(value)

    def __ge__(self, value: Self | frozenset[T], /) -> bool:
        return self.__data >= self.__cast(value)

    def __cast(self, value: Self | frozenset[T], /) -> frozenset[T]:
        if isinstance(value, self.__class__):
            return value.__data
        return value  # type: ignore

    def __sub__(self, value: Self | frozenset[T], /) -> Self:
        return self.difference(value)

    def __xor__(self, value: Self | frozenset[T], /) -> Self:
        return self.symmetric_difference(value)

    __rxor__ = __xor__

    def __and__(self, value: Self | frozenset[T], /) -> Self:
        return self.intersection(value)

    __rand__ = __and__

    def __or__(self, value: Self | frozenset[T], /) -> Self:
        return self.union(value)

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
        return str(self.__data).capitalize()

    def copy(self, /) -> Self:
        "Return a shallow copy of a Set."

        return self.__class__(self)

    def __copy__(self, /) -> Self:
        inst = self.__class__.__new__(self.__class__)
        inst.__dict__.update(self.__dict__)
        # Create a copy and avoid triggering descriptors
        inst.__dict__[f"_{self.__class__.__name__}__data"] = self.__dict__[
            f"_{self.__class__.__name__}__data"].copy()
        return inst

    def union(self, value: Iterable[T], /) -> Self:
        """Return the union of sets as a new set.

        (i.e. all elements that are in either set.)
        """
        new: set[T] = set()
        for x in value:
            if x not in self:
                new.add(x)
        return self.__class__(new)

    def intersection(self, value: Iterable[T], /) -> Self:
        """Return the intersection of two sets as a new set.

       (i.e. all elements that are in both sets.)
       """
        res: set[T] = set()
        for x in self:
            if x in value:
                res.add(x)
        return self.__class__(res)

    def difference(self, value: Iterable[T], /) -> Self:
        """Return the difference of two or more sets as a new set.

        (i.e. all elements that are in this set but not the others.)
        """
        res = set(self)
        for x in value:
            if x in self:
                res.remove(x)
        return self.__class__(res)

    def symmetric_difference(self, value: Iterable[T], /) -> Self:
        """Return the symmetric difference of two sets as a new set.

        (i.e. all elements that are in exactly one of the sets.)
        """
        res = set(self)
        for x in value:
            if x in self:
                res.remove(x)
            else:
                res.add(x)
        return self.__class__(res)

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
