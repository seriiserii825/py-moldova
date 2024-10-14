import turtle
import pandas
from myVersion import myVersion

# myVersion()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "states.gif"
screen.setup(width=725, height=491, startx=20, starty=20)
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?")
    if answer_state is None:
        break
    if answer_state == 'exit':
        break

    answer_state = answer_state.title()
    #print(f"answer_state: {answer_state}")

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# states to learn
states_to_learn = [state for state in all_states if state not in guessed_states]
print(f"states_to_learn: {states_to_learn}")

new_data = pandas.DataFrame(states_to_learn)
new_data.to_csv("states_to_learn.csv")

# turtle.mainloop()
