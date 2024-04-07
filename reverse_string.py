class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
    def is_empty(self):
        return len(self.items) ==0
    
def reverse_string(ans):
    stack=Stack()
        
    for char in ans:
        stack.push(char)

    reversed_string=''
    while not stack.is_empty():
        reversed_string+=stack.pop()
    return reversed_string

ans="SaakarLovesBigya"
reversed_string=reverse_string(ans)
print(reversed_string)
