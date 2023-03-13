class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def addElementHead(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
    
    def addElementTail(self, data):
        newNode = Node(data)
        if self.tail is None:
            self.tail = newNode
            self.head = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
    
    def maju(self, n):
        c = self.head
        for i in range(n):
            if c is None:
                break
            c = c.next
        if c is not None:
            print(c.data)
            self.head = c
    
    def mundur(self, n):
        c = self.head
        for i in range(n):
            if c is None:
                break
            c = c.prev
        if c is not None:
            print(c.data)
            self.head = c





# Contoh input & output program:
linkedlist = LinkedList()
linkedlist.addElementHead("Jogja")
linkedlist.addElementHead("Jakarta")
linkedlist.addElementTail("Bali")
linkedlist.addElementTail("Bandung")

linkedlist.maju(2) #output: Bali
linkedlist.mundur(1) #output: Jogja
linkedlist.maju(5) #output: Bali
linkedlist.mundur(3) #output: Bandung
