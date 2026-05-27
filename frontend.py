import customtkinter as ctk
import threading
import time 

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
app.attributes("-topmost", True)

app.overrideredirect(True)

app.configure(fg_color="black")

app.geometry("100x100")
app.title("Titan")
app.resizable(False, False)


# -------------------------
# STATE
# -------------------------

listening = False
animating = False

def close_app(event=None):
    app.destroy()

def start_move(event):
    app.x = event.x
    app.y = event.y


def do_move(event):
    x = app.winfo_x() + event.x - app.x
    y = app.winfo_y() + event.y - app.y

    app.geometry(f"+{x}+{y}")

def orb_animation():
    global animating

    grow = True

    while animating:

        try:

            if grow:
                orb_button.configure(
                    width=130,
                    height=130,
                    fg_color="#00cfff"
                )
            else:
                orb_button.configure(
                    width=120,
                    height=120,
                    fg_color="#2563eb"
                )

            grow = not grow

            time.sleep(0.5)

        except:
            break


# -------------------------
# LISTENING LOOP
# -------------------------


def titan_loop():
    global listening

    while listening:

        text = listen()

        if not text:
            continue

        print(f"You: {text}")

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
    print("Listening...")

    global listening

    listening = True

    global animating
    animating = True

    threading.Thread(target=orb_animation, daemon=True).start()

    orb_button.configure(
        fg_color="#00c853",
        hover_color="#00e676"
    )

    threading.Thread(target=titan_loop, daemon=True).start()



def stop_listening():
    global listening

    listening = False
    global animating
    animating = False

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

orb_button.bind("<Button-1>", start_move)
orb_button.bind("<B1-Motion>", do_move)

orb_button.bind("<Button-3>", close_app)
# -------------------------
# RUN APP
# -------------------------

app.mainloop()