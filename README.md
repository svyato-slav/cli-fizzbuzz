# Python FizzBuzz 

_Python FizzBuzz is a CLI tool for famous FizzBuzz task._

## Installation

To install Python FizzBuzz, first clone the repository and then run:
`pip install .`

## Basic Usage

Type `fizz_buzz` in command line.

Here's an example of Python FizzBuzz output.

```bash
Welcome to Fizz Buzz!
Submit a number and get an answer!
Number: 3
Fizz!
Number: 5
Buzz!
Number: 15
FizzBuzz!
Number: 11
11
```

## Run tests

First install test dependencies:
`pip install .[tests]`

Then, run tests:
`pytest --cov-report html --cov=src tests/`


## Run linter

First install lint dependencies:
`pip install .[lint]`

Then, run lint:
`pylint src tests`
