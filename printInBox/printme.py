import sys
import math
import argparse

def _print(margin, border, strings):
	if len(border) > 1:
		border = border[0]
	if isinstance(strings, str):
		strings = List(strings)
	chars = max([len(s) for s in strings])
	row_size = chars + margin * 2
	
	def __print(string):
		print(border + string + border)

	def header():
		__print(border * (row_size))

	def empty():
		__print(" " * row_size)

	def text(row):
		row_margin = row_size - len(row)
		halfmargin = row_margin / 2.0
		leftmargin = halfmargin
		if halfmargin > math.floor(halfmargin):
			halfmargin = math.floor(halfmargin)
			leftmargin = halfmargin + 1

		__print( " " * int(leftmargin) + row + " " * int(halfmargin))
		

	header()
	empty()
	for s in strings:
		text(s.replace("_", " "))
	empty()
	header()

if __name__ == "__main__":

	arg_parser = argparse.ArgumentParser()

	arg_parser.add_argument('-margin', default=4, type=int)
	arg_parser.add_argument('-border', default='*', type=str)
	arg_parser.add_argument('strings', nargs='+', type=str)

	args, other = arg_parser.parse_known_args(sys.argv[1:])


	_print(args.margin, args.border, args.strings)
