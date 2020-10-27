# WoltPartner-Schedule
A little help to get the Wolt shifts you want


A. PREREQUISITS

For the script to work you need to:
  1. Download and install python (tested on version 3.8.5) and modules: win32gui, pyautogui.
  2. Download and install BlueStacks 4
  3. Open and log-in to the WoltPartner App in BlueStacks. The app needs to be opened in white theme.
  4. Autoalign BlueStacks
  
  
B. MANUAL

  To set the booking times in the script scroll all the way down to "BODY".
  
  The functions you will be using:
    1. startAt(hh) - as "hh" put in the time the new hours appear in the 24h format (example: startAt(15), startAt(8) )
    2. booking(day,slot) - day - number (1-7), as they are listed in the top of the screen from left to right (including new ones)
                           slot - number (1-14), shift slot in order as they are listed from top to bottom
                           (example: booking(2,4) - will book 4th shift from the top on the 2nd day from the left)
                           
  After launching the script try not to move the mouse and not click on other windows as the script uses the UI.
  
  
  
  Good luck and enjoy the ride!
