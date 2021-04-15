class Node:

    def __init__(self,data):
        self.data=data
        self.nextNode=None

class LinkedList:

    def __init__(self):
        self.head=None

    def insert_start(self,data):
        new_node =Node(data)

        if not self.head:
            self.head=new_node
        else:
            new_node.nextNode=self.head
            self.head=new_node

    def insert_end(self,data):
        new_node = Node(data)

        actual_node =self.head

        while(actual_node.nextNode!=None):
            actual_node=actual_node.nextNode

        actual_node.nextNode = new_node


    def traverse(self):
        actual_node = self.head
        while(actual_node.nextNode!=None):
            print(actual_node.data)
            actual_node=actual_node.nextNode
        print(actual_node.data)

    def remove(self,data):

        if self.head is None:
            return
        actual_node=self.head
        previous_node=None


        while((actual_node.data!=data )and (actual_node.nextNode!=None)):
            previous_node=actual_node
            actual_node=actual_node.nextNode

        if (actual_node is None):
            return

        if previous_node is None:
            self.head =actual_node.nextNode
        else:
            previous_node.nextNode=actual_node.nextNode


    def findMiddle(self):
        actual_node=self.head
        fast=self.head
        slow=self.head

        while fast.nextNode.nextNode and slow.nextNode :
            fast=fast.nextNode.nextNode
            slow=slow.nextNode

        return slow.data


if __name__ == '__main__':

    linked_list=LinkedList()
    linked_list.insert_start(4)
    linked_list.insert_end(97)
    linked_list.insert_start(5)
    linked_list.insert_start(6)
    linked_list.traverse()
    data =linked_list.findMiddle()
    print(data)