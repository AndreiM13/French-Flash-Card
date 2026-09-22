from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"


# -------------------- LOAD DATA -------------------- #

try:
    data = pd.read_csv("data/words_to_learn.csv")

except (FileNotFoundError, pd.errors.EmptyDataError):
    data = pd.read_csv("data/french_words.csv")

data_to_use = data.to_dict(orient="records")

current_card = {}
flip_timer = None


# -------------------- NEW CARD -------------------- #

def words_peacker_french():
    global current_card, flip_timer

    # Stop the previous timer
    if flip_timer is not None:
        window.after_cancel(flip_timer)

    # Check that there are still words available
    if len(data_to_use) == 0:
        canvas.itemconfig(canvas_image, image=card_front)
        canvas.itemconfig(
            word_title,
            text="Congratulations!",
            fill="black"
        )
        canvas.itemconfig(
            word_text,
            text="You learned all the words!",
            fill="black",
            font=(FONT_NAME, 30, "bold")
        )
        return

    # Pick a random card
    current_card = random.choice(data_to_use)

    # Reset card to front
    canvas.itemconfig(canvas_image, image=card_front)

    canvas.itemconfig(
        word_title,
        text="French",
        fill="black"
    )

    canvas.itemconfig(
        word_text,
        text=current_card["French"],
        fill="black",
        font=(FONT_NAME, 60, "bold")
    )

    # Flip after 3 seconds
    flip_timer = window.after(3000, flip_card)


# -------------------- FLIP CARD -------------------- #

def flip_card():
    canvas.itemconfig(
        canvas_image,
        image=card_back
    )

    canvas.itemconfig(
        word_title,
        text="English",
        fill="white"
    )

    canvas.itemconfig(
        word_text,
        text=current_card["English"],
        fill="white"
    )


# -------------------- KNOWN WORD -------------------- #

def knowledge_check():

    # Make sure there is a current card
    if current_card in data_to_use:

        # Remove the known word
        data_to_use.remove(current_card)

        # Save remaining words
        data = pd.DataFrame(
            data_to_use,
            columns=["French", "English"]
        )

        data.to_csv(
            "data/words_to_learn.csv",
            index=False
        )

    # Show next card
    words_peacker_french()


# -------------------- WINDOW -------------------- #

window = Tk()

window.title("Flash Card")

window.config(
    padx=50,
    pady=50,
    bg=BACKGROUND_COLOR
)


# -------------------- CANVAS -------------------- #

canvas = Canvas(
    width=800,
    height=526
)

card_front = PhotoImage(
    file="images/card_front.png"
)

card_back = PhotoImage(
    file="images/card_back.png"
)

canvas_image = canvas.create_image(
    400,
    263,
    image=card_front
)

word_title = canvas.create_text(
    400,
    150,
    text="French",
    font=(FONT_NAME, 40, "italic")
)

word_text = canvas.create_text(
    400,
    263,
    text="word",
    font=(FONT_NAME, 60, "bold")
)

canvas.config(
    bg=BACKGROUND_COLOR,
    highlightthickness=0
)

canvas.grid(
    row=0,
    column=0,
    columnspan=2
)


# -------------------- WRONG BUTTON ❌ -------------------- #

wrong_image = PhotoImage(
    file="images/wrong.png"
)

unknown_button = Button(
    image=wrong_image,
    highlightthickness=0,
    command=words_peacker_french
)

unknown_button.grid(
    row=1,
    column=0
)


# -------------------- RIGHT BUTTON ✅ -------------------- #

right_image = PhotoImage(
    file="images/right.png"
)

check_button = Button(
    image=right_image,
    highlightthickness=0,
    command=knowledge_check
)

check_button.grid(
    row=1,
    column=1
)


# -------------------- START -------------------- #

words_peacker_french()

window.mainloop()