import unittest
import pytest
from pytest_bdd import feature, scenario, given, when, then
from main import get_roots
from unittest import TestCase


class GetNumCoef(TestCase):
    def test1(self):
        self.assertEqual(get_roots(3, 7, -10), [1.0, -1.0])
    def test2(self):
        self.assertEqual(get_roots(1, 1, 1), [])
    def test3(self):
        self.assertEqual(get_roots(8, -6, 1), [0.7071067811865476, -0.7071067811865476, 0.5, -0.5])


@scenario("scenarios.feature", "2 roots")
def test1():
    print("Scenario: 2 roots")

@given("nums")
def test1():
    print("\nnums")
    print(f"nums: {[3, 7, -10]}\n")

@when('equasion is solved')
def test2():
    print('equasion is solved')

@then('roots are')
def test3():
    print('roots are')
    assert get_roots(3, 7, -10) == [1.0, -1.0]

def main():
    unittest.main()