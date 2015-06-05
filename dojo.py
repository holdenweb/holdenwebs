#
# TODO: Add some means of ignoring cards already matched
#       Add sound effects
#       Ignore clicks after displaying second card until
#       either hit or miss is reported.
#       Consider re-casting the data structure as a dict
#       with two-element tuple keys.
#       Configure window size according to COLS and ROWS
#

checkmark = Actor('checkmark')
steve = Actor('steve', (50, 50))
steve.topleft = (0, 0)

import random
import time

COLS = 4
ROWS= 3
IMSIZE = 200
STATUS = []    # cells that have been clicked on
ignore = []   # cells that have been matches and are no longer in play

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
			if (row, col) in ignore:
				checkmark.topleft = IMSIZE*col, IMSIZE*row
				checkmark.draw()
			elif (row, col) in STATUS:
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
	if len(STATUS) == 2: # ignore until timeout redisplays
		return
	if pos in ignore: # has already been matched
		return
	if button == mouse.LEFT and (pos):
	# not sure why "and (pos)" - especially the parens!
		coords = findTile(pos)
		if coords not in STATUS:
			STATUS.append(coords) # now they are
			if len(STATUS) == 1:  # ignore first click
				pass
			elif len(STATUS) == 2: # second click - check for match
				(x1, y1), (x2, y2) = STATUS # an "unpacking assignment"
				if board[x1][y1].image_name == board[x2][y2].image_name:
					print("Success sound")
					# add coords to "ignore" list
					for pos in STATUS:
						ignore.append(pos)
				else:
					print("Failure sound")
				clock.schedule_unique(resume_game, 2.0)

def resume_game():
	del STATUS[:]
		
