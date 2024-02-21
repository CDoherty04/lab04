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
                    print()
                    break

                elif mode == "-v":
                    print(fib_value(value))
                    print()
                    break

                # Check for invalid input
                else:
                    print("\nUse -i or -v for index search and value search, respectively\n")
                    continue

        # Loop continues until integers are given
        except ValueError:
            print("\nThe input requires '-i' or '-v' and an integer value\n")


def fib_term(index):
    """Returns the result of the fibonacci sequence at a given index."""

    # Base cases
    if index == 0 or index == 1:
        return index

    # Return the last number plus the one before that
    else:
        return fib_term(index-1) + fib_term(index-2)


def fib_value(value):
    """Returns whether the fibonacci sequence contains a given value at any index"""

    # Base case
    if value == 0 or value == 1:
        return f"{value} is in the sequence"

    else:
        count = 3
        current = 0
        while current < value:
            current = fib_term(count)
            count += 1
        if value == current:
            return f"{value} is in the sequence"
        else:
            return f"{value} is not in the sequence"
