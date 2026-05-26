from titan.core.assistant import TitanAssistant
from titan.core.voice import listen, speak


assistant = TitanAssistant()

print("Titan Always-On Mode Activated")
print("Say 'Titan' or 'exit' to control it.\n")


while True:

    text = listen()

    if not text:
        continue

    text = text.lower().strip()

    print(f"You: {text}")

    # EXIT ALWAYS WORKS
    if "exit" in text:
        speak("Shutting down Titan")
        print("Titan: Shutdown")
        break

    # WAKE WORD OPTIONAL COMMAND MODE
    command = text

    if "titan" in text:
        command = text.replace("titan", "").strip()

        if not command:
            speak("Yes?")
            continue

    else:
        # if no wake word, ignore OR optionally allow direct mode
        continue

    response = assistant.process_command(command)

    print(f"Titan: {response}")

    if response:
        speak(str(response))