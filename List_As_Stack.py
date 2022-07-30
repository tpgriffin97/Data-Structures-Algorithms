
# We can utilize a list as a stack as it's an array,
# This is not optimal as a list in Python is a dynamic array
# This can end up costing us more time as programs scale upwards
# Credit for my studies goes to the youtube channels codebasics and CSDOJO
# As well as realpython.com, pynative.com, and freecodecamp.org

stack = []

stack.append('https://www.reddit.com/r/Knoxville/')
stack.append('https://www.reddit.com/r/Tennessee/')
stack.append('https://www.reddit.com/r/UTK/')
print(stack)

print("Pop the 0 element", stack.pop(0))
print("Pop an empty .pop", stack.pop())

stack.append("https://testdriven.io/blog/modern-tdd/")

print("The list after two elements have been popped", stack)

