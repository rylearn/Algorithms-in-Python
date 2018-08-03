#!/bin/python

import math
import os
import random
import re
import sys


def solve(s):
	pattern = "\w*\s*"
	temp_list = re.findall(pattern, s)
	new_list = []
	for curr_str in temp_list:
		new_list.append(curr_str.capitalize())
	res = "".join(new_list)
	return res

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	s = raw_input()

	result = solve(s)

	fptr.write(result + '\n')

	fptr.close()
