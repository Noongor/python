price = 100


def inc_vat(price):
    return price + (price * 7 / 100)


def exc_vat(price):
    return price + (price * 7 / 100)


if __name__ == '__main__':
    my_produc_price = 100
    print("price vat " + str(inc_vat(my_produc_price)))

    print("price exc" + str(exc_vat(my_produc_price)))
