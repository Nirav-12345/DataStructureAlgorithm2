def prime(lower, upper):
    list = []
    flag = 0
    for num in range(lower, upper + 1):
        flag = 0

        if num > 1:

            for i in range(2, num):
                if (num % i) == 0:
                    flag = 1
        if flag == 0:
           # print("Odd", num)
            list.append(num)

    return list


class Node:
    def __init__(self, value):  # the initializer is going to take a value which will be stored in the node
        self.value = value
        self.next = None

class Stack:
    '''
    This class will use the node objects to create a node
    '''

    def __init__(self, value=None):  # value is set to none so that we can initialize our stack with or without a value
        self.top = None  # initially the top points to None
        if (value):  # the following code will run only if the value has been passed
            self.push(value)  # this calls the push method which we will define in a while

    def push(self, value):  # takes the value to be inserted as an argument
        node = Node(value)  # creates a node object
        if (self.top == None):  # checks if the top exists already or not, if not run's the following code
            self.top = node
        else:
            node.next = self.top  # assigns the address of top to the next variable of the node object
            self.top = node  # top now points to the new node

    def display(self):
        current=self.top
        while current !=None:
            print(current.value)
            current=current.next

def anagram(lower, upper):


    list=[]
    a=Stack()
    an=prime(lower,upper)
    for i in range(len(an)):
        for j in range(i+1,len(an)):
            if(sorted(str(an[i]))==sorted(str(an[j]))):
                list.append(an[i])
                list.append(an[j])
                a.push(list)
    a.display()





    #return list
    #return a


#print(prime(0,1000))
print(anagram(0,1000))




















