from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty, NumericProperty, BooleanProperty
import random
import speech_recognition as sr
import pyttsx3


r = sr.Recognizer()
mic = sr.Microphone()
text_speech = pyttsx3.init()
class SubmitPageScreen(Screen):
    # def on_enter(self):
    #     Clock.schedule_once(MainApp().RecordVoice())
    pass
    
class WindowManager(ScreenManager):
    pass
class MainApp(App):
    display_message = StringProperty()
    answer = NumericProperty(0)
    check_answer = BooleanProperty(False)

    def RecordVoice(self):
        with mic as source:
            # print("Wait...")
            # r.adjust_for_ambient_noise(source, duration = 1)
            print ("Start: ")
            audio = r.listen(source)
            try:
                voiceToText = r.recognize_google(audio)
                print(voiceToText)
                inputVal = int(voiceToText)
                print(voiceToText)
                if (inputVal == self.answer):
                    self.check_answer = True
            except:
                print(":(")
            # if self.check_answer:
            #     WindowManager().current = "success"
            # else: 
            #     WindowManager().current = "failure"

    def MathOpera(self, symbol):
        parameter_a, parameter_b, answer = 1,1,1
        if (symbol == "+" or symbol == "-"):
            parameter_a, parameter_b = random.randint(0,20), random.randint(0,20)
            answer = parameter_a + parameter_b
        elif (symbol == "*" or symbol == "/"):
            parameter_a, parameter_b = random.randint(1,10), random.randint(1,10)
            answer = parameter_a * parameter_b
        return parameter_a, parameter_b, answer

    def PlayGame(self, mode, mixing = False):
        self.check_answer = False
        if (mode == "Add"):
            parameter_a, parameter_b, self.answer = self.MathOpera("+")
            self.display_message = f"{parameter_a} + {parameter_b} = "
            text_speech.say(parameter_a)
            text_speech.say("plus")
            text_speech.say(parameter_b)
            text_speech.runAndWait() 
        elif (mode == "Subtract"):
            parameter_b, self.answer, parameter_a = self.MathOpera("-")
            self.display_message =f"{parameter_a} - {parameter_b} = "
            text_speech.say(parameter_a)
            text_speech.say("minus")
            text_speech.say(parameter_b)
            text_speech.runAndWait() 
        elif (mode == "Multiply"):
            parameter_a, parameter_b, self.answer = self.MathOpera("*")
            self.display_message =f"{parameter_a} x {parameter_b} = "
            text_speech.say(parameter_a)
            text_speech.say("multiplied by")
            text_speech.say(parameter_b)
            text_speech.runAndWait() 
        elif (mode == "Divide"):
            parameter_b, self.answer, parameter_a = self.MathOpera("/")
            self.display_message =f"{parameter_a} / {parameter_b} = "
            text_speech.say(parameter_a)
            text_speech.say("divided by")
            text_speech.say(parameter_b)
            text_speech.runAndWait() 
        elif (mode == "Mix"):
            rand_select = random.randint(0, 3)
            rand_list = ["Add", "Subtract", "Multiply", "Divide"]
            self.PlayGame(rand_list[rand_select], mixing)



MainApp().run()
