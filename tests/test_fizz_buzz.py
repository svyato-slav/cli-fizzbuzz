import pytest
from click.testing import CliRunner

from src.fizz_buzz import cli

PARAM_ANSWER_MAPPING = {
    '3': 'Fizz!',
    '5': 'Buzz!',
    '15': 'FizzBuzz!',
    '11': '11',
}

INPUTS = PARAM_ANSWER_MAPPING.keys()


@pytest.fixture(params=INPUTS)
def integer_input(request):
    return request.param


def test_echo_answer(integer_input):
    runner = CliRunner()
    result = runner.invoke(cli, input=integer_input)
    answer = PARAM_ANSWER_MAPPING[integer_input]
    assert result.output == f'Welcome to Fizz Buzz!\n' \
                            f'Submit a number and get an answer!\n' \
                            f'Number: {integer_input}\n' \
                            f'{answer}\n'
