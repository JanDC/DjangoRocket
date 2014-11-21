from pygame import camera

devicePath='/dev/video2'

class Webcam():
    def __init__(self):
        camera.init()
        self.camera = camera.Camera(devicePath)

    def startCamera(self):
        self.camera.start()
    def getImage(self):
        return self.camera.get_raw