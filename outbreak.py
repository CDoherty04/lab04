class Outbreak:

    def __init__(self):
        """Gets valid input to be called recursively"""

        while True:
            try:

                # Get input
                self.day = int(input("What day do you want a sick count for?\n"))

                # Check for day less than 1
                if self.day < 1:
                    print("\nCan't have a day less than 1\n")
                    continue

                else:
                    # Begin recursive call, print the result, and end the loop
                    print(self.get_total_sick(self.day))
                    break

            # Loop continues until integers are given
            except ValueError:
                print("\nThe input requires integer values\n")

    def get_total_sick(self, day):
        """Prints the total number of people sick on the given day"""

        # Base cases
        if day == 1:
            return 6
        elif day == 2:
            return 20
        elif day == 3:
            return 75

        # After day 3 return the total of the last 3 days sick
        else:
            return self.get_total_sick(day-1) + self.get_total_sick(day-2) + self.get_total_sick(day-3)
