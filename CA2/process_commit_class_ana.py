# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 18:40:04 2020

@author: Ana
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 20:26:10 2020

@author: 99993
"""

# Algorithm to process revision commit to svn.

from commit import Commit

DEBUG = True

# a better way to read the lines of the file into a list in memory
def get_data():
    return [line.strip() for line in open('C:/Users/Ana/Documents/GitHub/assignments/CA2/data_in/dataset_CA2.log')]

def get_changes(data, start_index):
    changes = {}
    changes['added'] = 0
    changes['modified'] = 0
    changes['deleted'] = 0
    changes['changes'] = 0
    
    #while - loop condition (was the last line NOT empty?)
    index = start_index
    while index < len(data):
        line = data[index]
        changes['changes'] = changes['changes'] +1
        if line == '':
            break
        index = index +1
    return changes                
                
    #    increment the changes count
    
def get_commits(data):
    sep = 72 * '-'
    index = 0
    
    commits = []
    
    while (index < len(data) and index >= 0):
        if index + 1 >= len(data):
            break
        details = data[index + 1].split(' | ')
        comment = 'Renamed folder to the correct name'
        changes = get_changes(data, index+3)
        commits.append(Commit(details, changes, comment))
        index = data.index(sep, index + 1)
    return commits
    
def save_csv(commits):    
    csv_file = open('C:/Users/Ana/Documents/GitHub/assignments/CA2/data_out/dataset_output.csv', 'w')
    csv_file.write('revision,name,date,time,number of lines,comment,added,modified,deleted,changes\n')
    for commit in commits:
        csv_file.write(str(commit))
    csv_file.close()

##################################################

def main():
    data = get_data()
    if DEBUG:
        print(len(data))
    
    commits = get_commits(data)
    
    if DEBUG:
        print(len(commits))
    save_csv(commits)


main()
