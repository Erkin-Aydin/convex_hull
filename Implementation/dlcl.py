class Node:
    def __init__(self, point):
        self.point = point
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def add_node(self, point):
        copy = (point[0], point[1])
        new_node = Node(copy)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
            self.last = self.head
        else:
            self.last.next = new_node
            new_node.prev = self.last
            new_node.next = self.head
            self.head.prev = new_node
            self.last = new_node
    def delete_node(self, point):
        if point == self.head:
            self.head = None
        else: 
            prev = point.prev
            next = point.next
            prev.next = next
            next.prev = prev
            point = None

    def find_point(self, point):
        current = self.head
        while current:
            if current.point == point:
                return current
            current = current.next
            if current == self.head:
                break
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.point)
            current = current.next
            if current == self.head:
                break
