
import csv
from scipy.sparse import *
from scipy import *
import numpy as np
import time
import matplotlib.pyplot as plt
import warnings
from collections import defaultdict

def makeHeatMap(data, names, color, outputFileName):
    #to catch "falling back to Agg" warning
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        
        fig, ax = plt.subplots()
        #create the map w/ color bar legend
        heatmap = ax.pcolor(data, cmap=color)
        cbar = plt.colorbar(heatmap)

        # put the major ticks at the middle of each cell
        ax.set_xticks(np.arange(data.shape[0])+0.5, minor=False)
        ax.set_yticks(np.arange(data.shape[1])+0.5, minor=False)

        # want a more natural, table-like display
        ax.invert_yaxis()
        ax.xaxis.tick_top()

        ax.set_xticklabels(range(1, 21))
        ax.set_yticklabels(names)

        plt.tight_layout()

        plt.savefig(outputFileName, format = 'png')
        plt.close()

def process_files():
    group_matrix = [[defaultdict() for x in range(50)] for y in range(20)]
    word_counts = open("./data50.csv")
    word_reader = csv.reader(word_counts)
    for row in word_reader:
        article_num = int(row[0]) - 1	# Going to be 0 to 49
        group_num = article_num / 50
        article_num = article_num % 50
        word = int(row[1])
        count = int(row[2])
        group_matrix[group_num][article_num][word] = count 
    return group_matrix

def jaccard_similarity(group_matrix):
    # compare groupA, groupB
    jaccard_matrix = np.zeros((20, 20))
    for i in range(len(group_matrix)):
        for j in range(i, len(group_matrix)):
            groupA = group_matrix[i]
            groupB = group_matrix[j]

            total_jaccard = 0
            count = 0
            for articleA in range(len(groupA)):
                dictA = groupA[articleA]
                for articleB in range(len(groupB)):
                    dictB = groupB[articleB]

                    sum_min = sum(min(dictB[key], dictA.get(key, 0)) for key in dictB)
                    sum_max = 0

                    for (keyA, valueA) in dictA.items():
                        sum_max += max(dictA[keyA], dictB.get(keyA, 0))

                    for (keyB, valueB) in dictB.items():
                        if dictB.get(keyB, -1) == -1:
                            sum_max += dictB[keyB]

                    total_jaccard += sum_min/sum_max
                    count += 1
                    
            average_jaccard = float(total_jaccard)/count
            jaccard_matrix[i][j] = average_jaccard
            jaccard_matrix[j][i] = average_jaccard
    return jaccard_matrix

def l2_similarity(group_matrix):
    # compare groupA, groupB
    average_l2_matrix = np.zeros((20, 20))
    for i in range(len(group_matrix)):
        for j in range(i, len(group_matrix)):
            groupA = group_matrix[i]
            groupB = group_matrix[j]

            total_l2 = 0
            count = 0
            for articleA in range(len(groupA)):
                dictA = groupA[articleA]
                for articleB in range(len(groupB)):
                    dictB = groupB[articleB]

                    sum_squares = sum([(dictB[key]-dictA.get(key, 0))**2 for key in dictB])

                    for (keyA, valueA) in dictA.items():
                        if dictB.get(keyA, -1) == -1:
                            sum_squares += sum((dictA[keyA])**2)

                    total_l2 += -math.sqrt(float(sum_squares))
                    count += 1
            average_l2 = float(total_l2)/count

            average_l2_matrix[i][j] = average_l2
            average_l2_matrix[j][i] = average_l2
    return average_l2_matrix

def cosine_similarity(group_matrix):
    # compare groupA, groupB
    cosine_matrix = np.zeros((20, 20))
    for i in range(len(group_matrix)):
        for j in range(i, len(group_matrix)):
            groupA = group_matrix[i]
            groupB = group_matrix[j]

            total_cosine = 0
            count = 0
            for articleA in range(len(groupA)):
                dictA = groupA[articleA]
                for articleB in range(len(groupB)):
                    dictB = groupB[articleB]

                    dot_product = sum([dictA[keyA]*dictB.get(keyA, 0) for keyA in dictA])
                    normalization = sum(dictA[keyA]**2 for keyA in dictA)
                    normalization *= sum(dictB[keyB]**2 for keyB in dictB)

                    total_cosine += float(dot_product)/math.sqrt(normalization)
                    count += 1
            average_cosine = float(total_cosine)/count

            cosine_matrix[i][j] = average_cosine
            cosine_matrix[j][i] = average_cosine
    return cosine_matrix

group_matrix = process_files()

names = []
for i in range(1, len(group_matrix)+1):
    names.append('Group ' + str(i))

jaccard_matrix = jaccard_similarity(group_matrix)
makeHeatMap(jaccard_matrix, names, plt.cm.Blues, 'jaccardPlot.png')
l2_matrix = l2_similarity(group_matrix)
makeHeatMap(l2_matrix, names, plt.cm.Blues, 'l2Plot.png')
cos_matrix = cosine_similarity(group_matrix)
makeHeatMap(cos_matrix, names, plt.cm.Blues, 'cosPlot.png')



