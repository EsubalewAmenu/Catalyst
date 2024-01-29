from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from login import checkIfLoggedIn
from selenium.webdriver.common.by import By
from messages import subject_selector, body_selector  
import os



def is_string_in_file(search_string):
    file_path = 'sent_to.txt'


    # Create the file if it doesn't exist
    if not os.path.exists(file_path):
        open(file_path, 'w').close()

    with open(file_path, 'r') as file:
        return search_string in file.read()



def upload_image(driver, image_path):
    # Locate the input element for file upload
    upload_input = driver.find_element(By.CSS_SELECTOR, '.ql-image input[type="file"]')

    # Send the path of the image file to the input element
    upload_input.send_keys(image_path)

    # Wait for the upload to complete (adjust the timeout as needed)
    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '.upload-progress')))

    print(f"Image uploaded successfully: {image_path}")


def fill_message_form(driver):
    
    # Fill subject with "test"
    subject_input = driver.find_element(By.ID, 'message-modal-subject')
    subject_input.clear()
    subject_input.send_keys(subject_selector())

    # Find the div with contentEditable attribute
    body_input = driver.find_element(By.CSS_SELECTOR, '#message-modal-body [contentEditable="true"]')
    
    # Clear existing content (if any) and fill with "test 2"
    body_input.clear()
    body_input.send_keys(body_selector())

    upload_image(driver, '/Users/macbookpro/Downloads/proposals.jpg')

    print("Filled message form successfully.")


def click_send_pm_button(driver):
    # Find the Send PM button and click it
    send_pm_button = driver.find_element(By.CSS_SELECTOR, '.mt-2 button.btn-link')
    send_pm_button.click()

    print("Send PM button found and clicked.")

def send_message_to_user(user_profile, driver):
    url = "https://cardano.ideascale.com" + user_profile
    print(f"Loading page: {url}")
    driver.get(url)

    # Simulate loading time (20 seconds)
    time.sleep(20)

    checkIfLoggedIn(driver)

    click_send_pm_button(driver)
    time.sleep(5)
    fill_message_form(driver)
    time.sleep(20)

    with open('sent_to.txt', 'a') as file:
        file.write(f"\n{user_profile}")
    

    # soup = BeautifulSoup(driver.page_source, "html.parser")


def loop_all_users():


    options = Options()
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)


    file_path = "users_list.txt"


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



    # Close the browser window when done
    driver.quit()

loop_all_users()
