# pylint: disable=missing-docstring
import pytest

from prime import generate_prime_factors

def test_incorrect_dat_type():
    with pytest.raises(ValueError):
        generate_prime_factors("string")
        generate_prime_factors(6.6)

def test_1():
    assert generate_prime_factors(1) == []

def test_2():
    assert generate_prime_factors(2) == [2]

def test_3():
    assert generate_prime_factors(3) == [3]

def test_4():
    assert generate_prime_factors(4) == [2, 2]

def test_6():
    assert generate_prime_factors(6) == [2, 3]

def test_8():
    assert generate_prime_factors(8) == [2, 2, 2]

def test_9():
    assert generate_prime_factors(9) == [3, 3]
