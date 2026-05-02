class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    
    def __init__(self, capacity: int):
        self.table = [None] * capacity
        self.capacity = capacity
        self.size = 0

    def insert(self, key: int, value: int) -> None:
        index = self.hash(key)
        node = self.table[index]

        if not node:
            self.table[index] = Node(key, value)
        else:
            prev = None
            while node:
                if node.key == key:
                    node.value = value
                    return
                prev, node = node, node.next
            prev.next = Node(key, value)

        self.size += 1

        if self.size / self.capacity >= 0.5:
            self.resize()
        

    def hash(self, key):
        return key % self.capacity

    def get(self, key: int) -> int:
        idx = self.hash(key)
        target = self.table[idx]

        while target:
            if target.key == key:
                return target.value
            target = target.next

        return -1

    def remove(self, key: int) -> bool:
        idx = self.hash(key)
        target = self.table[idx]

        prev = None
        while target:
            if target.key == key:
                if prev:
                    prev.next = target.next
                else:
                    self.table[idx] = None

                self.size -= 1
                return True
            prev, target = target, target.next 
        
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity *= 2
        new_table = [None] * self.capacity

        for node in self.table:
            while node:
                idx = self.hash(node.key)
                if not new_table[idx]:
                    new_table[idx] = Node(node.key, node.value)
                else:
                    new_node = new_table[idx]
                    while new_node.next:
                        new_node = new_node.next
                    new_node.next = Node(node.key, node.value)
                node = node.next

        self.table = new_table

