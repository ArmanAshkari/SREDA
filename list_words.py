import pandas as pd
import os.path
import sys

input_label = sys.argv[1]
output_label = sys.argv[2]
if len(sys.argv) == 4:
    overwrite = sys.argv[3]
else:
    overwrite = 'N'

file_name = input_label + '.xlsx'
file_path = '.\\' + file_name
if not os.path.exists(file_path):
    print(file_path + ' does not exist...')
    exit(1)

df = pd.read_excel(file_path)

dict = {}

for i in range(len(df)):
    name = df.loc[i, 'CUSTOMER NAME']
    words = name.split()
    for word in words:
        if word not in dict:
            temp_dict = {}
            temp_dict['Word'] = word
            temp_dict['Frequency'] = 0
            dict[word] = temp_dict
        dict[word]['Frequency'] = dict[word]['Frequency']  + 1
 
out_df = pd.DataFrame(dict.values())
out_df = out_df.sort_values(by=['Frequency'], ascending=False)

file_name = output_label + '.xlsx'
file_path = '.\\' + file_name
if os.path.exists(file_path) and overwrite.__ne__('O'):
    print(file_path + ' already exists...')
    opt = input('Overwrite (y/n)?   ')
    if opt.lower().__eq__('y'):
        out_df.to_excel(file_path, index=False)
else:
    out_df.to_excel(file_path, index=False)