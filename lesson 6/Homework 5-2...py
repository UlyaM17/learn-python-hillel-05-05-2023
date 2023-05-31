# need to delete the content in '()'
x = 'Today it was a (very) beautiful day)).'
punctuation = '()'
what_we_seek = '('
i = x.find(what_we_seek)
new_x = ''
# to remove text inside parenthesis
while i != -1:
    print(i)
    i = x.find(what_we_seek, i + 1)
    if what_we_seek == '(' and i != -1:
        what_we_seek = ')'
    elif what_we_seek == ')' and i != -1:
        what_we_seek = '('
new_x = x[:15] + x[22:35]
print(new_x)

