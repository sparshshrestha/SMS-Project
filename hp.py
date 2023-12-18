import urllib.request
import json
import random


def hp():
    # Uses Harry Potter API to construct a message
    url = 'http://hp-api.herokuapp.com/api/characters'
    response = urllib.request.urlopen(url)  # Opening URL in Python
    result = json.loads(response.read())

    # Ensure that the result is a list of characters
    if not isinstance(result, list) or len(result) == 0:
        return "Unable to fetch Harry Potter characters."

    # Chooses a random character from the list of Harry Potter characters
    char_index = random.randint(0, len(result) - 1)
    chosen_char = result[char_index]

    # Check if the chosen character is a wizard
    is_wizard = chosen_char.get("wizard", False)

    # Construct the message based on whether the character is a wizard or not
    if is_wizard:
        return f"Which Harry Potter Character are you:\nYou are {chosen_char['name']}. You are a wizard."
    else:
        return f"Which Harry Potter Character are you:\nYou are {chosen_char['name']}. You are not a wizard."
