from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

########################################################################################################
def close_cookie_modal(driver):
    try:
        # Find the close button and click it
        close_button = driver.find_element(By.CSS_SELECTOR, '.modal-header .btn-close')
        close_button.click()
    except Exception as e:
        print()

########################################################################################################
def accept_cookie_modal(driver):
    try:


        # Wait for the cookie-consent-collapse class div to be visible
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.cookie-consent-collapse')))

        # Find all elements with class '.btn-primary' within the 'cookie-consent-collapse' class div
        elements = driver.find_elements(By.CSS_SELECTOR, '.cookie-consent-collapse .btn-primary')


        # Click the last button if it exists
        if elements:
            last_button = elements[-1]
            last_button.click()
            print("Cookie accept button found and clicked.")


        time.sleep(20)
    except Exception as e:
        print(f"Error closing cookie modal: {e}")



########################################################################################################

def checkIfLoggedIn(driver):
    close_cookie_modal(driver)

    # accept_cookie_modal(driver)
    
    try:
        # Find the login button without waiting
        login_button = driver.find_element(By.CLASS_NAME, 'community-login-link')

        # Click the login button
        login_button.click()

        print("Login button found and clicked.")

        time.sleep(4)
        close_cookie_modal(driver)
    
        # Find the email and password fields and input the values
        email_field = driver.find_element(By.ID, 'login-email')
        password_field = driver.find_element(By.ID, 'login-password')

        email_field.send_keys('esubalew.a2009@gmail.com')
        password_field.send_keys('testtest')

        # Find and click the login button
        login_button = driver.find_element(By.XPATH, '//button[text()="Log in"]')
        login_button.click()        
        time.sleep(10)

    except NoSuchElementException:
        print("Login button not found on the page.")
