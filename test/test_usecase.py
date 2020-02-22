import pytest
import sys
sys.path.append("/home/user/Desktop/TDDQuantityMeasurment/src")
from quantitymeasurment import FeetUnit,InchUnit

def test_givenZeroFeetAndZeroFeet_whenCompared_thenShouldEqual():
    first_zeroFeet_object = FeetUnit(0) 
    second_zeroFeet_object = FeetUnit(0)
    assert first_zeroFeet_object == second_zeroFeet_object


def test_givenNoneAndZeroFeet_whenCompared_thenShouldNotEqual():
    with pytest.raises(AssertionError) as e:
        none_feet_object = None
        zero_feet_object = FeetUnit(0)
        assert none_feet_object != zero_feet_object


def test_givenStringFeetAndZeroFeet_whenCompared_thenShouldNotEqual():
    with pytest.raises(AssertionError) as e:
        string_feet_object = FeetUnit("0")
        zero_feet_object = FeetUnit(0)
        assert string_feet_object != zero_feet_object


def test_givenZeroInchAndZeroInch_whenCompared_thenShouldEqual():
    first_zeroInch_object = InchUnit(0)
    second_zeroInch_object = InchUnit(0)
    assert first_zeroInch_object == second_zeroInch_object


def test_givenNoneAndZeroInch_whenCompared_thenShouldNotEqual():
    with pytest.raises(AssertionError) as e:
        none_inch_object = None
        zero_inch_object = InchUnit(0)
        assert none_inch_object != zero_inch_object
