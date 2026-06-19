#This is for creting Node 
class Node:

    #info is the data stored in first block and address is stored in second block
    def __init__(self,info,address=None):
        self.data = info
        self.next = address

#for Creating and performing Operation on singly linklist
class Singlylinklist:

    #head is pointing on first node of LL
    def __init__(self,head=None):
        self.head = head

    #to Insert value at end of LL
    def insertAtEnd(self,Value):

        #create Node and temp point on it
        temp = Node(Value)

        #t1 is a temporary variable pointing on head
        t1 = self.head

        #condition if LL is already exist
        if (self.head != None):

            #iterate on every node in LL using t1 until its reaches at the last node
            #last node next block contains None
            while (t1.next != None):

                #now t1 point on next node whose address stored in t1.next
                t1 = t1.next
            #condition for t1 finally reach to last node
            if (t1.next == None):

                #now at t1.next block stores newly created address(temp)
                t1.next = temp
        
        #LL already not exist
        else:

            #there is only option left for head to point on newly created node 
            self.head = temp
    
    
    def insertAtBeg(self,value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def insertATMid(self,value,x):
        temp = Node(value)
        t1 = self.head
        while (t1.next != None):
            if (t1.data == x):
                temp.next = t1.next
                t1.next = temp
            t1 = t1.next

    def deleteLL(self,value):
        t1 = self.head
        prev = t1
        if (t1.data == value):
            self.head = t1.next
        while (t1.next != None):
            if (t1.data == value):
                prev.next = t1.next
                break
            else:
                prev = t1
                t1 = t1.next
        if (t1.data == value):
            prev.next = None

    def printall(self):
        t1 = self.head
        while (t1.next != None):
            print(t1.data)
            t1 = t1.next
        print(t1.data)

obj = Singlylinklist()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtBeg(5)
obj.insertATMid(40,20)
obj.deleteLL(30)
obj.printall()