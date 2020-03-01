# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 19:56:44 2020

@author: Ana
"""

#opening file/close file

def escape_quotes(str):
    return str.replace('"', '""')


infile = open("C:\\Users\\Ana\\Desktop\\prosli testovi\\samplefile.txt", 'r')
outfile = open("C:\\Users\\Ana\\Desktop\\prosli testovi\\samplefile_out.csv", 'w')

#print(infile.read())

listVar = [line for line in infile] #read lines of file in a loop

outfile.write("Hex value")
outfile.write(',')
outfile.write("Hex Description")
outfile.write(',')
outfile.write("My Column")
outfile.write('\n')


for txt in listVar:
    txt = txt.strip()
    split_txt = txt.split(';')
    outfile.write(split_txt[0])
    outfile.write(',')
    outfile.write('"' + escape_quotes(split_txt[1]) + '"')
    outfile.write(',')
    outfile.write('"' + escape_quotes(split_txt[0] + ' ' + split_txt[1]) + '"')
    outfile.write('\n')


outfile.close()
infile.close()


