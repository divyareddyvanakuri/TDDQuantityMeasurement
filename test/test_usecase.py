def test_givenOneGallonAndThreePointSevenEightLitres_whenAdded_thenResultShouldInLitres():
    one_gallon_object = Quantity(1,GallonUnit())
    three_point_seven_eight_litre_object = Quantity(3.78,LitreUnit())
    assert one_gallon_object+three_point_seven_eight_litre_object == 7.57





