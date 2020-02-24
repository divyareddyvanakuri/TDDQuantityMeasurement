import sys
sys.path.append("/home/user/Desktop/TDDQuantityMeasurment/src")
from quantitymeasurment import GallonUnit,LitreUnit,MlUnit

#This is the composition class for feet and inch objects
class Quantity:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __eq__(self, other):
        self.factor = int(self.unit.comparisons_to_base(self.value))
        other.factor = int(other.unit.comparisons_to_base(other.value))
        if self.factor == other.factor:
            return True
        return False

    def __ne__(self, other):
        if isinstance(other,self.__class__) and type(other.value) == type(self.value):
            self.factor = int(self.unit.comparisons_to_base(self.value))
            other.factor = int(other.unit.comparisons_to_base(other.value))
            if self.factor == other.factor:
                return True
        return False

