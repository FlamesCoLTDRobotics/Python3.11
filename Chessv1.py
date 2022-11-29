import turtle

# Create the window and its attributes
window = turtle.Screen()
window.title("Chess")
window.bgcolor("white")
 
# Create the board 
square_size = 50  # size of each square in pixels 
num_squares = 8   # number of squares per side 
border_width = 5  # width of the border around the board in pixels  

 # Draw horizontal lines on board 
turtle.hideturtle()    # hide default turtle arrow  
for i in range(num_squares):     # draw num_squares lines  

    startx, starty = -square_size * (num_squares/2), square_size * (i - num_squares/2)    # starting coordinates for line segment  

    endx, endy = square_size * (num_squares/2), square_size*(i - num_squares/2)    # ending coordinates for line segment  

    turtle.penup()      # lift pen from paper to move it without drawing a line  

    turtle.goto(startx, starty)     # move pen to starting position for line segement  

    turtle.pendown()        # put pen back on paper to draw next line segment  

turtle.goto(startx, starty)         # move pen to starting position for line segement
turtle.pendown()                # put pen back on paper to draw next line segment
turtle.goto(endx, endy)               # draw line to ending position for current line segment
                                # repeat loop until all columns are drawn on board

window.mainloop()
    turtle.goto(endx, endy)       # draw line to ending position for current line segment 

    				# repeat loop until all rows are drawn on board 

                                 	# change color and repeat loop process with columns 

turtle.color("black")             	# change color of pen to black for column lines          	                                  	                   	                    	                    	                                        	                    for i in range(num_squares):     	                        startx, starty = square_size*(i-num_squares/2), -square_size*(num
turtle.color("red")                 # change color of pen to red for column lines
turtle.penup()                  # lift pen from paper to move it without drawing a line