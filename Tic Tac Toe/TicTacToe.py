
import time as t
import sys
import os
#import pygame
clear = lambda: os.system('cls')
# Start of Program


''' 1 2 3
		4 5 6
		7 8 9
'''
# Defining the spots to be replaced by X's or O's
s1 = 1
s2 = 2
s3 = 3
s4 = 4
s5 = 5
s6 = 6
s7 = 7
s8 = 8
s9 = 9

# Function that prints the board

def printRows():
		print("\n")
		print(s1, s2, s3)
		print(s4, s5, s6)
		print(s7, s8, s9)


#Asks for input from player with X

def askX():
		def check_stringX(x):
				if type(x) == str:
						print("That spot is already taken! Please choose another.")
						askX()
				else:
						pass


		while True:
				try:
						ansX = int(input("Please type the number you would like to place your X on:"))
						if ansX == 1:
								global s1
								check_stringX(x = s1)
								s1 = 'X'
								
						elif ansX == 2:
								global s2
								check_stringX(x = s2)
								s2 = 'X'
						elif ansX == 3:
								global s3
								check_stringX(x = s3)
								s3 = 'X'
						elif ansX == 4:
								global s4
								check_stringX(x = s4)
								s4 = 'X'
						elif ansX == 5:
								global s5
								check_stringX(x = s5)
								s5 = 'X'
						elif ansX == 6:
								global s6
								check_stringX(x = s6)
								s6 = 'X'
						elif ansX == 7:
								global s7
								check_stringX(x = s7)
								s7 = 'X'
						elif ansX == 8:
								global s8
								check_stringX(x = s8)
								s8 = 'X'
						elif ansX == 9:
								global s9
								check_stringX(x = s9)
								s9 = 'X'
						else:
								print("Please type a number 1 through 9 only!")
								askX()
						break
				except ValueError:
						print("Please type an integer only!")
						continue
				
		
def askO():
		def check_stringO(o):
				if type(o) == str:
						print("That spot is already taken! Please choose another.")
						askO()
				else:
						pass

		while True:
				try:
						ansX = int(input("Please type the number you would like to place your O on:"))
						if ansX == 1:
								global s1
								check_stringO(o = s1)
								s1 = 'O'
						elif ansX == 2:
								global s2
								check_stringO(o = s2)
								s2 = 'O'
						elif ansX == 3:
								global s3
								check_stringO(o = s3)
								s3 = 'O'
						elif ansX == 4:
								global s4
								check_stringO(o = s4)
								s4 = 'O'
						elif ansX == 5:
								global s5
								check_stringO(o = s5)
								s5 = 'O'
						elif ansX == 6:
								global s6
								check_stringO(o = s6)
								s6 = 'O'                        
						elif ansX == 7:
								global s7
								check_stringO(o = s7)
								s7 = 'O'                
						elif ansX == 8:
								global s8
								check_stringO(o = s8)
								s8 = 'O'                
						elif ansX == 9:
								global s9
								check_stringO(o = s9)
								s9 = 'O'                                
						else:
								print("Please type a number 1 through 9 only!")
								askX()
						break
				except ValueError:
						print("Please type an integer only!")
						continue


#Runs the ask X protocal with other features attached

def runX():
		printRows()
		askX()
		clear()

#Runs the ask O protocal with other features attached

def runO():
		printRows()
		askO()
		clear()

def check_win():

#                                       Acrosss 1 2 3                                                                   Across 4 5 6                                    Across 7 8 9                                                                    Down 1 4 7                                                              Down 2 5 8                                                                              Down 3 6 9                                                              Diagnol 1 5 9                                           Diagnol 3 5 7
		if (s1 == 'X' and s2 == 'X' and s3 == 'X') or (s4 == 'X' and s5 == 'X' and s6 == 'X') or (s7 == 'X' and s8 == 'X' and s9 == 'X') or (s1 == 'X' and s4 == 'X' and s7 == 'X') or (s2 == 'X' and s5 == 'X' and s8 == 'X') or (s3 == 'X' and s6 == 'X' and s9 == 'X') or (s1 == 'X' and s5 == 'X' and s9 == 'X') or (s3 == 'X' and s5 == 'X' and s7 == 'X'):
				printRows()
				print("X is the winner!")
				t.sleep(1)
				os.startfile("F:\Python\Projects\Tanner's Mini Games\main.bat")
				sys.exit()
		elif (s1 == 'O' and s2 == 'O' and s3 == 'O') or (s4 == 'O' and s5 == 'O' and s6 == 'O') or (s7 == 'O' and s8 == 'O' and s9 == 'O') or (s1 == 'O' and s4 == 'O' and s7 == 'O') or (s2 == 'O' and s5 == 'O' and s8 == 'O') or (s3 == 'O' and s6 == 'O' and s9 == 'O') or (s1 == 'O' and s5 == 'O' and s9 == 'O') or (s3 == 'O' and s5 == 'O' and s7 == 'O'):
				printRows()
				print("O is the winner!")
				t.sleeep(1)
				os.startfile("F:\Python\Projects\Tanner's Mini Games\main.bat")
				sys.exit()
		else:
				pass
'''
1 2 3
4 5 6
7 8 9
''' 
def run():
		runX()
		runO()
		runX()
		runO()
		runX()
		check_win()
		runO()
		check_win()
		runX()
		check_win()
		runO()
		check_win()
		runX()
		check_win()
		print("Tie!")
		t.sleep(1)
		os.startfile("F:\Python\Projects\Tanner's Mini Games\main.bat")
run()
'''
THIS IS NOW
200 LINES
OF CODE
YOUR WELCOME
''' 


