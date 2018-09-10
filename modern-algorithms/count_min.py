import hashlib
import sys
import random

def conservative_updates(value, hash_tables, trial = None):
    bucket_numbers = determine_buckets(value, hash_tables, trial)
    minimum_cnt_value = min([hash_tables[i][bucket_numbers[i]] for i in range(len (hash_tables))])
    for i in range(len (hash_tables)):
        if minimum_cnt_value == hash_tables[i][bucket_numbers[i]]:
            hash_tables[i][ bucket_numbers[i] ] += 1

def increment(value, hash_tables, trial = None, conservative_flag = None):
    if conservative_flag == True:
        conservative_updates(value, hash_tables, trial)
        return
    bucket_numbers = determine_buckets(value, hash_tables, trial)
    for i in range(len(hash_tables)):
        hash_tables[i][ bucket_numbers[i] ] += 1

def determine_count(value, hash_tables, trial = None):
    bucket_numbers = determine_buckets(value, hash_tables, trial)
    minimum_cnt_value = sys.maxint 
    for i in range(len(hash_tables)):
        minimum_cnt_value = min( minimum_cnt_value, hash_tables[i][ bucket_numbers[i] ] )
    return minimum_cnt_value

def determine_buckets(value, hash_tables, trial = None):
    bucket_numbers = [0 for i in range(len(hash_tables))]
    if trial is None:
        trial = ""
    md5_score = hashlib.md5()
    md5_score.update(str(value) + str(trial))
    md_hash_result = md5_score.hexdigest()
    for i in range(len (hash_tables)):
        s = md_hash_result[2*i : 2*i+2]
        y = int(s, 16)
        bucket_numbers[i] = y
    return bucket_numbers

def find_heavy_hitters(hash_tables, lower_value, upper_value, number_of_elements, trial = None):
    number_of_heavy_hitters = 0
    for i in range(lower_value, upper_value + 1):
        if determine_count(i, hash_tables, trial) * 100 > number_of_elements:
            number_of_heavy_hitters += 1
    return number_of_heavy_hitters

# data streams for count-min sketch
def datastream():
    count = 0
    current_list = []
    for i in range(9):
        for j in range(1000):
            currentValue = j + 1 + 1000 * i
            for k in range(i + 1):
                current_list.append(currentValue)
                count += 1
    for i in range(50):
        currentValue = 9000 + i + 1
        for k in range((i + 1) * (i + 1)):
            current_list.append(currentValue)
            count += 1
    return (count, current_list)

names = ["fwd", "rev", "rand"]
conserv_flag = False
for i in range(len(names)):
    print names[i]
    total_frequency = 0
    total_heavy_hitters = 0
    for inner_index in range(10):
        hash_tables = [[0 for j in range(256)] for i in range(4)]
        result = datastream()
        if i == 0:
            allNums = result[1]
        elif i == 1:
            allNums = list(reversed(result[1]))
        else:
            allNums = result[1]
            random.shuffle(allNums)
        count = result[0]
        for num in allNums:
            increment(num, hash_tables, inner_index, conserv_flag)
        total_frequency += determine_count(9050, hash_tables, inner_index)
        total_heavy_hitters +=  find_heavy_hitters(hash_tables, 1, 9050, count, inner_index)
    print "9050 estimate: ", 
    	total_frequency / 10.0, "Heavy hitters estimate: ", total_heavy_hitters / 10.0

