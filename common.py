import subprocess
import time
import os




def choose_file_in_dialog(file_path):
    # Split the file path into directory and file name
    directory, file_name = os.path.split(file_path)

    script = f"""
    tell application "System Events"
        -- Make sure the file chooser dialog is in the foreground
        set frontmost of (first process whose frontmost is true) to true

        -- Navigate to the specified directory
        keystroke "g" using {{command down, shift down}}
        delay 0.5
        keystroke "{directory}"
        delay 0.5
        keystroke return
        delay 0.5

        -- Select the specified file
        keystroke "{file_name}"
        delay 0.5
        keystroke return
    end tell
    """
    
    try:
        subprocess.run(['osascript', '-e', script], check=True)
        print(f"Selected file: {file_path}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")




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
        return True
    except subprocess.CalledProcessError:
        print(f"Window with prefix '{prefix}' not found or could not be activated.")
        return False
