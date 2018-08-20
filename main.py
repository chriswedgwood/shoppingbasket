import csv
from ShoppingBasket.shopping_basket import Basket, Product, LineItem


def main():

    basket = Basket()
    apples = LineItem(Product('apple', 0.20), 4)
    oranges = LineItem(Product('orange', 0.50), 3)
    watermelons = LineItem(Product('watermelon', 0.80), 5)
    line_items = [apples, oranges, watermelons]

    print("Shopping basket:")
    print("Name    Price    Count    Line Total")
    for line in line_items:
        line.apply_discount()
        print("%s    %s    %s    %s" % (line.product.name, line.product.price, line.count, line.line_total))





if __name__ == "__main__":
    main()


