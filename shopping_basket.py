import math

class Product(object):

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return self.name


class LineItem(object):

    def __init__(self, product, count):
        self.product = product
        self.count = count
        self.line_total = product.price * count

    def two_for_one(self):
        singles = self.count % 2
        groups_of_two = math.floor(self.count / 2)
        cost_for_singles = singles * self.product.price
        cost_for_groups = groups_of_two * self.product.price
        self.line_total = round(cost_for_singles + cost_for_groups, 2)

    def three_for_two(self):
        singles = self.count % 3
        groups_of_three = math.floor(self.count / 3)
        cost_for_singles = singles * self.product.price
        cost_for_groups = groups_of_three * self.product.price * 2
        self.line_total = round(cost_for_singles + cost_for_groups, 2)

    def apply_discount(self):
        if self.product.name == 'watermelon':
            self.three_for_two()
        elif self.product.name == 'apple':
            self.two_for_one()



class Basket(object):

    def __init__(self):

        self.line_items = []




