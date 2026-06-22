#This is for creating Node 
class Node:

    #info is the data stored in first block and address is stored in second block
    def __init__(self,info,address=None):
        self.data = info
        self.next = address

#for Creating and performing Operation on singly linklist
class Singlylinklist():

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
    
    
    #Insert node at the beginning 
    def insertAtBeg(self,value):

        #create Node and temp point on it
        temp = Node(value)

        #store address of head in t1.next block
        temp.next = self.head

        #now head variable pointing on the newly created node as it added to the beginning of th LL
        self.head = temp

    #Insrt a node at the middle of LL
    #"x" parameter  id taken as after which node newly created node to be added
    def insertATMid(self,value,x):
        temp = Node(value)
        t1 = self.head
        while (t1.next != None):

            #checks if the t1 which is iterated a node is same to node which we are finding 
            if (t1.data == x):

                #firtly link the next node to newly created(temp) by storing address of next node in temp.next block
                temp.next = t1.next

                #second store newly created node in current t1 node 
                t1.next = temp
            
            #this allow next iteration on node
            t1 = t1.next

    #for deletion of node from LL
    def deleteLL(self,value):
        t1 = self.head

        #this point the previous node of t1 currently iterate
        prev = t1

        #if we want to delete first node 
        if (t1.data == value):

            #head point the next node whoes address stored in t1.next
            self.head = t1.next
        while (t1.next != None):

            #checks for the middle 
            if (t1.data == value):

                #link with the next node of deletion one which is t1
                prev.next = t1.next
                break

            #if not found 
            else:
                # this point the previous node of t1 currently iterate
                prev = t1
                t1 = t1.next
        
        #if we want to delete last node 
        if (t1.data == value):

            #make previous node last by storing None at next block
            prev.next = None

    #this print all the node of LL
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