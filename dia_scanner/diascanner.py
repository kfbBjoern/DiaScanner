import xml.etree.ElementTree as ET
from pygame import mixer, time

__author__ = 'kfbBjoern'

class DiaScanner:

    def __init__(self, configFile, nofPictures):
        self.MaxPictures = nofPictures
        self.CurrentPicture = 0
        self.ProjectorSound = ""
        self.ProjectorWait = 10
        self.readConfiguration(configFile)
        self.Mixer = mixer
        self.Mixer.init()
        self.Mixer.music.load(self.ProjectorSound)

    def getNumberOfPicture(self):
        return self.MaxPictures

    def getCurrentPicture(self):
        return self.CurrentPicture

    def readConfiguration(self, file):
        tree = ET.parse(file)
        root = tree.getroot()

        for xml_child in root:
            if (xml_child.tag == 'projector'):
                for projector_child in (xml_child):
                    if (projector_child.tag == 'sound'):
                        self.ProjectorSound = projector_child.text
                    elif (projector_child.tag == 'wait'):
                        number = int(projector_child.text)
                        self.ProjectorWait = number
                    else:
                        print("unknown tag: {0}".format(projector_child.tag))
            else:
                print("unknown tag: {0}".format(xml_child.tag))

    def run(self):
        maxPicture = self.getNumberOfPicture()
        for picture in range(maxPicture):
            print("{}".format(picture))
            self.transport()
            self.takePicture()

    def transport(self):
        self.Mixer.music.play()
        time.wait(1000*self.ProjectorWait)

    def takePicture(self):
        pass
