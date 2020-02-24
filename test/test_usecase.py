def givenOneKgAndThousandGrams_whenCompared_thenShouldEqual():
    one_kg_object = Quantity(1,KgUnit())
    thousand_grams_object = Quantity(1000,GramsUnit())
    assert one_kg_object == thousand_grams_object

