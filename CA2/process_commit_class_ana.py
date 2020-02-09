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
    changes['added'] = 1
    changes['modified'] = 2
    changes['deleted'] = 3
    changes['changes']= 4
    #while - loop condition (was the last line NOT empty?)
    #    increment the changes count
    
    return changes
    
def get_commits(data):
    sep = 72 * '-'
    index = 0
    
    commits = []
    
    while index < len(data):
        try:
            details = data[index + 1].split(' | ')
            comment = 'Renamed folder to the correct name'
            changes = get_changes(data, index+3)
            commits.append(Commit(details, changes, comment))
            index = data.index(sep, index + 1)
        except:
            index = len(data)
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
