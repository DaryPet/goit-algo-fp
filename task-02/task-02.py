import turtle
import math

# drawing tree
def draw_pythagoras_tree (branch_length, level, t):
    if level == 0:
        return
    
    # drawing main branch
    t.forward(branch_length)

    # saving current pposition and angle
    current_position = t.position()
    current_heading = t.heading()

    # draw right angle
    t.left(45)
    draw_pythagoras_tree(branch_length * math.sqrt(2) / 2, level - 1, t)

    # return to previous posirion and angle
    t.setposition(current_position)
    t.setheading(current_heading)

    # draw left angle
    t.right(45)
    draw_pythagoras_tree(branch_length * math.sqrt(2) / 2, level -1, t)

    # return to beggining
    t.setposition(current_position)
    t.setheading(current_heading)
    t.backward(branch_length)

# executing code
if __name__ == "__main__":
    # ask user for recursion level
    level = int(input("Enter recursion level for pythagoras tree:"))
    # turtle settings
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.title("Pythagoras Tree")

    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    t.penup()
    t.goto(0, -300)
    t.pendown()

    # drawing tree
    draw_pythagoras_tree(200, level, t)
    # ending
    screen.mainloop()





