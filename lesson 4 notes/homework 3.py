greeting = input('Hi, how are you?')
print(greeting)

response = str(input())
if response == ('I am good'):
    print("Great to hear that! What do you do?")
else:
    if response == ('I am not good'):
        print("Sorry to hear that. What do you do?")
    else:
        print('Sorry, I do not understand your answer')
activity = str(input())

if activity == ('I am learning Python'):
    print('It must be hard. Here is a helpful link: https://peps.python.org/pep-0008/#indentation')
else:
    if activity == ('I am watching videos on YouTube'):
        print('It must be interesting! Here is a link to some interesting facts about Youtube: https://fortunelords.com/youtube-statistics/ ')
    else:
        print('Please rephrase your response, I do not understand')

conclusion = str(input())

if conclusion == ('Thank you'):
    print('You are welcome. Good luck')
else:
    print('Sorry that I could not help you.Please try again')



