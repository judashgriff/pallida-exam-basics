# We run a Candy shop where we sell candies and lollipops
# One lollipop's price is 10$
# And it made from 5gr of sugar
# One candie's price is 20$
# And it made from 10gr of sugar
# we can raise their prices with a given percentage
#
# Create a CandyShop class
# It can store sugar and money as income. The constructor should take the amount of sugar in gramms.
# we can create lollipops and candies store them in the CandyShop's storage
# If we create a candie or lollipop the CandyShop's sugar amount gets reduced by the amount needed to create the sweets
# We can raise the prices of all candies and lollipops with a given percentage
# We can sell candie or lollipop with a given number as amount
# If we sell sweets the income will be increased by the price of the sweets and we delete it from the inventory
# We can buy sugar with a given number as amount. The price of 1000gr sugar is 100$
# If we buy sugar we can raise the CandyShop's amount of sugar and reduce the income by the price of it.
# The CandyShop should be represented as string in this format:
# "Inventory: 3 candies, 2 lollipops, Income: 100, Sugar: 400gr"

# candy_shop = CandyShop(300)
# candy_shop.create_sweets("candy")
# candy_shop.create_sweets("candy")
# candy_shop.create_sweets("lollipop")
# candy_shop.create_sweets("lollipop")
# print(candy_shop)
# # Should print out:
# # Invetory: 2 candies, 2 lollipops, Income: 0, Sugar: 270gr
# candy_shop.sell("candy", 1)
# print(candy_shop)
# # Should print out:
# # "Invetory: 1 candies, 2 lollipops, Income:20, Sugar: 285gr"
# candy_shop.raise_prices(5)
# candy_shop.sell("lollipop", 1)
# print(candy_shop)
# # Should print out:
# # "Invetory: 1 candies, 1 lollipops, Income:35, Sugar: 285gr"
# candy_shop.buy_sugar(300)
# print(candy_shop)
# Should print out:
# "Invetory: 1 candies, 1 lollipops, Income:5, Sugar: 315gr"

class CandyShop:
    def __init__(self):
        self.sugar_amount = 150
        self.income = 50
        self.inventory = {"candy": 4,
                          "lollipop": 3}
        self.show_what_we_have()
        self.candy_price = 20
        self.lollipop_price = 10

    def calculate_sugar(self):
        return str(self.sugar_amount) + "gr"

    def show_what_we_have(self):
        print("Invetory: " + str(self.inventory["candy"]) +
              " candies, " + str(self.inventory["lollipop"]) +
              " lollipops, Income:" + str(self.income) +
              ", Sugar: " + self.calculate_sugar())


    def create_sweets(self, sweet):
        if sweet == "lollipop":
            self.sugar_amount -= 5
            self.inventory[sweet] += 1
        elif sweet == "candy":
            self.sugar_amount -= 10
            self.inventory[sweet] += 1
        else:
            print("\nWe don't make that kind of sweets here.")
            return
        self.show_what_we_have()


    def sell_sweets(self, sweet, amount):
        if sweet == "lollipop" and amount <= self.inventory[sweet]:
            self.inventory[sweet] -= amount
            self.income += amount * self.lollipop_price
        elif sweet == "candy" and amount <= self.inventory[sweet]:
            self.inventory[sweet] -= amount
            self.income += amount * self.candy_price
        elif sweet in self.inventory and amount > self.inventory[sweet]:
            print("\nWe don't have enaugh " + sweet + "s to sell!")
        else:
            print("\nWe don't sell that kind of sweets here.")
            return
        self.show_what_we_have()


    def buy_sugar(self, amount):
        if self.income >= int(amount / 10):
            self.sugar_amount += amount
            self.income -= int(amount / 10)
        else:
            print("\nWe don't have enough money to buy this much sugar!")        
        self.show_what_we_have()
        
    def increase_prices(self, amount):
        self.candy_price += self.candy_price * amount / 100
        self.lollipop_price += self.lollipop_price * amount / 100


''' Test the exercise with theese if you like '''


candy_shop = CandyShop()
# candy_shop.create_sweets("candy")
# candy_shop.create_sweets("lollipop")
# candy_shop.create_sweets("sweet roll")

# candy_shop.sell_sweets("candy", 3)
# candy_shop.sell_sweets("lollipop", 6)
# candy_shop.sell_sweets("sweet roll", 6)

# candy_shop.buy_sugar(500)
# candy_shop.buy_sugar(1500856)

# candy_shop.increase_prices(50)
# candy_shop.sell_sweets("candy", 1)
