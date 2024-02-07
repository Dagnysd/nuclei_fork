# create a class
class Nucleus:
        # constructor function    
    def __init__(self, label, area, ch1Intensity, ch2Intensity, ch3Intensity, ch4Intensity=None ):
        self.label = label
        self.area = area
        self.ch1Intensity = ch1Intensity
        self.ch2Intensity = ch2Intensity
        self.ch3Intensity = ch3Intensity
        self.ch4Intensity = ch4Intensity


    def has4Channels(self):
        return self.ch4Intensity != None
    

# create object of Room class
# nucleis = [Nuclei(), Nuclei()]

# if nucleis[0].has4Channels():
#     nucleis[0].ch4Intensity
