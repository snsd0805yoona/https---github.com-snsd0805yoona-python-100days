from tkinter import *
from tkinter import messagebox, font
import random
import pyperclip
import json

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

    data_dict = {
        website:
        {
            "email": user,
            "password": password,
        }
    }

    if len(website)==0 or len(user)==0 or len(password)==0:
        messagebox.showinfo(title="error", message="You have to enter all the fields!")
    else:
        try:        
            with open("data.json", "r") as f:
                data = json.load(f)
                
        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(data_dict, f, indent=4)
        else:        
            data.update(data_dict)
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)
        finally:
            entry_password.delete(0, END)
            entry_website.delete(0, END)


def search():
    website = entry_website.get()

    try:
        with open("data.json", "r") as f:
            data = json.load(f)
            
    except FileNotFoundError:
        messagebox.showinfo(title="File Not Found!", message="You haven't create the file yet!")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="Your password", message=f"Below is your password:\n Website: {website} \n Email: {email} \n Password: {password}")
        else:
            messagebox.showinfo(title="Website Not Found!", message=f"{website} is not found in the file!")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("我的密碼管理")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image= img)
canvas.grid(column=1, row=0)

label_website = Label(text="網站:")
label_website.grid(column=0, row=1)

entry_website = Entry(width=26)
entry_website.grid(column=1, row=1)
entry_website.focus()

label_user = Label(text="Email/使用者名稱:")
label_user.grid(column=0, row=2)

entry_user = Entry(width=42)
entry_user.grid(column=1, row=2, columnspan=2)

label_password = Label(text="密碼:")
label_password.grid(column=0, row=3)

entry_password = Entry(width=26)
entry_password.grid(column=1, row=3)

generate_password = Button(text="產生密碼", command=generate_password, width=15)
generate_password.grid(column=2, row=3)

button_add = Button(text="新增", width=43, command=save)
button_add.grid(column=1, row=4, columnspan=2)

Search = Button(text="搜尋", command=search, width=15)
Search.grid(column=2, row=1)

window.mainloop()