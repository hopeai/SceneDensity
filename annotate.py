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
instwin = gui("Açıklama", "800x700") 
instwin.setFont(18)
instwin.addLabel("title","Kullanım Kılavuzu.\n\n\
Görüntüleri etiketlemek için lütfen talimatları takip ediniz:\n\n\
Bu pencereği kapattıktan sonra, açılan yeni pencere'de\n\
sizden bir video dosyası adresi ve kaç saniye aralıklarla\n\
video frame'lerini görüntülemek istediğiniz sorulacaktır.\n\n\
Açılan pencerede 'Browse' tuşuna basın ve video dosyasın seçiniz.\n\
Sonra, saniye bilgisini girip ve 'Onay' tuşuna basınız.\n\n\
Yeni açılan pencerede, size frame'ler gösterilecektir. Frame'leri\n\
etiketlemek için aşağıda belirtilen klavyedeki tuşlara basınız.\n\n\
Boş olarak etiketlemek için '1'e basın.\n\
Orta olarak etiketlemek için '2'e basın.\n\
Dolu olarak etiketlemek için '3'e basın.\n\n")

def ok(button):
    if button == "Tamam":
        instwin.stop()

instwin.addButtons(["Tamam"], ok)

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
        pathwin.setEntry("Adres", videoFile)
    elif button == "Onay":
        global seconds
        seconds = int(pathwin.getEntry("Saniye"))
        pathwin.stop()


pathwin = gui("Bilgiler", "600x400")
pathwin.setFont(18)
pathwin.addLabel("title","Video dosyasının tam adresini giriniz.")
pathwin.addLabelEntry("Adres")
pathwin.addButtons(["Browse"], press)
pathwin.addLabelEntry("Saniye")
pathwin.setEntry("Saniye",60)
pathwin.setFocus("Adres")

       
pathwin.addButtons(["Onay"], press)
pathwin.go()

#####################################################################
#####################################################################



# Starts to capture from video file
vidcap = cv2.VideoCapture(videoFile)

# Check if the VideoCapture is opened successfully
if vidcap.isOpened() == False:
    app = gui("Variables Window", "600x400")
    app.setFont(18)
    app.addLabel("title","Dosya açılmıyor! Tekrar deneyin.")
    def ok(button):
        if button == "Tamam":
            app.stop()
        app.addButtons(["Tamam"], ok)
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

# Makes data directories for labeld images (frames)
dirlist = ['Bos', 'Orta', 'Dolu']

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
        path = 'data/Bos/'
        cv2.imwrite(os.path.join(path, prefix+'Frame_'+str(frameId)+'.jpg'), frame)
    elif (k == 50) or (k == 178): # Press 2 to save frame in half class
        path = 'data/Orta/'
        cv2.imwrite(os.path.join(path, prefix+'Frame_'+str(frameId)+'.jpg'), frame)
    elif (k == 51) or (k == 179): # Press 3 to save frame in full class
        path = 'data/Dolu/'
        cv2.imwrite(os.path.join(path, prefix+'Frame_'+str(frameId)+'.jpg'), frame)
    else:
        app = gui("Variables Window", "600x400")
        app.setFont(18)
        app.addLabel("title","Lütfen aşağıdakı tuşlara basınız:\n\
Boş olarak etiketlemek için '1'e basın.\n\
Orta olarak etiketlemek için '2'e basın.\n\
Dolu olarak etiketlemek için '3'e basın.")

        def ok(button):
            if button == "Tamam":
                app.stop()

        app.addButtons(["Tamam"], ok)
        app.go()

        # 
        frameId -= fps * seconds
        
       
    # get the next frame ID
    frameId += fps * seconds
    
    cv2.destroyAllWindows()

    
    
vidcap.release()
cv2.destroyAllWindows()
