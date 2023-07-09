# 2. String word generator

def string_word_split(my_string):
    # splitting string by words
    split_string = my_string.split()
    # defining the range by length of string
    length = len(split_string)
    for i in range(length):
        # split by word
        yield split_string[i]
        # indicator of generated word # if needed
        # print(f'(string word # {i + 1})\n')


if __name__ == '__main__':
    generator_by_word = string_word_split(my_string='Monday is always the hardest day of the week because you got to '
                                                    'return to work after a nice weekend')
    for word in generator_by_word:
        # generating a given string word by word
        print(word)
