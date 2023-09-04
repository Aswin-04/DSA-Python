#   Program to find the total number of nodes in a linkedList

class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None

head = Node(4)
nodeB = Node(6)
nodeC = Node(7)
nodeD = Node(9)
nodeE = Node(1)

head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE

def countNodes(head):

    count = 1
    while head.next != None:
        count+=1
        head = head.next
    
    return count

print(f"Total Nodes : {countNodes(head)}")