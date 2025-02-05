"""
U.S. States Game
An interactive game that tests knowledge of U.S. state locations.
Features:
- Uses turtle graphics for visual representation
- Tracks correct guesses and maintains score
- Saves unguessed states to a CSV file for future learning
- Implements list comprehension for state tracking
"""

import turtle
import pandas

from day_25_us_state_game import missing_states

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "day_25_blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("day_25_50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [states for states in all_states if states not in guessed_states]
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("day_25_states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
