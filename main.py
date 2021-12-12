#importing
import json
import difflib
from difflib import get_close_matches

#importing data fron thesaurus
data = json.load(open("data.json"))

    #logic
def translate (w):
    #lowercasing words
    w = w.lower()
    #checking for valid words
    if w in data:
        return data[w]
    #recommending words
    elif len(get_close_matches(w, data.keys())) > 0:
        yn =  input("Did you mean %s instead? Enter Y if yes or N if no: " % get_close_matches(w, data.keys())[0])
        #prompting yes or no
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        else:
            return "Well... your entry is wrong so please check it again"
    else:
        print("The word does not exist please double check.")
#input
word = input("enter word: ")

#output
output  = (translate(word))

    #making the dicts and errors more readable
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output) 
