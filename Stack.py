class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        if len(self.items) >= self.capacity:
            raise OverflowError("Stack is full")
        else:
            self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from an empty stack")
        
    def is_full(self):
        return len(self.items) == self.capacity
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Peek from an empty stack")
        
    def size(self):
        return len(self.items)
    
def array_kebalik(arr):
    stack = Stack(7) # Kapasitas array yang akan dibalik
    stack.push(1) # Array yang akan dibalik
    stack.push(0) # Array yang akan dibalik
    stack.push(9) # Array yang akan dibalik
    stack.push(8) # Array yang akan dibalik
    stack.push(2) # Array yang akan dibalik
    stack.push(4) # Array yang akan dibalik
    stack.push(5) # Array yang akan dibalik

    arr_kebalik = []
    while not stack.is_empty():
        arr_kebalik.append(stack.pop())
    return arr_kebalik
    
if __name__ == "__main__":
    input_arr = [1,0,9,8,2,4,5] # Original Array
    print(f"Original array : {input_arr}")
    print(f"Reversed array : {array_kebalik(input_arr)}")

    stack = Stack(4)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    print(f"Stack setelah push: {stack.items} \nItem yang dihapus: {stack.pop()} \nStack setelah pop: {stack.items} \n")
    print(f"Item teratas: {stack.peek()} \nUkuran Stack: {stack.size()} \nApakah stack kosong: {stack.is_empty()} \nApakah stack full?: {stack.is_full()}")