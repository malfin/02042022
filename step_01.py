# products = [1, 45, 87, 2, 5, 23, 9]
#
# seen_prods = [87, 1, 5]

# target_prods = [45, 2, 23, 9]


def filter_products(products, seen_prods):
    target_prods = list(set(products).symmetric_difference(seen_prods))

    return target_prods


print(filter_products(
    [1, 45, 87, 2, 5, 23, 9],
    [87, 1, 5]
))
