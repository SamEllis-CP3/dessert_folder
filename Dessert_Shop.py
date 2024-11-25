from abc import ABC, abstractmethod

from receipt import make_receipt

class DessertItem(ABC):
    def __init__(self, name):
        self.name = name
        self.tax_percent = 7.25

    def get_name(self):
        return self.name
    
    @abstractmethod
    def calc_cost(self):
        pass

    def calculate_tax(self) -> float:
        return self.calc_cost() * (self.tax_percent / 100)
        
    
    
class Candy(DessertItem):
    def __init__(self, name,candy_weight, price_per_pound):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound
    
    def get_cost(self):
        return self.price_per_pound
    
    def get_weight(self):
        return self.candy_weight
    
    def calc_cost(self):
        return self.candy_weight * self.price_per_pound

class Cookie(DessertItem):
    def __init__(self, name, quantity, price_per_dozen):
        super().__init__(name)
        self.quantity = quantity
        self.price_per_dozen = price_per_dozen

    def get_cost(self):
        return self.price_per_dozen
    
    def get_amount(self):
        return self.quantity
    
    def calc_cost(self):
        return (self.quantity / 12) * (self.price_per_dozen)
    
    
class IceCream(DessertItem):
    def __init__(self, name, scoop_count, price_per_scoop):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
    
    def get_scoop(self):
        return self.scoop_count
    
    def get_cost(self):
        return self.price_per_scoop
    
    def calc_cost(self):
        return self.price_per_scoop * self.scoop_count

class Sundae(IceCream):
    def __init__(self, name, scoop_count, price_per_scoop, topping_name, topping_price):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price

    def get_topping(self):
        return self.topping_name
    
    def get_topping_price(self):
        return self.topping_price
    
    def calc_cost(self):
        return super().calc_cost() + self.topping_price
    

class Order:
    def __init__(self):
        self.order = []

    def add(self, item):
        self.item = item
        
        self.order.append(self.item)
        

    def __len__(self):
        size = len(self.order)
        return size
    
    def order_cost(self) -> float:
        return sum(item.calc_cost() for item in self.order)
    
    def order_tax(self) -> float:
        return sum(item.calculate_tax() for item in self.order)
    
    def get_order_data(self) -> float:
        data = []
        for item in self.order:
            item_cost = item.calc_cost()
            tax_amount = item.calculate_tax()
            data.append([item.get_name(), f"${item_cost: .2f}", f"${tax_amount: .2f}"])
        return data
    


class DessertShop:
    @staticmethod
    def user_prompt_candy():
        name = input("Enter the type of candy: ").strip()
        
        while True:
            try:
                weight = float(input(f"Enter the weight of {name} in pounds: ").strip())
                if weight <= 0:
                    raise ValueError("Weight must be a positive number.")
                break
            except ValueError as e:
                print(f"Invalid input. Please enter a valid weight. {e}")
        
        while True:
            try:
                price_per_pound = float(input("Enter the price per pound: ").strip())
                if price_per_pound <= 0:
                    raise ValueError("Price must be a positive number.")
                break
            except ValueError as e:
                print(f"Invalid input. Please enter a valid price. {e}")

        return Candy(name, weight, price_per_pound)

    @staticmethod
    def user_prompt_cookie():
        name = input("Enter the type of cookie: ").strip()
        
        while True:
            try:
                amount = float(input(f"Enter the amount of {name} in dozens: ").strip())
                if amount <= 0:
                    raise ValueError("Amount must be a positive number.")
                break
            except ValueError as e:
                print(f"Invalid input. Please enter a valid amount. {e}")
        
        while True:
            try:
                price_per_dozen = float(input("Enter the price per dozen: ").strip())
                if price_per_dozen <= 0:
                    raise ValueError("Price must be a positive number.")
                break
            except ValueError as e:
                print(f"Invalid input. Please enter a valid price. {e}")

        return Cookie(name, amount, price_per_dozen)

    @staticmethod
    def user_prompt_icecream():
        name = input("Enter the type of icecream: ").strip()
        
        while True:
            try:
                scoops = float(input(f"Enter the scoop amount of {name}: ").strip())
                if scoops <= 0:
                    raise ValueError("Scoops must be a positive number.")
                break
            except ValueError as e:
                print(f"Invalid input. Please enter a valid amount. {e}")
        
        while True:
            try:
                price_per_scoop = float(input("Enter the price per scoop: ").strip())
                if price_per_scoop <= 0:
                    raise ValueError("Price must be a positive number.")
                break
            except ValueError as e:
                print(f"Invalid input. Please enter a valid price. {e}")

        return Candy(name, scoops, price_per_scoop)

    @staticmethod
    def user_prompt_sundae():
        name = input("Enter the type of icecream: ").strip()
        topping_name = input("Enter the type of topping you want: ").strip
        while True:
            try:
                scoop_count = float(input(f"Enter the scoop amount of {name}: ").strip())
                if scoop_count <= 0:
                    raise ValueError("Scoops must be a positive number.")
                break
            except ValueError as e:
                print(f"Invalid input. Please enter a valid amount. {e}")
        
        while True:
            try:
                price_per_scoop = float(input("Enter the price per scoop: ").strip())
                if price_per_scoop <= 0:
                    raise ValueError("Price must be a positive number.")
                break
            except ValueError as e:
                print(f"Invalid input. Please enter a valid price. {e}")

        while True:
            try:
                toppings = float(input(f"Enter the toppings amount of {topping_name}: "))
                if toppings <= 0:
                    raise ValueError("Toppings must be a positive number.")
                break
            except ValueError as e:
                print(f"Invalid input. Please enter a valid amount. {e}")

        while True:
            try:
                price_per_toppings = float(input("Enter the price per toppings: ").strip())
                if price_per_toppings <= 0:
                    raise ValueError("Price must be a positive number.")
                break
            except ValueError as e:
                print(f"Invalid input. Please enter a valid price. {e}")
        return Candy(name, scoop_count, price_per_scoop, topping_name, price_per_toppings)


def main():
    """
    
    Order_1 = Order()
    
    Order_1.add(Candy("Candy Corn", 1.5, .25))
    Order_1.add(Candy("Gummy Bears", .25, .35))
    Order_1.add(Cookie("Chocolate Chip", 6, 3.99))
    Order_1.add(IceCream("Pistachio", 2, .79))
    Order_1.add(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    Order_1.add(Cookie("Oatmeal Raisin", 2, 3.45))

    for item in Order_1.order:
        print(f"{item.get_name()} - ${item.calc_cost():.2f}")
        
    """

    order = Order()
    
    while True:
        print("\n1: Candy")
        print("2: Cookie")
        print("3: Ice Cream")
        print("4: Sundae")
        print("What would you like to add to the order? (1-4, Enter for done): ", end="")
        
        choice = input().strip()
        
        if choice == "":
            break
        
        if choice == "1":
            order.add(DessertShop.user_prompt_candy())
        elif choice == "2":
            order.add(DessertShop.user_prompt_cookie())
        elif choice == "3":
            order.add(DessertShop.user_prompt_icecream())
        elif choice == "4":
            order.add(DessertShop.user_prompt_sundae())
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
    
    print("\nOrder Summary:")
    for item in order.order:
        print(f"{item.get_name()} - ${item.calc_cost():.2f}")
    
    print(f"Total number of items in order: {len(order)}")
    print(f"Total cost of the order: ${order.order_cost():.2f}")
    print(f"Total tax applied: ${order.order_tax():.2f}")

    order_data = order.get_order_data()
    subtotal = order.order_cost()
    total_tax = order.order_tax()

    order_data.append(["Subtotal" , f"${subtotal: .2f}", f"${total_tax: .2f}"])
    order_data.append(["Total", "", f"${subtotal + total_tax: .2f}" ])
    order_data.append(["Total Items","", str(len(order))])

    make_receipt(order_data, "receipt.pdf")

if __name__ == "__main__":
    main()