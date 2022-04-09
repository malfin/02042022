import click


@click.command()
@click.option('--number', help='Number of greetings.', prompt='Numbers')
def number():
    summa = 0
    numbers_list = list(map(int, numbers.split("','")))
    for i in numbers_list:
        summa -= i

    click.echo(summa)


if __name__ == '__main__':
    number()
