#! python3

from time import sleep as sleep

import win32gui

from pyautogui import click as click
from pyautogui import typewrite as typewrite
from pyautogui import hotkey as hotkey

# ATTENTION !!!
# It is assumed that running this program you:
#   1.  Have your WoltPartnerApp opened in BlueStacks 4 and auto-aligned.
#   2.  Have the WoltPartnerApp control mapping imported into Blue BlueStacks.
#   3.  Are logged into the WoltPartnerApp with your number and are on the
#       'Scheduled hours -> Aarhus Central' tab.

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

def enterWolt():
    # enters the BlueStack window aligned to the top-left corner of the main screen
    click(10,70)

def blueStacksSetup():
    hwnd = win32gui.FindWindow(None, "BlueStacks")
    win32gui.ShowWindow(hwnd,5)
    win32gui.SetForegroundWindow(hwnd)
    rect = win32gui.GetWindowRect(hwnd)
    sleep(0.2)
    return rect

def refresh():
    # refresh the hours in WoltPartnerApp
    typewrite('r')

def changeDay(day):
    # moves to a day that is currently at 'day' position
    # note: 'day' must be an number between 1-7 (position from left to right)
    typewrite(str(day))

def book(slot):
    # presses the booking button on the chosen slot
    # note that 'slot' must be a number between 1-14 (position from top to bottom)
    position = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r']
    hotkey('shift', position[slot-1])

def closeCancel():
    # closes the booking cancel window without canceling
    click(282,623)

def get_pixel_colour(i_x, i_y):
    i_desktop_window_id = win32gui.GetDesktopWindow()
    i_desktop_window_dc = win32gui.GetWindowDC(i_desktop_window_id)
    long_colour = win32gui.GetPixel(i_desktop_window_dc, i_x, i_y)
    i_colour = int(long_colour)
    return (i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)

def pCheck(pc_x1,pc_x2,pc_y):
    for i in range(pc_x1,pc_x2):
        print(get_pixel_colour(i,pc_y))

def verifyPixel(vp_x,vp_y,vp_color):
    # compares pixel color to 'color'
    # x and y are pixel coordinates
    # color options:
    # w - ("255", 255, 255) - white, background
    # d - ("81", 81, 84) - black hours text, 1st pixel on the left
    # b - ("0", 157, 224) - blue, square on day's number
    # g - ("185", 186, 187) - grey hours text
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

def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)));

### BODY ###
wait()

blueStacksSetup()

wait();
