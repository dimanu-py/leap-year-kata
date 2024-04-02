import pytest

from leap_year.leap_year import leap_year


@pytest.mark.parametrize("year_number", [1993, 1997, 2001, 2005, 2009])
def test_is_not_leap_year(year_number: int):
    assert leap_year(year_number) == False


@pytest.mark.parametrize("year_number", [2016, 2020, 2024])
def test_leap_year_divisible_by_4(year_number: int):
    assert leap_year(year_number) == True


@pytest.mark.parametrize("year_number", [1700, 1800, 1900, 2100, 2200])
def test_is_not_leap_year_divisible_by_100_but_not_by_400(year_number: int):
    assert leap_year(year_number) == False


@pytest.mark.parametrize("year_number", [1600, 2000, 2400, 2800, 3200])
def test_leap_year_divisible_by_100_and_400(year_number: int):
    assert leap_year(year_number) == True
