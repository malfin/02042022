import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square",
                    help="display a square of a given number", nargs='+')
subtraction = 0
args = parser.parse_args()
print(args.square)
# answer -= args.square
#
# print(answer)
