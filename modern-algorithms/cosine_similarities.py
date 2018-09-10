import csv
from scipy.sparse import *
from scipy import *
import numpy as np
import time
import matplotlib.pyplot as plt
import warnings
from collections import defaultdict

def process_files_by_articles():
    # Map each article to bag of words
    articles_matrix = []
    word_counts = open("./data50.csv")
    word_reader = csv.reader(word_counts)
    new_article = True
    previous_article = 0
    for row in word_reader:
        if new_article == True:
            article_num = int(row[0]) - 1   # Going to be 0 to 49
            group_num = article_num / 50    # Going to be from 0 to 19
            new_dict = defaultdict()
            new_article = False
        article_num = int(row[0]) - 1
        word = int(row[1])
        count = int(row[2])
        if article_num != previous_article:
            articles_matrix.append((article_num - 1, group_num, new_dict))
            new_dict = defaultdict()
            new_dict[word] = count
            group_num = article_num / 50
        else:
            new_dict[word] = count
        previous_article = article_num
    articles_matrix.append((article_num, group_num, new_dict))
    return articles_matrix

def cos_sim(dictA, dictB):
    dot_product = sum([dictA[keyA]*dictB.get(keyA, 0) for keyA in dictA])
    normalization = sum(dictA[keyA]**2 for keyA in dictA)
    normalization *= sum(dictB[keyB]**2 for keyB in dictB)
    total_cosine = float(dot_product)/math.sqrt(normalization)
    return total_cosine


articles_matrix = process_files_by_articles()
classification_count = 0

baseline_matrix = np.zeros((20, 20))
for i in range(len(articles_matrix)):
    cos_sum_max = 0
    foundIndex = -1
    for j in range(len(articles_matrix)):
        if j != i:
            cos_sum_res = cos_sim(articles_matrix[i][2], articles_matrix[j][2])
            if cos_sum_res > cos_sum_max:
                cos_sum_max = cos_sum_res
                foundIndex = j
    group1 = i / 50
    group2 = foundIndex / 50
    if group1 != group2:
        classification_count += 1
    baseline_matrix[group1][group2] += 1

classification_error = float(classification_count)/1000
makeHeatMap(baseline_matrix, names, plt.cm.Blues, 'baselineCosPlot.png')
