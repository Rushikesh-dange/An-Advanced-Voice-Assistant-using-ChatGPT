import speech_recognition as sr
import math
import time
import serial
from espeak import espeak
import sys
import openai
import pygame
from gtts import gTTS
pygame.mixer.init()

#model_to_use="text-davinci-003" # most capable
#model_to_use="text-curie-001"
#model_to_use="text-babbage-001"
model_to_use="text-ada-001" # lowest token cost
r = sr.Recognizer()
openai.api_key="Enter Your API Key"
def chatGPT(query):
	response = openai.Completion.create(
		model=model_to_use,
		prompt=query,
		temperature=0,
		max_tokens=1000
		)
	return str.strip(response['choices'][0]['text']), response['usage']['total_tokens']

def main():
    print('LED is ON while button is pressed (Ctrl-C for exit).')
    while True:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Say something!")
            audio = r.listen(source)
            print("Recognizing Now .... ")
            try:
                # using google speech recognition
                command=str(r.recognize_google(audio))
                print(command)
            except Exception as e:
                print("Error: " + str(e))
                command=""
            print("Google Speech Recognition thinks you said " + command)
            query=command
            (res, usage) = chatGPT(query)
            print(res)
            tts = gTTS(text=res, lang='en')
            tts.save("good.mp3")
            pygame.mixer.music.load("good.mp3")
            pygame.mixer.music.play()
            #espeak.synth(res)
            
                        


if __name__ == '__main__':
    main()
