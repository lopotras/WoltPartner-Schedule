#! python3

### LIBRARIES IMPORT ###
from time import sleep as sleep
from time import strftime as strftime
from time import time as time

import win32gui

import pyautogui
from pyautogui import click as click
from pyautogui import typewrite as typewrite
from pyautogui import hotkey as hotkey



### FUNCTIONS DEFINITIONS ###
def wait():
    input( "press ENTER to continue..." )

def enterWolt():
    hwnd = win32gui.FindWindow( None, "BlueStacks" )
    win32gui.ShowWindow( hwnd,5 )
    win32gui.SetForegroundWindow( hwnd )
    rect = win32gui.GetWindowRect( hwnd )
    sleep( 0.2 )
    return rect

def refresh():
    pos = translatedCoordinates( refreshCircle )
    pyautogui.moveTo( pos )
    pyautogui.drag( 0, 200, 0.2, button = 'left' )

def changeDay(day):
    # moves to a day that is currently at 'day' position
    # note: 'day' must be an number between 1-7 (position from left to right)
    pos = translatedCoordinates( thuDays[day-1] )
    click( pos[0], pos[1] )
    verifyPixelColorChange(  int( pos[0] ), int( pos[1] ), 255  )
    print( timeStamp + " Changed day to " + str(day) )

def bookShift(slot):
    # Clicks on the booking button space on the chosen slot
    # note that 'slot' must be a number between 1-14 (position from top to bottom)
    verifyBooking( slot )
    click( translatedCoordinates( shifts[slot-1] ) )

def get_pixel_colour( i_x, i_y ):
    # returns the color of a pixel with coordinates i_x, i_y
    # in the format (r, g, b)
    i_desktop_window_id = win32gui.GetDesktopWindow()
    i_desktop_window_dc = win32gui.GetWindowDC( i_desktop_window_id )
    long_colour = win32gui.GetPixel( i_desktop_window_dc, i_x, i_y )
    i_colour = int( long_colour )
    return (i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)

def verifyPixelColorChange(x,y,startColor):
    # stops until the color changes from startColor
    # compares pixel color to the first number of 'color'
    # x and y are pixel coordinates
    # startColor values (in ""):
    # ("255", 255, 255) - white, background
    # ("81", 81, 84) - black, active hours text, 1st pixel on the left
    # ("0", 157, 224) - blue, square on currently chosen day's number
    # ("185", 186, 187) - grey, inactive hours text
    # ("250", 250, 250) - grey, refresh circle
    currentColor = get_pixel_colour(x,y)
    while currentColor[0] == startColor:
        currentColor = get_pixel_colour(x,y)

def verifyBooking(slot):
    # Stops script
    # Verifies if the chosen slot has a booking option available
    # Used also to see if the page loaded already after previous booking

    posXstart = int (  translatedCoordinates( bookButton[0] ) [0]  )    # start point of booking button area
    posXend = int (  translatedCoordinates( bookButton[1] ) [0]  )      # end point of booking button area
    posY = int(  translatedCoordinates( shifts[slot-1] ) [1]  )         # Y coordinate of booking button area

    marker = False              # define a condition marker for the while loop
    timeout = time() + 4        # set waiting time for booking verification before moving on

    while marker == False:      # while loop checks if the "Book" option appeared

        for j in range( posXstart, posXend ):           # define the range for verification
            currentColor = get_pixel_colour(j,posY)     # get color of current pixel

            if currentColor[0] < 100:
                # checks if the pixel is a part of an availale "Book" option
                marker = True
                print( timeStamp + " Booking..." )
                break

            elif time() > timeout:
                # checks if the waiting time for "Book" option to appear has been exceeded
                marker = True
                print( timeStamp + " Booking unavailable" )
                break

def verifyRefresh():
    pos = translatedCoordinates( refreshCircle )

    # see if the refreshing circle appeared
    verifyPixelColorChange( int(pos[0]), int(pos[0]), 255 )
    print( timeStamp + " refreshing..." )

    # see if the refreshing circle disappeared
    verifyPixelColorChange( int(pos[0]), int(pos[0]), 250 )
    print( timeStamp + " refreshed" )

def translatedCoordinates(xyIn):
    ### Translator for the coordinates in 0-1 value range ###
    # Translates the relative coordinates into pixel position on the screen
    # using the current window position and size
    hwnd = win32gui.FindWindow( None, "BlueStacks" )
    rect = win32gui.GetWindowRect( hwnd )
    xOut = rect[0] + (  xyIn[0] * ( rect[2] - rect[0] )  )
    yOut = rect[1] + (  xyIn[1] * ( rect[3] - rect[1] )  )
    return [ int(xOut), int(yOut) ]



### GLOBAL VARIABLES DEFINITIONS ###
timeStamp = strftime( "%c" )

# RELATIVE COORDINATES

refreshCircle = [0.4370015948963317, 0.26601941747572816] # X and Y coordinates

shifts = [[0.8229665071770335, 0.27475728155339807],    # X and Y coordinates
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

thuDays = [[0.0430622009569378, 0.1941747572815534],    # X and Y coordinates
            [0.11961722488038277, 0.19611650485436893],
            [0.20574162679425836, 0.19223300970873786],
            [0.2886762360446571, 0.19320388349514564],
            [0.3700159489633174, 0.19611650485436893],
            [0.44657097288676234, 0.19320388349514564],
            [0.532695374800638, 0.19320388349514564]]

bookButton = [[0.7751196172248804, 0.3300970873786408], # X and Y coordinates of
            [0.8500797448165869, 0.32815533980582523]]  # start and end


### BODY ###
wait()

enterWolt()
refresh()
verifyRefresh()
changeDay(4)
bookShift(8)
changeDay(5)
bookShift(13)

wait();
