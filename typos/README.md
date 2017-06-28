# usage

`python addtypes.py [string] [n] [alpha]`

defaults:

- string = "all work and no play makes jack a dull boy."
- n = 100
- alpha = 0.01

will write the string n times with alpha (\in [0, 1]) chance of mistake in every char.
mistakes include: duplicating char, skipping, replacing with some other char

output is <string with mistakes> (<number of mistakes>)
