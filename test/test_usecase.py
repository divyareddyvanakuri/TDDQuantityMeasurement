def test_givenTwoInchAndFiveCentiMeter_whenCompared_thenShouldEqual():
    two_inch_object = InchUnit(2) 
    five_cm_object = CentiMeterUnit(5)
    assert two_inch_object == five_cm_object


