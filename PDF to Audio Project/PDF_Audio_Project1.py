import PyPDF2
from gtts import gTTS

File = open('Sample PDF.pdf', 'rb')

reader = PyPDF2.PdfReader(File)

text = ''

for page in reader.pages:
    page_text = page.extract_text()
    if page_text:
        text += page_text + '\n'

speech = gTTS(text, lang = 'en', slow = False)

speech.save('Final_Output_Audio.mp3')

File.close()

print("Audio File 'Final_Output_Audio.mp3' has been Created Successfully")