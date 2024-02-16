"""
Author: Charlie Doherty
KUID: 3115329
Date: 2/16/24
Lab: 04
Last modified: 02/16/24
Purpose: Use recursion to solve given problems

Run driver to execute the program
"""
from executive import Executive


def main():
    """Hands the process over to an Executive object"""

    my_exec = Executive()
    my_exec.run()


if __name__ == "__main__":
    """Call stack begins here"""

    main()
