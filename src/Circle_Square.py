import turtle

def square(var):
	for i in range(4):
		var.forward(100)
		var.right(90)
		
def drawCircle():
	angle = 10
	
	window = turtle.Screen()
	window.bgcolor("white")
	
	brad = turtle.Turtle()
	for i in range(36):
		square(brad)
		brad.right(angle)
		
	window.exitonclick()
	
drawCircle()