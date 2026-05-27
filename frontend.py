import customtkinter as ctk
import threading

from titan.core.voice import listen, speak
from titan.core.assistant import TitanAssistant


# -------------------------
# TITAN BACKEND
# -------------------------

assistant = TitanAssistant()


# -------------------------
# APP WINDOW
# -------------------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.geometry("220x220")
app.title("Titan")
app.resizable(False, False)


# -------------------------
# STATE
# -------------------------

listening = False


# -------------------------
# LISTENING LOOP
# -------------------------


def titan_loop():
    global listening

    while listening:

        text = listen()

        if not text:
            continue

        text = text.lower().strip()

        # Fix misheard wake word
        text = text.replace("title", "titan")

        print(f"You: {text}")

        # EXIT
        if "exit" in text:
            speak("Shutting down Titan")
            stop_listening()
            break

        # WAKE WORD
        if "titan" in text:

            command = text.replace("titan", "").strip()

            if not command:
                speak("Yes?")
                continue

            response = assistant.process_command(command)

            print(f"Titan: {response}")

            if response:
                speak(response)


# -------------------------
# BUTTON TOGGLE
# -------------------------


def start_listening():
    global listening

    listening = True

    orb_button.configure(
        fg_color="#00c853",
        hover_color="#00e676"
    )

    threading.Thread(target=titan_loop, daemon=True).start()



def stop_listening():
    global listening

    listening = False

    orb_button.configure(
        fg_color="#2563eb",
        hover_color="#3b82f6"
    )



def toggle_listening():
    global listening

    if listening:
        stop_listening()
    else:
        start_listening()


# -------------------------
# TITAN ORB BUTTON
# -------------------------

orb_button = ctk.CTkButton(
    app,
    text="",
    width=120,
    height=120,
    corner_radius=60,
    fg_color="#2563eb",
    hover_color="#3b82f6",
    command=toggle_listening
)

orb_button.place(relx=0.5, rely=0.5, anchor="center")


# -------------------------
# RUN APP
# -------------------------

app.mainloop()