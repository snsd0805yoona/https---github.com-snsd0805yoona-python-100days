from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    entry_password.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters=[random.choice(letters) for i in range(nr_letters)]
    password_symbols = [random.choice(symbols) for i in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for i in range(nr_numbers)]

    password_list=password_letters+password_numbers+password_symbols
    random.shuffle(password_list)

    password= "".join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=entry_website.get()
    user = entry_user.get()
    password = entry_password.get()

    if len(website)==0 or len(user)==0 or len(password)==0:
        messagebox.showinfo(title="error", message="You have to enter all the fields!")
    else:        
        is_ok = messagebox.askokcancel(title=website, message=f"Are you sure the following is correct?\n username:{user}\n password:{password}")

        if is_ok:
            f = open("data.txt", "a")
            f.write(f"{website} | {user} | {password}\n")
            f.close()
            entry_password.delete(0, END)
            entry_website.delete(0, END)
            entry_user.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("My Password")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image= img)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

entry_website = Entry(width=35)
entry_website.grid(column=1, row=1, columnspan=2)
entry_website.focus()

label_user = Label(text="Email/Username:")
label_user.grid(column=0, row=2)

entry_user = Entry(width=35)
entry_user.grid(column=1, row=2, columnspan=2)

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

entry_password = Entry(width=23)
entry_password.grid(column=1, row=3)

generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(column=2, row=3)

button_add = Button(text="Add", width=36, command=save)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()