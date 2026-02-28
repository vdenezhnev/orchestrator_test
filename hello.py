"""Module containing a simple hello world function."""


def hello_world():
    """Return a greeting string.

    Returns:
        str: The greeting "Hello, World!"

    Example:
        >>> hello_world()
        'Hello, World!'
    """
    return "Hello, World!"


def print_numbers():
    """Print numbers from 1 to 100.

    Prints each number from 1 to 100 on a separate line.

    Example:
        >>> print_numbers()
        1
        2
        3
        ...
        100
    """
    for i in range(1, 101):
        print(i)


if __name__ == "__main__":
    print(hello_world())
    print_numbers()
