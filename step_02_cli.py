import click


@click.command()
@click.option('--number', prompt='Your number')
def hello(numbers):
    subtraction = 0
    """Simple program that greets NAME for a total of COUNT times."""
    numbers_list = list(map(int, numbers.split(',')))
    for x in numbers_list:
        subtraction -= x
    click.echo(subtraction)


if __name__ == '__main__':
    hello()
