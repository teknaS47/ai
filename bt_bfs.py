class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def printnode(self):
    	if self.left:
    		print("left")
    		self.left.printnode()
    	print(self.left)
    	if self.right:
    		print("right")
    		self.right.printnode()
    	print(self.right)

    #def bfs(search):
		

rootnode = Node(input("Enter the value for the rootnode"))
n=input("Enter the number of nodes you want to create : ")
for x in range(n):
	value=input("Enter the value of the node : ")
	rootnode.insert(value)
rootnode.printnode()

