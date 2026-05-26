import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty("rate", 175)


def speak(text: str):
    engine.say(text)
    engine.setProperty("volume", 1.0)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)

            audio = recognizer.listen(
                source,
                timeout=5,            # waits max 5 sec for speech
                phrase_time_limit=6   # max speech length
            )

        text = recognizer.recognize_google(audio)
        print("You:", text)
        return text.lower().strip()

    except sr.WaitTimeoutError:
        return ""

    except sr.UnknownValueError:
        return ""

    except sr.RequestError:
        return ""

    except Exception as e:
        print("Voice Error:", repr(e))
        return ""