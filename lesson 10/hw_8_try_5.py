def word(keyword_input: str) -> list:
    """
    :rtype: list
    """
    # my_list = []
    while True:
        user_input = input(f'{keyword_input}\n>>')
        try:
            user_list = [user_input]
            return user_list
        except Exception:
            print('Try again')


def key_word_add(user_list: list) -> list:
    """
    :param user_list
    :return: list
    """
    if 'add' in user_list:
        return [user_list.append(user_list)]


def key_word_earliest(user_list: list) -> list:
    """
    :param user_list
    :return: list
    """
    if 'earliest' in user_list:
        return [user_list.append(user_list)]


def key_word_latest(user_list: list) -> list:
    """
    :param user_list
    :return: list
    """
    if 'latest' in user_list:
        return user_list.append(user_list)[::-1]


def key_word_shortest(user_list: list) -> list:
    """
    :param user_list
    :return: list
    """
    if 'shortest' in user_list:
        return sorted(user_list, key=len)


def key_word_longest(user_list: list) -> list:
    """
    :param user_list
    :return: list
    """
    if 'longest' in user_list:
        return sorted(user_list, key=len, reverse=True)


if __name__ == '__main__':
    while True:
        user_command = word(keyword_input='Please input a command: add, earliest, latest, shortest '
                                          'or '
                                          'longest \n>>')
        print(user_command)
        if user_command:
            add_entry = key_word_add(user_command)
            print(add_entry)
        if user_command:
            earliest_entry = key_word_earliest(user_command)
            print(earliest_entry)
        if user_command:
            latest_entry = key_word_latest(user_command)
            print(latest_entry)
        if user_command:
            shortest_entry = key_word_shortest(user_command)
            print(shortest_entry)
        if user_command:
            longest_entry = key_word_longest(user_command)
            print(longest_entry)
