import requests

# def send_string_to_server(string_to_send):
#     # Replace 'user_input' and 'check_button' with the appropriate IDs in your HTML
#     user_input = 'user_input'
#     check_button = 'check_button'
#
#     # Simulate setting the value and triggering the click event
#     document = {
#         'getElementById': lambda x: {'value': string_to_send} if x == user_input else None
#     }
#
#     click_event = {
#         'type': 'click',
#         'view': 'window',
#         'bubbles': True,
#         'cancelable': True
#     }
#
#     document[check_button] = click_event
#
#     check_button_dispatch_event(document, check_button)
#
# def check_button_dispatch_event(document, check_button):
#     click_event = document[check_button]
#
#     if click_event:
#         # Dispatch the click event
#         handle_click_event(click_event)
#
# def handle_click_event(click_event):
#     # Handle the click event as needed
#     pass
#
# # Replace 'YourDesiredString' with the desired string to send
# send_string_to_server('1234')


import requests

# The data you want to send
user_input = '004'

# URL of your Flask server
url = 'http://127.0.0.1:5000/'

# Data to send in the POST request
data = {'user_input': user_input}

letters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')  # includes both uppercase and lowercase letters
numbers = list('0123456789')
special_characters = list('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')

def cartesian_product(arrays):
    return [x + y for x in arrays[0] for y in cartesian_product(arrays[1:])] if arrays else ['']

password_strength = {
    'numbers': numbers,
    'numbers_letters': numbers + letters,
    'numbers_letters_special_characters': numbers + letters + special_characters
}

# Generate combinations for the 'numbers' key, repeat=4 times
level = cartesian_product([password_strength['numbers']] * 4)

for combination in level:
    tmp = ''.join(combination)
    data['user_input'] = tmp
    response = requests.post(url, data=data)

    if response.status_code == 200:
        print(response.status_code)
        print(tmp)
        break
    elif response.ok:
        print(response.text())  # Process the response data here
    # else:
    #     print('There was a problem with the fetch operation:', response.status_code)
