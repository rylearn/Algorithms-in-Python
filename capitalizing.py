#!/bin/python
import math
import os
import re

def capitalize_words(s):
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
	capitalized_words = capitalize_words(s)
	fptr.write(capitalized_words + '\n')
	fptr.close()
