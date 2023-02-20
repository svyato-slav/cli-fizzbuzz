import click
import pytest

from src.fizz_buzz import calculate_answer


def echo_answer(number):
    answer = calculate_answer(number)
    click.echo(answer)


@pytest.fixture(autouse=True)
def patch_echo_answer(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr('src.fizz_buzz.echo_answer', echo_answer)
