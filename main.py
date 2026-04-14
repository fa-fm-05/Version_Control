def greet(name):
    """This code prints out greeting"""
    print("hello", name, "! How are you doing?")

greet("Mehtab Ahmed")

for: global variables:
    y = 20
def access_global():
    print("global variable y:", y)
access_global()

def modify_global():
    global y
    y = 30
modify_global()
print("Modified global variable", y) # output will be 30

def modify_list(lst):
    lst.append(4)

numbers = [1,2,3]
modify_list(numbers)a
print(numbers)

def try_modify_string():
    s = "new value"

text = "original"
try_modify_string(text)
print(text)