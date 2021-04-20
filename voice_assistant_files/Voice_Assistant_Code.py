import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

## for the introduction of the device for eg olivia here
def my_speak1(text):
    tts = gTTS(text=text,lang='en')
    filename="voice1.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    
    
## for letting the user know that the command is being processed
def my_speak2():
    text='running the command please wait'
    tts = gTTS(text=text,lang='en')
    filename2="voice2.mp3"
    try:
        tts.save(filename2)
    except :
        playsound.playsound(filename2)    

## for getting the voice input from the user and printing the command entered on the console.        
def get_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
        said=' '
        try:
            said = recognizer.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception : " + str(e))
    return said
        
my_speak1("Hello Arsh Mishra this is olivia your personal voice assistant")
print("____________________________________________Hello Arsh This Is Olivia Here!____________________________________________")
print()
while True:
   ## speak_function('What program would u like to open?')   
    print("___________________________________________What Program would you like to open?_________________________________________")
    q = get_audio()
    p=q.lower()
    if(("run" in p) or "open" in p) and (("browser" in p) or ("explorer" in p)):
       ## speak_function('Opening a Browser')
        my_speak2()
        print("Opening a Browser!")
        os.system("iexplore")
    elif(("run" in p) or ("open" in p)) and (("mediaplayer" in p) or ("songplayer" in p)):
        ##speak_function("Opening Media Player")
        my_speak2()
        print("Opening Media Player!")
        os.system("wmplayer")
    elif(("run" in p) or ("open" in p)) and (("notepad" in p)or("editor" in p)):
        ##speak_function("Opening Text Editor")
        my_speak2()
        print("Opening Text Editor! ")
        os.system("notepad")
    elif (("run" in p) or ("open" in p)) and ("calculator" in p):
        ##speak_function("Opening Calculator")
        my_speak2()
        print("Opening Calculator")
        os.system("calc")    
    elif(("run" in p) or ("open" in p))  and (("jupyter" in p)or("IDE" in p)):
        ##speak_function("Opening Jupyter IDE")
        my_speak2()
        print("Opening Jupyter IDE")
        os.system("jupyter notebook")
    elif(("run" in p) or ("open" in p))  and (("paint" in p) or ("drawing software" in p)):
        ##speak_function("Opening Paint Software")
        my_speak2()
        print("Opening Paint Software!")
        os.system("mspaint")
    elif(("run" in p) or ("open" in p))  and ("gitbash" in p):
        ##speak_function("Opening Git Bash")
        my_speak2()
        print("Opening Git Bash")
        os.system("git bash")
    elif(("run" in p) or ("open" in p))  and ("chrome" in p):
        print("Opening the Chrome Browser")
        ## speak_function("Opening the Chrome Browser")
        my_speak2()
        os.system("chrome")
    elif(("run" in p) or ("open" in p)) and ("putty" in p):
        ##speak_function("Opening Putty Software")
        my_speak2()
        print("Opening Putty Software....")
        os.system("putty")
    elif(("run" in p) or ("open" in p))  and("kubernetes" in p):
        ##  speak_function("Opening Kubernetes")
        my_speak2()
        print("Opening the Kubernetes Cluster in VM....Might Take some time.....")      
        os.system("minikube.exe start") 
    elif(("show" in p)or("listout" in p))and("directory" in p):
       ## speak_function("We are Listing all the directories")
        my_speak2()  
        print("We are Listing all the directories...")
        os.system("dir")  
    elif("clear" in p)and("screen" in p):
        my_speak2()
        os.system("cls")     
                      
    elif("exit" in p):
       ## speak_function("we are closing the program")
        print("We are closing the program!")
        print("________________________________________________________________________________________________________________________")
        os.system(exit())
        break
    
                   


