from typing import Union

class Node:
    def __init__(self, value):
        self.value: int = value
        self.next: Union[Node, None] = None

class LinkedList:
    def __init__(self) -> None:
        self.head: Union[Node, None] = None

    def insert_at_start(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    
    def insert_at_last(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = node
    
    def insert_after(self, key, value):
        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while temp is not None:
                if temp.value == key:
                    node.next = temp.next
                    temp.next = node
                temp = temp.next
    
    def remove_at_start(self):
        self.head = self.head.next

    def remove_at_end(self):
        temp = self.head
        ref = self.head
        while temp.next is not None:
            ref = temp
            temp = temp.next
        ref.next = None

    def find(self, key):
        temp = self.head
        while temp is not None:
            if temp.value == key:
                print("Found " + str(key))
                return
            else:
                temp = temp.next
        print(str(key) + " not Found")

    def print(self):
        temp = self.head
        result = ""
        while temp is not None:
            result += (str(temp.value ) + " -> ")
            temp = temp.next
        print(result[:len(result) - 4])
        
def linked_list():
    l = LinkedList()
    l.insert_at_start(1)
    l.insert_at_start(2)
    l.insert_at_start(3)
    l.print()
    l.insert_at_last(4)
    l.insert_at_last(5)
    l.print()
    l.insert_after(4, 99)
    l.print()
    l.remove_at_start()
    l.print()
    l.remove_at_end()
    l.print()
    l.find(2)
    l.find(4)
    l.find(99)
    l.find(239487)