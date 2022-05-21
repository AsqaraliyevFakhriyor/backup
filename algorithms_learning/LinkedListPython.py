class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None

    def printLists(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self,prev_node, new_data):
        """Biror tugundan so'ng tugun qo'shish"""
        if prev_node is None:
            print("Tugun mavjud emas")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        if new_data is None:
            print("you cannot insert empty data!")
            return

        new_node = Node(new_data)

        if self.head is None:
            self.head =  new_node
        
        list = self.head
        while list.next:
            list = list.next
        list.next = new_node
        print("added new data!")

    def delete_all(self):
        if self.head is None:
            print("List is already empy!")
            return
        list = self.head
        while list:
            perv = list.next
            del list.data
            list = perv
        list = None 

    def deleteNode(self,node_data):
        if node_data is None:
            print("Node data(key) is Empty!")
            return

        temp = self.head
        if temp and temp.data == node_data:
            self.head = temp.next
            temp = None
            print("Node: {} deleted successfully".format(node_data))
            return
        while temp:
            if temp.data == node_data:
                break
            perv = temp
            temp = temp.next
        if temp==None:
            return
        perv.next = temp.next
        temp = None