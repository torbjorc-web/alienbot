# AlienBot

AlienBot is a simple rule-based chatbot built in Python. It simulates a conversation with an alien by matching user input to predefined intents using regular expressions.

## Features

- Greets the user and asks for their name.
- Handles exit commands like `quit`, `bye`, and `exit`.
- Matches user input to different intents.
- Responds with randomized replies for:
  - describing the alien’s planet
  - explaining why the alien is visiting Earth
  - cubing a number
  - general fallback replies when no intent matches

## How It Works

AlienBot uses:
- `re` for regular expression matching
- `random` for choosing random responses
- class methods to separate chatbot behavior into small parts

### Intents

- `describe_planet_intent`
- `answer_why_intent`
- `cubed_intent`
- `no_match_intent`

## Requirements

- Python 3

## How to Run

1. Save the chatbot code in a file called `script.py`.
2. Open a terminal in the same folder.
3. Run:

```bash
python3 script.py
```

## Example Conversation

```text
Hello there, what's your name? Codecademy
Hi Codecademy, I'm Etcetera. I'm not from this planet. Will you help me learn about your planet? yes
What do you consume for sustenance? tell me about your planet
My planet is a utopia of diverse organisms and species.
```

## Notes

This is a rule-based chatbot, so it only understands inputs that match the patterns defined in the code. It can be extended by adding more intents and regular expressions.

## Author

Created as a learning project for building a basic NLP chatbot in Python.
