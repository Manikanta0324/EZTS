class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.items:
            return None
        return self.items.pop()
    
    def is_empty(self):
        return len(self.items) == 0

def is_balanced(expression):
    stack = Stack()
    opening_brackets = "([{"
    closing_brackets = ")]}"
    matching_bracket = {')': '(', ']': '[', '}': '{'}
    
    for char in expression:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty():
                return False
            top = stack.pop()
            if top != matching_bracket[char]:
                return False
    
    return stack.is_empty()
expression = "[3+7{52/11}(3+5)]"
if is_balanced(expression):
    print("Valid")
else:
    print("Invalid")
