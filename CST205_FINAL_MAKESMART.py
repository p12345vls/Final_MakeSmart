# CST205 FINAL ASSIGNMENT
# Completed by: Team MakeSmart
# Pavlos Papadonikolakis, Maco Doussias, Jake McGhee

# TITLE: RPG Character Generator
# This program serves as the RPG character generator for a video game
# Gets user to choose a character type (Wizard, Barbarian, Archer)
# Gets user to choose a voice for the character (six different voices)
# Gets user to choose a color for their character (Black, Red, Blue)
# On completion of choosing character, plays characters voice and displays image

#NOTE:  characterGenerator() function will run the program


#TODO this is just preliminary code.... Make major changes to sructure or content as needed

#TODO make a function called characterImage(characterType,characterColor) and returns an image of character

import os


def getSound():
# TODO remove this function before final submission as it won't be needed in the program.... just here for testing purposes
  filePath = pickAFile()
  soundObject = makeSound(filePath)
  return soundObject


def cMaj():
  """ Plays c major chord (C-E-G) for game using diatonic scale"""
  playNote(60,250,130)  #play c note
  playNote(64,250,130) #play e note
  playNote(69,250,130) #play g note 
  
def fMaj():
  #TODO make sure this is in fact an f maj triad?  This might be wrong
  """ Plays an f Major chord (D-E-G) for game using diatonic scale"""
  playNote(60,250,130) #play D note
  playNote(65,250,130) #play F note
  playNote(69,250,130) #play G note   
  
def dMin():
  """ Plays a d minor chord (D-F-E) for game using diatonic scale"""
  playNote(62,250,130)  #play D note
  playNote(65,250,130) #play F note
  playNote(69,250,130) #play G note    

def playSong(numOfLoops):
  """ Plays a theme song for the game """
  """ Args: integer value defines how many times the theme song will loop """
  for x in range(0,numOfLoops):
    cMaj()
    dMin()
    fMaj()
    dMin()
  #fade away  
  playNote(60, 250,130)
  playNote(64, 250,100)    
  playNote(69, 250,70)
   
   
   
def copy(soundOne, soundTwo, start):
  #TODO this function could be refactored to be a little bit simpler than it is... 
  #TODO are two for loops really needed?
   """This functiontion copes the second sound file into the first at the start argument """
   """Args:  """
   """      soundOne: A sound object"""
   """      soundTwo: A sound object that will be copied into soundOne"""
   """      start: Integer value that represents the start of where soundTwo will be copied into soundOne"""
   """Returns: """
   """      A new sound with sound one copied into sound one.  Note sampling rate will be same as soundOne."""

   lenSoundOne = getLength(soundOne)
   lenSoundTwo = getLength(soundTwo)
   samplingRate = int(getSamplingRate(soundOne))
   newSound = makeEmptySound(lenSoundOne, samplingRate)
   index = int(start);
   #First add in sound one
   for i in range(0, lenSoundOne):
      value = getSampleValueAt(soundOne, i)
      setSampleValueAt(newSound, i, value)
   #Second add in sound 2
   for i in range(0, lenSoundTwo):
      value = getSampleValueAt(soundTwo, i)
      setSampleValueAt(newSound, index, value)
      index = index + 1
   return newSound   
   
def changePitch(sound, delta):
  """ Changes the pitch of a sound object """
  """ Args:  """
  """     sound: sound object received for manipulation """
  """     delta: allows for a value from .5 to 1.5 to change the pitch.  1.5 == higher pitch, .5 == lower pitch """ 
  """ Returns: """
  """       A sound object with a new pitch """  
  #TODO could add some low level validation to ensure delta arg is within range
  samplingRate = samplingRate = getSamplingRate(sound)
  numSamples = getNumSamples(sound)
  newSound = makeEmptySound(numSamples,int(samplingRate*delta)) #by changing the sampling rate the frequency adjusts the pitch
  newSound = copy(newSound,sound,0)
  return maxVolume(newSound)

def maxSample(sound):
  """ sound:(string) the sound file """
  """ returns the largest sample value in a sound """
  largest = 0
  for s in getSamples(sound):
    largest = max(largest,getSample(s))
  factor = 32767.0 / largest
  return largest

def maxVolume(sound):
  """ sets the maximum posible volume """
  """ sound:(string) the sound file """
  factor = 32767.0 / maxSample(sound)
  for s in getSamples(sound):
    louder = factor * getSample(s)
    setSample(s,louder)
  return sound


def getPicture(fileName):
    """ Returns a picture from the folder same folder that that the program is being run in """
    """ If the picture is not found, it prompts the user to select a picture """

    # Get the programs working directory
    directory = os.path.dirname(__file__) 
    
    # Make full path name
    path = directory + "\\" + fileName
    
    # Open the file if it exists
    if os.path.exists(path):
        return makePicture(path)
    # Manually select file if not found
    else:
        showInformation("File not found\nPlease select " + fileName)
        return makePicture(pickAFile())
        
def getVoice(fileName):
    """ Returns a sound from the same folder that that the program is being run in """
    """ If the sound is not found, it prompts the user to select a sound """
    """ Args: """
    """     fileName: string argument for name of file contained in top directory of program """

    # Get the programs working directory
    directory = os.path.dirname(__file__) 
    
    # Make full path name
    path = directory + "\\" + fileName
    
    # Open the file if it exists
    if os.path.exists(path):
        return makeSound(path)
    # Manually select file if not found
    else:
        showInformation("File not found\nPlease select " + fileName)
        return makeSound(pickAFile())        
        
def colorize(picOriginal, picColoredArea, targetColor, threshold, tintColor, multiplier):
    """ Takes a picture and a reference picture and tints the area in the original picture based on the colored area in the reference picture """
    """ 
        Args:
            picOriginal (pic): The picture that will be altered
            picColoredArea (pic): The picture containing the colored area that will be referenced and tinted in picOriginal
                                  Must be same width and height as picOriginal
            targetColor (color): The color of the reference area in picColoredArea
            threshold (int): The amount of leeway the function will give between the difference of the targetColor and the actual color in picColoredArea
            tintColor (string): The color to tint to. Should be the result of chooseCharacterColor()
            multiplier (float): The amount by which targeted pixels will be tinted. Should be a smallish number (probably somewhere between 1.5 and 3)
    """
            
    # Scan picColoredArea for targetColor
    for x in range(0, getWidth(picColoredArea)):
        for y in range(0, getHeight(picColoredArea)):    
            p = getPixel(picColoredArea, x, y)
            color = getColor(p)
            # If pixel is within the threshold of the targetColor
            if distance(color, targetColor) <= threshold:
                p = getPixel(picOriginal, x, y)
                # tint that pixel
                if tintColor == 'RED':
                    if getRed(p) < 50:
                        setRed(p, 50) 
                    setRed(p, getRed(p)*multiplier)
                elif tintColor == 'GREEN':
                    if getGreen(p) < 50:
                        setGreen(p, 50)
                    setGreen(p, getGreen(p)*multiplier)
                elif tintColor == 'BLUE':
                    if getBlue(p) < 50:
                        setBlue(p, 50)
                    setBlue(p, getBlue(p)*multiplier)          
    show(picOriginal)                                
    return picOriginal   

def getSelection(msg, list):
    """ Presents the user with a given list of options """
    """ Checks to see that they have entered a valid option """
    """ Returns the result """
    
    # Display the list of available options
    for i in xrange(0, len(list)):
        msg += "\n" + str(i+1) + " - " + list[i].title()
    
    while true:
         # Get user input
        selection = requestString(msg) 
        
        # If user selects an option using string input  
        if selection.upper() in list:
            return selection.upper()
        # If user selects an option using integer input
        elif selection.isdigit() and int(selection) > 0 and int(selection) < len(list)+1:
            return list[int(selection)-1] #returns the element of list corresponding to user choice
        # If user enters invalid input
        else:
            showInformation("Invalid input")
         

def chooseClass(): # Wizard, Barbarian, Archer
    """ Prompts user to choose a character class and returns that class """
    
    classes = ['WIZARD', 'BARBARIAN', 'ARCHER']
    msg = "Please select a class"
    return getSelection(msg, classes)
    
      
def chooseCharacterColor():
    """ Shows user a slection of character color choices """
    """ Prompts user to pick a color for their character """
    """ Returns the character color """
    
    colors = ['RED', 'GREEN', 'BLUE']
    msg = "Please select a character color"
    return getSelection(msg, colors)

def chooseCharacterVoice():
    #TODO make this function work
    """ Prompts user to choose a character voice """
    
    voices = ['HIGH', 'MEDIUM', 'LOW']
    msg = "Please select a character voice"
    return getSelection(msg, voices)

def welcomeMessage():
    #TODO make this function work
    """ Displays a textbox welcome message to the user """
    showInformation('Welcome to RPG Character Generator!\n'\
                     'You can choose the character of your choice\n'\
                     'change the color of the character and the pitch of its voice!')
                     
    
def characterGenerator():
    #TODO make this function work
    #TODO need to figure out how to have a characterImage and a characterType
    """ Runs the RPG character generator. """ 
    # welcomeMessage() #displays a welcome message to user 
    # characterImage = chooseCharacterType()
    # characterVoice = chooseCharacterVoice(characterVoice)
    # characterColor = chooseCharacterColor()
    # 
    welcomeMessage() #displays the welcome message
    characterClass = chooseClass()
    if characterClass == 'WIZARD':
      voice = getVoice('wizardVoice.wav')
    elif characterClass == 'ARCHER':
      voice = getVoice('archerVoice.wav')
    elif characterClass == 'BARBARIAN':
      voice = getVoice('barbarianVoice.wav')
    
    voicePitch = chooseCharacterVoice()   
    if voicePitch == 'HIGH':
      voice = changePitch(voice, 1.15)      
    elif voicePitch == 'LOW':
      voice = changePitch(voice, .85)
    else:
      voice = changePitch(voice, 1)
     
    #TODO Just testing the colorize function, this should be edited later
    #TODO I made the wizard_example_colored in MS paint so the threshold will be way lower when I make the real photos in photoshop
    tintColor = chooseCharacterColor()
    colorize(getPicture("wizard_example.jpg"), getPicture("wizard_example_colored.jpg"), green, 200, tintColor, 2.0)
    play(voice) 
    playSong(2) #plays the theme song looped 3 times
