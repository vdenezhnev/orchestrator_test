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


if __name__ == "__main__":
    print(hello_world())
