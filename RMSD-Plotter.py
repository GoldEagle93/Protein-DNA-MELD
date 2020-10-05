#!/usr/bin/env python

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input_file', type=str, required=True, dest='input_file', help= 'input file name with extension')
parser.add_argument('-s', '--skip', type=int, default=0, dest='skip', help= 'number of steps between every trajectory writing')
args = parser.parse_args()

def plot_RMSD():

    '''
Plots RMSD from file provided in -i option.
X-axis can be shown as time if trajectory writing interwal (in number of steps) is provided in -s, otherwise, frame number will be used.
    '''

    df = pd.read_csv(args.input_file, sep='\s+')

    if args.skip == 0:
        ax = plt.gca()
        for i in df.columns[1:]:
            df.plot(kind='line',x=df.columns[0],y=i, ax = ax)
        plt.title('RMSD')
        plt.ylabel('RMSD (Å)')
        plt.xlabel('Frames')
        plt.show()
    else:
        timed_df = df.apply(lambda x: int(args.skip)*x*.001 if x.name == df.columns[0] else x)
        ax = plt.gca()
        for i in timed_df.columns[1:]:
            timed_df.plot(kind='line',x=timed_df.columns[0],y=i, ax = ax)        
        plt.title('RMSD')
        plt.ylabel('RMSD (Å)')
        plt.xlabel('Time (ns)')
        plt.show()

plot_RMSD()