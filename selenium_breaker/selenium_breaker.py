import string
import time
from typing import Dict
from itertools import product
from selenium import webdriver
from selenium.webdriver.common.by import By

# selenium script which will send a POST request to the web app. This request will contain a string
# with possible password. Than it will check if the request was successful. If not, it will send another request

#generate all characters possible for password level
letters = list(string.ascii_letters)  # includes both uppercase and lowercase letters
numbers = list(string.digits)
special_characters = list(string.punctuation)
pasword_strength: Dict[str, list] = {'numbers': numbers, 'numbers_letters': numbers + letters,
                                     'numbers_letters_special_characters': numbers + letters + special_characters}

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
url = 'http://127.0.0.1:5000/'
driver.get(url)

level = list(product(pasword_strength.get('numbers'), repeat=4))  # define password complex

start_time = time.time()
for item in level:
    tmp_pass = ''.join(item)
    driver.find_element(By.ID, "user_input").send_keys(tmp_pass)
    driver.find_element(By.ID, "check_button").click()

    # check if the request was successful
    status_code_script = """
    return fetch(arguments[0], { method: 'HEAD' }).then(response => response.status);
    """
    status_code = driver.execute_script(status_code_script, driver.current_url)
    if status_code == 200:
        print(f"Password: {tmp_pass}")
        break
end_time = time.time()
elapsed_time = end_time - start_time
print("Elapsed time: ", elapsed_time)

driver.quit()
