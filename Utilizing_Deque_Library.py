from collections import deque

stack = deque()

stack.append('https://www.reddit.com/r/Knoxville/')
stack.append('https://www.reddit.com/r/Tennessee/')
stack.append('https://www.reddit.com/r/UTK/')

print(stack)

stack.pop()
print(stack)


def return_empty(list):
    return len(list) == 0


stack = return_empty(stack)
print(stack)


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def seek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)
