from Internal.framework import *
from Internal.functions import *

Instance = Interface()

def listen():
    Talokan = 1
    while True:
        try:
            Instance.VoiceCommand()
            ResponseOutput, intent_class = Instance.send_audio()
            DoFunction(intent_class)
            tts(ResponseOutput)
        except Exception as e:
            print(f"Error: {e}")

def text():
    Talokan = 2
    while True:
        try:
            Text = input("You: ")
            Instance.send(Text)
            ResponseJson = loadconfig("./local_memory/current_class.json")
            ResponseOutput, intent_class = ResponseJson.get("response"), ResponseJson.get("intent_class")
            DoFunction(intent_class)
            tts(ResponseOutput)
        except Exception as e:
            print(f"Error: {e}")

text()