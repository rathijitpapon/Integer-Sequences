import logging

def main():
    """
    main function of the program for inputs and functions calling.

    """
    # take user input
    error_message = "Invalid input, please enter a non-negative integer"

    try:
        n = input("Please enter a non-negative integer: ")
    except KeyboardInterrupt:
        print("----ABORTED!----") # If the program is stopped with ctrl+c
        return
    except TypeError:
        print(error_message) # In case the user inputs something different from numbers
        return
    except ValueError: # In case user inputs a different value than integer
        print(error_message)
        return
    except:
        logging.exception("ERROR: ") # Shows any kind of message with the full stack trace in case we don't know what exception ocurred

    if int(n) < 0:  # n cannot be less than zero
        print(error_message)
        return

    print_chosen_prime(n)


def print_chosen_prime(n):
    """
    print the nth prime number, where n is a non-negative integer
    indexing starts at zero, so if n == 0 print the first prime number
    """

# if n == 0 print the first prime number
    # n == 1 print the second prime number and so on...
    count = 0  # number of prime numbers seen so far
    number = 2  # prime numbers start from 2

    while True:
        if is_prime(number):  # found a prime number
            count += 1
            if count == int(n) + 1:  # found the prime number the user asked for
                print(number)
                return

        number += 1


def is_prime(n):
    """returns True if n is prime, False otherwise"""

    for i in range(2, n):
        if n % i == 0:  # not a prime number
            return False

    # if we reached so far, the number should be a prime number
    return True

if __name__ == "__main__":
    main()
