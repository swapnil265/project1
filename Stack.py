
#LIFO Structure -last in first out structure

class Stack:

    def __init__(self):
        self.stack = []

        # insert item in stack O(1)

    def push(self, data):
        self.stack.append(data)

        # remove and return the last item (01)

    def pop(self):
        if self.stack_size() < 1:
            return
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        data = self.stack[-1]

    def is_empty(self):
        return self.stack == []

    def stack_size(self):
        return len(self.stack)






stack =Stack()
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.push(60)
stack.push(70)
stack.push(80)

print(stack.pop())
stack.peek()



