import click


@click.command()
@click.option('--number', prompt='Your number')
def hello(numbers):
    subtraction = 0
    numbers_list = list(map(int, numbers.split(',')))
    for x in numbers_list:
        subtraction -= x
    click.echo(subtraction)


if __name__ == '__main__':
    hello()
