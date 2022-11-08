import pytest
import utils as u

@pytest.mark.parametrize('a, b, res', [
    (4, -4, 4),
    (3, 1, 1),
    (-1, -3, 3),
    (-1, 1, 2)])

def test_check_quarter_good(a, b, res):
    assert u.check_quarter(a, b) == res


@pytest.mark.parametrize('a, res', [
    ([2, 3, 5, 9, 3], 12),
    ([2, 1, 5, 2, 3, 4], 7),
    ([1, 2, 3, 1, 4, 2], 5),
    ([3, 0, 2, 5, 2, 5], 10)])

def test_summ_good(a, res):
    assert u.summ(a) == res


@pytest.mark.parametrize('a, res', [
    ([2, 3, 4, 5, 6], [12, 15, 16]),
    ([2, 3, 5, 6], [12, 15]),
    ([1, 2, 3, 1, 4, 2], [2, 8, 3]),
    ([3, 0, 2, 5, 2, 5], [15, 0, 10])])

def test_mult_list_good(a, res):
    assert u.mult_list(a) == res


@pytest.mark.parametrize('a, res', [
    ([1.1, 1.2, 3.1, 5, 10.01], 0.19),
    ([2.4, 3.05, 5.55, 6.02], 0.53),
    ([1.1, 2.4, 3.09, 1.03, 4.3, 2.02], 0.38),
    ([3.4, 0.02, 2.2, 5.3, 2.05, 5.1], 0.38)])

def test_fractional_part_difference_good(a, res):
    assert u.fractional_part_difference(a) == res
