import pandas as pd
import os.path
import sys

input_label = sys.argv[1]
output_label = sys.argv[2]
if len(sys.argv) == 4:
    overwrite = sys.argv[3]
else:
    overwrite = 'N'

out_file = output_label + '.xlsx'
files = os.listdir('categorized')
if out_file in files:
    files.remove(out_file)

x = set()

for file in files:
    file_path = 'categorized\\'+ file
    df = pd.read_excel(file_path)
    for i in range(len(df)):
        x.add(df.loc[i, 'CUSTOMER CODE'])

print(len(x))

file_name = input_label + '.xlsx'
file_path = 'ann_consum\\' + file_name
if not os.path.exists(file_path):
    print(file_path + ' does not exist...')
    exit(1)

df = pd.read_excel(file_path)

list = []
for i in range(len(df)):
    code = df.loc[i, 'CUSTOMER CODE']

    if code not in x:
        list.append(i)

out_df = df.iloc[list]

file_name = output_label + '.xlsx'
file_path = '.\\' + file_name
if os.path.exists(file_path) and overwrite.__ne__('O'):
    print(file_path + ' already exists...')
    opt = input('Overwrite (y/n)?   ')
    if opt.lower().__eq__('y'):
        out_df.to_excel(file_path, index=False)
else:
    out_df.to_excel(file_path, index=False)