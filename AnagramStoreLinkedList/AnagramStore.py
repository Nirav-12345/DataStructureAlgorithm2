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

def anagram(lower, upper):
    class Node:
        def __init__(self,data):
            self.data=data
            self.next=None

    class Stack:
        def __init__(self):
            self.head=None

        def push(self,data):
            if self.head==None:
                self.head=Node(data)
            else:
                newNode=Node(data)
                newNode.next=self.head
                self.head=Node(data)

    list=[]
    a = Stack()
    an=prime(lower,upper)
    for i in range(len(an)):
        for j in range(i+1,len(an)):
            if(sorted(str(an[i]))==sorted(str(an[j]))):
                list.append(an[i])
                list.append(an[j])
                a.push(list)

    #return list
    return a


#print(prime(0,1000))
print(anagram(0,1000))



















