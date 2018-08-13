
import re

# str = 'an example word:caoskdf9234KDF_\234 t!!'
# match = re.search(r'word:\S+', str)
# # use if statement to check if you succeeded
# if match:
# 	print 'found', match.group() ## 'found word:cat'
# else:
# 	print 'did not find'


float_str = '.0'
# num = float(float_str)
# print num
match = re.search(r'(^\s*[+-]?\d*)\.(\d+\s*$)', float_str)
# use if statement to check if you succeeded
if match:
	print 'found', match.group() ## 'found word:cat'
else:
	print 'did not find'