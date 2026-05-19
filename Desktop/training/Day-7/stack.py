#implement a Stack using single linked List
import sys

class GetNode:
    def __init__(self):
        self.data = None
        self.right = None


class LinkedList:
    def __init__(self):
        self.head = None


    # Append at end
    def append(self):
        data = int(input("Enter data: "))
        newNode = GetNode()
        newNode.data = data

        if self.head is None:
            self.head = newNode

        else:
            ptr = self.head

            while ptr.right != None:
                ptr = ptr.right

            ptr.right = newNode


    # Add at beginning
    def addAtBeginning(self):
        data = int(input("Enter data: "))
        newNode = GetNode()
        newNode.data = data

        newNode.right = self.head
        self.head = newNode


    # Delete at end
    def deleteAtEnd(self):

        if self.head is None:
            print("List is empty")

        elif self.head.right is None:
            self.head = None

        else:
            ptr = self.head

            while ptr.right.right != None:
                ptr = ptr.right

            ptr.right = None


    # Traverse list
    def traverse(self):

        if self.head is None:
            print("List not present")

        else:
            ptr = self.head

            while ptr != None:
                print(ptr.data, "->", end=" ")
                ptr = ptr.right

            print()


obj = LinkedList()

while True:

    print("\n1. Append")
    print("2. Traverse")
    print("3. Add At Beginning")
    print("4. Delete At End")
    print("0. Exit")

    n = int(input("Enter choice: "))

    if n == 1:
        obj.append()

    elif n == 2:
        obj.traverse()

    elif n == 3:
        obj.addAtBeginning()

    elif n == 4:
        obj.deleteAtEnd()

    elif n == 0:
        sys.exit()

    else:
        print("Invalid choice")