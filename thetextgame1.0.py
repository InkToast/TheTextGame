import os, time, keyboard

character = 'X'
background = '.'
wall = '#'
while True:
	if input(f'[>>>] Enter 1 to start, 0 to end: ') == '0': break
	print(f'Welcome back to The Text Game')
	print(f'Please choose a level from the below\n')

	lvls = ''
	lcount = 0
	for i in os.listdir():
		if i[-3:] == 'tgl':
			lcount += 1
			lvls = lvls + f'{lcount}: {i[:-4]}\n'

	print(f'{lvls}')
	while True:
		try:
			lvl = input(f">>> ")
			level = open(f'{lvl}.tgl','r')
			break
		except:
			print(f"Invalid level")

	x = 4
	y = 3
	def up():
		global y
		if y < 9:
			y-=1
	def down():
		global y
		if y > 0:
			y+=1
	def left():
		global x
		if x > 0:
			x-=1
	def right():
		global x
		if x < 8:
			x+=1

	keyboard.add_hotkey('w', up)
	keyboard.add_hotkey('s', down)
	keyboard.add_hotkey('a', left)
	keyboard.add_hotkey('d', right)
	win = 0
	for i in level.readlines():
		time.sleep(0.12)
		os.system('cls')
		n = (y*18)+(x*2) -1
		text = ' '+' '.join(list('\n'.join(i.split('|')))).replace('0',background).replace('1',wall	)
		text = list(text)
		if text[n] == wall:
			win = 1
			break
		else:
			text[n] = character
		text = ''.join(text)
		print(text)

	if win == 0:
		print(f"You Won!")
	else:
		print(f"Game Over!")
	keyboard.unhook_all_hotkeys()
	time.sleep(1)
	os.system('cls')
