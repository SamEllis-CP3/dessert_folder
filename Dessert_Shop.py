from abc import ABC, abstractmethod
from packaging import Packaging
from receipt import make_receipt

class DessertItem(ABC, Packaging):
    def __init__(self, name):
        self.name = name
        self.tax_percent = 7.25
        self.packaging = None
    def __str__(self):
        return f"You ordered a {self.name}"
    def get_name(self):
        return self.name
    def calculate_tax(self):
        return round(self.calculate_cost() * (self.tax_percent/100), 2)

    @abstractmethod
    def calculate_cost(self):
        pass
    
class Candy(DessertItem):
    def __init__(self, name, candy_weight, price_per_pound):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound
        self.packaging = "Bag"
    def get_candy_weight(self):
        return self.candy_weight
    def get_price_per_pound(self):
        return self.price_per_pound
    def calculate_cost(self):
        return round(self.candy_weight * self.price_per_pound, 2)
    def __str__(self):
        return f"{self.name} ({self.packaging}), {self.candy_weight}lbs, ${self.price_per_pound}/lbs, ${self.calculate_cost()}, ${self.calculate_tax()}"
    
class Cookie(DessertItem):
    def __init__(self, name, cookie_quantity, price_per_dozen):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen
        self.packaging = "Box"
    def get_cookie_quantity(self):
        return self.cookie_quantity
    def get_price_per_dozen(self):
        return self.price_per_dozen
    def calculate_cost(self):
        return round(self.cookie_quantity * (self.price_per_dozen/12), 2)
    def __str__(self):
        return f"{self.name} ({self.packaging}), {self.cookie_quantity} cookie(s), ${self.price_per_dozen}/dozen, ${self.calculate_cost()}, ${self.calculate_tax()}"
    
class IceCream(DessertItem):
    def __init__(self, name, scoop_count, price_per_scoop):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
        self.packaging = "Bowl"
    def get_scoop_count(self):
        return self.scoop_count
    def get_price_per_scoop(self):
        return self. price_per_scoop
    def calculate_cost(self):
        return round(self.scoop_count * self.price_per_scoop, 2)
    def __str__(self):
        return f"{self.name} ({self.packaging}), {self.scoop_count} scoop(s), ${self.price_per_scoop}/scoop, ${self.calculate_cost()}, ${self.calculate_tax()}"

class Sundae(IceCream):
    def __init__(self, name, scoop_count, price_per_scoop, topping_name, topping_price):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price
        self.packaging = "Boat"
    def get_topping_name(self):
        return self.topping_name
    def get_topping_price(self):
        return self.topping_price
    def calculate_cost(self):
        return round((self.scoop_count * self.price_per_scoop) + self.topping_price, 2)
    def __str__(self):
        return f"{self.name} ({self.packaging}), {self.scoop_count} scoop(s), ${self.price_per_scoop}/scoop, {self.topping_name}, ${self.topping_price}, ${self.calculate_cost()}, ${self.calculate_tax()}"

class Order():
    def __init__(self):
        self.order = []
    def add(self, dessertitem):
        self.order.append(dessertitem)
    def __len__(self):
        return len(self.order)
    def order_cost(self):
        cost = 0.0
        for item in self.order:
            cost += item.calculate_cost()
        return cost
    def order_tax(self):
        tax = 0.0
        for item in self.order:
            tax += item.calculate_cost() * (item.tax_percent/100)
        return tax
    def __str__(self):
        order_summary = []
        for item in self.order:
            order_summary.append(str(item))
        return '; '.join(order_summary)


class DessertShop():
    def user_prompt_candy(self):
        while True:
            candy_name = input("Candy name: ")
            if isinstance(candy_name, str):
                break
            else:
                print("This is not a String, Try again!")
                continue
            
        while True:        
            try:
                weight = float(input("Candy weight in pounds: "))
            except ValueError:
                print("Thats not a float, try again!")
                continue
            if isinstance(weight, float):
                break
        while True:
            try:
                price = float(input("Price per pounds: "))
            except ValueError:
                print("Thats not a float, try again!")
                continue
            if isinstance(price, float):
                break

        candy1 = Candy(candy_name, weight, price)
        return candy1    

    def user_prompt_cookie(self):
        while True:
            cookie_name = input("Cookie name: ")
            if isinstance(cookie_name, str):
                break
            else:
                print("This is not a String, Try again!")
                continue
        while True:
            try:       
                amount = int(input("Amount of cookies: ")) 
            except ValueError:
                print("That's not a integer. Type in a integer.")
                continue
            if isinstance(amount, int):
                break
        while True:
            try:
                price_12 = float(input("Price per dozen: "))
            except ValueError:
                print("Thats not a float, try again!")
                continue    
            if isinstance(price_12, float):
                break
        cookie1 = Cookie(cookie_name, amount, price_12)
        return cookie1    

    def user_prompt_icecream(self):
        while True:
            icecream_name = input("Icecream name: ")
            if isinstance(icecream_name, str):
                break
            else:
                print("This is Not a string, Try again")
                continue

        while True:
            try:
                scooby_number = int(input("How many scoops: "))
            except ValueError:
                print("This is not a integer, Try again!")
                continue
            if isinstance(scooby_number, int):
                break
        while True:
            try:
                scooby_price = float(input("Price per scoop: "))
            except ValueError:
                print("Thats not a float, Try again!")
                continue
            if isinstance(scooby_price, float):
                break
            
        icecream1 = IceCream(icecream_name, scooby_number, scooby_price)
        return icecream1
        
    def user_prompt_sundae(self):
        while True:
            sundae_name = input("Ice cream name: ")
            if isinstance(sundae_name, str):
                break
            else:
                print("This is not a String, Try again!")
                continue
        while True:  
            try:      
                scoop_num = int(input("Amount of scoops: "))
            except ValueError:
                print("This is not a Integer, Try again!")
                continue
            if isinstance(scoop_num, int):
                break

        while True:
            try:
                scoop_price = float(input("Price per scoop: "))
            except ValueError:
                print("Thats not a float, try again!")
                continue
            if isinstance(scoop_price, float):
                break

        while True:
            topping_name = input("Topping name: ")
            if isinstance(topping_name, str):
                break
            else:
                print("This is not a String, Try again!")
                continue
        while True:
            try:
                topping_price = float(input("Topping price: "))
            except ValueError:
                print("Thats not a float, try again!")
                continue
            if isinstance(topping_price, float):
                break

        sundae1 = Sundae(sundae_name, scoop_num, scoop_price, topping_name, topping_price)
        return sundae1
    
def main(Order):
    shop = DessertShop()
    order = Order()
    '''
    order.add(Candy('Candy Corn', 1.5, 0.25))
    order.add(Candy('Gummy Bears', 0.25, 0.35))
    order.add(Cookie('Chocolate Chip', 6, 3.99))
    order.add(IceCream('Pistachio', 2, 0.79))
    order.add(Sundae('Vanilla', 3, 0.69, 'Hot Fudge', 1.29))
    order.add(Cookie('Oatmeal Raisin', 2, 3.45))
    '''
    # boolean done = false
    done: bool = False
    # build the prompt string once
    prompt = '\n'.join([ '\n',
        '1: Candy',
        '2: Cookie',
        '3: Ice Cream',
        '4: Sunday',
        '\nWhat would you like to add to the order? (1-4, Enter for done): '
    ])

    while not done:
        choice = input(prompt)
        match choice:
            case '':
                done = True
            case '1':
                item = shop.user_prompt_candy()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case '2':
                item = shop.user_prompt_cookie()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case '3':
                item = shop.user_prompt_icecream()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case '4':
                item = shop.user_prompt_sundae()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case _:
                print('Invalid response: Please enter a choice from the menu (1-4) or Enter')
        print()

    data = [["Name", "Amount", "Price"]]
    for item in order.order:
        if isinstance(item, Candy):
            data.append([item.name, item.candy_weight, item.price_per_pound])
        elif isinstance(item, Cookie):
            data.append([item.name, item.cookie_quantity, item.price_per_dozen])
        elif isinstance(item, IceCream):
            data.append([item.name, item.scoop_count, item.price_per_scoop])
        elif isinstance(item, Sundae):
            data.append([item.name, item.scoop_count, item.price_per_scoop, item.topping_name, item.topping_price])
    data.append(["Order Subtotals", "$"+str(round(order.order_cost(), 2)), "$" + str(round(order.order_tax(), 2))])
    data.append(["Total", "", "$" + str(round(order.order_cost() + order.order_tax(), 2))])
    data.append(["Total items in the order", "", str(order.__len__())])
    import receipt
    receipt.make_receipt(data, "receipt.pdf")
    print(order)

main(Order)
