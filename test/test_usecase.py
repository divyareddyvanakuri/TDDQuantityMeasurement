import pytest
import sys
sys.path.append("/home/user/Desktop/TDDQuantityMeasurment")
from main import Quantity
sys.path.append("/home/user/Desktop/TDDQuantityMeasurment/src")
from quantitymeasurment import KgUnit,GramUnit,TonneUnit


def test_givenOneKgAndThousandGrams_whenCompared_thenShouldEqual():
    one_kg_object = Quantity(1,KgUnit())
    thousand_grams_object = Quantity(1000,GramUnit())
    assert one_kg_object == thousand_grams_object


def test_givenOneTonneAndThousandKg_whenCompared_thenShouldEqual():
    one_tonne_object = Quantity(1,TonneUnit())
    thousand_kgs_object = Quantity(1000,KgUnit())
    assert one_tonne_object == thousand_kgs_object


def test_givenOneTonneAndThousandKg_whenAdded_thenResultShouldInKgs():
    one_tonne_object = Quantity(1,TonneUnit())
    thousand_grams_object = Quantity(1000,GramUnit())
    assert one_tonne_object + thousand_grams_object == 1001