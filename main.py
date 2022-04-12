import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
file_data = pandas.read_csv("50_states.csv")
states = file_data["state"].to_list()
x_axis = file_data["x"].to_list()
y_axis = file_data["y"].to_list()

tom = turtle.Turtle()
tom.penup()
tom.hideturtle()
guess_states = []
while len(guess_states) < 50:
    answer_state = turtle.textinput(title=f"{len(guess_states)}/50 States Correct", prompt="What is another states").title()
    if answer_state == "Exit":
        break
    for i in range(0, len(states)):
        if answer_state == states[i] and answer_state not in guess_states:
            guess_states.append(answer_state)
            tom.goto(x_axis[i], y_axis[i])
            tom.write(arg=f"{states[i]}", align="center")

#
'''
dont_know_state = []
for state in states:
    if state not in guess_states:
        dont_know_state.append(state)

state_dont_know_library = {
    "state": dont_know_state
}

data_out = pandas.DataFrame(state_dont_know_library)
data_out.to_csv("states_to_learn.csv")
'''

dont_know_state = [state for state in states if state not in guess_states]
data_out = pandas.DataFrame(dont_know_state)
data_out.to_csv("states_to_learn.csv")

















