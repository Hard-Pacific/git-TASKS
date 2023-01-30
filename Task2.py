#класс Node для определения элемента списка
class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class List:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        if self.first != None:
            current = self.first
            out = 'List [' +str(current.value) +' '
            while current.next != None:
                current = current.next
                out += str(current.value) + ' '
            return out + ']'
        return 'List []'


    def add(self, x):
        self.length+=1
        if self.first == None:
            self.last = self.first = Node(x, None)
        else:
            self.last.next = self.last = Node(x, None)

    def delete(self,i):
        if (self.first == None):
            return
        curr = self.first
        count = 0
        if i == 0:
            self.first = self.first.next
            return
        while curr != None:
            if count == i:
                if curr.next == None:
                    self.last = curr
                old.next = curr.next 
                break
            old = curr  
            curr = curr.next
            count += 1
    def del_numbers(self, l):
        if self.first != None:
            current = self.first
            step = 0
            while current.next != None:
                if current.value % 2 != 0:
                    l.delete(0)
                current = current.next
                step += 1
                if current.value % 2 != 0:
                     l.delete(step)
                     step = 0
                     current = self.first

import random
l=List()
for i in range(20):
    l.add(random.randint(-100, 100))

l.del_numbers(l)
print("result",l)
