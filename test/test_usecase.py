import pytest
import sys
sys.path.append("/home/user/Desktop/TDDQuantityMeasurment")
from main import Quantity
sys.path.append("/home/user/Desktop/TDDQuantityMeasurment/src")
from quantitymeasurment import GallonUnit,LitreUnit,MlUnit


def test_givenOneGallonAndThreePointSevenEightLitres_whenCompared_thenShouldEqual():
    one_gallon_object = Quantity(1,GallonUnit())
    three_point_seven_eight_litre_object = Quantity(3.78,LitreUnit())
    assert one_gallon_object == three_point_seven_eight_litre_object


def test_givenOneLitreAndThousandMl_whenCompared_thenResultShouldInInches():
    one_litre_object = Quantity(1,LitreUnit())
    thousand_ml_object = Quantity(1000,MlUnit())
    assert one_litre_object  == thousand_ml_object


