import os
import msvcrt

def menu(content, menus):
	os.system("cls")
	print("═════════════════════════════════════════════════")
	print("                      \33[93mAIO\33[0m                        ")
	print("═════════════════════════════════════════════════")
	if(content != ""):
		print("\n" + content)
	print()
	if(len(menus) != 0):
		i = 1
		for menu in menus:
			print(" [" + str(i) + "] " + menu)
			i += 1
		print("\n" + "═════════════════════════════════════════════════")

	return

def notificator(text, color, borderLen, parentLen):
	sym1 = "┌"
	sym2 = "─"
	sym3 = "┐"
	sym4 = "│"
	sym5 = "└"
	sym6 = "┘"
	textLen = len(text)
	splitTextLen = int(textLen / 2)
	splitBorderLen = int(borderLen / 2)
	colorReset = "\33[0m"
	confirm = "Press any key to continue..."
	confirmLen = len(confirm)
	splitConfirmLen = int(confirmLen / 2)
	intPosition = int((parentLen - (borderLen + 2)) / 2)
	strPosition = ""

	if(textLen <= 0):
		print("Error 1")
		return
	elif (color >= 1 & color <= 2) == False:
		print("Error 2")
		return
	elif(borderLen <= 0):
		print("Error 3")
		return
	
	if(textLen > borderLen):
		print("Error 3")
		return
	elif(borderLen > parentLen):
		print("Error 4")
		return

	if(color == 1):
		color = "\33[92m"
	elif(color == 2):
		color = "\33[91m"

	i = 1
	while(i <= intPosition):
		strPosition += " "
		i += 1
	
	print(strPosition + sym1, end='')

	i = 1
	while(i <= borderLen):
		print(sym2, end='')
		i += 1
	
	print(sym3)

	print(strPosition + sym4, end='')
	i = 1
	while(i <= (splitBorderLen - splitTextLen)):
		print(" ", end='')
		i += 1
	
	print(color + text + colorReset, end='')

	i = 1
	while(i <= (borderLen - ((splitBorderLen - splitTextLen) + textLen))):
		print(" ", end='')
		i += 1
	
	print(sym4)
	print(strPosition + sym4, end='')

	i = 1
	while(i <= (splitBorderLen - splitConfirmLen)):
		print(" ", end='')
		i += 1
	
	print(confirm, end='')

	i = 1
	while(i <= (borderLen - ((splitBorderLen - splitConfirmLen) + confirmLen))):
		print(" ", end='')
		i += 1
		
	print(sym4)
	print(strPosition + sym5, end='')

	i = 1
	while(i <= borderLen):
		print(sym2, end='')
		i += 1
		
	print(sym6)
	msvcrt.getch()
	return