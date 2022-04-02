# products = [1, 45, 87, 2, 5, 23, 9]
#
# seen_prods = [87, 1, 5]


# target_prods = ?


def filter_products(products, seen_prods):
    target_prods = []
    for item in products:
        if item not in seen_prods:
            target_prods.append(item)
    return target_prods


print(filter_products(
    [1, 45, 87, 2, 5, 23, 9],
    [87, 1, 5]
))

# target_prods = [45, 2, 23, 9]
