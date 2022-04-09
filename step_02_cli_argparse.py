"""
USE CLI:
    python step_02_cli_argparse.py '1,2,3,4,5'
Linux and MacOS:
    python3 step_02_cli_argparse.py '1,2,3,4,5'
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("subtraction",
                    help="subtraction numbers", nargs='+')
args = parser.parse_args()
# print(args.subtraction)

for x in args.subtraction:
    # print(type(x))  # str
    subtraction = 0
    expo = map(int, x.split(','))
    for i in expo:
        subtraction -= i
    print(subtraction)

"""
nargs - ввод нескольких чисел
"""
