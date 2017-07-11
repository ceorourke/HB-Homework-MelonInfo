"""Print out all the melons in our inventory."""


# from melons import melon_names, melon_seedlessness, melon_prices

from melons import melons


def print_melon(melons):
    """Print each melon"""

    for melon in melons.items():

        name = melon[0]
        seedlessness = melon[1]['seedlessness']
        price = melon[1]['price']
        flesh_color = melon[1]['flesh_color']
        weight = melon[1]['weight']
        rind_color = melon[1]['rind_color']

        print name.upper()
        print "    seedless:", seedlessness
        print "    price:", price
        print "    flesh_color:", flesh_color
        print "    weight:", weight
        print "    rind_color:", rind_color
        print

print_melon(melons)