import csv
import collections
import math
import time
# comment code, try doing scipy stuff instead

def process_files():
    groups = [[] for x in range(20)]
    article_nums = open("./label.csv")
    article_reader = csv.reader(article_nums)
    lineCounter = 1
    for row in article_reader:
        d = collections.Counter()
        groups[int(row[0]) - 1].append(d)
        lineCounter += 1
    word_counts = open("./data50.csv")
    word_reader = csv.reader(word_counts)
    for row in word_reader:
        article_num = int(row[0]) - 1
        group_num = article_num / 50
        article_num = article_num % 50
        word = int(row[1])
        count = int(row[2])
        groups[group_num][article_num] [word] = count
    return groups

def group_sim(group1, group2, jacc = True):

    sim_sum = 0.0
    count = len(group1) * len(group2)
    for i in xrange(len(group1)):
        for j in xrange(len(group2)):
            sim_sum += sum((group1[i]&group2[j]).values())/(sum((group1[i]|group2[j]).values()))
    return sim_sum/count

old_time = time.clock()
all_articles = process_files()
print time.clock() - old_time
old_time = time.clock()
for i in xrange(len(all_articles)):
    sumSims = 0
    for j in xrange(i, len(all_articles)):
        x =  group_jacc_sim(all_articles[i],all_articles[j], True)
        sumSims += x # not doing anything with it currently

print time.clock() - old_time
old_time = time.clock()
