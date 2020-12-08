import PyPDF2
import pyttsx3
engine = pyttsx3.init()

""" RATE"""
#rate = engine.getProperty('rate')   # getting details of current speaking rate
#print("old rate: ",engine.getProperty('rate'))                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate
#print("new rate: ",engine.getProperty('rate')) 

"""VOLUME"""
#volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
#print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[2].id)   #changing index, changes voices. 1 for female


 
file_name = ''#enter_file_name

a = PyPDF2.PdfFileReader(file_name)
pg = a.numPages
text = a.getPage(67).extractText().encode('utf-8').replace(b'\n',b'')

for s in (b'\f', b'\n', b'\r', b'\t', b'\v'):
    text = text.replace(s, b'')

text = text.decode('utf-8')

print(pg)
print(text)

engine.say('hello there') #replacewith-text
engine.runAndWait()