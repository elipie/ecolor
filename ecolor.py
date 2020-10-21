from time import sleep
import sys
#ex:  
bold_blue = "\033[1;34m"
bold_cyan="\033[1;36m"
bold_white="\033[1;37m" 
bold_green="\033[1;32m"
bold_orange ="\033[1;33m"
bold_pink = "\033[1;31m"
bold_black = "\033[1;30m"
bold_purple = "\033[1;35m"

#bold/ other decorators:
bold = "\033[1m" 
reset  = "\033[0m"
dim = "\033[2m"
underline = "\033[4m"
bg = "\033[44m"

#colors 
blue="\033[0;34m"
cyan="\033[0;36m"
white="\033[0;37m" 
green="\033[0;32m"
orange ="\033[0;33m"
pink = "\033[0;31m"
black = "\033[0;30m"
purple = "\033[0;35m"



# Change later maybe :
# def ecolor(text, color, decorator)
def ecolor(text, color):
	if color == "blue":
		print(blue+text)
	elif color == "cyan":
		print(cyan+text)
	elif color == "green":
		print(green+text)
	elif color == "orange":
		print(orange+text)
	elif color == "purple":
		print(purple+text)
	elif color == "red" or color == "pink":
		print(pink+text)
	elif color == "reset":
		print(reset)
	elif color == "bold":
		print(bold+text)
	elif color == "bg":
		print(bg+text)
	elif color == "underline":
		print(underline+text)

	elif color == "dim":
		print(dim+text)
	elif color == "bold_blue":
		print(bold_blue+text)
	elif color == "bold_cyan":
		print(bold_cyan+text)
	elif color == "bold_green":
		print(bold_green+text)
	elif color == "bold_orange":
		print(bold_orange+text)
	elif color == "bold_purple":
		print(bold_purple+text)
	elif color == "bold_pink" or color == "bold_red":
		print(bold_pink+text)
	elif color == "bold_black":
		print(bold_black+text)
	else:
		raise NameError('Invalid Color name')
def slow_color(text, color, slptime):
	if color == "blue":
		slow_print(blue+text, slptime)
	elif color == "cyan":
		slow_print(cyan+text, slptime)
	elif color == "green":
		slow_print(green+text, slptime)
	elif color == "orange":
		slow_print(orange+text, slptime)
	elif color == "purple":
		slow_print(purple+text, slptime)
	elif color == "red" or color == "pink":
		slow_print(pink+text, slptime)
	elif color == "reset":
		slow_print(reset, slptime)
	elif color == "bold":
		slow_print(bold+text, slptime)
	elif color == "bg":
		slow_print(bg+text)
	elif color == "underline":
		slow_print(underline+text, slptime)

	elif color == "dim":
		slow_print(dim+text, slptime)
	elif color == "bold_blue":
		slow_print(bold_blue+text, slptime)
	elif color == "bold_cyan":
		slow_print(bold_cyan+text, slptime)
	elif color == "bold_green":
		slow_print(bold_green+text, slptime)
	elif color == "bold_orange":
		slow_print(bold_orange+text, slptime)
	elif color == "bold_purple":
		slow_print(bold_purple+text, slptime)
	elif color == "bold_pink" or color == "bold_red":
		slow_print(bold_pink+text, slptime)
	elif color == "bold_black":
		slow_print(bold_black+text, slptime)
	else:
		raise NameError('Invalid Color name')
def slow_print(str, slptime):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    sleep(slptime)
