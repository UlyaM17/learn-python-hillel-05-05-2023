PRIME_SET = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
             31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
# set of prime numbers in caps: CONSTANT
# it does not change or is a default
# must be in the beginning of the file


def is_prime(user_prompt):
    """
    function is checking if entry was numeric
    also if it is listed in given constant set
    :param user_prompt: user entry
    :return: yes, no
    """
    while True:
        # if entry is numeric
        user_input = input(f'{user_prompt}\n>> ')
        try:
            # checking if entered number is in given set
            user_input = int(user_input)
            if user_input in PRIME_SET:
                return True
            else:
                return False
        except Exception:
            # if value entered is not in a set
            print(f'\nPlease try again, entry is not numeric')


if __name__ == '__main__':
    while True:
        if is_prime(user_prompt="\nEnter a numeric value from 1 till 100"):
            print('\n\tYour number is prime')
        else:
            print('\n\tYour number is not prime')
