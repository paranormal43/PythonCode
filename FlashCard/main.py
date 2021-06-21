from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"


# --------------------------- Read File -------------------------------#

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")

def next_card():
    current_word = random.choice(to_learn)
    canvas.itemconfig(cn_text_country, text="French")
    canvas.itemconfig(cn_text_word, text=current_word["French"])

# --------------------------- UI SETUP ---------------------------------#
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800,bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file='images/card_front.png')
canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

# Canvas Text
cn_text_country = canvas.create_text(400, 150, text="Country", font=("Ariel", 40, "italic"))
cn_text_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

# Button
img_know = PhotoImage(file="images/right.png")
bt_known = Button(image=img_know, highlightthickness=0, command= next_card)
bt_known.grid(column=1, row=1)

img_unknown = PhotoImage(file="images/wrong.png")
bt_unknown = Button(image=img_unknown, highlightthickness=0, command= next_card)
bt_unknown.grid(column=0, row=1)





window.mainloop()
