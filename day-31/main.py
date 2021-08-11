from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current = {}
to_learn={}
try:
    data = pandas.read_csv("data\words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data\words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



def next_card():
    global current, flip_timer
    window.after_cancel(flip_timer)
    current = random.choice(to_learn)
    canvas.itemconfig(card_languages, text="French", fill="black")
    canvas.itemconfig(card_word, text=current["French"], fill="black")
    canvas.itemconfig(canvas_image, image=front)
    flip_timer = window.after(ms=3000, func=flip)

def flip():
    canvas.itemconfig(canvas_image, image=back)
    canvas.itemconfig(card_languages, text="English", fill="white")
    canvas.itemconfig(card_word, text=current["English"], fill="white")
    
def is_known():
    to_learn.remove(current)
    next_card()

    data = pandas.DataFrame(to_learn)
    data.to_csv("data\words_to_learn.csv", index=False)

# #UI

window=Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(ms=3000, func=flip)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
front = PhotoImage(file="images\card_front.png")
back = PhotoImage(file="images\card_back.png")
canvas_image = canvas.create_image(400, 263, image=front)
canvas.grid(column=0, row=0, columnspan=2)

card_languages = canvas.create_text(400,150, text="French", font=("Ariel", 40, "italic"))

card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

wrong = PhotoImage(file="images\wrong.png")
button_no = Button(image=wrong, highlightthickness=0, command=next_card)
button_no.grid(column=0, row=1)

yes = PhotoImage(file="images\yes.png")
button_yes = Button(image= yes, highlightthickness=0, command=is_known)
button_yes.grid(column=1, row=1)

next_card()


window.mainloop()