# need to delete the content in '()'
x = 'Today it was a (very) beautiful day))'
punctuation = '()'
# to remove text inside parenthesis
for punctuation_symbol in punctuation:
    # removing each character and the word
    x = x.replace('(', '').replace(')', '').replace('very', '')
    print(x)






















