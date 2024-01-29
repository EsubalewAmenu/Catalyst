from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from login import checkIfLoggedIn
from selenium.webdriver.common.by import By
from messages import subject_selector, body_selector  
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def is_string_in_file(search_string):
    file_path = 'sent_to.txt'


    # Create the file if it doesn't exist
    if not os.path.exists(file_path):
        open(file_path, 'w').close()

    with open(file_path, 'r') as file:
        return search_string in file.read()




def add_image(driver):
    try:
        link = 'https://pbs.twimg.com/media/GFAB-a5XYAAt2yl?format=jpg&name=large'
        
        # Find and click the "Add Image" button
        add_image_button = driver.find_element(By.CSS_SELECTOR, 'button.ql-image')
        add_image_button.click()

        time.sleep(2)
        
        css_selector = 'ul.nav-tabs li.nav-item button.btn.btn-link'
        add_links_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
        )

        add_links_button.click()



        css_selector = 'div.modal-content div.tab-pane.active input.form-control'
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
        )

        input_field.clear()
        input_field.send_keys(link)

        time.sleep(2)

        css_selector = 'div.modal-content div.modal-footer button.btn.btn-primary'
        add_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
        )

        add_button.click()
        print("Image added successfully.")

        return True
    except Exception as e:
        print(f"Error adding image: {e}")
        return False


def fill_message_form(driver):
    try:
        # Fill subject with "test"
        subject_input = driver.find_element(By.ID, 'message-modal-subject')
        subject_input.clear()
        subject_input.send_keys(subject_selector())



        # Find the div with contentEditable attribute
        body_input = driver.find_element(By.CSS_SELECTOR, '#message-modal-body [contentEditable="true"]')
        print(body_selector())
        # Clear existing content (if any) and fill with "test 2"
        body_input.clear()
        # body_input.send_keys(handle_newlines_and_emojis(body_selector()), Keys.ENTER)  # Pressing Enter to create a new line
        body_input.send_keys(body_selector())

        # Check if the emoji is present in the body input
        print("Body input content:", body_input.text)

        is_image_uploaded = add_image(driver)
        
        print("Filled message form successfully.")
        if is_image_uploaded:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error filling message form: {e}")
        return False

def click_send_pm_button(driver):
    try:
        # Find the Send PM button and click it
        send_pm_button = driver.find_element(By.CSS_SELECTOR, '.mt-2 button.btn-link')
        send_pm_button.click()

        print("Send PM button found and clicked.")

    except Exception as e:
        print(f"Error clicking Send PM button: {e}")

def send_message_to_user(user_profile, driver):
    url = "https://cardano.ideascale.com" + user_profile
    print(f"Loading page: {url}")
    driver.get(url)

    # Simulate loading time (20 seconds)
    time.sleep(20)

    checkIfLoggedIn(driver)

    click_send_pm_button(driver)
    time.sleep(1)

    is_filled = fill_message_form(driver)

    time.sleep(2)


    if is_filled :
        print("message is prepared successfuly")
        time.sleep(20)

        with open('sent_to.txt', 'a') as file:
            file.write(f"\n{user_profile}")
    

def loop_all_users():


    options = Options()
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)


    file_path = "users_list.txt"

    try:

        # Create the file if it doesn't exist
        if not os.path.exists(file_path):
            open(file_path, 'w').close()


        with open(file_path, 'r') as file:
            for line in file:
                if line.startswith('/'):
                    result = is_string_in_file(line.strip())

                    if result:
                        print(f'Already sent to {line.strip()}')
                    else:
                        send_message_to_user(line.strip(), driver)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {str(e)}")


    # Close the browser window when done
    driver.quit()

loop_all_users()
