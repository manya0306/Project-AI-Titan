# Project AI Titan

Titan is a Python-based desktop AI assistant with:

* Voice commands
* Wake-word activation (`Titan`)
* App automation
* Floating orb UI
* Speech recognition + text-to-speech
* Generic app/process management

---

# Features

## Voice Interaction

* Always-listening mode
* Wake-word support
* Google Speech Recognition
* `pyttsx3` voice responses
* Ambient noise adjustment
* Wake-word correction (`title` → `titan`)

## App Control

* Open apps
* Close running apps
* Search Google
* Time & date commands
* Fuzzy matching for commands/apps

Examples:

```text
Titan open chrome
Titan search AI
Titan what is the time
Titan close edge
```

---

# Floating Orb UI

Built using `CustomTkinter`.

Features:

* Draggable orb
* Always-on-top window
* Borderless UI
* Click to start/stop listening
* Right-click to close Titan
* Animated listening state

---

# Technologies Used

* Python
* CustomTkinter
* SpeechRecognition
* pyttsx3
* psutil

---

# Installation

```bash
git clone https://github.com/manya0306/Project-AI-Titan.git
cd Project-AI-Titan
```

Create virtual environment:

```bash
python -m venv titanvenv
```

Activate:

```bash
titanvenv\\Scripts\\activate
```

Install dependencies:

```bash
pip install customtkinter pyttsx3 SpeechRecognition pyaudio psutil
```

Run Titan:

```bash
python frontend.py
```

---

# Planned Features

* AI interpretation layer
* Offline speech recognition
* Smarter memory/context
* System tray mode
* Better animations
* Semantic understanding

---

# Status

Current Version: Titan Prototype v1
