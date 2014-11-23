import pygame, sys
from pygame.locals import *
import pygame.camera
pygame.init()
pygame.camera.init()
class Webcam():
    def __init__(self):
        devicePath='/dev/video2'

        cam = pygame.camera.Camera(devicePath)
        cam.start()
    def startCamera(self):
        self.cam.start()
    def getImage(self):
        return self.cam.get_raw()

