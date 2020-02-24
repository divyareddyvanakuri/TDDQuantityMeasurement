import pytest
import sys
sys.path.append("/home/user/Desktop/TDDQuantityMeasurment")
from main import Quantity
sys.path.append("/home/user/Desktop/TDDQuantityMeasurment/src")
from quantitymeasurment import FeetUnit,YardUnit,InchUnit

def test_givenThreeFeetAndOneYard_whenCompared_thenShouldEqual():
    three_feet_object = Quantity(3,FeetUnit()) 
    one_yard_object = Quantity(1,YardUnit())
    assert three_feet_object == one_yard_object


def test_givenOneFeetAndOneYard_whenCompared_thenShouldNotEqual():
    with pytest.raises(AssertionError) as e:
        one_feet_object = Quantity(1,FeetUnit()) 
        one_yard_object = Quantity(1,YardUnit())
        assert one_feet_object != one_yard_object


def test_givenOneInchAndOneYard_whenCompared_thenShouldNotEqual():
    with pytest.raises(AssertionError) as e:
        one_inch_object = Quantity(1,InchUnit()) 
        one_yard_object = Quantity(1,YardUnit())
        assert one_inch_object != one_yard_object


def test_givenOneYardAndThirtySixInch_whenCompared_thenShouldEqual():
    one_yard_object = Quantity(1,YardUnit())
    thirtySix_inch_object = Quantity(36,InchUnit()) 
    assert one_yard_object == thirtySix_inch_object


def test_givenThirtySixInchAndOneYard_whenCompared_thenShouldEqual():
    thirtySix_inch_object = Quantity(36,InchUnit()) 
    one_yard_object = Quantity(1,YardUnit())
    assert thirtySix_inch_object == one_yard_object