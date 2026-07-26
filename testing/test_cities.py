from city_country import city_country

def test_city_country():
    formatted_cities = city_country('Bogota', "Colombia")
    assert formatted_cities == 'Bogota, Colombia'