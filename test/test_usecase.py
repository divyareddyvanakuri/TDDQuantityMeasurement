def test_givenTwoInchAndTwoInch_whenAdded_thenResultShouldInInches():
    first_two_inch_object = Quantity(5,InchUnit())
    second_two_inch_object = Quantity(5,InchUnit())
    assert first_two_inch_object == second_two_inch_object


