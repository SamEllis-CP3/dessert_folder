from Dessert_Shop import DessertItem, Sundae

def test_sundae():
    test_sun1 = Sundae("Starwberry", 2, 2.50, "sprinkles", 0.25)
    test_sun2 = Sundae("Chocolate", 3, 1.75, "Fudge", 0.75)
    test_sun3 = Sundae("Pecan", 1, 3.50, "Nuts", 0.50)
    
    assert test_sun1.get_cost() == 2.50
    assert test_sun1.get_scoop() == 2
    assert test_sun1.get_name() == "Starwberry"
    assert test_sun1.get_topping() == "sprinkles"
    assert test_sun1.get_topping_price() == 0.25
    assert test_sun1.calc_cost() == 2.75
    assert test_sun1.calculate_tax() == 0.18

    assert test_sun2.get_cost() == 1.75
    assert test_sun2.get_scoop() == 3
    assert test_sun2.get_name() == "Chocolate"
    assert test_sun2.get_topping() == "Fudge"
    assert test_sun2.get_topping_price() == 0.75
    assert test_sun2.calc_cost() == 2.50
    assert test_sun2.calculate_tax() == 0.13

    assert test_sun3.get_cost() == 3.50
    assert test_sun3.get_scoop() == 1
    assert test_sun3.get_name() == "Pecan"
    assert test_sun3.get_topping() == "Nuts"
    assert test_sun3.get_topping_price() == 0.50
    assert test_sun3.calc_cost() == 4.00
    assert test_sun3.calculate_tax() == 0.25