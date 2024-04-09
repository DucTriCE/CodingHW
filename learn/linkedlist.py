#Create a Node class
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

#Create a linked list class
        
class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def insertAtBegin(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        else:
            newNode.next = self.head
            self.head = newNode
    
    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        else:
            currentNode = self.head
            while currentNode.next:
                currentNode = currentNode.next
            currentNode.next = newNode
    
    def insertAtIndex(self, data, index):
        newNode = Node(data)
        position = 0
        currentNode = self.head
        if position == index:
            self.insertAtBegin(data)
        else:
            while currentNode!=None and position+1 != index:
                position+=1
                currentNode = currentNode.next
            if currentNode != None:
                newNode.next = currentNode.next
                currentNode.next = newNode
            else:
                print("Index not present")

    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while(current_node != None and position != index):
                position = position+1
                current_node = current_node.next
    
            if current_node != None:
                current_node.data = val
            else:
                print("Index not present")

    def removeFirstNode(self):
        if(self.head == None):
            return
        self.head = self.head.next
    
    def removeLastNode(self):
        if self.head == None:
            return
        currentNode = self.head
        while currentNode.next.next:
            currentNode = currentNode.next
        currentNode.next = None
    
    def removeAtIndex(self, index):
            if self.head == None:
                return
    
            current_node = self.head
            position = 0
            if position == index:
                self.remove_first_node()
            else:
                while(current_node != None and position+1 != index):
                    position = position+1
                    current_node = current_node.next
    
                if current_node != None:
                    current_node.next = current_node.next.next
                else:
                    print("Index not present")

    def removeAtData(self, data):
        current_node = self.head
    
        if current_node.data == data:
            self.remove_first_node()
            return
    
        while current_node is not None and current_node.next.data != data:
            current_node = current_node.next
    
        if current_node is None:
            return
        else:
            current_node.next = current_node.next.next

    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next

            
if __name__ == '__main__':
    pass