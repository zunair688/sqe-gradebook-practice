
import pytest
from gradebook import student


def test_valid_score_is_accepted():
    s = student("Ali", 101)
    s.add_score(80)
    assert s.score == [80]


def test_negative_score_is_rejected():
    s = student("Ali", 101)

    with pytest.raises(ValueError):
        s.add_score(-1)


def test_score_above_100_is_rejected():
    s = student("Ali", 101)

    with pytest.raises(ValueError):
        s.add_score(101)
