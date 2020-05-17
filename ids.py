import node
from queue import LifoQueue
'''Lớp này sẽ thực hiện thuật toán IDS để tìm kiếm hướng di chuyển cho puzzle'''
class AI:
	def __init__(self,puzzle):
		self.root = node.Node(puzzle)

	'''Hàm tìm kiếm DFS giới hạn theo độ sâu'''
	def depthLimited(self,depth):
		frontier = LifoQueue()
		frontier.put(self.root)
		while True:
			if frontier.empty():
				return None
			node = frontier.get()
			print('')
			node.state.printPuzzle()
			if node.goalState():
				return node
			elif node.depth is not depth:
				expandingNodeList = node.getExpandingNode()
				while not expandingNodeList.empty():
					frontier.put(expandingNodeList.get())

	'''Triển khải thuật toán IDS(Lặp sâu dần)'''
	def interativeDeepening(self):
		depth = 0
		result = None
		while result == None:
			result = self.depthLimited(depth)
			depth+=1
		return result
