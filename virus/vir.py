import random
import re

if __name__ == "__main__":
	current = "vir.py"
	name = random.random()
	with open("file" + str(name) + ".py", "w+") as f:
		with open(current, "r+") as c:
			for line in c:
				if re.match("/current/", line):
					f.write("	current = vir" + name + ".py")
				else:
					f.write(line)