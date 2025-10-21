import pytest

from largest_remainder import LargestRemainder


def test_list_basic():
    result = LargestRemainder.round([1, 1, 1, 1], total=10)
    assert sum(result) == 10
    assert sorted(result, reverse=True)[0] - sorted(result, reverse=True)[-1] <= 1


def test_dict_basic():
    data = {"a": 1.0, "b": 2.0, "c": 3.0}
    result = LargestRemainder.round(data, total=12)
    assert sum(result.values()) == 12
    assert set(result.keys()) == {"a", "b", "c"}


def test_zero_total_with_zero_values():
    assert LargestRemainder.round([0, 0], total=0) == [0, 0]


def test_zero_values_with_non_zero_total_raises():
    with pytest.raises(ValueError, match="total is not"):
        LargestRemainder.round([0, 0], total=5)


def test_negative_values_raise():
    with pytest.raises(ValueError, match="non-negative"):
        LargestRemainder.round([-1, 2, 3])


def test_wrong_input_type_raises():
    with pytest.raises(TypeError):
        LargestRemainder.round("not a list or dict")  # type: ignore


def test_empty_list_returns_empty():
    assert LargestRemainder.round([], total=0) == []


def test_empty_list_with_non_zero_total_raises():
    with pytest.raises(ValueError, match="total is not"):
        LargestRemainder.round([], total=1)


@pytest.mark.parametrize("invalid_total", ["10", object()])
def test_non_numeric_total_raises(invalid_total: object):
    with pytest.raises(TypeError, match="must be a number"):
        LargestRemainder.round([1, 2], total=invalid_total)  # type: ignore[arg-type]


def test_negative_total_raises():
    with pytest.raises(ValueError, match="must be non-negative"):
        LargestRemainder.round([1, 2], total=-1)


def test_empty_dict_returns_empty():
    assert LargestRemainder.round({}, total=0) == {}


@pytest.mark.parametrize(
    "scenario",
    [
        {
            "name": "proportional_percentages",
            "data": [49.7, 20.1, 30.2],
            "total": 10,
            "expected": [5, 2, 3],
        },
        {
            "name": "zeros_and_sparse_allocation",
            "data": [5.0, 0.0, 0.0],
            "total": 5,
            "expected": [5, 0, 0],
        },
        {
            "name": "probability_distribution_dict",
            "data": {"x": 0.33, "y": 0.33, "z": 0.34},
            "total": 3,
            "expected": {"x": 1, "y": 1, "z": 1},
        },
    ],
    ids=lambda scenario: scenario["name"],
)
def test_rounding_scenarios(scenario: dict[str, object]):
    data = scenario["data"]
    total = scenario["total"]
    expected = scenario["expected"]

    result = LargestRemainder.round(data, total=total)  # type: ignore[arg-type]

    if isinstance(expected, dict):
        assert isinstance(result, dict)
        assert result == expected
        result_total = sum(result.values())
    else:
        assert isinstance(result, list)
        assert result == expected
        result_total = sum(result)

    assert result_total == total
