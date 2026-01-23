"""
Lab 3: Draw some basic shapes with Turtle Graphics, using loop algorithms.

Complete exercise 1-2 (each values 50 points, 100 points in total).

Author:  <Kirti>
Due Date: This Friday (Jan. 23) 5:00pm.
    
"""

import turtle
drawing_screen = turtle.Screen()

"""
Understanding the following three examples is beneficial for you to move to the exercise 1 below.
"""

# Example 1 - Draw 10 steps with each step 20 pixels by 20 pixels.

num_steps = 10
alex = turtle.Turtle()
alex.speed(5) 
alex.color("pink")
alex.pensize(7)                                      # 1 sets the drawing speed as the slowest.
for _ in range(num_steps):                          # _ means this loop variable is unused, just repeat loop body num_steps times. we can use _ or i interchangeably 
    alex.forward(20)                                # 20 pixels is the step length 
    alex.left(90)                                   # Angle is 90 degree 
    alex.forward(20)
    alex.right(90)
alex.shape("blank")                                 # After drawing, make the alex/pen/brush invisible.
                                                    # There are various types of atrributes of turtle shapes like circle, square, triangle, arrow, turtle and blank. 


#Example 2 - Draw an equilateral triangle with side length 100 pixels
#Uncomment the line 33 to 41

alex.clear()                                        # This is used to Clear the previous drawing on the screen. In this case it is clearing the stairs. 
alex.speed(1)
alex.color("pink")
alex.pensize(7)
alex.shape("circle")                                # Here always remember attribute shape of object turtle is alwasy in small letters. 
side_of_triangle = 100                              # Here instead of typing forward and left/right multiple times. we are defining the variable side_length to store the ltngth of each side of triangle. 
angle_of_triangle = 360 / 3                         # Calculate the angle of an equilateral triangle. we can also use 120 degree instead as well. 
for i in range(3):
    alex.forward(side_of_triangle)
    alex.left(angle_of_triangle)
alex.shape("blank")


# Example 3 - Draw a sqaure with side length 200 pixels
# Uncomment the line 47 to 57

alex.clear()                                        # Clear the previous drawing on the screen.
alex.shape("square")
alex.color("pink")
alex.pensize(7)
alex.up()                                           # alex.up() lifts alex/pen/brush up;
alex.goto(0, 0)                                     # Go to the center of the drawing screen
alex.down()                                         # alex.down() means putting alex/pen/brush down, ready for drawing.
length_of_square = 100
exterior_angle = 360 / 4                            # Calculate the exterior angle of an square.
for _ in range(4):
    alex.forward(length_of_square)
    alex.left(exterior_angle)
alex.shape("blank")


'''
Exercise 1 - To draw a regular hexagon:

You may have noticed that to draw a square is very similar 
to draw an equilateral triangle. We need to calculate 
the exterior angle of a square, which is the angle your turtle/pen/brush
will turn.

Now, similar as example 2 and 3, 
but draw a regular hexagon (6 sides) with side length 100.

Hint:
num_sides = 6
exterior_angle = 360 / num_sides
'''

# Code your exe 1 here

alex.clear()                                         # Clearing the previous turtle object called alex 
hexagon = turtle.Turtle()                            # Creating the new turtle named hexagon for hexagon exercise 
hexagon.clear()
hexagon.speed(1)
hexagon.width(3)
hexagon.color("green")                               # Setting the atribute color,shape,fillcolor of hexagon turtle object 
hexagon.shape("triangle")
hexagon.fillcolor("yellow")
hexagon.begin_fill()
side_of_hexagon = 100
exterior_angle_of_hexagon = 360 / 6 
for i in range(6):
    hexagon.forward(side_of_hexagon)
    hexagon.left(exterior_angle_of_hexagon)
hexagon.shape("blank")
hexagon.end_fill()                                   # Ending the fill color of hexagon turtle object 


"""
Part 2

Understanding the following examples 4 and 5 is beneficial for you to move to the exercise 2 below.
"""

'''
Example 4 - Review lab2 last exercise
Uncomment the code below in this example, run the file and see the output 
This example clearly demonstrates accessing list elements by index.
'''
day_today = 3
days_trip = 5
day_back = (day_today + days_trip) % 7
days_week = ["Monday", "Tuesday", "Wednesday","Thursday", "Friday", "Saturday", "Sunday"]
print(f'''
Your trip starts on day {day_today},({days_week[day_today]}),lasts days {days_trip}. 
You are back on day {day_back} ({days_week[day_back]}).
''')


'''
Example 5 - Draw a number of concentric circles
Uncomment the code below in this example, run the file and see the output 
This example clearly demonstrates accessing list elements by loop variables.
'''

hexagon.clear()                                                                            # Clearing the previous drawing i.e hexagon 

number_of_circles = 7                                                                      # This is how many circle i want 
colors_of_circle = ["violet", "indigo", "blue","green", "yellow", "orange", "red"]         # This is the color of seven different circle 
radius = 50                                                                                # This is the radius of first circle 
radius_increase = 10                                                                       # Circle No. 2,3,4,5,6,7 are going to increase by unit 10  

circle = turtle.Turtle()                                                                   # Created neqw turtle object named circle                                                               
circle.pensize(5)
circle.speed(5)
circle.up()
for colors_of_circle in colors_of_circle:
    circle.color(colors_of_circle)
    circle.goto(0, -radius)
    circle.down()
    circle.circle(radius)
    radius = radius + radius_increase
    circle.up()
circle.shape("blank")


'''
Exercise 2 - To draw a rainbow (like this one https://elearn.capu.ca/mod/assign/view.php?id=3237843):
You can set your own initial radius and increment value.

Hint: You may need to use the functions below:
alex.circle(-radius, 180)
alex.backward()
'''

# Code your exe 2 here

circle.clear()                                                                                 # Clearing the previous drawing i.e concentric circles 

rainbow = turtle.Turtle()                                                                      # Created New turtle object names Rainbow cause i am making rainbow 
rainbow.pensize(12)
rainbow.speed(5)
rainbow.shape("circle")
color_of_rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
radius_of_rainbow = 150                                                                       # First variable is radius of rainbow i.e 150 and will increase after every semi circle by 10 
increase_in_rainbow = 10
rainbow.setheading(90)                                                                        # Forcing the turtle to face upward so i can start making first semi circle with color red 
for color_of_rainbow in color_of_rainbow : 
    rainbow.color(color_of_rainbow)
    rainbow.circle(radius_of_rainbow, 180)                                                    # Making semi circle with 150 radius 
    rainbow.up()                                                                              # Lifting the pen up so that it won't draw line 
    rainbow.left(90)                                                                          # It currently facing south so turning it 90 degree left to face east again 
    diameter_of_radius = radius_of_rainbow * 2                                                # Want it to move twice as radius to reach starting point 
    rainbow.forward(diameter_of_radius + increase_in_rainbow)                                 # Moving forward by diameter plus increase of 10 unit for semi circle wont overlap 
    rainbow.left(90)
    rainbow.down()
    radius_of_rainbow = radius_of_rainbow + increase_in_rainbow                               # Increasing the radius by 10 units 


rainbow.color("lightblue")                                                                    # Just for Extra : Making tiny cloud at the end of rainbow 
rainbow.right(90)
rainbow.fillcolor("lightblue")
rainbow.begin_fill()
rainbow.circle(-20, 180)
rainbow.left(90)
rainbow.circle(-30, 180)
rainbow.left(90)
rainbow.circle(-20, 180)
rainbow.forward(45)
rainbow.end_fill()

rainbow.left(180)
rainbow.up()
rainbow.forward(diameter_of_radius)
rainbow.down()
rainbow.fillcolor("lightblue")
rainbow.begin_fill() 
rainbow.circle(-20, 180)
rainbow.left(90)
rainbow.circle(-30, 180)
rainbow.left(90)
rainbow.circle(-20, 180)
rainbow.forward(45)
rainbow.end_fill()
  

drawing_screen.mainloop() # Wait for the user to close the drawing screen

"""
Well done! Now you've finished your lab3 successfully. Please upload it 
to your GitHub repository and submit your lab3 GitHub link on e-learn, 
as you did for lab1 and lab2. That's all.

Resource (optional): For exercise 1, feel free to review the concept of exterior angles of regular polygons from here:
https://www.teachoo.com/8592/2789/Exterior-Angles-of-Regular-Polygons/category/Sum-of-Exterior-Angles-of-Polygons/
"""