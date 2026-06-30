import turtle
import pandas


def state_name_visualize(state_data):
    new_turtle = turtle.Turtle()
    new_turtle.hideturtle()
    new_turtle.penup()
    new_turtle.goto(int(state_data.x), int(state_data.y))
    new_turtle.write(answer_state)


screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

my_turtles = []

data = pandas.read_csv("50_states.csv")

states_list = data.state.to_list()

correctly_guessed_states = []

while len(correctly_guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(correctly_guessed_states)}/{len(states_list)} states correct.", prompt="Guess another state!").title()
    if answer_state == "Exit":
        missed_states = [state for state in states_list if state not in correctly_guessed_states]
        # for states in states_list:
        #     if states not in correctly_guessed_states:
        #         missed_states.append(states)
        data_dict = {
            "All_states": [states_list],
            "Correct_states": [correctly_guessed_states],
            "Missed_states": [missed_states]
        }
        data_to_create_csv = pandas.DataFrame(data_dict)
        data_to_create_csv.to_csv("Result.csv")
        break
    if answer_state in states_list:
        correctly_guessed_states.append(answer_state)
        guessed_state_data = data[data.state == answer_state]
        state_name_visualize(guessed_state_data)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()