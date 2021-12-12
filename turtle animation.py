import turtle
turtle.bgcolor('black')
turtle.speed(25)
turtle.hideturtle()
for i in range(10):
	for color in ['yellow','hotpink','orange','green','red','blue','navy','lime','aqua','fuchsia','purple']:
		turtle.color(color)
		turtle.circle(50,180,3)
		turtle.circle(-50)
		turtle.left(10)