# need to delete the content in '()'
x = 'Today it was a (very) beautiful day))'
punctuation = '()'
# to remove text inside parenthesis
for punctuation_symbol in punctuation:
    x = x.strip('()')
    x = x.replace('(', '').replace(')', '').replace('very', '')
    print(x)






















