import pyscreenshot as ImageGrab
import subprocess
import pyautogui
import time
import os


def move_to_locations():

    x, y = pyautogui.position()
    print("current mouse location is ", x, y)
    r,g,b = pyautogui.pixel(x, y)
    print("current location color ", r,g,b)

    if r == 24 and g == 24 and b == 24:
        print("blue btn is available")
    else:
        print("color is not blue")

    # mac m2 pro
    return {"proposals_tab_w": 1468, "proposals_tab_h": 1068, 
    "search_box_w": 1636, "search_box_h": 385, 
    "search_btn_w": 1701, "search_btn_h": 371, 
    "searched_proposal_w": 1414, "searched_proposal_h": 555,
    "yes_vote_btn_w": 1394, "yes_vote_btn_h": 987,
    "my_selections_w": 1600, "my_selections_h": 911,
    "remove_proposal_l_w": 1720, "remove_proposal_l_h": 603,
    "remove_proposal_s_w": 1729, "remove_proposal_s_h": 575,
    "screenshot_top_w": 1342, "screenshot_top_h": 211,
    "screenshot_bottom_w": 1773, "screenshot_bottom_h": 624}

def search_proposal(locations, title):
    print("searching started")

    pyautogui.moveTo(locations["proposals_tab_w"], locations["proposals_tab_h"])
    time.sleep(1)
    pyautogui.click()
    time.sleep(5)

    pyautogui.moveTo(locations["search_btn_w"], locations["search_btn_h"])
    time.sleep(1)
    
    x, y = pyautogui.position()
    r,g,b = pyautogui.pixel(x, y)
    if r == 30 and g == 31 and b == 34:
        print("search btn is available")
        pyautogui.moveTo(locations["search_box_w"], locations["search_box_h"])
        time.sleep(1)
        pyautogui.click()
        time.sleep(2)
        pyautogui.write(title)
        time.sleep(2)

        pyautogui.moveTo(locations["search_btn_w"], locations["search_btn_h"])
        pyautogui.click()
        time.sleep(5)

        pyautogui.moveTo(locations["searched_proposal_w"], locations["searched_proposal_h"])
        pyautogui.click()
        time.sleep(5)

    else:
        print("search btn is not still available ... witing for 5 sec")
        time.sleep(5)
        search_proposal(locations, title)

def vote_for_proposal(locations):
    print("voting started")
    pyautogui.moveTo(locations["yes_vote_btn_w"], locations["yes_vote_btn_h"])
    time.sleep(1)
    
    x, y = pyautogui.position()
    r,g,b = pyautogui.pixel(x, y)
    if r == 30 and g == 31 and b == 34:
        pyautogui.click()
        print("vote btn clicked")
        time.sleep(3)
        pyautogui.click()
        time.sleep(3)
    else:
        print("voting page not loaded yet")
        time.sleep(5)
        vote_for_proposal(locations)

def take_screenshoot(locations, idea_id):
    print("screenshoot taking started")

    path = os.path.join("/Users/macbookpro/Desktop/catalyst", f'{idea_id}.png')

    area = (locations["screenshot_top_w"], locations["screenshot_top_h"], locations["screenshot_bottom_w"], locations["screenshot_bottom_h"])
    im = ImageGrab.grab(bbox=area)
    im.save(path)
    time.sleep(3)

def remove_proposal_from_selection(locations):
    pyautogui.moveTo(locations["remove_proposal_l_w"], locations["remove_proposal_l_h"])
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(locations["remove_proposal_s_w"], locations["remove_proposal_s_h"])
    pyautogui.click()
    time.sleep(2)

def activate_window_by_title_prefix(prefix):
    # Get a list of all running applications and their windows
    script = f"""
    tell application "System Events"
        set allProcesses to application processes
        repeat with eachProcess in allProcesses
            set allWindows to windows of eachProcess
            repeat with eachWindow in allWindows
                set windowName to name of eachWindow as text
                if windowName starts with "{prefix}" then
                    tell process (name of eachProcess)
                        perform action "AXRaise" of eachWindow
                        set frontmost to true
                    end tell
                    return true
                end if
            end repeat
        end repeat
    end tell
    """

    try:
        subprocess.run(['osascript', '-e', script], check=True)
        print(f"Activated window with prefix: {prefix}")
    except subprocess.CalledProcessError:
        print(f"Window with prefix '{prefix}' not found or could not be activated.")

def get_proposal_vote(title, idea_link):
    locations = move_to_locations()
    
    activate_window_by_title_prefix("Running Devices")

    search_proposal(locations, title)
    vote_for_proposal(locations)
    take_screenshoot(locations, idea_link[8:])
    remove_proposal_from_selection(locations)
