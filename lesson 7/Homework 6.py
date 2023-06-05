# any from homework 1 or 5
# re-do with use of "def"
# answer="return"
# homework 5.1 - palindrome

def is_palindrome(string):
    # reversed string
    if (string==string[::-1]):
        # confirm that it is a palindrome
        return input(), 'is a palindrome'
    else:
        # not a palindrome
        return input(), 'is not a palindrome'

# Enter input string
string=input("Enter word:\n>")
# did not specify numeric or not
# works both for words and numbers
print(is_palindrome(string))











