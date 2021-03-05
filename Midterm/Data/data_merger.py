'''
    See those xls files here... they are in different categoroies
    So let me merge them first
    Hey, before starting the engine, gotta install that xlrd by pip install xlrd
'''
# Libs import
import os 
import pandas as pd 
import xlwt

cwd = os.path.abspath('./Data/Data')
files = os.listdir(cwd)

print(str(files))

df = pd.DataFrame()
for file in files:
    if file.endswith('.xls'):
        df = df.append(pd.read_excel('./Data/Data/' + file), ignore_index=True) 
df.head() 
merge_path = "./Data/dataset_merged.xls"
df.to_excel(merge_path)