import string, turtle
letters = string.ascii_letters

def reverse(str):
	if len(str) == 1:
		return str
	else:
		return str[len(str)-1] + reverse(str[0:len(str)-1])


def isPalindrom(str):
	temp = "".join([i.lower() for i in str if i in letters])
	if len(temp) <= 1:
		return True
	else:
		if temp[0] == temp[len(temp)-1]:
			return isPalindrom(temp[1:len(temp)-1])	
		else:
			return False

def toStr(n, base):
	nums = "0123456789ABCDEF"
	if n < base:
		return nums[n]
	else:
		return toStr(n//base, base) + nums[n%base]

def drawTree(steps, t, wd):
	if steps > 5:
		t.width(wd)
		t.forward(steps)
		t.right(20)
		drawTree(steps-10, t, wd-2)
		t.left(40)
		drawTree(steps-10, t, wd-2)
		t.right(20)
		t.backward(steps)






##################################################################################

print(reverse("Super mega test"))

print(isPalindrom("aibohphobia"))
print(isPalindrom("Reviled did I live, said I, as evil I did deliver"))
print(isPalindrom("Go hang a salami; I'm a lasagna hog"))
print(isPalindrom("Go hang a salami; I'm lasagna hog"))

print(toStr(5, 2))

t = turtle.Turtle()
win = turtle.Screen()
t.color("green")
t.left(90)
drawTree(50, t, 10)
win.exitonclick()

