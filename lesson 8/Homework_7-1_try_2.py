def read_user_number(user_prompt) -> int:
    """
            function checks if the number is numeric and whole
            :param user_prompt: user entry
            :return: yes, not
            """
    while True:
        user_input = input(f'{user_prompt}\n>> ')
        try:
            user_input = int(user_input)
            # is a whole number
            return user_input
        except Exception:
            # if decimal/ negative number entered
            print(f'\nPlease enter a whole numeric value')


def convert_user_number(user_input) -> dict:
    """
            :param: user_input
            :return: dictionary
            """
    if type(user_input) == int:
        d = {'seconds': user_input,
             'minutes': user_input // 60,
             'hours': user_input // 3600,
             'days': user_input // 86400
             }
        return d
    else:
        print(f'\nCould not calculate')


if __name__ == '__main__':
    while True:
        seconds_entry = read_user_number(user_prompt='Enter number of seconds\n>> ')
        seconds_converted = convert_user_number(seconds_entry)
        print(seconds_converted)
