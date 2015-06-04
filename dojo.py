steve = Actor('steve', (50, 50))
steve.topleft = (0, 0)

import random
import time

COLS = 4
ROWS= 3
IMSIZE = 200
STATUS = []

START_IMAGES= [ "im"+str(i+1) for i in range(COLS*ROWS//2)]*2
random.shuffle(START_IMAGES)


STATUS=[]

board = []
for row in range(ROWS):
	new_entry=[]
	for col in range(COLS):
		image_name = START_IMAGES.pop()
		temp=Actor(image_name, (col*IMSIZE, row*IMSIZE))
		temp.image_name = image_name
		temp.topleft=(col*IMSIZE, row*IMSIZE)
		new_entry.append(temp)

		#STATUS.append([tileId,0])

		# print (col*IMSIZE, row*IMSIZE)
		# board[row][col].topleft = (col*IMSIZE, row*IMSIZE)
	board.append(new_entry)

def draw():
	screen.clear()
	for row in range(ROWS):
		for col in range(COLS):
			if (row, col) in STATUS:
				board[row][col].draw()
			else:
				steve.topleft = IMSIZE*col, IMSIZE*row
				steve.draw()

def findTile(pos):
	y, x = pos
	result = x // IMSIZE , y // IMSIZE
	return result

def showTile():
	pass


def on_mouse_down(pos, button):
	if button == mouse.LEFT and (pos):
		coords = findTile(pos)
		if coords not in STATUS:
			STATUS.append(coords)
			if len(STATUS) == 1:
				pass
			elif len(STATUS) == 2:
				(x1, y1), (x2, y2) = STATUS
				print("Status", STATUS, x1, y1, x2, y2)
				if board[x1][y1].image_name == board[x2][y2].image_name:
					print("A HIT!")
				clock.schedule_unique(killstatus, 2.0)

def killstatus():
	del STATUS[:]
		
