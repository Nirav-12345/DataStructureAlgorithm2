class node:
    def __init__(self, data):
        self.data=data
        self.next=None



class Stack:
    def __init__(self):
        self.head=None

    def push(self,data):
        if self.head ==None:
            self.head=node(data)

        else:
            current=self.head
            current.next=self.head
            self.head=node(data)

    def pop(self):
        if self.head ==None:
            return None
        else:
            temp=self.head.data
            self.head=self.head.next

        return temp

    def size(self):
        current=self.head
        count=0
        while current !=None:
            current+=current.next
            count=count+1

        return count

    def isEmpty(self):
        return self.head is None
    def display(self):
        current=self.head
        while current !=None:
            print(current.data)
            current.next



a=Stack()

inp=input("Enter the expression")

for n in inp:
    if n=='(':
        a.push(1)
        a.display()
        if n==')':
            if a.isEmpty():
                balanced=False
            a.pop()







    else:
        if a.isEmpty():
            balanced=True

        else:
            balanced=False

        if balanced:
            print('Expression ', inp, ' is correctly parenthesized.')
        else:
            print('Expression ', inp, ' is not correctly parenthesized.')


