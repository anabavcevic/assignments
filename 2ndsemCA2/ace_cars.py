import sys

from dbdealership import Dealership


def main(argv):
    """Main application code loads the database and enters rental loop."""

    # Default DB path is 'data' subdirectory of the current working directory.
    data_path = './data'

    # If there was at least one argument passed to the application and
    # that argument is not an empty string, assume that was an explicit
    # path to the DB files.
    if len(argv) >= 2 and argv[1]:
        data_path = argv[1]

    # Create a new instance of Dealership, loading the data from the specified
    # data path and print the current state of stock.
    ds = Dealership(data_path)
    ds.stock_count()

    # Enter the main rental loop and continue asking for rentals until the user
    # responds with 'n' to the Continue request.
    proceed = 'y'
    while proceed == 'y':
        ds.process_rental()
        proceed = input('Continue? y/n\n')


# This is needed if I want to test main().
# Testing main() requires the test package to import ace_cars which must not
# trigger the execution of the application. The way to achieve this is to have
# the application code contained in a function that a top-level code calls
# only when being executed directly (__name__ will euqal '__main__' in that case)
# and not in import.
if __name__ == '__main__':
    main(sys.argv)