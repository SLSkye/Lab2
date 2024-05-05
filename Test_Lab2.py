import Lab2 

def test_find_min_max():
    input_list = [2,19,20,3]
    test = (2,20)
    result = Lab2.calc_min_max_temperature(input_list)
    assert (result == test)

def test_find_average():
    input_list = [3,1,23]
    test = 9.0
    result = Lab2.calc_average_temperature(input_list)
    assert (result == test)

def test_find_median_even_numbers_entered():
    input_list = [2,9,10,23,1,14]
    test = 9.5
    result = Lab2.calc_median_temperature(input_list)
    assert (result == test)

def test_find_median_odd_numbers_entered():
    input_list = [2,9.5,10,1,14]
    test = 9.5
    result = Lab2.calc_median_temperature(input_list)
    assert (result == test)