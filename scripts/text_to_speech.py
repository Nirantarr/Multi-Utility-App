import pyttsx3
import tkinter as tk
from tkinter import ttk

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Text To Speech")
        self.root.geometry("500x400")

        # Set up text-to-speech engine
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')

        # Store all available voices with their IDs
        self.voice_options = {}
        for voice in self.voices:
            # Add each voice by name to the dropdown options
            self.voice_options[voice.name] = voice.id

        # Label prompting user to enter text
        self.label = tk.Label(self.root, text="Type what you want me to say!", font=('Arial', 16))
        self.label.pack(padx=10, pady=10)

        # Entry widget for text input
        self.textbox = tk.Entry(self.root, font=('Arial', 16), width=30)
        self.textbox.pack(padx=10, pady=10)
        self.textbox.focus_set()

        # Combobox for voice selection
        self.voice_var = tk.StringVar()
        self.voice_dropdown = ttk.Combobox(self.root, textvariable=self.voice_var, font=('Arial', 14), state="readonly")
        self.voice_dropdown['values'] = list(self.voice_options.keys())  # Set available voice options
        self.voice_dropdown.set("Select Voice")  # Default display text
        self.voice_dropdown.pack(padx=10, pady=10)

        # Button to trigger text-to-speech
        self.button = tk.Button(self.root, text="CLICK ME!", font=('Arial', 16), command=self.button_click)
        self.button.pack(padx=10, pady=10)

        self.root.mainloop()

    def button_click(self):
        text_to_say = self.textbox.get()
        selected_voice = self.voice_var.get()

        if text_to_say and selected_voice in self.voice_options:
            # Set the selected voice
            self.engine.setProperty('voice', self.voice_options[selected_voice])
            
            # Speak the text
            self.engine.say(text_to_say)
            self.engine.runAndWait()

GUI()