import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
# get image to use as a new shape(background)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state_name = turtle.Turtle()
state_name.penup()
state_name.hideturtle()

# Reading csv data with Pandas
data = pandas.read_csv("50_states.csv")
# May need to convert to list or dictionary to iterate and match user input.
state_list = data.state.to_list()
guessed_list = []
missing_states = []

title = "Guess the State"
while len(guessed_list) < 50:
    user_answer = screen.textinput(title=f"{len(guessed_list)}/50 States Correct", prompt="What's another state's name?").title()
    states = data[data.state == user_answer]
    x_cor = list(states.x)
    y_cor = list(states.y)

    if user_answer == "Exit":
        break
    if user_answer in guessed_list:
        print(f"{user_answer} already listed")
    elif user_answer in state_list:
        guessed_list.append(user_answer)
        state_name.goto(x_cor[0], y_cor[0])
        state_name.write(user_answer)
    else:
        print(f"{user_answer} does not exist.")

missing_states = [state for state in state_list if state not in guessed_list]

states_to_find_data = pandas.DataFrame(missing_states)
states_to_find_data.to_csv("states_to_discover.csv")

screen.exitonclick()

