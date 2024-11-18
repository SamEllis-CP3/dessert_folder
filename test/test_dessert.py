from Dessert_Shop import DessertItem, Candy

def test_tax():
    test_1 = Candy("Carmel")
    assert test_1.tax_percent == 7.25