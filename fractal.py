import turtle
monda = 5
def build_tree(t, branch_length, acortar, anguloxd):
  if branch_length > monda:
    
    t.forward(branch_length)

    nueva_lon = branch_length - acortar

    t.left(anguloxd)
    build_tree(t, nueva_lon, acortar, anguloxd)

    t.right(anguloxd * 2)
    build_tree(t, nueva_lon, acortar, anguloxd)

    t.left(anguloxd)

    t.backward(branch_length)
tree = turtle.Turtle()

tree.hideturtle()

tree.setheading(90)

tree.color('purple')

build_tree(tree, 50, 5, 30)

turtle.mainloop()