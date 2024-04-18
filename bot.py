
import pyttsx3
import speech_recognition as sr
from PyQt5.QtCore import pyqtSignal, QThread
from freeGPT import Client


class ChatbotEngine(QThread):
    text_generated = pyqtSignal(str, str)

    def __init__(self):
        QThread.__init__(self)
        self.r = sr.Recognizer()
        self.engine = pyttsx3.init()

        self.generator = Client  

        self.listening = False

        self.free_questions = 3 

    def run(self):
        self.listening = True
        self.engine.say("Hello, My name is chintu. How can I help you? Go ahead. I'm listening.")
        self.engine.runAndWait()
        self.update()

    def stop(self):
        self.listening = False
        self.engine.stop()

    def update(self):
        if not self.listening:
            return None, None

        while self.listening:
            recognized_text = None
            generated_text = None

            with sr.Microphone() as source:
                
                self.r.adjust_for_ambient_noise(source)
            
                try:
                    audio = self.r.listen(source)
                except sr.UnknownValueError:
                    self.engine.say("I'm sorry, I didn't understand that. Come again?")
                    self.engine.runAndWait()
                    continue
                except sr.RequestError:
                    self.engine.say("Oops, I spaced out for a moment. Could you please repeat what you just said?")
                    self.engine.runAndWait()
                    continue

            try:
                text = self.r.recognize_google(audio)
                recognized_text = text 
            except sr.UnknownValueError:
                self.engine.say("I'm sorry what? Could you repeat that?")
                self.engine.runAndWait()
                continue
            except sr.RequestError:
                self.engine.say("Hang on. My brain is still catching up. Could you tell me that again?")
                self.engine.runAndWait()
                continue

        
            if text.lower() == "that's all for now, chintu":
                self.stop()
                return None, None

        
            try:
                generated_text = self.generator.create_completion("gpt4", text)
            except RuntimeError:
                self.engine.say("I don't know what to say. Could you please try again?")
                self.engine.runAndWait()
                continue


            self.engine.say(generated_text)
            self.engine.runAndWait()
        
            self.text_generated.emit(recognized_text, generated_text)


            self.free_questions -= 1
            if self.free_questions == 0:
                self.engine.say("I'm sorry, but I need to go. I have another call coming in.")
                self.engine.runAndWait()
                self.stop()
                return None, None
            if text.lower() == ", your thoughts?":
                continue
        return recognized_text, generated_text
