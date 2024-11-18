from Dessert_Shop import DessertItem, Cookie

def test_cookie():
    test_cookies_1 = Cookie("choclate chip", 36, 3.75)
    test_cookies_2 = Cookie("Snicker doodle", 24, 5.50)
    test_cookies_3 = Cookie("Sugar", 48, 3.50)
    
    assert test_cookies_1.get_amount() == 36
    assert test_cookies_1.get_cost() == 3.75
    assert test_cookies_1.get_name() == "choclate chip"
    assert test_cookies_1.calc_cost() == 11.25
    assert test_cookies_1.calculate_tax() == 0.82

    assert test_cookies_2.get_amount() == 24
    assert test_cookies_2.get_cost() == 5.50
    assert test_cookies_2.get_name() == "Snicker doodle"
    assert test_cookies_2.calc_cost() == 11.00
    assert test_cookies_2.calculate_tax() == 0.80

    assert test_cookies_3.get_amount() == 48
    assert test_cookies_3.get_cost() == 3.50
    assert test_cookies_3.get_name() == "Sugar"
    assert test_cookies_3.calc_cost() == 14.00
    assert test_cookies_3.calculate_tax() == 1.01