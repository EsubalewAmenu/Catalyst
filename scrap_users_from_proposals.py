from bs4 import BeautifulSoup
import requests
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from login import close_cookie_modal

def category_infinity_scroll(category_url):
    print(category_url)

    options = Options()
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)
    driver.get(category_url)
    time.sleep(20)  # Adjust the initial wait time as needed


    close_cookie_modal(driver)

    # Scroll to the bottom of the page to load more content
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(25)  # Adjust the scroll wait time as needed

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break  # Break the loop if no more content is loaded
        last_height = new_height

    # Now the page should have loaded all content
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()  # Close the browser

    return soup

def scrap_submitters(soup):
    href_list = []

    # Find all author-details divs in the HTML
    author_details_list = soup.find_all('div', class_='author-details')

    # Loop through each author-details div
    for author_details in author_details_list:
        # Get href value from all <a> tags within the author-details div
        for a_tag in author_details.find_all('a', class_=['member-item', 'avatar-link']):
            href_list.append(a_tag.get('href'))
    
    
    # Return the list of href values
    return href_list

def update_users_file(profile_url_list, title):
    file_path = "users_list.txt"
    try:
        # Create the file if it doesn't exist
        if not os.path.exists(file_path):
            open(file_path, 'w').close()

        # Read existing links from the text file
        with open(file_path, 'r') as file:
            existing_links = [line.strip() for line in file]

        # Open the file in append mode and add new links
        with open(file_path, 'a') as file:
            file.write(f"Category title: {title}\n")

            for href in profile_url_list:
                if href not in existing_links:
                    # Append the new link to the file
                    file.write(href + '\n')
                    existing_links.append(href)

        print("File updated successfully.")
    except Exception as e:
        print(f"Error updating file: {str(e)}")


categories = [
    # Fund11
    # "https://cardano.ideascale.com/c/campaigns/407/stage/stage-moderatione8a811/ideas/unspecified",
    # "https://cardano.ideascale.com/c/campaigns/404/stage/stage-moderationb4ff7a/ideas/unspecified", 
    # "https://cardano.ideascale.com/c/campaigns/405/stage/stage-moderationf8cce8/ideas/unspecified",
    # "https://cardano.ideascale.com/c/campaigns/406/stage/stage-moderationd45a46/ideas/unspecified",
    # "https://cardano.ideascale.com/c/campaigns/408/stage/stage-moderationd3ce6f/ideas/unspecified",
    # "https://cardano.ideascale.com/c/campaigns/409/stage/stage-moderation6f2647/ideas/unspecified",
    # "https://cardano.ideascale.com/c/campaigns/410/stage/stage-moderation6d38b3/ideas/unspecified",

    # Fund10
    "https://cardano.ideascale.com/c/campaigns/346/stage/stage-governance2c657a/ideas/unspecified",
    "https://cardano.ideascale.com/c/campaigns/347/stage/stage-governance5f5374/ideas/unspecified",
    "https://cardano.ideascale.com/c/campaigns/348/stage/stage-governancee61d9e/ideas/unspecified",
    "https://cardano.ideascale.com/c/campaigns/349/stage/stage-governance644f71/ideas/unspecified",
    "https://cardano.ideascale.com/c/campaigns/350/stage/stage-governance624c1d/ideas/unspecified",
    "https://cardano.ideascale.com/c/campaigns/351/stage/stage-governanceac575b/ideas/unspecified",
    "https://cardano.ideascale.com/c/campaigns/352/stage/stage-governancee7c869/ideas/unspecified",
    "https://cardano.ideascale.com/c/campaigns/353/stage/stage-governancec3ddde/ideas/unspecified",
    "https://cardano.ideascale.com/c/campaigns/354/stage/stage-governance8ea19c/ideas/unspecified",
    "https://cardano.ideascale.com/c/campaigns/355/stage/stage-governancea12b48/ideas/unspecified"

]


for category in categories:

    soup = category_infinity_scroll(category)
    profile_url_list = scrap_submitters(soup)

    title = soup.find('h1').get_text(strip=True)

    update_users_file(profile_url_list, title)