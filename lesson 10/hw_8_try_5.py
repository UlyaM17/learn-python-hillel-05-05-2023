my_list = []


def key_word_add(keyword_add: str) -> list:
    """
    :rtype: list
    """
    while True:
        keyword_input = input('>>\n>>')
        if 'add' in keyword_input:
            return [my_list.append(keyword_add)]


def key_word_earliest(keyword_input: list) -> list:
    """
    :rtype: list
    """
    if 'earliest' in keyword_input:
        return [my_list]


def key_word_latest(keyword_input: list) -> list:
    """
    :rtype: list
    """
    if 'latest' in keyword_input:
        return [my_list[::-1]]


def key_word_shortest(keyword_input: list) -> list:
    """
    :rtype: list
    """
    if 'shortest' in keyword_input:
        return [sorted(my_list, key=len)]


def key_word_longest(keyword_input: list) -> list:
    """
    :rtype: list
    """
    if 'longest' in keyword_input:
        return [sorted(my_list, key=len, reverse=True)]


if __name__ == '__main__':
    while True:
        notes_completed = key_word_add(keyword_add='Please add note or input command: add, earliest, latest, shortest '
                                                   'or'
                                                   'longest \n>>')
        print(notes_completed)
        earliest_entry = key_word_earliest(notes_completed)
        print(earliest_entry)
        latest_entry = key_word_latest(notes_completed)
        print(latest_entry)
        shortest_entry = key_word_shortest(notes_completed)
        print(shortest_entry)
        longest_entry = key_word_longest(notes_completed)
        print(longest_entry)

