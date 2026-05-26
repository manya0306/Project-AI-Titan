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

    # 🔧 FIX MISHEARD WAKE WORD
    text = text.replace("title", "titan")

    print(f"You: {text}")

    # -------------------------
    # EXIT (HIGHEST PRIORITY)
    # -------------------------
    if "exit" in text:
        speak("Shutting down Titan")
        print("Titan: Shutdown")
        break

    # -------------------------
    # WAKE WORD SYSTEM
    # -------------------------
    if "titan" in text:

        command = text.replace("titan", "").strip()

        if not command:
            speak("Yes?")
            continue

        response = assistant.process_command(command)

        print(f"Titan: {response}")

        if response:
            speak(response)