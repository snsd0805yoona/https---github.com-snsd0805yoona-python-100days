from random import setstate
from tkinter import *
from quiz_brain import QuizBrain
import time
THEME_COLOR = "#375362"


class QInterface: 

    def __init__(self, quizbrain: QuizBrain) -> None:
        self.quiz = quizbrain
        self.window = Tk()
        true = PhotoImage(file="images/true.png")
        false = PhotoImage(file="images/false.png")
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(text="Score: 0", foreground="white", bg=THEME_COLOR, font=("Arial", 15, "italic"))
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.quiz_text = self.canvas.create_text(
            150,125,text="Some Question text", fill=THEME_COLOR, font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        
        self.true_button = Button(image=true, command=self.check_true)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=false, command=self.check_false)
        self.false_button.grid(column=1, row=2)
        
        self.get_next_question()
        
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.quiz_text, text="You reach the end of the question!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_true(self):
        answer = self.quiz.check_answer("true")
        self.feedback(answer)

    def check_false(self):
        answer = self.quiz.check_answer("false")
        self.feedback(answer)

    def feedback(self, answer):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,func=self.get_next_question)
        