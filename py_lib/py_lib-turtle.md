[Turtle Graphics](https://docs.python.org/3/library/turtle.html)
================================================================

Turtle methods
--------------

**1\. Turtle motion**

Move and draw:

```python
forward() | fd() , backward() | bk() | back()
right() | rt() , left() | lt()
goto() | setpos() | setposition()
setx() , sety() , setheading() | seth()
home() , circle() , dot()
stamp() , clearstamp() , clearstamps()
undo() , speed()
```

Tell Turtle's state

```python
position() | pos() , towards()
xcor() , ycor() , heading() , distance()
```

Setting and measurement

```python
degree() , radians()
```

**2\. Pen control**

Drawing state

```python
pendown() | pd() | down()
penup() | pu() | up()
pensize() | width() , pen() , isdown()
```

Color control

```python
color() , pencolor() , fillcolor()
```

Filling

```python
filling() , begin_fill() , end_fill()
```

Move drawing control

```python
reset() , clear() , write()
```

**3\. Turtle state**

Visibility

### Turtle motion

#### Change turtle position and angle

```python
turtle.goto(x, y=None)
turtle.setpos(x, y=None)
turtle.setposition(x, y=None)
#x - a number or a pair/vector of numbers
#y - a number or `None`
#Ex:
turtle.setpos(60,30)
turtle.pos()
#(60.00,30.00)
turtle.setpos((20,80))
turtle.pos()
#(20.00,80.00)

turtle.setx(x) #Set the turtle's 1st coordinate to x.
turtle.sety(y) #Set the turtle's 2nd coordinate to y.

turtle.setheading(to_angle)
turtle.seth(to_angle)
#Set the orientation of the turtle to to_angle.
#In standard mode: 0 - east, 90 - north, 180 - west, 270 - south
#In logo mode: 0 - north, 90 - east, 180 - south, 270 - west
turtle.setheading(90)
turtle.heading()
#90.0

turtle.home()
#Move turtle to the origin – coordinates (0,0) – and set its heading
#to its start-orientation (which depends on the mode)
```

#### Draw A Circle

```python
turtle.circle(radius, extent=None, steps=None)
#If `extent` is not given, draw the entire circle. If `extent` is
#not a full circle, one endpoint of the arc is the current pen
#position. Draw the arc in counterclockwise direction if `radius` is
#positive, otherwise in clockwise direction. Finally the direction
#of the turtle is changed by the amount of `extent`.
#Ex:
turtle.home()
turtle.position()
#(0.00,0.00)
turtle.heading()
#0.0
turtle.circle(50)
turtle.position()
#(-0.00,0.00)
turtle.circle(120, 180)
turtle.pos()
#(0.00,240.00)
turtle.heading()
#180.0


turtle.dot(size=None, *color)
#Draw a circular dot with diameter `size`, using `color`.
#If `size` is not given, the max of `pensize+4` and `2*pensize` is used
```

#### Stamp

```python
turtle.stamp()
#stamp a copy of the turtle shape onto the canvas at the current position.
#Return a `stamp_id` for that stamp, which can be used to delete it by calling `clearstamp(stamp_id)`

turtle.clearstamp(stamid)
#Delete stamp with given `stamid`.
#`stamid`: an integer, must be return value of previous `stamp()` call

turtle.clearstamps(n=None)
#Delete all or 1st/last n of turtle's stamps. If n is `None`, delete all stamps, if n > 0 delete 1st n stamps, else if n < 0 delete last n stamps.
```

#### Speed & Undo

```python
turtle.speed(speed=None)
#Set the turtle’s speed to an integer value in the range 0..10.
#If no argument is given, return current speed.
#If input is a number greater than 10 or smaller than 0.5, speed is set to 0
#`speed` - an integer in the range 0..10 or a speedstring
#0 - 'fastest' , 10 - 'fast' , 6 - 'normal' , 3 - 'slow' , 1 - 'slowest'
#Attention: `speed` = 0 means that no animation takes place.
#forward/back makes turtle jump and likewise left/right make the turtle turn instantly.

turtle.undo()
#Undo (repeatedly) the last turtle action(s).
#Number of available undo actions is determined by the size of the undobuffer.
```

### Tell Turtle's state

```python
turtle.position()
turtle.pos()
#Return the turtle's current location (x,y)

turtle.towards(x, y=None)
#Return the angle between the line from turtle position to position specified by (x,y), the vector or the other turtle.
#This depends on the turtle’s start orientation which depends on the mode - “standard”/”world” or “logo”).

turtle.xcor() #Return the turtle's x coordinate
turtle.ycor() #Return the turtle's y coordinate
turtle.heading() #Return the turtle's current heading (value depends on the turtle mode)
#Ex:
turtle.home()
turtle.left(67)
turtle.heading()
#67

turtle.distance(x, y=None)
#Return the distance from the turtle to (x,y), the given vector or
#the given other turtle, in turtle step units
#Ex:
turtle.home()
turtle.distance(30,40)
#50.0
turtle.distance((30,40))
#50.0
joe = Turtle()
joe.forward(77)
turtle.distance(joe)
#77.0
```

### Settings for measurement

```python
turtle.degrees(fullcircle=360.0)
#Set angle measurement units. Default value is 360 degrees.
#Ex:
turtle.home()
turtle.left(90)
turtle.heading()
#90.0
#Change angle measurement unit to grad (also known as gon,
#grade, or gradian and equals 1/100-th of the right angle.)
turtle.degrees(400.0)
turtle.heading()
#100.0
turtle.degrees(360)
turtle.heading()
#90.0

turtle.radians()
#Set the angle measurement units to radians. Equivalent to `degrees(2*math.pi)`
```

### Pen control

#### Drawing state

```python
turtle.pendown()
turtle.pd()
turtle.down()
#Pull the pen down - drawing when moving

turtle.penup()
turtle.pu()
turtle.up()
#Pull the pen up - no drawing when moving

turtle.pensize(width=None)
turtle.width(width=None)
#Set the line thickness to `width` or return it.
#If `resizemode` is set to “auto” and `turtleshape` is a polygon,
#that polygon is drawn with the same line thickness.
#If no argument is given, the current pensize is returned.
#`width` - a positive number

turtle.pen(pen=None, **pendict)
#Return or set the pen's attributes in a "pen-dictionary" with the following key/value pairs:
#`shown`: True/False
#`pendown`: True/False
#`pencolor`: color-string or color-tuple
#`fillcolor`: color-string or color-tuple
#`pensize`: positive number
#`speed`: number in range 0...10
#`resizemode`: `auto` or `user` or `noresize`
#`stretchfactor`: (positive number, positive number)
#`outline`: positive number
#`tilt`: number
#This dictionary can be used as argument for a subsequent call to `pen()` to restore the former pen-state.
#Moreover one or more of these attributes can be provided as keyword-arguments.
#This can be used to set several pen attributes in one statement.

turtle.isdown() #Return `True` if pen is down, `False` if it's up
```

#### Color control

```python
turtle.pencolor(*args)
#Return or set the pencolor. Four input formats are allowed:
##`pencolor()` - Return the current `pencolor` as color specification string or as a tuple (see example). May be used as input to another `color`/`pencolor`/`fillcolor` call.
##`pencolor(colorstring)` - Set `pencolor` to `colorstring`, which is a Tk color specification string, such as `red`, `yellow`, or `#33cc8c`.
##`pencolor((r,g,b))` or `pencolor(r,g,b)`- Set `pencolor` to the RGB color represented by the tuple of r, g, and b. Each of r, g, and b must be in the range 0..colormode, where `colormode` is either 1.0 or 255 (see `colormode()`).

turtle.fillcolor(*args)
#Return or set the `fillcolor`. Accepts four input formats above.

turtle.color(*args)
#Return or set `pencolor` and `fillcolor`. Use 0 to 3 arguments with input formats like above.
```

#### Filling

```python
turtle.filling() #Return fillstate (`True` if filling, `False` else)
#Ex:
turtle.begin_fill()
if turtle.filling():
    turtle.pensize(5)
else:
    turtle.pensize(3)

turtle.begin_fill() #To be called just before drawing a shape to be filled
turtle.end_fill() #Fill the shape drawn after the last call to `begin_fill()`
#Ex:
turtle.color("black", "red")
turtle.begin_fill()
turtle.circle(80)
turtle.end_fill()
```

#### Move drawing control

```python
turtle.reset()
#Delete the turtle's drawings from the screen,
#re-center the turtle and set variables to the default values

turtle.clear()
#Delete the turtle’s drawings from the screen. Do not move turtle.
#State and position of the turtle as well as drawings of other turtles are not affected.

turtle.write(arg, move=False, align="left", font=("Arial", 8, "normal"))
#Write text - the string representation of `arg` -
#at the current turtle position according to `align` ("left", "center" or "right") and with the given font.
#If `move` is true, the pen is moved to the bottom-right corner of the text.
#By `default`, `move` is `False`
#Ex:
turtle.write("Home = ", True, align="center", font=("Roboto", 45, "bold"))
#Home =
turtle.write((0,0), True)
#(0,0)
```

### Turtle state

#### Visibility

```python
turtle.hideturtle()
turtle.ht() #Make the turtle invisible

turtle.showturtle()
turtle.st() #Make the turtle visible

turtle.isvisible() #Answer if turtle's visible or not
```

#### Appearance

```python
turtle.shape(name=None)
#Set turtle shape to shape with given `name`:
#`turtle`, `circle`, `square`, `triangle`, or `classic`
#If name is not given, return name of current shape.

turtle.resizemode(rmode=None)
#Set `resizemode` to one of the values: “auto”, “user”, “noresize”.
#If `rmode` is not given, return current `resizemode`. Different `resizemodes` have the following effects:
##`auto`: adapts the appearance of the turtle corresponding to the value of `pensize`
##`user`: adapts the appearance of the turtle according to
##the values of `stretchfactor` and `outlinewidth` (outline), which are set by `shapesize()`.
##`noresize`: no adaption of the turtle’s appearance takes place.
#`resizemode('user')` is called by `shapesize()` when used with arguments.

turtle.shapesize(stretch_wid=None, stretch_len=None, outline=None)
turtle.turtlesize(stretch_wid=None, stretch_len=None, outline=None)
#Return or set the pen’s attributes x/y-stretchfactors and/or outline.
#Set `resizemode` to “user”.
#If and only if resizemode is set to “user”, the turtle will be displayed stretched according to its stretchfactors:
##`stretch_wid` is stretchfactor perpendicular to its orientation, ##`stretch_len` is stretchfactor in direction of its orientation,
##`outline` determines the width of the shapes’s outline.

turtle.shearfactor(shear=None)
#Set or return the current shearfactor.
#Shear the `turtleshape` according to the given shearfactor `shear`, which is the tangent of the shear angle.
#Do not change the turtle’s heading (direction of movement).
#If shear is not given: return the current shearfactor

turtle.tilt(angle)
#Rotate the `turtleshape` by angle from its current tilt-angle,
#but do not change the turtle’s heading (direction of movement).

turtle.settiltangle(angle)
#Rotate the turtleshape to point in the direction specified by angle, regardless of its current tilt-angle.
#Do not change the turtle’s heading (direction of movement).

turtle.tiltangle(angle=None)
#Set or return the current tilt-angle.
#If angle is given, rotate the turtleshape to point in the direction specified by angle, regardless of its current tilt-angle
#Do not change the turtle’s heading (direction of movement).
#If angle is not given: return the current tilt-angle

turtle.shapetransform(t11=None, t12=None, t21=None, t22=None)
#Set or return the current transformation matrix of the turtle shape.

turtle.get_shapepoly()
#Return the current shape polygon as tuple of coordinate pairs.
#This can be used to define a new shape or components of a compound shape
```

### Using events

```python
turtel.onclick(fun, btn=1, add=None)
#Bind `fun` to mouse-click events on this turtle.
#If `fun` is `None`, existing bindings are removed.
#`fun` – a function with two arguments which will be called with the coordinates of the clicked point on the canvas.
#`num` - number of the mouse-button, defaults to 1 (left mouse button)
#`add` – `True` or `False` – if `True`, a new binding will be added, otherwise it will replace a former binding
#Ex
def turn(x, y):
    left(180)
onclick(turn)  # Now clicking into the turtle will turn it.
onclick(None)  # event-binding will be removed

turtle.onrelease(fun, btn=1, add=None)
#Bind `fun` to mouse-button-release events on this turtle.
#If `fun` is `None`, existing bindings are removed.
#Ex
class MyTurtle(Turtle):
    def glow(self,x,y):
        self.fillcolor("red")
    def unglow(self,x,y):
        self.fillcolor("")
turtle = MyTurtle()
turtle.onclick(turtle.glow)     # clicking on turtle turns `fillcolor` red,
turtle.onrelease(turtle.unglow) # releasing turns it to transparent.

turtle.ondrag(fun, btn=1, add=None)
#Bind `fun` to mouse-move events on this turtle.
#If `fun` is `None`, existing bindings are removed.
#Remark: Every sequence of mouse-move-events on a turtle is preceded by a mouse-click event on that turtle.
#Ex
turtle.ondrag(turtle.goto)
```

### Special Turtle methods

```python
turtle.begin_poly()
#Start recording the vertices of a polygon
#Current turtle position is first vertex of polygon.

turtle.end_poly()
#Stop recording the vertices of a polygon.
#Current turtle position is last vertex of polygon.
#This will be connected with the first vertex.

turtle.get_poly() #Return the last recorded polygon

turtle.clone()
#Create and return a clone of the turtle with same position, heading and turtle properties.

turtle.getturtle()
turtle.getpen()
#Return the Turtle object itself. Only reasonable use: as a function to return the “anonymous turtle”:
pet = getturtle()
pet.fd(50)
pet
#<turtle.Turtle object at 0x...>

turtle.getscreen()
#Return the `TurtleScreen` object the turtle is drawing on
#`TurtleScreen` methods can then be called for that object.
ts = turtle.getscreen()
ts
#<turtle._Screenobject at 0x...>
ts.bgcolor("pink")

turtle.setundobuffer(size)
#Set or disable `undobuffer`. If `size` is an integer, an empty undobuffer of given size is installed.
#`size` gives the maximum number of turtle actions that can be undone by the `undo()` method/function.
#if `size` is `None`, the undobuffer is disabled.

turtle.undobufferentries()
#Return number of entries in the undobuffer
while undobufferentries():
    undo()
```

TurtleScreen/Screen methods and functions
-----------------------------------------

### Window control

```python
turtle.bgcolor(*args)
#Set or return background color of the `TurtleScreen`

turtle.bgpic(picname=None)
#Set background image or return name of current background image
#`picname` – a string, name of a gif-file or "nopic", or `None`

turtle.clear()
turtle.clearscreen()
#Delete all drawings and all turtles from the `TurtleScreen`
#Reset the now empty `TurtleScreen` to its initial state:
#white background, no background image, no event bindings and tracing on.

turtle.reset()
turtle.resetscreen()
#Reset all `Turtle`s on the `Screen` to their initial state.

turtle.screensize(canvwidth=None, canvheight=None, bg=None)
#`canvwidth` – positive integer, new width of canvas in pixels
#`canvheight` – positive integer, new height of canvas in pixels
#`bg` – colorstring or color-tuple, new background color
#If no arguments are given, return current (canvaswidth, canvasheight)
#Do not alter the drawing window
#e.g. to search for an erroneously escaped turtle ;-)

turtle.setworldcoordinates(llx, lly, urx, ury)
#Set up user-defined coordinate system and switch to mode `world` if necessary
#`llx` – a number, x-coordinate of lower left corner of canvas
#`lly` – a number, y-coordinate of lower left corner of canvas
#`urx` – a number, x-coordinate of upper right corner of canvas
#`ury` – a number, y-coordinate of upper right corner of canvas
screen.reset()
screen.setworldcoordinates(-50,-7.5,50,7.5)
for _ in range(72):
    left(10)
for _ in range(8):
    left(45); fd(2)   # a regular octagon
```

### Animation control

```python
turtle.delay(delay=None)
#Set or return the drawing delay in milliseconds.
#(This is approximately the time interval between two consecutive canvas updates.)
#The longer the drawing delay, the slower the animation.

turtle.tracer(n=None,delay=None)
#Turn turtle animation on/off and set delay for update drawings.
#If n is given, only each n-th regular screen update is really performed.
#(Can be used to accelerate the drawing of complex graphics.)
#When called without arguments, returns the currently stored value of n.
#Second argument sets delay value (see `delay()`)
screen.tracer(8, 25)
dist = 2
for i in range(200): #build a labyrinth
    fd(dist)
    rt(90)
    dist += 2

turtle.update()
#Perform a `TurtleScreen` update. To be used when `tracer` is turned off.
```

### Using screen events

```python
turtle.listen(xdummy=None, ydummy=None)
#Set focus on `TurtleScreen` (in order to collect key-events).
#Dummy arguments are provided in order to be able to pass `listen()` to the `onclick` method.

turtle.onkey(fun, key)
turtle.onkeyrelease(fun,key)
#Bind `fun` to key-release event of key. If `fun` is `None`, event bindings are removed
#Remark: in order to be able to register key-events, `TurtleScreen` must have the focus
#`fun` – a function with no arguments or `None`
#`key` – a string: key (e.g. “a”) or key-symbol (e.g. “space”)
def f():
    fd(50)
screen.onkey(f, "Up")
screen.listen()

turtle.onkeypress(fun, key=None)
#TODO: https://docs.python.org/3/library/turtle.html#turtle.onkeypress
```
