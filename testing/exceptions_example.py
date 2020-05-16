import random
# define Python user-defined exceptions


class InputTooSmallError(Exception):
    """Raised when the entered alpahbet is smaller than the actual one"""
    pass

 
class InputTooLargeError(Exception):
    """Raised when the entered alpahbet is larger than the actual one"""
    pass


class NotAlphabetCharacterError(Exception):
    """Raised when alphabet character is not member of alphabet"""


lower_upper_alphabet = 'abcdefghijklmnopqrstuvwxyz'
# you need to guess this letter
letter = random.choice(lower_upper_alphabet)
run_script = True
while run_script:
    # user guesses an alphabet until he/she gets it right
    try:
        apb = input("Enter an alphabet: ")
        if len(apb) != 1:
            raise NotAlphabetCharacterError
        if apb < letter:
            raise InputTooSmallError
        elif apb > letter:
            raise InputTooLargeError
        run_script = False
    except NotAlphabetCharacterError:
        print("The entered string is not character of alphabet")
    except InputTooSmallError:
        print("The entered character is too small")
    except InputTooLargeError:
        print("The entered character is too large")
    finally:
        if run_script:
            print("Try again!")
 
print("Congratulations! You guessed it correctly.")
