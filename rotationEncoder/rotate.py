from __future__ import print_function
import sys

def scramble(lines, seq):

	ph = ["@@@", "$$$"]

	ph_index = 0
	new_lines = []
	for line in lines:
		line = line.replace(seq[0], ph[ph_index])
#		print(line.replace("a", "@@@@"))
		for x in range(1, len(seq)):
			#print(line)
			line = line.replace(seq[x], ph[not ph_index])
			line = line.replace(ph[ph_index], seq[x])
			#line = line.replace(seq[x], ph[not ph_index])
			ph_index = not ph_index
		
		#print(line)
		line = line.replace(ph[ph_index], seq[0])
		new_lines.append(line)

	return list(filter(None, new_lines))

def main(args):

	file = args[0]
	with open(file) as f:
		lines = f.readlines()

	if len(args) > 1:
		seq = list(args[1])
	else:
		seq = [" ", "e", ".", "i", "3", "y", ",", "o"]

	return scramble(lines, seq)


if __name__ == "__main__":
	res = main(sys.argv[1:])
	for r in res:
		print(r, end='')

