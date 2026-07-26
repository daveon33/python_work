from testing.cities.city_country import city_country

def test_city_country():
    formatted_cities = city_country('Bogota', "Colombia")
    assert formatted_cities == 'Bogota, Colombia'

def test_city_country_population():
    formatted_cities = city_country('Medellin', 'Colombia', '6.000.000')
    assert formatted_cities == 'Medellin, Colombia - population 6.000.000'