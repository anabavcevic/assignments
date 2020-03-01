# -*- coding: utf-8 -*-
# Algorithm to process revision commit to svn.

from commit import Commit

DEBUG = True

file_data = [line.strip() for line in open('C:/Users/Ana/Documents/GitHub/assignments/CA2/data_in/dataset_CA2.log')]
if DEBUG:
    print(len(file_data))

sep = 72 * '-'
line_index = 0

commits = []

while (line_index < len(file_data) and line_index >= 0):
    if line_index + 1 >= len(file_data):
        break
    details = file_data[line_index + 1].split(' | ')
    
while (line_index < len(file_data) and line_index >= 0):
    if line_index + 1 >= len(file_data):
        break
    details = file_data[line_index + 1].split(' | ')
    
    #############
    changes = {}
    changes['added'] = 0
    changes['modified'] = 0
    changes['deleted'] = 0
    changes['changes'] = 0
    
    #while - loop condition (was the last line NOT empty?)
    second_index = line_index + 3
    
    while second_index < len(file_data):
        line = file_data[second_index]
        if line == '':
            break
        changes['changes'] = changes['changes'] + 1
        if 'A ' in line:
            changes['added'] =  changes['added'] + 1
        if 'M ' in line:
            changes['modified'] =  changes['modified'] + 1
        if 'D ' in line:
            changes['deleted'] =  changes['deleted'] + 1
        second_index = second_index + 1
    #############
    data = file_data
    start_index = line_index + 3
    ##
    index = start_index
    while index < len(data):
        line = data[index]
        if line == '':
            break
        index = index + 1
    return_value = data[index + 1]
    ##
    comment = return_value
    #############

    commits.append(Commit(details, changes, comment))
    line_index = file_data.index(sep, line_index + 1)

if DEBUG:
    print(len(commits))
csv_file = open('C:/Users/Ana/Documents/GitHub/assignments/CA2/data_out/dataset_output.csv', 'w')
csv_file.write('revision,name,date,time,number of lines,comment,added,modified,deleted,changes\n')
for commit in commits:
    csv_file.write(str(commit))
csv_file.close()

