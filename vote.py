import pyautogui
import time

def move_to_locations():

    currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
    print("current mouse location is ", currentMouseX, currentMouseY)

    # mac m2 pro
    return {"proposals_tab_w": 1532, "proposals_tab_h": 904, 
    "search_box_w": 1610, "search_box_h": 345, 
    "search_btn_w": 1741, "search_btn_h": 345, 
    "searched_proposal_w": 1570, "searched_proposal_h": 481,
    "yes_vote_btn_w": 1526, "yes_vote_btn_h": 850,
    "my_selections_w": 1600, "my_selections_h": 911}

def change_window():
    # change_to_emulator and back_to_browser
    # pyautogui.hotkey('ctrl', 'tab')
    pyautogui.hotkey('command', 'tab')
    print("tab changed")
    time.sleep(2)



def search_proposal(locations, title):
    print("search started")
    pyautogui.moveTo(locations["proposals_tab_w"], locations["proposals_tab_h"])
    time.sleep(1)
    pyautogui.click()
    time.sleep(5)

    pyautogui.moveTo(locations["search_box_w"], locations["search_box_h"])
    time.sleep(1)
    pyautogui.click()
    time.sleep(2)
    pyautogui.write(title)
    time.sleep(2)

    pyautogui.moveTo(locations["search_btn_w"], locations["search_btn_h"])
    time.sleep(1)
    pyautogui.click()
    time.sleep(5)

    pyautogui.moveTo(locations["searched_proposal_w"], locations["searched_proposal_h"])
    time.sleep(1)
    pyautogui.click()
    time.sleep(2)

def vote_for_proposal():
    print("vote started")
    # vote for proposal
    # sleep

def take_screenshoot():
    print("screenshoot taking started")
    # click takescreenshot btn
    # sleep

def get_proposal_vote(title):
    print()
    locations = move_to_locations()

    change_window()    
    change_window()    
    search_proposal(locations, title)
    # vote_for_proposal()
    # take_screenshoot()
    change_window()