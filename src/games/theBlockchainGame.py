'''
Created by Surya Selvam on 9/15/2023.
'''
import datetime
import hashlib

class Node:
    def __init__(self, data="ThreadNode", name="Genesis", nextNode = None, hasRoot = True):
        self.name = name
        self.data = data
        self.nextNode = nextNode
        self.hasRoot = hasRoot
        print("Node Name: " + str(name) + " | Data: " + str(data) + " |  Previous Hash: " + str(self.nextNode)[25:43])
    def get_next(self):
        return self.nextNode
    def set_next(self, data):
        self.nextNode = data
    def get_data(self):
        return self.data
    def get_name(self):
        return self.name
    def get_name(self):
        return str(self.name)
    def has_next(self):
        if self.get_next() is None:
            return False
        return True
    def print(self):
        return str("Node Name: " + str(self.name) + " | Data: " + str(self.data) + " | Hash: " + "  Previous Hash: " + str(self.nextNode)[25:43])


class List:
    def __init__(self, root=None, name="Genesis"):
        self.root = root
        self.name = name
        print(self.root)
        print(self.name)
        self.size = 1
    def add(self, data, name):
        #m = hashlib.sha3_256()
        self.data = data
        self.name = name
        new_node = Node(data, name, self.root, True)
        self.root = new_node
        newRoot = str(new_node)
        print("Hash: " + newRoot[25:43])
        print(" ")

    def remove(self, d):  #don't fully understand this method
        this_node = self.root
        next_node = this_node.get_next

        while this_node is not None:
            if this_node.get_data() == d:
                if next_node is not None:
                    next_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -= 1
                return True  # data removed
            else:
                next_node = this_node
                this_node = this_node.get_next()
        return False  # data not found

    def display(self):
        this_node = self.root
        if this_node is None:
            return
        print(this_node.print())
        while this_node.has_next():
            this_node = this_node.get_next()
            print(this_node.print())

    def findByName(self, name):
        this_node = self.root
        next_node = this_node.get_next()
        if this_node.get_name() == name:
            print(this_node.print())
            return
        while this_node.has_next():
            this_node = this_node.get_next()
            if this_node.get_name() == name:
                print(this_node.print())

        #if this_node.get_name() == name:

    def find(self, d):
        this_node = self.root
        next_node = this_node.get_next()
        if this_node.get_data() == d:
            print(this_node.print())
            return
        while this_node.has_next():
            this_node = this_node.get_next()
            if this_node.get_data() == d:
                print(this_node.print())

        #if this_node.get_name() == name:

    def get_size(self):
        return self.size


list = List()
list.add(0, "Genesis Node")
list.add(2, "First Node")
list.add(3, "Next")
list.add(6, "Root")
list.remove(2)
#list.removeByName("Root")
list.display()
print(" ")
list.findByName("Next")
list.find(6)