'''Trò chơi sẽ được quản lý tại đây'''
import puzzle
import ids
def main():

	pz = puzzle.Puzzle(3)
	pz.generateRandomPuzzle(10)
	pz.printPuzzle()
	s = ids.AI(pz)
	print('Ô trống sẽ di chuyển theo hướng: ',s.depthLimited(5))

main()