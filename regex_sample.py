
import re

pattern = re.compile(r'(\w+):(.*)')
pattern_tab = re.compile(r'    ')
pattern_equals = re.compile(r'(\s*\w+)(:)(\S*\w+)')

with open('text_output.txt') as fp:
    file_lines = fp.readlines()

dict_patterns = {} # dictionary of dictionaries
for i in range(len(file_lines)):
    is_member = pattern_tab.search(file_lines[i])

    if not is_member:
        success = pattern.search(file_lines[i])
        if success != None:
            key = success.group(1)
            dict_patterns[key] = {}

    found_pats = pattern_equals.findall(file_lines[i])
    for j in range(len(found_pats)):
        inner_key = found_pats[j][0].strip()
        inner_value = found_pats[j][2].strip()
        dict_patterns[key][inner_key] = inner_value

# for key, value in dict_patterns.items():
#     print(key)
#     print(value)
print(dict_patterns['en9'])