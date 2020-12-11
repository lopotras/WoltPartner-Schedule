# WoltPartner-Schedule
A little help to get the Wolt shifts you want.

The script uses GUI automation to try and book chosen shifts in the **Wolt Courier Partner** app opened in BlueStacks 4.

This is a project I developed while working with Wolt as a courier to facilitate scheduling the shifs.
The code generator was created as an excersise after finishing the JavaScript course on Ivan on Tech Blockchain Academy.

<h2>PREREQUISITS</h2>

  1. Download and install python and required modules. To do that you can use **miniconda**
  (<a href="https://docs.conda.io/en/latest/miniconda.html">link<a>). After installing it open <b>Anaconda Prompt</b> and type and confirm the following commands:

  <code>conda install pywin32</code>

  <code>conda install -c conda-forge pyautogui</code>

  2. Download and install **BlueStacks 4** (<a href="https://www.bluestacks.com/download.html">link</a>).
  3. Once inside **BlueStacks** go to Google Play Store. Find and download the **Wolt Courier Partner** app. Open and log-in to the app. **Wolt Courier Partner** needs to run in white theme (default).

<h2>USER MANUAL</h2>

  1. Download and extract the files (<a href="https://github.com/lopotras/WoltPartner-Schedule/blob/main/manuals/downloadRepo.png">pic</a>).
  2. Open **BlueStacks** and log-in to the **Wolt Courier Partner** app.
  3. In **Wolt Courier Partner** open the menu (top left corner of the screen) and go to _Scheduled hours -> Aarhus Central_ (or the city you are delivering in, <a href="https://github.com/lopotras/WoltPartner-Schedule/blob/main/manuals/scheduledHours.png">pic</a>).
  4. Make sure that the display resolution is set to **1600x900** (<a href="https://github.com/lopotras/WoltPartner-Schedule/blob/main/manuals/setResolution.png">pic</a>).
  5. Autoalign BlueStacks (<a href="https://github.com/lopotras/WoltPartner-Schedule/blob/main/manuals/autoAlign.png">pic</a>).
  6. Open codeGenerator.html and choose the shift slots you want to book (1). Copy the code (2, <a href="https://github.com/lopotras/WoltPartner-Schedule/blob/main/manuals/codeGenerator.png">pic</a>).
  7. Open **woltPartnerBooking.py** in a text editor. Delete all contents. Paste the code in the empty file and save (<a href="https://github.com/lopotras/WoltPartner-Schedule/blob/main/manuals/pasteCode.png">pic</a>).
  8. Run **woltPartnerBooking.py** through _Open with..._  -> **python**. You can find **python.exe** in the **miniconda** installation directory (<a href="https://github.com/lopotras/WoltPartner-Schedule/blob/main/manuals/python.png">pic</a>).
  9. After running he scrip try not to move the mouse as the program uses the cursor to interact with WoltPartner App.

<h2>WHAT TO EXPECT</h2>

  You can expect the script to serve as an extra person while booking your shifts. It proves useful for not having to wait on the phone for the new shifts to arrive, while refreshing constantly. You can just run it earlier and go have fun.

  If you are aiming for the shifts that are booked very quickly you may experience errors during booking (similarly as during manual booking).

<h2>ADVANCED TIPS</h2>

  1. If you run the program between Thursday 03:00pm and Friday 08:00am the script will wait for 08:00am to start. Otherwise it will start booking at 03:00pm.
  2. You can tweak with the starting time by exchanging _f.autoStart()_ with _f.startAt(hh,mm,ss)_. **Note:** In _f.startAt(hh,mm,ss)_ _mm_ and _ss_ default to _0_. Single digit agruments should not be padded with _0_'s (example: if you want to start at 15:01:00 the arguments should be: _f.startAt(15,1)_).


  **Good luck and enjoy the ride!**
