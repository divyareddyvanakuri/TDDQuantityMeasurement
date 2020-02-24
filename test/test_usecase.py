import pytest
import sys
sys.path.append("/home/user/Desktop/TDDQuantityMeasurment")
from main import Quantity
sys.path.append("/home/user/Desktop/TDDQuantityMeasurment/src")
from quantitymeasurment import InchUnit,FeetUnit,CentiMeterUnit


def test_givenTwoInchAndTwoInch_whenAdded_thenResultShouldInInches():
    first_two_inch_object = Quantity(2,InchUnit())
    second_two_inch_object = Quantity(2,InchUnit())
    assert first_two_inch_object + second_two_inch_object == 4


def test_givenOneFeetAndTwoInch_whenAdded_thenResultShouldInInches():
    one_feet_object = Quantity(1,FeetUnit())
    two_inch_object = Quantity(2,InchUnit())
    assert one_feet_object + two_inch_object == 14


def test_givenOneFeetAndOneFeet_whenAdded_thenResultShouldInInches():
    first_one_feet_object = Quantity(1,FeetUnit())
    second_one_feet_object = Quantity(1,FeetUnit())
    assert first_one_feet_object + second_one_feet_object == 24


def test_givenTwoInchAndTwoPointFiveCentiMeter_whenAdded_thenResultShouldInInches():
    two_inch_object = Quantity(2,InchUnit())
    twoPointFive_cm_object = Quantity(2.5,CentiMeterUnit())
    assert two_inch_object + twoPointFive_cm_object == 3
