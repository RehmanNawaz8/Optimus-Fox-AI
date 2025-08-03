
import speech_recognition as sr

def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f" You said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("Could not understand your voice.")
        return ""
    except sr.RequestError:
        print(" Speech recognition service failed.")
        return ""
