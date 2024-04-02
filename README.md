# :date: Leap Year Kata :date:

[![Python](https://img.shields.io/badge/Python-3.11+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)

## Resources

These instructions where extracted from Codurance Kata Catalogue. You can find the original instructions in the link below.

[![Web](https://img.shields.io/badge/Codurance-Website-14a1f0?style=for-the-badge&logo=web&logoColor=white&labelColor=101010)](https://www.codurance.com/katas/leap-year)

## Description
  
Write a function that:
- Receives an integer as input.
- Returns `True` if the input is a leap year
- Returns `False` if the input is not a leap year

A leap year must follow these rules:

- A year is not leap if it is not divisible by 4
- A year is leap if it is divisible by 4
- A year is leap if it is divisible by 400
- A year is not leap if it is divisible by 100 but not by 400

### Examples

- 1997 is not leap (not divisible by 4)
- 1996 is leap (divisible by 4)
- 1600 is leap (divisible by 400)
- 1800 is not leap (divisible by 4, divisible by 100, NOT divisible by 400)

## Objective

The main objective of this kata is to improve logic skills in Python.

Additionally, TDD is going to be used as methodology to develop the function. The following concepts will be applied:

- Red-Green-Refactor cycle
- Fake it till you make it
- Baby steps
- Test parametrization


## Configuration

The project can be configured either by using `pip` or `pipenv`. Both ways will be explained.

<details><summary>Using pip</summary>

1. Create a virtual environment:
    ```bash
    python -m venv .venv
    ```
2. Activate the virtual environment:
    ```bash
    source .venv/bin/activate # Linux / Mac
    .venv\Scripts\activate # Windows
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
</details>

<details><summary>Using pipenv</summary>

1. Install pipenv:
    ```bash
    pip install pipenv
    ```
2. Create a virtual environment with desire python version
    ```bash
    pipenv --python 3.11
    ```
   
    By default it will create the virtual environment outside the project. To create it inside the project, use the following command:
    ```bash
    PIPENV_VENV_IN_PROJECT=1 pipenv --python 3.11
    ```
3. Install the dependencies:
    ```bash
    pipenv install
    ```
</details>

## Running the tests

To run the tests, execute one of the following commands:

```bash
pytest
```

or

```bash
pipenv run test
```

### Visit my GitHub profile to see all solved katas 🚀

[![Web](https://img.shields.io/badge/GitHub-Dimanu.py-14a1f0?style=for-the-badge&logo=github&logoColor=white&labelColor=101010)](https://github.com/dimanu-py/code-katas)