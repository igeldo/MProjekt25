from typing import Type, TypeVar


def check_float(value: float, name: str = "value") -> float:
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} can only be a float or int")
    return float(value)


def check_float_positive(value: float, name: str = "value") -> float:
    result = check_float(value, name)
    if result <= 0.0:
        raise ValueError(f"{name} must be greater than zero")
    return result


T = TypeVar("T")


def check_type(value: T, requested_type: Type[T], name: str = 'value') -> T:
    if not isinstance(value, requested_type):
        raise TypeError(f"{name} can only be a {requested_type.__name__}")
    return value
