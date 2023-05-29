# program is asking for a word to be entered
print('Please input your word')
# user answers
x = input()
w = ''
punctuation = ',./<>()-+=:;" '
# reverse x:
# x = x[::-1]

for i in x:
    # lower case
    x = x.lower()
    # discard punctuation if any
    for punctuation_symbol in punctuation:
        x = x.replace(punctuation_symbol, '')
if x == x[::-1]:
    # is a palindrome
    print(x, 'is a palindrome')
else:
    # is not
    print(x, 'is not a palindrome')
