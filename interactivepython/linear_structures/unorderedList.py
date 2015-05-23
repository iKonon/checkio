'''
Assume that position names are integers starting with 0.
'''
from __future__ import print_function
class Node:
    def __init__(self,initdata=None):   # The node initializes with a data value, its pointer set to None by default 
        self.data = initdata
        self.next = None

    def __str__(self):
        return str(self.data)

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext
            
    def printBackward(self):
        if self.next != None:
            tail = self.getNext()
            tail.printBackward()
        print(self.data, end=" ")     

class UnorderedList:
    def __init__(self):
        self.head = None    # When the list is first initialized it has no nodes, so the head is set to None

    # This implementation of insert is constant O(1)        
    def add(self,item):
        if not self.head:
            self.head = Node(item)        
        else:
            newNode = Node(item)
            newNode.setNext(self.head) # set new nodes pointer to old head
            self.head = newNode        # reset head to new node

    # The time complexity for delete is O(n)
    def remove(self,item):
        if self.size() == 0:
            raise ValueError("List is empty")
        else:        
            current = self.head
            previous = None
            found = False
            while not found:
                if current.getData() == item:
                    found = True
                elif current is None:
                    raise ValueError("Node is not in the list")
                else:
                    previous = current
                    current = current.getNext()
            if previous is None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())

    # The time complexity of search is O(n)
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    # The time complexity of size is O(n)    
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count    

    def isEmpty(self):
        return self.head == None
   
    def append(self,item): # adds a new item to the end of the list making it the last item in the collection
        temp = Node(item)
        current = self.head
        previous = None
        while current != None:
            previous = current
            current = current.getNext()
        previous.setNext(temp)

    def index(self,item):
        if self.search(item) == False:
            return "Item is not in the list"
        current = self.head
        found = False
        index = -1
        while current != None and not found:
            index += 1
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return index

    def insert(self,pos,item):
        if self.size() < pos:
            return "Index is out of range"        
        if self.isEmpty() == True or pos == 0:
            self.add(item)
        else:        
            temp = Node(item)
            current = self.head
            previous = None
            index = 0
            while current != None and index < pos:
                index += 1
                previous = current
                current = current.getNext()
            temp.setNext(current)
            previous.setNext(temp)

    def pop(self, pos = None):
        if self.isEmpty() == True:
            return "The list is already empty"         
        current = self.head
        following = current.next      
        if pos is None:          
            while following != None:
                if following.next == None:
                    current.next = None
                    return following
                current = following
                following = following.next
            self.head = None
            return current
        
        if pos == 0:
            self.head = following
            return current
        
        index = 0
        while following != None:          
            if index == pos - 1:
                current.next = following.next
                return following
            current = following
            following = following.next
            index += 1        
    
    def printForward(self):
        current = self.head
        output = ""
        while current is not None:
            output += str(current.getData()) + " "
            current = current.getNext()
        print(output)

    def printBackward(self):
        if self.head != None:
            self.head.printBackward()    

    # Iterative
    def reverse(self):
        if self.isEmpty() == True:
            return "The list is empty"         
        current = self.head
        previous = None
 
        while current is not None:
            tmp = current.getNext()
            current.setNext(previous) 
            previous = current
            current = tmp
        self.head = previous
 
    # Recursive
    def reverseRecursive(self) :
        self._reverseRecursive(self.head)
 
    def _reverseRecursive(self,node) :
        if None != node:
            right = node.next
            if self.head != node:
                node.next = self.head
                self.head = node
            else:
                node.next = None
            self._reverseRecursive( right )

if __name__ == '__main__':
    temp = Node(93)
    print(temp.getData())
    
    mylist = UnorderedList()
    print(mylist.isEmpty())
    
    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)
    print(mylist.size())
    print(mylist.search(17))
    mylist.remove(17)
    print(mylist.size())
    print(mylist.search(17))
    
    mylist.append(2)
    print(mylist.size())
    print(mylist.index(2))
    
    mylist.insert(1, 43)
    print(mylist.size())
    print(mylist.index(43))

    mylist.pop()
    print(mylist.size())
    mylist.pop(3)
    print(mylist.size())
    
    mylist.printForward()
    mylist.printBackward()  
    
    mylist.reverse()
    print()
    mylist.printForward()
    
    mylist.reverseRecursive()
    mylist.printForward()