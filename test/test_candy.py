from Dessert_Shop import DessertItem, Candy

def test_candy():
    testcandy_1 = Candy("Jolly Ranchers", 2, 6.50)
    testcandy_2 = Candy("M&M", 1, 7.25)
    testcandy_3 = Candy("Jelly Beans", 27, 3.50)
    
    assert testcandy_1.get_weight() == 2
    assert testcandy_1.get_cost() == 6.50
    assert testcandy_1.get_name() == "Jolly Ranchers"
    assert testcandy_1.calc_cost() == 13.00
    assert testcandy_1.calculate_tax() == 0.94

    assert testcandy_2.get_weight() == 1
    assert testcandy_2.get_cost() == 7.25
    assert testcandy_2.get_name() == "M&M"
    assert testcandy_2.calc_cost() == 7.25
    assert testcandy_2.calculate_tax() == 0.53

    assert testcandy_3.get_weight() == 27
    assert testcandy_3.get_cost() == 3.50
    assert testcandy_3.get_name() == "Jelly Beans"
    assert testcandy_3.calc_cost() == 94.50
    assert testcandy_3.calculate_tax() == 6.85