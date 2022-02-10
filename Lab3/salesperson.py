# Your task is to implement the following class methods:
# (1) __init__(self, name): the constructor creates a student instance with a given name.
# After initialization, the record is an empty dictionary and the value is 0.
# (2) get_name(self): returns the name of the salesman
# (3) buy_pro(self, product_name, market_price, quantity):  buy a product, (product_name, market_price, quantity),
# to owner's record. You need to update the record and value. If the product is in the record, update the values of
# record[product_name]; if not, create a new key.
# (4) sell_pro(self, product_name, market_price, quantity):  sell a product, (product_name, market_price, quantity),
# to owner's record. You need to update the record and value. Update the values of record[product_name]. After the update,
# if the quantity becomes zero, delete the key.
# (5) get_record(self): returns the owner's product record.
# (6) get_value(self): returns the value in the account.

class Salesperson:
    def __init__(self, name):
        self.name = name
        self.record = {}
        self.value = 0

    def get_name(self):
        return self.name

    def buy_pro(self, product_name, market_price, quantity):
        if(product_name not in self.record):
            self.record[product_name] = [market_price, quantity]
            self.value = -market_price * quantity
        else:
            new_price = 0
            new_quantity = 0
            new_cost = 0
            previous_price = self.record[product_name][0]

            new_quantity += self.record[product_name][1] + quantity

            new_cost = (-self.get_value() + market_price)/new_quantity

            self.record[product_name][0] = new_cost
            self.record[product_name][1] = new_quantity

            self.value = -new_cost * new_quantity


    def sell_pro(self, product_name, market_price, quantity):
        change_val = market_price * quantity
        self.value = self.get_value() + change_val
        self.record[product_name][1] -= quantity

        if(self.record[product_name][1] == 0):
            del self.record[product_name]

    def get_record(self):
        return self.record

    def get_value(self):
        return self.value


# Example:

sp_amy = Salesperson('Amy')
sp_john = Salesperson('John')
print(sp_amy.get_name())

if sp_amy.record != {}:
    print("something is wrong")
# Amy
#
# print(sp_john.get_value())
# # 0
#
# sp_john.buy_pro('iwatch', 350,3)
# print(sp_john.get_record())
# # {'iwatch': [350, 3]}
#
# print(sp_john.get_value())
# # -1050
#
# sp_john.buy_pro('iwatch', 300,1)
# print(sp_john.get_record())
# # {'iwatch': [337.5, 4]}
#
# print(sp_john.get_value())
# # -1350
#
#
# sp_john.sell_pro('iwatch', 400,2)
# print(sp_john.get_record())
# # {'iwatch': [337.5, 2]}
#
# print(sp_john.get_value())
# # -550
#
#
# sp_amy.buy_pro("TV", 500,2)
# print(sp_amy.get_record())
# # {'TV': [500, 2]}
#
# print(sp_amy.get_value())
# # -1000
