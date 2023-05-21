print()
response = ''
response2 = ''
activity = ''
conclusion = ''

greeting = input('Hello')
response = str(input())
if 'Hi' in response:
    print('How are you?')
elif 'Hello' in response:
    print('How are you?')
else:
    print('Hello?')

response2 = str(input())
if "good" in response2:
    print("Great to hear that! What are you doing right now?")
elif "well" in response2:
    print("Great to hear that! What are you doing right now?")
else:
    print('Sorry, I do not understand your answer')

activity = str(input())
if "Python" in activity:
    print('It must be hard. Here is a helpful link: https://peps.python.org/pep-0008/#indentation')
else:
    if "video" in activity:
        print('It must be interesting! Here is a link to some interesting facts about Youtube: https://fortunelords.com/youtube-statistics/ ')
    else:
        print('Please rephrase your response, I do not understand')

conclusion = str(input())
if "thank" in conclusion:
    print('You are welcome. Good luck')
else:
    print('Sorry that I could not help you.Please try again')
