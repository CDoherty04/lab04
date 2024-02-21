"""
Author: Charlie Doherty
KUID: 3115329
Date: 2/16/24
Lab: 04
Last modified: 02/21/24
Purpose: Use recursion to solve given problems

Run driver to execute the program
"""
import recursivepower
import outbreak
import fibonacci


def main():
    """Runs the functions"""

    while True:
        try:

            # Have the user choose a program they want to use
            choice = int(input("With recursion...\n"
                               "1) Get a power of a base\n"
                               "2) Play Outbreak\n"
                               "3) Experiment with the fibonacci sequence\n"
                               "4) Quit the program\n"))
            print()

            # Run choice program
            match choice:
                case 1:
                    recursivepower.run()
                case 2:
                    outbreak.run()
                case 3:
                    fibonacci.run()
                case 4:
                    quit("Exiting...")

                # Check input's range
                case _:
                    print("Make sure the number you give is an integer between 1-4\n")
                    continue

        except ValueError:
            print("\nMake sure the number you give is an integer between 1-4\n")


if __name__ == "__main__":
    """Call stack begins here"""

    main()
