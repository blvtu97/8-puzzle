from queue import Queue
from copy import deepcopy
'''Lớp này đại diện cho một trạng thái của puzzle'''
class Node:
	def __init__(self,puzzle,parent=None,move=""):
		self.state = puzzle
		self.parent = parent
		self.depth = 0 # Độ sâu từ root tới node hiện tại
		#Nếu hiện tại đang là root node thì độ sâu sẽ là 0 và hướng di chuyển là chưa có
		if parent == None:
			self.depth = 0
			self.moves = move
		#Ngược lại là node mở rộng từ parent, thì độ sâu sẽ tăng lên
		else:
			self.depth = parent.depth + 1
			self.moves = parent.moves + move +" "

	'''Kiểm tra xem puzzle đã xếp đúng hay chưa'''
	def goalState(self):
		return self.state.checkPuzzle()

	'''Thêm các node con từ node cha, hay nói cách khác ta thêm node này vào
	frontier'''
	def getExpandingNode(self):
		exs = Queue()
		#Với mỗi bước di chuyển, ta tạo ra một bản sao của state hiện tại và
		#thực hiện di chuyển, nếu di chuyển thành công, nghĩa là node đó có
		#thể mở rộng ta thêm nó vào frontier
		for dic in self.state.moves:
			pz =  deepcopy(self.state)
			pz.performMove(dic)
			if pz.zeroPosition is not self.state.zeroPosition:
				exs.put(Node(pz,self,dic))
		return exs

	def __str__(self):
		return str(self.moves)


