#! python3

# Fuctions used for mapping the application

from win32gui import GetCursorPos as position

    ### Function used to generate coordinates lists ###
    # Returns coordiantes in the local coordiante system of the BlueStacks window
    # Coordinates values range between 0-1

def getCoordinates(coordinatesNumber):
    coordinateList = []
    hwnd = win32gui.FindWindow(None, "BlueStacks")
    rect = win32gui.GetWindowRect(hwnd)
    for i in range(0,coordinatesNumber):
        input("press Key for next coordinate...")
        coordinateList.append([ (position()[0]/rect[2]), (position()[1]/rect[3]) ])
    return coordinateList

def translatedCoordinates(xyIn):
    ### Translator for the coordinates in 0-1 value range ###
    # Translates the coordinates using the current window position
    hwnd = win32gui.FindWindow(None, "BlueStacks")
    rect = win32gui.GetWindowRect(hwnd)
    xOut = rect[0] + ( xyIn[0] * (rect[2]-rect[0]) )
    yOut = rect[1] + ( xyIn[1] * (rect[3]-rect[1]) )
    return [xOut, yOut]

refreshCircle = [[0.4370015948963317, 0.26601941747572816]]

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

def listTrans(list,i):
    return list[i]

def colorInspect(pointList):
    for i in range(0, 7):
        point = (  translatedCoordinates( pointList[i] )  )
        pointX = listTrans( point,0 )
        pointY = listTrans( point,1 )
        print(  get_pixel_colour( int(pointX), int(pointY) )  )
