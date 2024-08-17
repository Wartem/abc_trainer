![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Click](https://img.shields.io/badge/Click-4A4A55?style=flat&logo=python&logoColor=white)
![gTTS](https://img.shields.io/badge/gTTS-FF9900?style=flat&logo=google&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-00A86B?style=flat&logo=python&logoColor=white)
![PySide6](https://img.shields.io/badge/PySide6-41CD52?style=flat&logo=qt&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-2C8EBB?style=flat&logo=python&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-11557C?style=flat&logo=python&logoColor=white)

# ABC_Trainer

ABC_Trainer is a specialized program designed to help users learn the letters of the alphabet through interactive exercises. The program features a clean and simple design, ensuring a distraction-free learning environment. The goal of each exercise is to press the correct keys (A-Z) on your keyboard.

## Features

### Interactive Exercises
ABC_Trainer offers four distinct exercises to enhance your learning experience:
- **Mixed**: Type letters in the alphabet (A-Z) unordered.
- **A-Z**: Type all letters (A-Z) in alphabetical order.
- **Words**: Type words.
- **Unique**: Find the unique letter that occurs only once and type it.

### Launching an Exercise
Start an exercise by clicking one of the four buttons on the main menu.

### Window Resize
Adjust the window size by changing the width and height in the settings or by dragging the window edges. A full-screen option is also available.

### Exit an Exercise
Exit an exercise by pressing the "Esc" key or clicking the arrow in the upper left corner. Alternatively, close the window by clicking the "X" button.

### Customizable Settings
Access the settings menu via 'File' in the menu bar to adjust audio volume, letter case, language, and color scheme. Save changes by clicking OK.

### Text-to-Speech Instructions
Instructions and feedback are provided via Text-to-Speech. An internet connection is required for downloading TTS audio. The program supports English and Swedish, among other languages.

### Python-Powered
The program is built using Python, with PySide6 for the menu and PyGame for the exercises. User input is handled via keyboard and mouse.

## Tips and Tricks
- Access and customize the word list for the Words exercise via the "Open" option under "File".
- Add more fonts by placing them in the fonts folder (must be in .ttf format).

### Advanced Customization
Modify text and instructions by editing the .json files in the settings folder. For example, change the "Take" instruction in "instructions.json" from "Good! Press," to "Good! Type,".

## Code Authorship Declaration

This project primarily consists of code written by me (Wartem). However, certain sections may have been generated or refactored with the assistance of AI tools.

## Installation

1. Clone the repository:
   ```bash
   git clone git clone https://github.com/Wartem/abc_trainer.git

## Release with .exe (Windows): https://wartem.itch.io/abc-trainer
