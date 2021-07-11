import tkinter

window = tkinter.Tk()
window.title('My first GUI')
window.minsize(width=500, height=300)


my_label=tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"]="new text"
my_label.config(text="new text")
i=0
def click():
    global i
    i=i+1
    my_label.config(text=i)

button=tkinter.Button(text="click", command=click)
button.pack()

def click_me():
    label2=tkinter.Label(text="input text", font=("Arial", 24, "bold"))
    label2.pack()
    label2.config(text=input.get())

input = tkinter.Entry(width=10)
input.pack()
button2=tkinter.Button(text="click me", command=click_me)
button2.pack()




window.mainloop()