def run():
    """Gets valid input to be called recursively"""

    while True:
        try:

            # Get input
            command = input("Enter mode and value (-i or -v with an integer [0, inf)): ").strip().lower()
            mode, value = command.split(" ")
            value = int(value)

            # Check for negative numbers
            if value < 0:
                print("\nThe given value must be 0 or higher\n")
                continue

            else:

                # Begin recursive call, print the result, and end the loop
                if mode == "-i":
                    print(fib_term(value))
                    break

                elif mode == "-v":
                    print(fib_value(value))
                    break

                # Check for invalid input
                else:
                    print("\nUse -i or -v for index search and value search, respectively\n")
                    continue

        # Loop continues until integers are given
        except ValueError:
            print("\nThe input requires '-i' or '-v' and an integer value\n")


def fib_term(term):
    """Prints the result of the fibonacci sequence at a given term."""

    # Base cases
    if term == 0 or term == 1:
        return term

    # Return the last number plus the one before that
    else:
        return fib_term(term-1) + fib_term(term-2)


def fib_value(value):
    """Prints the result of the base taken to the given power."""
    pass
