import pytest
import sys
sys.path.append("/home/user/Desktop/TDDQuantityMeasurment")
from main import Quantity
sys.path.append("/home/user/Desktop/TDDQuantityMeasurment/src")
from quantitymeasurment import InchUnit,CentiMeterUnit


def test_givenTwoInchAndFiveCentiMeter_whenCompared_thenShouldEqual():
    two_inch_object = Quantity(2,InchUnit()) 
    five_cm_object = Quantity(5,CentiMeterUnit())
    assert two_inch_object == five_cm_object


