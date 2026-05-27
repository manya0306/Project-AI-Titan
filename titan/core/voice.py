import pyttsx3
import speech_recognition as sr

# -------------------------
# TTS ENGINE (REINIT EACH TIME)
# -------------------------

def speak(text: str):
    if not text:
        return

    try:
        engine = pyttsx3.init()   # fresh engine every time
        engine.setProperty("rate", 175)

        engine.say(str(text))
        engine.runAndWait()

        del engine

    except Exception as e:
        print("Speech Error:", repr(e))


# -------------------------
# SPEECH TO TEXT
# -------------------------

recognizer = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    recognizer.adjust_for_ambient_noise(source, duration=0.5)


def listen():
    try:
        with mic as source:

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=6
            )

        text = recognizer.recognize_google(audio)
        text = text.replace("title", "titan")
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