# -*- coding: latin-1 -*-
# import libraries

import numpy as np
import cv2
import os
import warnings
import Tkinter as tk
import tkFileDialog
from time import gmtime, strftime
from appJar import gui

root = tk.Tk()
root.withdraw()

# Filter all warnings
warnings.filterwarnings("ignore")


#####################################################################
#               Create a GUI for instruction                        #
#####################################################################
instwin = gui("Instruction Window", "800x700") 
instwin.setFont(18)
instwin.addLabel("title","Instruction\n\n\
Please follow the instruction in order to label frames:\n\n\
After closing this window you will be asked to browse\n\
a video file and enter the interval between frames in\n\
seconds.\n\n\
In the Input window browse and select a video.\n\
Then, enter the seconds (default = 60) and press Submit.\n\n\
Afterwards, you will be shown frames. In order to label\n\
frames with corresponding class, press the following\n\
keys as stated beolow.\n\n\
Press '1' for empty class.\n\
Press '2' for half class.\n\
Press '3' for full class.\n\n")

def ok(button):
    if button == "Ok":
        instwin.stop()

instwin.addButtons(["Ok"], ok)

instwin.go()

####################################################################
####################################################################
####################################################################
#   Create a GUI to ebtervideo file path and seconds               #
####################################################################
def press(button):
    if button == "Browse":
        global videoFile
        videoFile = tkFileDialog.askopenfilename()
        pathwin.setEntry("Path", videoFile)
    elif button == "Submit":
        global seconds
        seconds = int(pathwin.getEntry("Seconds"))
        pathwin.stop()


pathwin = gui("Input Window", "600x400")
pathwin.setFont(18)
pathwin.addLabel("title","Please select video file.")
pathwin.addLabelEntry("Path")
pathwin.addButtons(["Browse"], press)
pathwin.addLabelEntry("Seconds")
pathwin.setEntry("Seconds",60)
pathwin.setFocus("Path")

       
pathwin.addButtons(["Submit"], press)
pathwin.go()

#####################################################################
#####################################################################



# Starts to capture from video file
vidcap = cv2.VideoCapture(videoFile)

# Check if the VideoCapture is opened successfully
if vidcap.isOpened() == False:
    app = gui("Error Window", "600x400")
    app.setFont(18)
    app.addLabel("title","File cannot be opened!")
    def ok(button):
        if button == "Ok":
            app.stop()
        app.addButtons(["Ok"], ok)
        app.go()


# Gets a prefix for name of the frames in video
prefix=strftime("%Y_%m_%d_%H_%M_%S_", gmtime())
videoFileName = videoFile.split('/')
for s in videoFileName[-2:]:
    prefix += s+'_'

# Gets total number of frames
nframes = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

# Gets number of frames per second
fps = int(vidcap.get(cv2.CAP_PROP_FPS))
print (fps)
# Makes directories for labeld images (frames)
dirlist = ['Empty', 'Half', 'Full']

# Checks if the directories exist
for d in dirlist:
    if not os.path.exists(d):
        # Makes directories
        os.makedirs('data/'+d)


frameId = 1
while (vidcap.isOpened) and (frameId < nframes):
    
    # Sets the starting frame to read 
    vidcap.set(1, frameId)

    # Read the frames
    ret, frame = vidcap.read()
    
    # Shows the frame
    cv2.imshow('Frame_'+str(frameId), frame)

    # Gets height and width of frame
    height,width = frame.shape[:2]

    # Checks if the frame is wide (This is specific for this project)
    if (width > 2 * height):
        frame = frame[:height, :int(width/2)]

    
    # Listens to the pressed key
    k = cv2.waitKey(0)
        
    
    # Label the images and save them to specific folder
    if (k == 49) or (k == 177): # Press 1 to save frame in empty class
        path = 'data/Empty/'
        cv2.imwrite(os.path.join(path, prefix+'Frame_'+str(frameId)+'.jpg'), frame)
    elif (k == 50) or (k == 178): # Press 2 to save frame in half class
        path = 'data/Half/'
        cv2.imwrite(os.path.join(path, prefix+'Frame_'+str(frameId)+'.jpg'), frame)
    elif (k == 51) or (k == 179): # Press 3 to save frame in full class
        path = 'data/Full/'
        cv2.imwrite(os.path.join(path, prefix+'Frame_'+str(frameId)+'.jpg'), frame)
    else:
        app = gui("Warning Window", "600x400")
        app.setFont(18)
        app.addLabel("title","Please press following keys:\n\
Press '1' for empty class.\n\
Press '2' for half class.\n\
Press '3' for full class.\n")

        def ok(button):
            if button == "Ok":
                app.stop()

        app.addButtons(["Ok"], ok)
        app.go()

        # 
        frameId -= fps * seconds
        
       
    # get the next frame ID
    frameId += fps * seconds
    
    cv2.destroyAllWindows()

    
    
vidcap.release()
cv2.destroyAllWindows()
