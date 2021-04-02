#! python3
import time
import win32gui
import pyautogui

def setup():
    # Global variables definition
    # check if next booking is expected on friDays
    global friday
    friday = fridayCheck()
    print(friday)

    # (relative coordinates)
    global refreshCircle
    refreshCircle = [0.4370015948963317, 0.26601941747572816]   # X and Y coordinates
                                                                # of the circle that appears when refreshing

    # in case the refresh circle is not grey in color 
    # the coordinates of the moving black circle can be used to locate it
    # NOTE: this method will be a bit slower than the original one
    global refreshCircleBlackPart
    refreshCircleBlackPart = [0.463884430176565, 0.2586538461538462]

    global shifts
    shifts = [[0.8229665071770335, 0.27475728155339807],    # X and Y coordinates
                [0.810207336523126, 0.3300970873786408],    # of shift slots
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

    global thuDays
    thuDays = [[0.0430622009569378, 0.1941747572815534],    # X and Y coordinates
                [0.11961722488038277, 0.19611650485436893], # of days
                [0.20574162679425836, 0.19223300970873786],
                [0.2886762360446571, 0.19320388349514564],
                [0.3700159489633174, 0.19611650485436893],
                [0.44657097288676234, 0.19320388349514564],
                [0.532695374800638, 0.19320388349514564]]

    # X and Y coordinates of days for booking in Munich, after moving them all the way to the right
    # starting from right side
    global munichDaysFromRight
    munichDaysFromRight = [[0.8764044943820225, 0.2],
                        [0.7849117174959872, 0.2],
                        [0.7046548956661316, 0.2],
                        [0.6163723916532905, 0.2],
                        [0.5296950240770465, 0.2],
                        [0.43980738362760835, 0.2],
                        [0.3563402889245586, 0.2],
                        [0.2712680577849117, 0.2],
                        [0.1781701444622793, 0.2],
                        [0.09470304975922954, 0.2]]

    global bookButton
    bookButton = [[0.7751196172248804, 0.3300970873786408], # X and Y coordinates of
                [0.8500797448165869, 0.32815533980582523]]  # start and end of the button area

    print( time.strftime("%c") + " All set")

def fridayCheck():
    # returns true if the time is between
    # Thursday 15:00 (included) and Friday 08:00 (excluded)
    currentDay = time.strftime("%c")[0:3]
    currentHour = int(time.strftime("%c")[11:13])
    currentMinute = int(time.strftime("%c")[14:16])
    
    if(currentDay == "Thu"):
        if(currentHour >= 15):
            return True
    elif(currentDay == "Fri"):
        if(currentHour < 8):
            return True

    return False

def pause():
    input( "press ENTER to continue..." )

def startAt(hour, minute = 0, second = 0):
    # stop until the chosen hour comes
    print( time.strftime("%c") + " Waiting for {:02}:{:02}:{:02}...".format(hour, minute, second) )
    while True:
        if time.localtime()[3] == hour:
            if time.localtime()[4] == minute:
                if time.localtime()[5] == second:
                    print( time.strftime("%c") + " Initiate booking actions")
                    break

# automatic start for Aarhus
def autoStart():
    if(friday):
        startAt(8)
    else:
        startAt(15)

# automatic start for Munich
def autoStartMunich():
    startAt(10,30)

def enterWolt():
    # Finds and brings BlueStacks window to the front
    # Returns window coordinates
    print( time.strftime("%c") + " Entering WoltPartner...")
    hwnd = win32gui.FindWindow( None, "BlueStacks" )
    win32gui.ShowWindow( hwnd,5 )
    win32gui.SetForegroundWindow( hwnd )
    print( time.strftime("%c") + " Entered WoltPartner")

def refresh():
    # refreshes the page by dragging cursor
    print( time.strftime("%c") + " Initiating refresh operations..." )
    pos = translatedCoordinates( refreshCircle )
    print( time.strftime("%c") + " Movinging to refresh start position..." )
    pyautogui.moveTo( pos )
    print( time.strftime("%c") + " Moved. Initiating drag..." )
    pyautogui.drag( 0, 200, 0.2, button = 'left' )
    print( time.strftime("%c") + " Drag finished. Initiating refresh verification..." )
    verifyRefresh()     #checks if the refreshing worked properly

def refreshMunich():
    # refreshes the page by dragging cursor
    # uses a different verification function than refresh()
    # used when the refresh circle is of white color
    # NOTE: slightly slower than refresh()
    print( time.strftime("%c") + " Initiating refresh operations..." )
    pos = translatedCoordinates( refreshCircle )
    print( time.strftime("%c") + " Movinging to refresh start position..." )
    pyautogui.moveTo( pos )
    print( time.strftime("%c") + " Moved. Initiating drag..." )
    pyautogui.drag( 0, 200, 0.2, button = 'left' )
    print( time.strftime("%c") + " Drag finished. Initiating refresh verification..." )
    verifyRefreshMunich()     # checks if the refreshing worked properly

def changeDay(day):
    # moves to a day that is currently at 'day' position
    # note: 'day' must be an number between 1-7 (position from left to right)
    pos = translatedCoordinates( thuDays[day-1] )
    pyautogui.click( pos[0], pos[1] )
    verifyPixelColorChange(  int( pos[0] ), int( pos[1] ), 255  )
    print( time.strftime("%c") + " Changed day to {}".format(day) )

def changeDayMunich(day):
    # moves to a day that is currently at 'day' position
    # note: 'day' must be an number between 1-10 (position from right to left)
    pos = translatedCoordinates( munichDaysFromRight[day-1] )
    pyautogui.click( pos[0], pos[1] )
    verifyPixelColorChange(  int( pos[0] ), int( pos[1] ), 255  )
    print( time.strftime("%c") + " Changed day to {}".format(day) )

def bookShift(slot):
    # Clicks on the booking button space on the chosen slot
    # note that 'slot' must be a number between 1-14 (position from top to bottom)
    verifyBooking( slot )
    pyautogui.click( translatedCoordinates( shifts[slot-1] ) )

# booking function for cities where shifts appear on one day only
def bookingMunich(day, slot):
    changeDayMunich(day)
    bookShift(slot)

# booking function for cities where shifts appear on Thursday and Friday
def booking(day, slot, fridayBooking):
    if(fridayBooking == friday):
        changeDay(day)
        bookShift(slot)

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

def verifyPixelColorChangeTimed(x,y,startColor,probingTime):
    # stops until the color changes from startColor and does not come back to startColor within 0.5s
    # compares pixel color to the first number of 'color'
    # x and y are pixel coordinates
    # startColor values (in ""):
    # ("255", 255, 255) - white, background
    # ("81", 81, 84) - black, active hours text, 1st pixel on the left
    # ("0", 157, 224) - blue, square on currently chosen day's number
    # ("185", 186, 187) - grey, inactive hours text
    # ("250", 250, 250) - grey, refresh circle
    currentColor = get_pixel_colour(x,y)
    currentTime = time.time()
    finishTime = currentTime + probingTime
    while currentColor[0] == startColor or currentTime < finishTime:
        currentColor = get_pixel_colour(x,y)
        # print( time.strftime("%c") + " " + str(currentColor) )
        currentTime = time.time()
        if currentColor[0] == startColor:
            finishTime = currentTime + probingTime

def verifyBooking(slot):
    # Stops script
    # Verifies if the chosen slot has a booking option available
    # Used also to see if the page loaded already after previous booking
    print( time.strftime("%c") + " Checking booking availability for slot {}...".format(slot) )
    posXstart = int (  translatedCoordinates( bookButton[0] ) [0]  )    # start point of booking button area
    posXend = int (  translatedCoordinates( bookButton[1] ) [0]  )      # end point of booking button area
    posY = int(  translatedCoordinates( shifts[slot-1] ) [1]  )         # Y coordinate of booking button area

    marker = False              # define a condition marker for the while loop
    timeout = time.time() + 5        # set waiting time for booking verification before moving on

    while marker == False:      # while loop checks if the "Book" option appeared

        for j in range( posXstart, posXend ):           # define the range for verification
            currentColor = get_pixel_colour(j,posY)     # get color of current pixel

            if currentColor[0] < 100:
                # checks if the pixel is a part of an availale "Book" option
                marker = True
                print( time.strftime("%c") + " Booking" )
                break

            elif time.time() > timeout:
                # checks if the waiting time for "Book" option to appear has been exceeded
                marker = True
                print( time.strftime("%c") + " Booking unavailable" )
                break

def verifyRefresh():
    # verify if refreshing worked
    pos = translatedCoordinates( refreshCircle )

    # see if the refreshing circle appeared
    verifyPixelColorChange( int(pos[0]), int(pos[1]), 255 )
    print( time.strftime("%c") + " Refreshing..." )

    # see if the refreshing circle disappeared
    verifyPixelColorChange( int(pos[0]), int(pos[1]), 250 )
    print( time.strftime("%c") + " Refreshed" )

def verifyRefreshMunich():
    # verify if refreshing worked
    # use only when the refresh circle has a plain white color (the same as background)
    # tracks the black circle that turns around when refreshing
    # NOTE: slightly slower than verifyRefresh()
    pos = translatedCoordinates( refreshCircleBlackPart )

    # see if the refreshing circle appeared
    verifyPixelColorChange( int(pos[0]), int(pos[1]), 255 )
    print( time.strftime("%c") + " Refreshing..." )

    # see if the black moving circle on the refreshing circle disappeared
    verifyPixelColorChangeTimed( int(pos[0]), int(pos[1]), 0,  0.5)
    print( time.strftime("%c") + " Refreshed" )

def translatedCoordinates(xyIn):
    ### Translator for the coordinates in 0-1 value range ###
    # Translates the relative coordinates into pixel position on the screen
    # using the current window position and size
    hwnd = win32gui.FindWindow( None, "BlueStacks" )
    rect = win32gui.GetWindowRect( hwnd )
    xOut = rect[0] + (  xyIn[0] * ( rect[2] - rect[0] )  )
    yOut = rect[1] + (  xyIn[1] * ( rect[3] - rect[1] )  )
    return [ int(xOut), int(yOut) ]

# moves the days all the way to the right
# setup for the city that has all shifts showing up on one day
def moveToLaterDays():
    posStart = translatedCoordinates( thuDays[6] )          # 7th day from the left
    posEnd = translatedCoordinates( thuDays[0] )            # 1st day from the left
    pyautogui.moveTo( posStart )                            # move to posStart
    distance = posEnd[0] - posStart[0]                      # calculate distance to move                     
    pyautogui.drag( distance, 0, 0.2, button = 'left' )     # drag coursor 
    print( time.strftime("%c") + " Moved to new days" )