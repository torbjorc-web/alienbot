import tkinter as tk
from tkinter import scrolledtext
import re
import random

class AlienBot:
    def __init__(self):
        self.alienbabble = {
            'describe_planet_intent': r'(can you tell me about your planet|i am interested in your planet)',
            'answer_why_intent': r'(why are you here|why are you asking me so many questions)',
            'cubed_intent': r'(can you cube the number (\d+))'
        }

    def match_reply(self, reply):
        for intent, regex_pattern in self.alienbabble.items():
            found_match = re.match(regex_pattern, reply.lower())

            if found_match and intent == 'describe_planet_intent':
                return self.describe_planet_intent()
            elif found_match and intent == 'answer_why_intent':
                return self.answer_why_intent()
            elif found_match and intent == 'cubed_intent':
                return self.cubed_intent(found_match.group(1))

        return self.no_match_intent()

    def describe_planet_intent(self):
        responses = (
            "My planet is a utopia of diverse organisms and species.",
            "I am from Opidipus, the capital of the Wayward Galaxies."
        )
        return random.choice(responses)

    def answer_why_intent(self):
        responses = (
            "I come in peace.",
            "I am here to collect data on your planet and its inhabitants.",
            "I heard the coffee is good."
        )
        return random.choice(responses)

    def cubed_intent(self, number):
        number = int(number)
        cubed_number = number * number * number
        return f"The cube of {number} is {cubed_number}. Isn't that cool?"

    def no_match_intent(self):
        responses = (
            "Please tell me more.",
            "Tell me more!",
            "Why do you say that?",
            "I see. Can you elaborate?"
        )
        return random.choice(responses)

bot = AlienBot()

root = tk.Tk()
root.title("AlienBot")

chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
chat_area.pack(padx=10, pady=10)
chat_area.config(state="disabled")

entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=(0, 10))

def send_message():
    user_text = entry.get().strip()
    if not user_text:
        return

    chat_area.config(state="normal")
    chat_area.insert(tk.END, f"You: {user_text}\n")
    response = bot.match_reply(user_text)
    chat_area.insert(tk.END, f"AlienBot: {response}\n\n")
    chat_area.config(state="disabled")
    entry.delete(0, tk.END)

button = tk.Button(root, text="Send", command=send_message)
button.pack(pady=(0, 10))

root.mainloop()
