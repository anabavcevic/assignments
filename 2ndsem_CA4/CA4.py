#!/usr/bin/python3

## code calculates  mean of population,
## max of highest point
## plots a visualisation for 10 most populated croatian islands 
##github: 

import matplotlib.pyplot as plt
import pandas
import sys

def main(argv):
    df = pandas.read_csv(
        argv[1] if len(argv) > 1
        else 'CA1Ana_1.csv',
        index_col=0,
        usecols=[0, 1, 2, 3, 4])

    df['Pop_Dens'] = df['Population'] / df['Area']

    top_dens = df[['Area', 'Highest Point', 'Pop_Dens']].sort_values(
            ['Pop_Dens']
        ).nlargest(
            10, ['Pop_Dens'])

    dens_plt = top_dens.plot(kind='line')

    plt.show()
    
    print( df["Population"].mean())

    print( df["Highest Point"].max())



if __name__ == '__main__':
    main(sys.argv)
