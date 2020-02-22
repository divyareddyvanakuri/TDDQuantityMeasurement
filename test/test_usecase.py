import pytest
import sys
sys.path.append("/home/user/Desktop/TDDQuantityMeasurment/src")
from quantitymeasurment import FeetUnit

def test_givenZeroFeetAndZeroFeet_whenCompared_thenShouldEqual():
    first_zeroFeet_object = FeetUnit(0) 
    second_zeroFeet_object = FeetUnit(0)
    assert first_zeroFeet_object == second_zeroFeet_object


def test_givenNoneAndZeroFeet_whenCompared_thenShouldNotEqual():
    with pytest.raises(AssertionError) as e:
        none_feet_object = None
        zero_feet_object = FeetUnit(0)
        assert none_feet_object != zero_feet_object