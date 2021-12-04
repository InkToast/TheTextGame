import os
os.system('cls')
os.system('title InkOnToast\'s 1.4 release ')
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
		setting = ''
		while True:
			setting = input("Press 1 to change gane text, Press 2 to change game colours: ")
			if '1' in setting or '2' in setting:
				break
			else:
				continie
		if setting.lower()[0] == '1':
			character = input(f"{color}[>>>] Please enter text of character (X by default): ")[0]
			background = input(f"{color}[>>>] Please enter text of background (. by default): ")[0]
			wall = input(f"{color}[>>>] Please enter text of walls (# by default): ")[0]
		else:
			color = input(f"{Style.RESET_ALL}[>>>] Do you want colour on the game, N for text to look like this, Y for colour in game: ")
			if color[0].lower() == 'n':
				color = Style.RESET_ALL
				wallcolor = color = Style.RESET_ALL
				colorcharacter = Style.RESET_ALL
			else:
				os.system('cls')
				colorlist = [Fore.LIGHTRED_EX,Fore.LIGHTYELLOW_EX,Fore.LIGHTGREEN_EX,Fore.LIGHTCYAN_EX,Fore.LIGHTMAGENTA_EX,Fore.WHITE]
				color = Fore.LIGHTGREEN_EX
				colors = ''
				for i in range(len(colorlist)):
					colors = colors + f'{colorlist[i]}Choose {i} for this colour\n'
				print(colors)
				while True:
					try:
						colorcharacter = input(f"{color}\nChoose your colour for your character (an X): ")
						colorcharacter = colorlist[int(colorcharacter)]
						print(f"{colorcharacter}Successfully changed character colour to this")
						break
					except:
						print(f"{wallcolor}Invalid Choice, Please choose a number.")
						continue
				while True:
					try:
						wallcolor = input(f"{color}Choose your colour for the walls (a #): ")
						wallcolor = colorlist[int(wallcolor)]
						print(f"{wallcolor}Successfully changed wall colour to this")
						break
					except:
						print(f"{wallcolor}Invalid Choice, Please choose a number.")
						continue
				while True:
					try:
						color = input(f"{color}Choose your colour for the background (a .): ")
						color = colorlist[int(color)]
						print(f"{color}Successfully changed background colour to this")
						break
					except Exception as e:
						color = Fore.LIGHTGREEN_EX
						print(e)
						print(f"{wallcolor}Invalid Choice, Please choose a number.")
						continue

		print(f"{color}Settings Completed")
		time.sleep(.3)

	now = time.time()
	os.system('cls')

	print(f'{color}Welcome back to The Text Game')
	print(f'{color}Please choose a level from the below (https://discord.gg/szA5kwJkrD)')
	print(f"{color}You may also type 'chase' or 'infinirain' for a infinite mode\n")

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
			if lvl == 'chase':
				level = 'chase'
				break
			if lvl == 'infinirain':
				level = 'infinirain'
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
	if type(level) != str:
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
	elif lvl == 'chase':
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

	else:
		prngx = [3, 3, 2, 7, 5, 4, 8, 1, 8, 5, 6, 3, 5, 4, 3, 6, 6, 2, 1, 4, 6, 2, 2, 5, 2, 7, 2, 6, 4, 1, 5, 5, 5, 7, 4, 5, 5, 5, 1, 4, 1, 5, 5, 4, 2, 4, 1, 4, 6, 2, 8, 7, 6, 6, 7, 2, 2, 6, 7, 6, 1, 5, 6, 5, 3, 1, 6, 7, 8, 8, 5, 3, 1, 3, 5, 7, 4, 6, 4, 2, 5, 4, 7, 8, 3, 2, 7, 5, 1, 4, 7, 6, 2, 5, 7, 2, 8, 6, 6, 4, 6, 7, 5, 4, 6, 3, 2, 3, 2, 3, 7, 6, 5, 2, 6, 3, 6, 4, 6, 4, 2, 8, 7, 7, 6, 6, 6, 4, 7, 2, 2, 3, 1, 1, 5, 4, 7, 6, 8, 4, 5, 6, 1, 3, 5, 6, 7, 5, 7, 3, 5, 1, 8, 2, 6, 2, 6, 1, 5, 6, 1, 5, 3, 1, 1, 1, 3, 8, 4, 5, 4, 4, 1, 8, 1, 4, 4, 5, 3, 5, 1, 6, 1, 2, 1, 7, 5, 2, 5, 7, 4, 7, 3, 1, 8, 3, 8, 7, 7, 7]
		x0,x1,x2 = prngx[0],prngx[1],prngx[2]
		prngx.append(prngx[0])
		prngx.pop(0)
		prngx.append(prngx[0])
		prngx.pop(0)
		prngx.append(prngx[0])
		prngx.pop(0)
		y0,y1,y2 = 0,0,0
		turn = 0
		now = time.time()
		while True:
			turn += 1
			time.sleep(.07)
			text = '00000000|00000000|00000000|00000000|00000000|00000000|00000000|00000000'
			text = ' '+' '.join(list('\n'.join(text.split('|')))).replace('0',background)
			y0 += 1
			if turn > 3:
				y1 += 1
			if turn > 6:
				y2 += 1
			if y0 > 7:
				x0 = prngx[0]	
				prngx.append(prngx[0])
				prngx.pop(0)
				y0 = 0
			if y1 > 7:
				x1 = prngx[0]	
				prngx.append(prngx[0])
				prngx.pop(0)
				y1 = 0
			if y2 > 7:
				x2 = prngx[0]	
				prngx.append(prngx[0])
				prngx.pop(0)
				y2 = 0
			text = list(text)
			text[(y0*18)+(x0*2) -1] = wall
			text[(y1*18)+(x1*2) -1] = wall
			text[(y2*18)+(x2*2) -1] = wall
			while x > 8:
				x -= 1
			while y > 7:
				y -= 1
			while x < 1:
				x += 1
			while y < 0:
				y += 1
			if text[(y*18)+(x*2) -1] == wall:
				break
			else:
				text[(y*18)+(x*2) -1] = character
			text = ''.join(text)
			os.system('cls')
			print((f'{color}'+text).replace(wall,f'{wallcolor}{wall}{color}').replace(character,f'{colorcharacter}{character}{color}'))
		print(f'{wallcolor}Game Over, You survived for {round(time.time()-now)} Seconds')
		input("Press enter to continue...")
		os.system('cls')
		keyboard.unhook_all_hotkeys()

print(f"{color}Goodbye!")
time.sleep(.5)