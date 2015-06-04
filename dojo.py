"""steve = Actor('steve', (50, 50))
steve.topleft = (0, 0)"""
import random

COLS = 4
ROWS= 3
IMSIZE = 200
STATUS = []

START_IMAGES= [ "im"+str(i+1) for i in range(COLS*ROWS//2)]*2
random.shuffle(START_IMAGES)


images=['']

board = []
for row in range(ROWS):
	new_entry=[]
	for col in range(COLS):
		temp=Actor(START_IMAGES.pop(), (col*IMSIZE, row*IMSIZE))
		temp.topleft=(col*IMSIZE, row*IMSIZE)
		new_entry.append(temp)

		#STATUS.append([tileId,0])

		# print (col*IMSIZE, row*IMSIZE)
		# board[row][col].topleft = (col*IMSIZE, row*IMSIZE)
	board.append(new_entry)

pictures=[[1,2,3,4],[5,6,1,2],[3,4,5,6]]

def draw():
	screen.clear()
	for row in range(ROWS):
		for col in range(COLS):
			board[row][col].draw()

def findTile(pos):
	x,y = pos
	return x// IMSIZE , y//IMSIZE

def showTile():
	pass


def on_mouse_down(pos, button):
	if button == mouse.LEFT and (pos):
		print(findTile(pos))
		print("Eek!")
