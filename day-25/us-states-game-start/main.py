import turtle
import pandas
screen = turtle.Screen()
guessed_states = []
count = 0

image ="blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)




while len(guessed_states)<50:

    answer_state = screen.textinput(title="Guess the state", prompt="What's another state name?").title()

    df = pandas.read_csv("50_states.csv")
    all_states = df.state.to_list()

    if answer_state=="Exit":
        missing_states=[]
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)

        new_csv = pandas.DataFrame(missing_states)
        new_csv.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.pu()
        data = df[df.state == answer_state]
        t.goto(int(data.x), int(data.y))
        t.write(answer_state)
        count = count+1
        screen.title(f"{count}/52 U.S. States Game")


