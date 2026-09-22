# 🇫🇷 French Flash Card

A simple **French-English flashcard application** built with Python, Tkinter, and Pandas.

The application displays random French words and automatically flips each card after 3 seconds to reveal the English translation.

This project was created as part of my Python learning journey through the **100 Days of Code: The Complete Python Pro Bootcamp by Angela Yu**.

## ✨ Features

* 🇫🇷 Displays random French words
* 🇬🇧 Automatically reveals the English translation after 3 seconds
* ❌ Skip words you don't know
* ✅ Mark words you already know
* 💾 Saves learning progress to a CSV file
* 🔄 Loads previous progress when the application is restarted
* 🎴 Interactive graphical interface built with Tkinter

## 🛠️ Technologies Used

* Python
* Tkinter
* Pandas
* CSV files

## 📂 Project Structure

```text
French-Flash-Card/
│
├── main.py
│
├── data/
│   ├── french_words.csv
│   └── words_to_learn.csv
│
├── images/
│   ├── card_front.png
│   ├── card_back.png
│   ├── right.png
│   └── wrong.png
│
└── README.md
```

`words_to_learn.csv` is created/updated as the user marks words as known.

## 🚀 How It Works

When the application starts, it loads the words that still need to be learned.

A French word is displayed on the front of the flash card. After 3 seconds, the card flips and shows its English translation.

Press:

* ❌ if you still need to learn the word.
* ✅ if you know the word.

When a word is marked as known, it is removed from the learning list and the remaining words are saved.

## ▶️ Running the Project

Make sure Python is installed and install Pandas:

```bash
pip install pandas
```

Then run:

```bash
python main.py
```

## 📚 What I Practised

Through this project, I practised:

* Building graphical interfaces with Tkinter
* Working with Canvas widgets
* Using functions and callbacks
* Working with dictionaries and lists
* Reading and writing CSV files with Pandas
* Handling files with `try` / `except`
* Using `window.after()` for timed events
* Managing application state
* Saving user progress between sessions

## 🎯 Learning Project

This is a learning project created while completing **Day 31 of the 100 Days of Code Python course**.

The goal of the project was to practice combining Python fundamentals, Pandas, file handling, and Tkinter into a complete desktop application.
