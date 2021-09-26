import pytest
from fizzbuzz import FizzBuzz


def test_fizzbuzz():
    fb = FizzBuzz(15)
    assert fb.fizzbuzz() == 'FizzBuzz'


def test_fizz():
    fb = FizzBuzz(6)
    assert fb.fizzbuzz() == 'Fizz'


def test_buzz():
    fb = FizzBuzz(10)
    assert fb.fizzbuzz() == 'Buzz'


def test_other():
    fb = FizzBuzz(4)
    assert fb.fizzbuzz() == 4
