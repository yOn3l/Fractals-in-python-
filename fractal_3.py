# import turtle 
import turtle 
  
# 
stars = turtle.Turtle() 
  
 
stars.speed(10) 

stars.getscreen().bgcolor("black") 

stars.color("red") 

stars.penup() 
  
stars.goto((-200, 50)) 
  
stars.pendown() 
  
# function to draw stars 
def star(turtle, size): 
    if size <= 10: 
        return
    else: 
        for i in range(5): 
            
           
            turtle.forward(size)

            star(turtle, size/3) 
  
           
            turtle.left(216) 
  

star(stars, 360) 

turtle.done()