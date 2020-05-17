from random import randint
'''
Lớp đại diện cho puzzle, lớp này sẽ tạo ra bản đồ ngẫu nhiên các số
'''
class Puzzle:
	def __init__(self,size):
		self.size = size
		self.map = []
		self.zeroPosition = 8 #Vị trí ô trống trên bản đồ
		self.moves = ['UP','DOWN','LEFT','RIGHT']

		for i in range(self.size*self.size):
			self.map.append(i+1)
		self.map[self.size*self.size - 1] = 0
		'''
		Hàm trên sẽ tạo ra map = [1,2,3,4,5,6,7,8,0]
		'''

	'''Hàm kiểm tra xem puzzle đã xếp đúng thự tự hay chưa'''
	def checkPuzzle(self):
		for i in range(self.size*self.size - 1):
			if self.map[i] != (i+1):
				return False
		return True

	'''Hàm in ra puzzle'''
	def printPuzzle(self):
		for i in range(self.size*self.size):
			print(self.map[i],end=' ')
			if(i+1)%3 ==0:
				print('')

	'''Hàm này sẽ xáo trộn ngẫu nhiên các con số trên bản đồ'''
	def generateRandomPuzzle(self,performNum):
		for i in range(performNum):
			self.performMove(self.moves[randint(0,3)])

	'''Hàm thực hiện di chuyển puzzle theo hướng chỉ định'''
	def performMove(self,direction):
		if direction == 'UP':
			if(self.zeroPosition != 0 and self.zeroPosition != 1 and self.zeroPosition !=2 ):
				self.swap(self.zeroPosition-3,self.zeroPosition)
				self.zeroPosition = self.zeroPosition - 3
		elif direction == 'DOWN':
			if(self.zeroPosition != 6 and self.zeroPosition != 7 and self.zeroPosition !=8 ):
				self.swap(self.zeroPosition+3,self.zeroPosition)
				self.zeroPosition = self.zeroPosition + 3
		elif direction == 'LEFT':
			if(self.zeroPosition != 0 and self.zeroPosition != 3 and self.zeroPosition != 6 ):
				self.swap(self.zeroPosition-1,self.zeroPosition)
				self.zeroPosition = self.zeroPosition - 1
		elif direction == 'RIGHT':
			if(self.zeroPosition != 2 and self.zeroPosition != 5 and self.zeroPosition != 8 ):
				self.swap(self.zeroPosition+1,self.zeroPosition)
				self.zeroPosition = self.zeroPosition + 1

	def swap(self,a,b):
		temp = self.map[a]
		self.map[a]=self.map[b]
		self.map[b]=temp


