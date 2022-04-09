import click


@click.command()
@click.option('--number', prompt='Your numbers')
def hello(number):
    subtraction = 0
    numbers_list = list(map(int, number.split(',')))
    for x in numbers_list:
        subtraction -= x
    click.echo(subtraction)


if __name__ == '__main__':
    hello()
