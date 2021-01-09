import json
from difflib import get_close_matches

file = r"python_apps\IED\data.json"
read = "r"
input_message = "Enter word: "

data = json.load(open(file, read))

def translate(w):
    w = w.lower()
    close_match = get_close_matches(w, data.keys())
    if w in data:
        return data[w]
    elif len(close_match) > 0:
        yn = input("Did you mean %s instead?. Enter Y if yes or N if no: " % close_match[0])
        if yn.lower() == "y":
            return data[close_match[0]]
        elif yn.lower() == "y":
            return "%s does'nt exist. Please double check it" % w
        else:
            return "We do not understand you"
    else:
        return "%s does'nt exist. Please double check it" % w
    

word = input(input_message)

output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)