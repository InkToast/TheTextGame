import os
os.system('cls')
print(f"Loading. Made By InkOnToast#0001")
import time, keyboard
from colorama import Fore,Style

time.sleep(.5)
os.system('cls')
print(f"{Fore.LIGHTGREEN_EX}Loading.. Made By InkOnToast#0001")
time.sleep(.5)
os.system('cls')
print(f"{Fore.LIGHTGREEN_EX}Loading... Made By InkOnToast#0001")
time.sleep(.5)
os.system('cls')

character = 'X'
color = Fore.LIGHTGREEN_EX
colorcharacter = Fore.LIGHTCYAN_EX
wallcolor = Fore.LIGHTRED_EX

background = '.'
wall = '#'
while True:
	choice = input(f'{color}[>>>] Enter 1 to start, 2 to customize, 0 to end: ')
	if choice == '0': break
	if choice == '2':
		os.system('cls')
		character = input(f"{color}[>>>] Please enter text of character (X by default): ")[0]
		background = input(f"{color}[>>>] Please enter text of background (. by default): ")[0]
		wall = input(f"{color}[>>>] Please enter text of walls (# by default): ")[0]
		color = input(f"{Style.RESET_ALL}[>>>] Do you want colour on the game, N for text to look like this, Y for colour in game: ")
		if color[0].lower() == 'n':
			color = Style.RESET_ALL
			wallcolor = color = Style.RESET_ALL
			colorcharacter = Style.RESET_ALL
		else:
			color = Fore.LIGHTGREEN_EX
		print(f"{color}Settings Completed")
		time.sleep(.3)

	now = time.time()
	os.system('cls')

	print(f'{color}Welcome back to The Text Game')
	print(f'{color}Please choose a level from the below (https://discord.gg/szA5kwJkrD)')
	print(f"{color}You may also type 'infinite' for a infinite chase mode\n")

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
			if lvl == 'infinite':
				level = 'infinite'
				break
			else:
				level = open(f'{lvl}.tgl','r')
				break
		except:
			print(f"{wallcolor}Invalid level")

	x = 4
	y = 3
	def up():
		global y
		y-=1
	def down():
		global y
		y+=1
	def left():
		global x
		x-=1
	def right():
		global x
		x+=1

	keyboard.add_hotkey('w', up)
	keyboard.add_hotkey('s', down)
	keyboard.add_hotkey('a', left)
	keyboard.add_hotkey('d', right)
	win = 0
	if level != 'infinite':
		for i in level.readlines():
			time.sleep(0.07)
			os.system('cls')
			while x > 8:
				x -= 1
			while y > 7:
				y -= 1
			while x < 1:
				x += 1
			while y < 0:
				y += 1
			n = (y*18)+(x*2) -1
			text = ' '+' '.join(list('\n'.join(i.split('|')))).replace('0',background).replace('1',wall	)
			text = list(text)
			if text[n] == wall:
				win = 1
				break
			else:
				text[n] = character
			text = ''.join(text)
			print((f'{color}'+text).replace(wall,f'{wallcolor}{wall}{color}').replace(character,f'{colorcharacter}{character}{color}'))

		if win == 0:
			print(f"{color}You Won!")
		else:
			os.system('cls')
			print(f"{wallcolor}Game Over!")
		keyboard.unhook_all_hotkeys()
		time.sleep(1)
		os.system('cls')
	else:
		turn = 0
		x0,y0=2,2
		originalbg = ["10000000|00000000|00000000|00000000|00000000|00000000|00000000|00000000",
		"01000000|00000000|00000000|00000000|00000000|00000000|00000000|00000000",
		"00100000|00000000|00000000|00000000|00000000|00000000|00000000|00000000",
		"00010000|00000000|00000000|00000000|00000000|00000000|00000000|00000000",
		"00001000|00000000|00000000|00000000|00000000|00000000|00000000|00000000",
		"00000100|00000000|00000000|00000000|00000000|00000000|00000000|00000000",
		"00000010|00000000|00000000|00000000|00000000|00000000|00000000|00000000",
		"00000001|00000000|00000000|00000000|00000000|00000000|00000000|00000000",
		"00000000|00000001|00000000|00000000|00000000|00000000|00000000|00000000",
		"00000000|00000000|00000001|00000000|00000000|00000000|00000000|00000000",
		"00000000|00000000|00000000|00000001|00000000|00000000|00000000|00000000",
		"00000000|00000000|00000000|00000000|00000001|00000000|00000000|00000000",
		"00000000|00000000|00000000|00000000|00000000|00000001|00000000|00000000",
		"00000000|00000000|00000000|00000000|00000000|00000000|00000001|00000000",
		"00000000|00000000|00000000|00000000|00000000|00000000|00000000|00000001",
		"00000000|00000000|00000000|00000000|00000000|00000000|00000000|00000010",
		"00000000|00000000|00000000|00000000|00000000|00000000|00000000|00000100",
		"00000000|00000000|00000000|00000000|00000000|00000000|00000000|00001000",
		"00000000|00000000|00000000|00000000|00000000|00000000|00000000|00010000",
		"00000000|00000000|00000000|00000000|00000000|00000000|00000000|00100000",
		"00000000|00000000|00000000|00000000|00000000|00000000|00000000|01000000",
		"00000000|00000000|00000000|00000000|00000000|00000000|00000000|10000000",
		"00000000|00000000|00000000|00000000|00000000|00000000|10000000|00000000",
		"00000000|00000000|00000000|00000000|00000000|10000000|00000000|00000000",
		"00000000|00000000|00000000|00000000|10000000|00000000|00000000|00000000",
		"00000000|00000000|00000000|10000000|00000000|00000000|00000000|00000000",
		"00000000|00000000|10000000|00000000|00000000|00000000|00000000|00000000",
		"00000000|10000000|00000000|00000000|00000000|00000000|00000000|00000000"]
		now = time.time()
		while True:
			turn +=1
			time.sleep(.05)
			while x > 8:
				x -= 1
			while y > 7:
				y -= 1
			while x < 1:
				x += 1
			while y < 0:
				y += 1
			if turn%5 == 0:
				closest = []
				closest.append(x0-x) #it goes left
				closest.append(x-x0) #it goes right
				closest.append(y0-y) #it goes up
				closest.append(y-y0) #it goes down
				if max(closest) == closest[0]:
 					x0 -= 1
				elif max(closest) == closest[1]:
					x0 += 1
				elif max(closest) == closest[2]:
					y0 -= 1
				elif max(closest) == closest[3]:
					y0 += 1
			i = originalbg[0]
			originalbg.append(originalbg[0])
			originalbg.pop(0)
			bg = ' '+' '.join(list('\n'.join(i.split('|')))).replace('0',background).replace('1',wall)
			bg = list(bg)
			bg[(y0*18)+(x0*2) -1] = wall
			if bg[(y*18)+(x*2) -1] == wall:
				break
			else:
				bg[(y*18)+(x*2) -1] = character
			bg = ''.join(bg)
			os.system('cls')
			print(((f'{color}'+bg).replace(wall,f'{wallcolor}{wall}{color}').replace(character,f'{colorcharacter}{character}{color}')))
		os.system('cls')
		print(f'{wallcolor}Game Over! You lasted {round(time.time()-now)} Seconds!')
		input("Press enter to continue... ")
		keyboard.unhook_all_hotkeys()
		os.system('cls')

print(f"{color}Goodbye!")
time.sleep(.5)