import argparse

parser = argparse.ArgumentParser()
answer = 0
parser.add_argument("square",
                    help="display a square of a given number", nargs='+')
numbers_list = list(map(int, parser.parse_args().split(',')))
print(numbers_list)
args = parser.parse_args()
answer -= args.square

print(answer)
