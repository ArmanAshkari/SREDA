import pandas as pd
import os.path
import sys

input_label = sys.argv[1]
output_label = sys.argv[2]
min_consum = int(sys.argv[3])
if len(sys.argv) == 5:
    overwrite = sys.argv[4]
else:
    overwrite = 'N'

file_name = input_label + '.xlsx'
file_path = 'ann_consum\\' + file_name
if not os.path.exists(file_path):
    print(file_path + ' does not exist...')
    exit(1)

df = pd.read_excel(file_path)
column_names = df.columns
years = column_names[4:]

list = []
for i in range(len(df)):
    flag = False
    for year in years:
        if df.loc[i, year] >= min_consum:
            flag = True
    
    if flag:
        list.append(i)

out_df = df.iloc[list]

file_name = output_label + '.xlsx'
file_path = 'ann_consum\\' + file_name
if os.path.exists(file_path) and overwrite.__ne__('O'):
    print(file_path + ' already exists...')
    opt = input('Overwrite (y/n)?   ')
    if opt.lower().__eq__('y'):
        out_df.to_excel(file_path, index=False)
else:
    out_df.to_excel(file_path, index=False)
