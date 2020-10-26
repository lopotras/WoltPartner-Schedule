#! python3

### LIBRARIES IMPORT ###
from time import sleep as sleep
from time import strftime as strftime

import win32gui

import pyautogui
from pyautogui import click as click
from pyautogui import typewrite as typewrite
from pyautogui import hotkey as hotkey



### FUNCTIONS DEFINITIONS ###
def wait():
    input("press ENTER to continue...")

def welcome():
    print("Welcome to the Wolt Schedling Solution")
    sleep(1)
    print("""
    It is assumed that running this program you:

        1.  Have your WoltPartnerApp opened in BlueStacks 4 and auto-aligned.

        2.  Have the WoltPartnerApp control mapping imported into Blue BlueStacks.

        3.  Are logged into the WoltPartnerApp with your number and are on the
            'Scheduled hours -> Aarhus Central' tab.
    """)
    sleep(1)

def weekDay():
    # Verify the weekday
    day = strftime("%a")
    if (day == "Thu"):
        return day
    elif (day == "Fri"):
        return day
    else:
        print("There are no new shifts coming up today.")
        return false

def enterWolt():
    hwnd = win32gui.FindWindow(None, "BlueStacks")
    win32gui.ShowWindow(hwnd,5)
    win32gui.SetForegroundWindow(hwnd)
    rect = win32gui.GetWindowRect(hwnd)
    sleep(0.2)
    return rect

def refresh():
    pyautogui.moveTo( translatedCoordinates(refreshCircle) )
    pyautogui.drag(0,200,0.2,button = 'left')

def changeDay(day):
    # moves to a day that is currently at 'day' position
    # note: 'day' must be an number between 1-7 (position from left to right)
    click( translatedCoordinates( thursdayDays[day-1] ) )
    print( timeStamp + " changed day" )

def bookShift(slot):
    # Clicks on the booking button space on the chosen slot
    # note that 'slot' must be a number between 1-14 (position from top to bottom)
    click( translatedCoordinates( shifts[slot-1] ) )

def get_pixel_colour(i_x, i_y):
    # returns the color of a pixel with coordinates i_x, i_y
    # in the format (r, g, b)
    i_desktop_window_id = win32gui.GetDesktopWindow()
    i_desktop_window_dc = win32gui.GetWindowDC(i_desktop_window_id)
    long_colour = win32gui.GetPixel(i_desktop_window_dc, i_x, i_y)
    i_colour = int(long_colour)
    return (i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)

def pCheck(pc_x1,pc_x2,pc_y):
    for i in range(pc_x1,pc_x2):
        print(get_pixel_colour(i,pc_y))

def verifyPixelColorChange(vp_x,vp_y,vp_color):
    # stops until the color changes from vp_color
    # compares pixel color to the first number of 'color'
    # vp_x and vp_y are pixel coordinates
    # vp_color values (in ""):
    # ("255", 255, 255) - white, background
    # ("81", 81, 84) - black, active hours text, 1st pixel on the left
    # ("0", 157, 224) - blue, square on currently chosen day's number
    # ("185", 186, 187) - grey, inactive hours text
    # ("250", 250, 250) - grey, refresh circle
    a = get_pixel_colour(vp_x,vp_y)
    while a[0] == vp_color:
        a = get_pixel_colour(vp_x,vp_y)

def verifyNewHours(vp_x1,vp_x2,vp_y,vp_color):
    a = 0
    while a == 0:
        refresh()
        for i in range(vp_x1,vp_x2):
            b = get_pixel_colour(i,vp_y)
            print(i, b)
            if b[0] != vp_color:
                a += 1

def verifyRefresh():
    verifyPixelColorChange(273,271,255)
    print(timeStamp + " refreshing...")
    verifyPixelColorChange(273,271,250)
    print(timeStamp + " refreshed")

def translatedCoordinates(xyIn):
    ### Translator for the coordinates in 0-1 value range ###
    # Translates the relative coordinates into pixel position on the screen
    # using the current window position and size
    hwnd = win32gui.FindWindow(None, "BlueStacks")
    rect = win32gui.GetWindowRect(hwnd)
    xOut = rect[0] + ( xyIn[0] * (rect[2]-rect[0]) )
    yOut = rect[1] + ( xyIn[1] * (rect[3]-rect[1]) )
    return [xOut, yOut]



### GLOBAL VARIABLES DEFINITIONS ###
timeStamp = strftime("%c")

# RELATIVE COORDINATES

refreshCircle = [0.4370015948963317, 0.26601941747572816]

shifts = [[0.8229665071770335, 0.27475728155339807],
            [0.810207336523126, 0.3300970873786408],
            [0.8118022328548644, 0.38058252427184464],
            [0.8118022328548644, 0.4349514563106796],
            [0.8133971291866029, 0.49029126213592233],
            [0.8149920255183413, 0.5446601941747573],
            [0.8181818181818182, 0.5980582524271845],
            [0.8086124401913876, 0.6524271844660194],
            [0.8133971291866029, 0.7029126213592233],
            [0.8070175438596491, 0.7621359223300971],
            [0.8070175438596491, 0.8097087378640777],
            [0.8054226475279107, 0.8699029126213592],
            [0.8133971291866029, 0.9262135922330097],
            [0.8054226475279107, 0.9757281553398058]]

thursdayDays = [[0.05422647527910686, 0.2058252427184466],
                [0.1419457735247209, 0.2058252427184466],
                [0.22169059011164274, 0.2058252427184466],
                [0.3014354066985646, 0.20388349514563106],
                [0.379585326953748, 0.20388349514563106],
                [0.46411483253588515, 0.20485436893203884],
                [0.5454545454545454, 0.20194174757281552]]



### BODY ###
wait()

enterWolt()
refresh()
verifyRefresh()
changeDay(7)
bookShift(9)

wait();
