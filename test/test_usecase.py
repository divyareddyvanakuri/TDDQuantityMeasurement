import pytest
import sys
sys.path.append("/home/user/Desktop/TDDQuantityMeasurment")
from main import Quantity
sys.path.append("/home/user/Desktop/TDDQuantityMeasurment/src")
from quantitymeasurment import FeetUnit,YardUnit

def test_givenThreeFeetAndOneYard_whenCompared_thenShouldEqual():
    three_feet_object = Quantity(3,FeetUnit()) 
    one_yard_object = Quantity(1,YardUnit())
    assert three_feet_object == one_yard_object


def test_givenOneFeetAndOneYard_whenCompared_thenShouldNotEqual():
    with pytest.raises(AssertionError) as e:
        one_feet_object = Quantity(1,FeetUnit()) 
        one_yard_object = Quantity(1,YardUnit())
        assert one_feet_object != one_yard_object