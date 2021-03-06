import pytest

from hacker_rank_problems.medium.minimum_bribes.alg import minimum_bribes


@pytest.mark.parametrize('array, expected', [
    ([1, 2, 3, 4, 5], 0),
    ([2, 1, 5, 3, 4], 3),
    ([2, 5, 1, 3, 4], "Too chaotic"),
    ([1, 2, 5, 3, 4, 7, 8, 6], 4),
    ([5, 1, 2, 3, 7, 8, 6, 4], 'Too chaotic'),
    ([1, 2, 5, 3, 7, 8, 6, 4], 7)
    ])
def test_minimum_bribes(array, expected):
    assert minimum_bribes(array) == expected
