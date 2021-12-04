import os, time, keyboard
from colorama import Fore,Style

os.system('cls')
print(f"{Fore.LIGHTGREEN_EX}Loading. Made By InkOnToast#0001")
time.sleep(1)
os.system('cls')
print(f"{Fore.LIGHTGREEN_EX}Loading.. Made By InkOnToast#0001")
time.sleep(1)
os.system('cls')
print(f"{Fore.LIGHTGREEN_EX}Loading... Made By InkOnToast#0001")
time.sleep(1)
os.system('cls')

character = 'X'
color = Fore.LIGHTGREEN_EX
background = '.'
wall = '#'
while True:
	choice = input(f'{color}[>>>] Enter 1 to start, 2 to customize, 0 to end: ')
	if choice == '0': break
	if choice == '2':
		os.system('cls')
		color = input(f"{Style.RESET_ALL}[>>>] Do you want colour on the game, N for text to look like this, Y for colour in game: ")
		if color[0].lower() == 'n':
			color = Style.RESET_ALL
		else:
			color = Fore.LIGHTGREEN_EX
		print(f"{color}Settings Completed")
		time.sleep(.3)

	now = time.time()
	os.system('cls')

	print(f'{color}Welcome back to The Text Game')
	print(f'{color}Please choose a level from the below (Website for free levels soon)\n')

	lvls = ''
	lcount = 0
	for i in os.listdir():
		if i[-3:] == 'tgl':
			lcount += 1
			lvls = lvls + f'{lcount}: {i[:-4]}\n'

	print(f'{color}{lvls}')
	while True:
		try:
			lvl = input(f"{color}>>> ")
			level = open(f'{lvl}.tgl','r')
			break
		except:
			print(f"{color}Invalid level")

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
		time.sleep(0.07)
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
		print(f'{color}'+text)

	if win == 0:
		print(f"{color}You Won!")
	else:
		os.system('cls')
		print(f"{color}Game Over!")
	keyboard.unhook_all_hotkeys()
	time.sleep(1)
	os.system('cls')

print(f"{color}Goodbye!")
time.sleep(.5)