from common import choose_file_in_dialog, activate_window_by_title_prefix
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from login import checkIfLoggedIn
from selenium.webdriver.common.by import By
from messages import subject_selector, body_selector, we_are_voting, signature
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from vote import get_proposal_vote
import pyautogui


def is_string_in_file(search_string):
    file_path = 'sent_to.txt'


    # Create the file if it doesn't exist
    if not os.path.exists(file_path):
        open(file_path, 'w').close()

    with open(file_path, 'r') as file:
        return search_string in file.read()

def add_image(link, driver):
    try:
        # Find and click the "Add Image" button
        add_image_button = driver.find_element(By.CSS_SELECTOR, 'button.ql-image')
        add_image_button.click()
        print("add img btn beclicked")

        time.sleep(2)
        
        css_selector = 'ul.nav-tabs li.nav-item button.btn.btn-link'
        add_links_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
        )

        add_links_button.click()
        print("image link tab changed")



        css_selector = 'div.modal-content div.tab-pane.active input.form-control'
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
        )

        input_field.clear()
        input_field.send_keys(link)
        print("img link pasted")

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

def fill_message_form(idea_link, driver):
    try:
        # Fill subject with "test"
        subject_input = driver.find_element(By.ID, 'message-modal-subject')
        subject_input.clear()
        subject_input.send_keys(subject_selector())

        # Find the div with contentEditable attribute
        body_input = driver.find_element(By.CSS_SELECTOR, '#message-modal-body [contentEditable="true"]')

        # Clear existing content (if any) and fill with "test 2"
        body_input.clear()

        body_input.send_keys(we_are_voting())

        # body_input.click()
        # body_input.send_keys(Keys.END)  # Ensures the cursor is at the end
        # is_vote_added = add_their_proposal_image(idea_link, driver)

        body_input.click()
        body_input.send_keys(Keys.END)  # Ensures the cursor is at the end
        print("User proposal image added")
        time.sleep(2)

        body_input.send_keys(body_selector())
        print("Body message added")
        time.sleep(5)

        is_image_uploaded1 = add_image("https://pbs.twimg.com/media/GRNopQNWAAER12p?format=jpg&name=4096x4096",driver)

        body_input.click()
        body_input.send_keys(Keys.END)  # Ensures the cursor is at the end
        print("Esubalew's proposals image added")
        time.sleep(5)

        is_image_uploaded2 = add_image("https://pbs.twimg.com/media/GRNorQPXQAErKPH?format=jpg&name=4096x4096",driver)
        # is_image_uploaded = add_their_proposal_image(idea_link, driver)
        
        body_input.click()
        body_input.send_keys(Keys.END)  # Ensures the cursor is at the end
        print("Tadesse's proposals image added")
        time.sleep(5)

        body_input.send_keys(signature())
        print("Signature message added")
        time.sleep(5)
        

        # if is_vote_added and is_image_uploaded1 and is_image_uploaded2:
        if is_image_uploaded1 and is_image_uploaded2:
            print("Filled message form successfully.")
            return True
        else:
            print(" message form not Filled successfully.")
            return False
    except Exception as e:
        print(f"Error filling message form: {e}")

        pyautogui.moveTo(893, 795)
        time.sleep(1)
        pyautogui.click()
        print("Cancel browse file dialog box btn clicked")
        time.sleep(1)

        return False

def click_send_pm_button(driver):
    try:
        # Find the Send PM button and click it
        send_pm_button = driver.find_element(By.CSS_SELECTOR, '.mt-2 button.btn-link')
        send_pm_button.click()

        print("Send PM button found and clicked.")

    except Exception as e:
        print(f"Error clicking Send PM button: {e}")

def add_their_proposal_image(idea_link, driver):
    try:
        # Find and click the "Add Image" button
        add_image_button = driver.find_element(By.CSS_SELECTOR, 'button.ql-image')
        add_image_button.click()
        print("add img btn clicked")

        time.sleep(5)
        
        css_selector = '.file-upload-label.form-control.h-auto'
        browse_file_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
        )

        browse_file_button.click()
        print("browse file btn clicked")
        time.sleep(2)


        path = os.path.join("/Users/macbookpro/Desktop/catalyst", f'{idea_link}.png')
        choose_file_in_dialog(path)

        time.sleep(5)

        css_selector = 'div.modal-content div.modal-footer button.btn.btn-primary'
        add_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
        )

        add_button.click()
        print("Image added successfully.")
        time.sleep(2)


        return True
    except Exception as e:
        print(f"Error adding image: {e}")


        return False

def send_message_to_user(user_profile, idea_link, driver):
    url = "https://cardano.ideascale.com" + user_profile
    print(f"Loading page: {url}")
    driver.get(url)

    # Simulate loading time (20 seconds)
    time.sleep(20)

    checkIfLoggedIn(driver)

    click_send_pm_button(driver)
    time.sleep(1)

    is_filled = fill_message_form(idea_link, driver)

    time.sleep(3)


    if is_filled :
        print("message is prepared successfuly")
        time.sleep(2)

        css_selector = 'div.modal-content form#message-modal button.btn-primary'
        send_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
        )

        send_button.click()

        print("message sent successfuly")
        time.sleep(2)

        with open('sent_to.txt', 'a') as file:
            file.write(f"\n{user_profile}")
    
        time.sleep(2)

def loop_all_users():
    # get_proposal_vote("idea_title", "idea_link")
    # time.sleep(2000)

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
                author_links = []
                if line.startswith('Idea'):
                    
                    idea_title = line[6:line.index(' | Idea link:')]
                    idea_link = line[(line.index(' | Idea link:') + len(' | Idea link:')+1):line.index(' | Author link:')]
                    author_link = line[(line.index(' | Author link:')+16):]

                    result = is_string_in_file(author_link.strip())

                    if result:
                        print(f'Already sent to {author_link.strip()} {idea_title}')
                    else:

                        path = os.path.join("/Users/macbookpro/Desktop/catalyst", f'{idea_link[8:]}.png')

                        # if not os.path.exists(path):
                        #     get_proposal_vote(idea_title, idea_link)
                        #     time.sleep(2)
                        
                        # # Check if the file exists
                        # if os.path.exists(path):
                            # print(f"Screenshot exists.")
                        activate_window_by_title_prefix("Profile")
                        send_message_to_user(author_link, idea_link[8:], driver)

                        # else:
                        #     print(f"Screenshot does not exist.")


    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {str(e)}")


    # # Close the browser window when done
    # driver.quit()

loop_all_users()
