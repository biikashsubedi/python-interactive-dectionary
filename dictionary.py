import json
from difflib import get_close_matches

data = json.load(open('files/dictionary.json'))


def dictionary(word):
    # w = SequenceMatcher(word.lower())
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yes_no = input(
            "Did you mean %s instead? Enter Y for Yes and N for No: " % get_close_matches(word, data.keys())[0])
        if yes_no == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yes_no == 'N':
            return f'{word} does not exist☹️, Please try another'
        else:
            return 'Wrong Input, Please choose Y or N'
    else:
        return f'{word} does not found ☹️, Please try another'


word = input('Enter word to get definition: ')
result = dictionary(word)

if type(result) == list:
    for item in result:
        print(item)
else:
    print(result)
