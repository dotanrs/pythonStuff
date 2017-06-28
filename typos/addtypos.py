import random
import string
import sys

class mistakes:

	@staticmethod
	def duplicate(char):
		return char + char

	@staticmethod
	def skip(char):
		return ""

	@staticmethod
	def other(char):
		return random.choice(string.letters)

errors = [getattr(mistakes, function) for function in dir(mistakes) if function[0:2] != "__"]

def with_errors(in_str, rand=0.01, show_counter=False):
	
	res = ""
	count = 0

	for char in in_str:
		do_error = random.random() < rand
		if do_error:
			choose_error = random.randint(0, len(errors) - 1)
			error = errors[choose_error](char)
			res = res + error
			count += 1
		else:
			res = res + char

	if show_counter:
		return res + "\t({})".format(count)
	else:
		return res


if __name__ == "__main__":

	the_string = sys.argv[1] if len(sys.argv) > 1 else "all work and no play makes jack a dull boy."

	n = int(sys.argv[2]) if len(sys.argv) > 2 else 100 
	
	alpha = float(sys.argv[3]) if len(sys.argv) > 3 else 0.01 

	for i in range(n):
		print(with_errors(the_string, alpha))