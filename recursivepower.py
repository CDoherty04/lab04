class RecursivePower:

    def __init__(self):
        """Gets valid input to be called recursively"""

        while True:
            try:

                # Get input
                self.base = int(input("Give an integer base: "))
                self.power = int(input("Give an integer power greater than or equal to 0: "))

                # Check for power less than 0
                if self.power < 0:
                    print("\nThe power requires an integer greater than or equal to 0\n")
                    continue

                else:
                    # Begin recursive call, print the result, and end the loop
                    print(self.recursive_power(self.base, self.power))
                    break

            # Loop continues until integers are given
            except ValueError:
                print("\nThe input requires integer values\n")

    def recursive_power(self, base, power):
        """Prints the result of the base taken to the given power."""

        # Base cases
        if power == 0:
            return 1
        elif power == 1:
            return self.base

        # Return the base times the base to the power-1
        # eg: 3^2 would become 3 * 3^1
        else:
            return base * self.recursive_power(base, power-1)
