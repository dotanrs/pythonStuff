import addtypos
import sys

def times_until_mistake(n=100, inpt="dotan", outpt="botan", alpha=0.1):
	counters = []
	for i in range(n):
		counter = 0
		while True:
			res = addtypos.with_errors(inpt, alpha)
			counter += 1
			if (res == outpt):
				#print(counter, res)
				break

		counters.append(counter)

	print(float(sum(counters)) / len(counters))


if __name__ == "__main__":

	input_string = sys.argv[1] if len(sys.argv) > 1 else "dotan"

	required_error = sys.argv[2] if len(sys.argv) > 2 else "yotam"

	alpha = float(sys.argv[3]) if len(sys.argv) > 3 else 0.1

	n = int(sys.argv[4]) if len(sys.argv) > 4 else 1

	times_until_mistake(n, input_string, required_error, alpha)