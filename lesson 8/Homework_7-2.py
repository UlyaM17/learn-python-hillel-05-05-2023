prime_set = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}


def is_prime(user_prompt):
    number = input(f'{user_prompt}\n>>')
    try:
        # checking if entered number is in given set
        if number in prime_set:
            return True
    except Exception:
        # if value entered is not in a set
        print(f'\nPlease try again')
        return False


if __name__ == '__main__':
    print(type(is_prime), is_prime)
    while True:
        # number was found in given set
        n = is_prime('Please enter a numeric value from 1 till 100:\n')
        prime_set = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
        if is_prime(user_prompt=n) is True:
            # conclusion
            print(f'Your number is prime')

