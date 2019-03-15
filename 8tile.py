class tree(object):

	def __init__(self):
		self.a = None



	print("Initail state : ")
	a=[[1,2,3],[5,4,6],[7,-1,8]]
	print(a)
	print("Enter Final state : ")
	b=[[1,2,3],[4,5,6],[7,8,-1]]
	print(b)

	def check(self,a,b):
		if a==b:
			print("Got the Output")
		else:
			combination=0
			for x in range(0,3):
				for y in range(0,3):
					if(a[x][y]==-1):
						if x==1 and y==1:
							combination=4
							print("4 Combination possible")
							list1 = [[]]

							temparray1 = a
							temp = a[0][y]
							a[0][y] = a[x][y]
							a[x][y] = temp
							temp1 = a
							a = temparray1


						if (x==0 and y==0) or (x==2 and y==2) or (x==0 and y==2) or (x==2 and y==0):
							combination=2
							print("2 Combination possible")
						if (x==0 and y==1) or (x==1 and y==0) or (x==2 and y==1) or (x==1 and y==2):
							combination=3
							print("3 Combination possible")

print("Initail state : ")
a=[[1,2,3],[4,6,5],[7,-1,8]]
print(a)
print("Enter Final state : ")
b=[[1,2,3],[4,5,6],[7,8,-1]]
print(b)
root = tree()
root.check(a,b)
print(root)