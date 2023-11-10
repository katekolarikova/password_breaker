import string
import time
from typing import Dict
from itertools import product

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

# list(product([1,2,3,4], repeat=3))
#

letters = list(string.ascii_letters)  # includes both uppercase and lowercase letters
numbers = list(string.digits)
special_characters = list(string.punctuation)

pasword_strength: Dict[str, list] = {'numbers': numbers, 'numbers_letters': numbers + letters,
                                     'numbers_letters_special_characters': numbers + letters + special_characters}

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
url = 'http://127.0.0.1:5000/'
driver.get(url)

level = list(product(pasword_strength.get('numbers'), repeat=4))
inputArea = driver.find_element(By.ID, "user_input")
checkButton = driver.find_element(By.ID, "check_button")
start_time = time.time()
for item in level:
    tmp_pass = ''.join(item)
    driver.find_element(By.ID, "user_input").send_keys(tmp_pass)
    driver.find_element(By.ID, "check_button").click()

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
