# A example of adding argparse-style options to pytest
# Adds the argparse-like option


def pytest_addoption(parser):
    parser.addoption(
        "--length", action="store", default="0", help="Total number of characters"
    )
    parser.addoption(
        "--no_of_alphanum",
        action="store",
        default="0",
        help="Number of alphabetic characters",
    )
