class FeetUnit:
    def __init__(self,value):
        self.value = value

    def __eq__(self, other):
        if other.value == self.value:
                return True
        return False 
    
    def __ne__(self, other):
        if isinstance(other,self.__class__):
            if other.value == self.value:
                return True
        return False