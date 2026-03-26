import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = 0
        self.y = 0
        if (type(x) is not float or type(y) is not float):
            print('only numbers can be accepted as input\npoint is initialized to 0,0')
            return
        self.x = x
        self.y = y
    def distance_from_origin(self) -> float:
        return math.sqrt((self.x - 0)**2 + (self.y - 0)**2)

# Linked list implementation
#---------------------------

class Node:
    def __init__(self, value : int):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, value: int):
        new_node = Node(value)
        if (self.head == None):
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def pop(self):
        if self.head == None:
            return
        self.head = self.head.next

    def get_head(self) -> int:
        if (self.head != None):
            return self.head.value
        return -1

    def len(self) -> int:
        if (self.head != None):
            return 0
        count = 0
        current = self.head
        while current.next:
            count += 1
            current = current.next
        return count

    def is_empty(self) -> bool:
        if (self.head == None):
            return True
        return False

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


#-----------------------------------------------------------------------------------------

if __name__ == '__main__':
    p1 = Point()
    p2 = Point(1.2, 4.5)
    p3 = Point(1, 'a')
    print(p1.x, p1.y)
    print(p2.x, p2.y)
    print(p3.x, p3.y)
    print(p1.distance_from_origin())
    print(p2.distance_from_origin())

    linked_list = LinkedList()
    linked_list.push(32)
    linked_list.push(45)
    linked_list.push(13)
    linked_list.push(17)
    linked_list.print_list()
    print(linked_list.get_head())
    linked_list.pop()
    linked_list.print_list()
    linked_list.pop()
    linked_list.print_list()
    print('empty?', linked_list.is_empty())
    linked_list.pop()
    linked_list.print_list()
    print('empty?', linked_list.is_empty())
    linked_list.pop()
    linked_list.print_list()
    print('empty?', linked_list.is_empty())
