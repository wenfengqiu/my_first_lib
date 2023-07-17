def factorial(n):
    """
    Calculates the factorial of a number.

    Args:
      n: The number to calculate the factorial of.

    Returns:
      The factorial of n.
    """

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    print(factorial(5))


if __name__ == "__main__":
    main()
