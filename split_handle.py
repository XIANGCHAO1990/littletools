# coding=utf-8
import sys
import pandas as pd

def handle(file):
    df = pd.read_excel(file)
    items = df['liuliangjiazhuang'].map(lambda x:x.split(';'))
    for i,n in enumerate(items.values[0]):
        df['liuliangjiazhuang{}'.format(i)] = n
    df = df.drop(['liuliangjiazhuang',],axis=1)
    df.to_excel('splited_output.xlsx')          


if __name__ == '__main__':
    filepath = sys.argv[1]
    handle(filepath)