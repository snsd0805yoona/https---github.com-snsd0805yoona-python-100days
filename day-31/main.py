from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"


#read csv


#UI

window=Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
front = PhotoImage(file="images\card_front.png")
canvas.create_image(400, 263, image=front)
canvas.grid(column=0, row=0, columnspan=2)

canvas.create_text(400,150, text="French", font=("Ariel", 40, "italic"))

canvas.create_text(400, 263, text="troure", font=("Ariel", 60, "bold"))

wrong = PhotoImage(file="images\wrong.png")
button_no = Button(image=wrong, highlightthickness=0)
button_no.grid(column=0, row=1)

yes = PhotoImage(file="images\yes.png")
button_yes = Button(image= yes, highlightthickness=0)
button_yes.grid(column=1, row=1)

window.mainloop()