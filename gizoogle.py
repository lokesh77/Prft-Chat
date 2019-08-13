import json
import backend
from difflib import get_close_matches
data = json.load(open("data.json"))


def text(input_text):
    input_text = input_text.lower()
    if input_text in data:
        return data[input_text]
    elif len(get_close_matches(input_text, data.keys())) > 0:
        return data[get_close_matches(input_text, data.keys())[0]]
    else:
        return "I'm not Ok Google or Siri stop spamming!!!,I'm Perficient Buddy 😉 /buddy"


def pto(input_name):
    input_name = input_name.lower()
    for row in backend.search(name=input_name):
        return row
