import pandas as pd
import os.path
import re
import sys

input_label = sys.argv[1]
output_label = sys.argv[2]
regex_arg = sys.argv[3]
regex_arg = regex_arg.replace('_', ' ')
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
    name = df.loc[i, 'CUSTOMER NAME']

    x = re.search(regex_arg, name.lower())
    if x:
        list.append(i)

out_df = df.iloc[list]

file_name = output_label + '.xlsx'
file_path = 'categorized\\' + file_name
if os.path.exists(file_path) and overwrite.__ne__('O'):
    print(file_path + ' already exists...')
    opt = input('Overwrite (y/n)?   ')
    if opt.lower().__eq__('y'):
        out_df.to_excel(file_path, index=False)
else:
    out_df.to_excel(file_path, index=False)
