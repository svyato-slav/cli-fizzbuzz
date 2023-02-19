import click


def calculate_answer(number):
    if number % 15 == 0:
        return "FizzBuzz!"
    if number % 3 == 0:
        return "Fizz!"
    if number % 5 == 0:
        return "Buzz!"
    return number


def echo_answer(number):
    answer = calculate_answer(number)
    click.echo(answer)
    prompt()


def prompt():
    number = click.prompt('Number', type=int)
    echo_answer(number)


@click.command()
def cli():
    """
    A little tool that get an integer and instead of multiples of 3 print the word "Fizz".
    Instead of multiples of 5 the word "Buzz".
    If the number is a multiple of both 3 and 5 display the word "FizzBuzz"
    """
    click.echo("Welcome to Fizz Buzz!")
    click.echo("Submit a number and get an answer!")
    prompt()
