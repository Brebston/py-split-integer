from app.split_integer import split_integer
import pytest


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value, parts = 10, 3
    result = split_integer(value, parts)
    assert sum(result) == value
    assert len(result) == parts


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(12, 4) == [3, 3, 3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value, parts = 10, 3
    result = split_integer(value, parts)
    assert len(result) == parts
    assert sum(result) == parts
    assert result == sorted(result)
    assert max(result) - min(result) <= 1


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value, parts = 2, 5
    result = split_integer(value, parts)
    assert len(result) == parts
    assert sum(result) == value
    assert result == sorted(result)
    assert max(result) - min(result) <= 1


def test_should_match_explicit_example_17_4() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


@pytest.mark.parametrize("value,parts", [(10, 3), (11, 3), (5, 2)])
def test_parts_should_satisfy_max_min_property(value: int, parts: int) -> None:
    result = split_integer(value, parts)
    assert len(result) == parts
    assert sum(result) == value
    assert result == sorted(result)
    assert max(result) - min(result) <= 1
