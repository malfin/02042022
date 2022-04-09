"""
USE CLI:
    python step_02_cli.py --number='1,2,3,4,5'

"""

import click


@click.command()
@click.option('--number', prompt='Your numbers')
def numbers(number):
    subtraction = 0
    numbers_list = list(map(int, number.split(',')))
    for x in numbers_list:
        subtraction -= x
    click.echo(subtraction)


if __name__ == '__main__':
    numbers()
