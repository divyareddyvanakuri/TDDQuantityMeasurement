import pytest
import sys
sys.path.append("/home/user/Desktop/TDDQuantityMeasurment")
from main import Quantity
sys.path.append("/home/user/Desktop/TDDQuantityMeasurment/src")
from quantitymeasurment import InchUnit,FeetUnit

def test_givenZeroFeetAndZeroFeet_whenCompared_thenShouldEqual():
    first_zeroFeet_object = Quantity(0,FeetUnit()) 
    second_zeroFeet_object = Quantity(0,FeetUnit())
    assert first_zeroFeet_object == second_zeroFeet_object


def test_givenNoneAndZeroFeet_whenCompared_thenShouldNotEqual():
    with pytest.raises(AssertionError) as e:
        none_feet_object = None
        zero_feet_object = Quantity(0,FeetUnit())
        assert none_feet_object != zero_feet_object


def test_givenStringFeetAndZeroFeet_whenCompared_thenShouldNotEqual():
    with pytest.raises(AssertionError) as e:
        string_feet_object = Quantity("0",FeetUnit())
        zero_feet_object = Quantity(0,FeetUnit())
        assert string_feet_object != zero_feet_object


def test_givenZeroInchAndZeroInch_whenCompared_thenShouldEqual():
    first_zeroInch_object = Quantity(0,InchUnit())
    second_zeroInch_object = Quantity(0,InchUnit())
    assert first_zeroInch_object == second_zeroInch_object


def test_givenNoneAndZeroInch_whenCompared_thenShouldNotEqual():
    with pytest.raises(AssertionError) as e:
        none_inch_object = None
        zero_inch_object = Quantity(0,InchUnit())
        assert none_inch_object != zero_inch_object


def test_givenStringInchAndZeroInch_whenCompared_thenShouldNotEqual():
    with pytest.raises(AssertionError) as e:
        string_inch_object = Quantity("0",InchUnit())
        zero_inch_object = Quantity(0,InchUnit())
        assert string_inch_object != zero_inch_object


def test_givenZeroFeetAndZeroInch_whenCompared_thenShouldEqual():
    zero_feet_object = Quantity(0,FeetUnit())
    zero_inch_object = Quantity(0,InchUnit())
    assert zero_feet_object == zero_inch_object


def test_givenOneFeetAndOneInch_whenCompared_thenshouldNotEqual():
    one_feet_object = Quantity(1,FeetUnit())
    one_inch_object = Quantity(1,InchUnit())
    assert one_feet_object != one_inch_object