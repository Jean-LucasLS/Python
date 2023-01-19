from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QApplication, QSystemTrayIcon, QMenu

app = QApplication([])
app.setQuitOnLastWindowClosed(False)

# Adding an icon
icon = QIcon("3b08b8f5-5279-4b7f-ba7f-0cfd788de46c.png")

# Adding item on the menu bar
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

def juca():
    print('rei das dicas')

# Creating the options
menu = QMenu()
option1 = QAction("Start/Stop")
option1.setIcon(icon)
option1.triggered.connect(juca)
option2 = QAction("2")
menu.addAction(option1)
menu.addAction(option2)
# To quit the app
quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

# Adding options to the System Tray
tray.setContextMenu(menu)

app.exec_()

#########################################################################################

# import pyvirtualcam
# from pypylon import pylon as py

# #Initializing the virtual camera
# with pyvirtualcam.Camera(width=1280, height=720, fps=20, device='/dev/video2') as cam:

#     # Finding the first Basler device
#     device = py.InstantCamera(py.TlFactory.GetInstance().CreateFirstDevice())

#     # Opening a connection with the camera
#     device.Open()

#     # Starting image acquisition
#     device.StartGrabbing(py.GrabStrategy_LatestImageOnly)

#     keyPress = False
#     # Continuously acquiring Basler frames
#     while not keyPress:
        
#         while device.IsGrabbing():

#             # Obtaining the next image available
#             grabResult = device.RetrieveResult(5000, py.TimeoutHandling_ThrowException)

#             # Creating the converter and setting parameters
#             converter = py.ImageFormatConverter()
#             converter.OutputPixelFormat = py.PixelType_RGB8packed
#             converter.OutputBitAlignment = py.OutputBitAlignment_MsbAligned

#             # Checking if the image was successfully acquired
#             if grabResult.GrabSucceeded():

#                 # Accessing the frame as NumPy array
#                 image = grabResult.Array

#                 # Sending the frame to the virtual camera
#                 cam.send(image)
#                 cam.sleep_until_next_frame()
#             else:
#                 print("Erro while acquiring image:", grabResult.ErrorCode, grabResult.ErrorDescription)

# # stop acquiring image and closing connection
# device.StopGrabbing()
# device.Close()
# #########################################################################################


