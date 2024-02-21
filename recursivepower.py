def run():
    """Gets valid input to be called recursively"""

    while True:
        try:

            # Get input
            base = int(input("Give an integer base: "))
            power = int(input("Give an integer power greater than or equal to 0: "))

            # Check for power less than 0
            if power < 0:
                print("\nThe power requires an integer greater than or equal to 0\n")
                continue

            else:
                # Begin recursive call, print the result, and end the loop
                print(recursive_power(base, power))
                print()
                break

        # Loop continues until integers are given
        except ValueError:
            print("\nThe input requires integer values\n")


def recursive_power(base, power):
    """Prints the result of the base taken to the given power."""

    # Base cases
    if power == 0:
        return 1
    elif power == 1:
        return base

    # Return the base times the base to the power-1
    # eg: 3^2 would become 3 * 3^1
    else:
        return base * recursive_power(base, power-1)
