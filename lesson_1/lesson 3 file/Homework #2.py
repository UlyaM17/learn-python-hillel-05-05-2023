text = input("Hello, my favorite color is blue. What about you?")
print(text)

# lower case phrase
print(str.lower(text))

# omitting punctuation symbols
punctuation = ('?', '.', ',', '!', ':', ';', '-')
for objects in text:
    text = text.replace('?', ' ')
    text = text.replace('.', ' ')
    text = text.replace(',', ' ')
print(text)

# omitting spaces
text = text.replace(" ", "")
print(text)

# replacing a word
sentence = input(text)
word = input("favorite")
replacement = input("most-liked")
text2 = text.replace('favorite', 'most-liked')
print(text2)

# find the word meant to be replaced
index = text.find("favorite")
if text.find("favorite"):
    print("success")

# indicate the specific string
word = 'favorite'
result = word.find('favorite')
print("Word 'favorite ' found at index:", result)






















