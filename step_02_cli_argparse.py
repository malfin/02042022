import argparse

parser = argparse.ArgumentParser()
parser.add_argument("subtraction",
                    help="subtraction", nargs='+')
args = parser.parse_args()
# print(args.subtraction)

for x in args.subtraction:
    print(type(x))  # str
    subtraction = 0
    expo = map(int, x.split(','))
    for i in expo:
        subtraction -= i
    print(subtraction)
