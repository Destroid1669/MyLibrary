from typing import Any, Iterable, Protocol, TypeAlias, TypeVar, Union

NumberType = Union[int, float]

ReadableBuffer: TypeAlias = bytes | str

_KT = TypeVar("_KT")
_T_co = TypeVar("_T_co", covariant=True)


class SupportsLenAndGetItem(Protocol[_T_co]):
    def __len__(self) -> int:
        ...

    def __getitem__(self, __k: int) -> _T_co:
        ...


class SupportsKeysAndGetItem(Protocol[_KT, _T_co]):
    def keys(self) -> Iterable[_KT]:
        ...

    def __getitem__(self, __key: _KT) -> _T_co:
        ...


class TranslateTable(Protocol):
    def __getitem__(self, __key: int) -> str | int | None:
        ...


class FormatMapMapping(Protocol):
    def __getitem__(self, __key: str) -> Any:
        ...


def check_type(message: str, *args: list[Any]) -> None:
    """Raise TypeError if any of the values in *args
        is not an instance of its corresponding datatype.
    """
    for value, datatype in args:
        if not isinstance(value, datatype):
            raise TypeError(f"{message}" % type(value).__name__)


def verify_type(*args: list[Any], message: str | None = None) -> None:
    """Raise TypeError if any of the values in *args
        is not an instance of its corresponding datatype.
    """
    if message is None:
        message = "expected {} found {}"
    for value, datatype in args:
        if not isinstance(value, datatype):
            raise TypeError(
                message.format(datatype.__name__, type(value).__name__))
