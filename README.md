## This is my first ever serious project ever created, I made it purely for entertainment and did not take into account code organization or effectiveness at that time; therefore, please expect the project's code to be a bit messy.

## How to Play

### On macOS
- Double-click `Play_Pokemon_on_Mac.command`

### On Windows
- Double-click `Play_Pokemon_on_Windows.bat`

## Notes
- Both launchers automatically run the game from the `GameFiles/` folder.
- Make sure Python 3 is installed.
- If dependencies are missing, run:
  ```bash
  pip install -r requirements.txt
  ```

## About the Launchers
The `.bat` (Windows) and `.command` (Mac) launchers are simple text scripts.  
- They **only run the main Python file** (`GameFiles/scripts/main.py`).  
- You can open them in Notepad/TextEdit to verify before running.

## Troubleshooting


**UPDATE:** If none of the below work, simply run `main.py` on a valid platform/IDE.

If double-clicking the launcher does not work:

### On macOS:
  #### Option 1: Open a Terminal window, navigate into the project folder, and run:
  ```python3 GameFiles/scripts/main.py```
  #### Option 2: Run the following command below on the terminal. First, open the terminal by right-clicking Pokemon-Final-Protocol and selecting New Terminal at Folder, this is to ensure the terminal has the project path set. Then try `Play_Pokemon_on_Mac.command` again.
  ```bash
  chmod +x Play_Pokemon_On_Mac.command
  ```
### On Windows:
  #### Option 1: Open cmd, navigate into the project folder, and run:
  ```bash python GameFiles\scripts\main.py```
  #### Option 2: If you get a SmartScreen warning, click "More info" → "Run anyway". If you see "Access Denied", Right-click `Play_Pokemon_on_Windows.bat` and choose "Run as Administrator".
  
