import math
import pandas as pd
import os.path
import sys

output_label = sys.argv[1]
min_consum = int(sys.argv[2])
if len(sys.argv) == 4:
    overwrite = sys.argv[3]
else:
    overwrite = 'N'

years = ['16', '17', '18', '19', '20']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
column_names = ['LED.MN', 'INVOICE NO', 'ACTUAL CONSM', 'BILLED CONSM']

dict = {}
list = []
x = 0
files = os.listdir('data\\bulk_invoice')
for file in files:
    file_path = 'data\\bulk_invoice\\'+ file
    df = pd.read_excel(file_path)
    cust_name = df.iloc[6, 9]
    cust_addr = df.iloc[8, 9]

    temp_dict = {}
    temp_dict['CUST CODE'] = file.split('.')[0]
    temp_dict['CUST NAME'] = cust_name
    temp_dict['CUST ADDR'] = cust_addr
    for year in years:
        for month in months:
            month_year = month + ' ' + year
            temp_dict[month_year] = 0
    
    df = pd.read_excel(file_path, usecols=column_names, skiprows=11, skipfooter=1)

    for i in range(len(df)):
        bill_consum = df.loc[i, 'BILLED CONSM']
        if not math.isnan(bill_consum):
            bill_month = df.loc[i, 'LED.MN']
            temp_dict[bill_month] = bill_consum
    
    flag = False
    for year in years:
        ann_consum = 0
        for month in months:
            month_year = month + ' ' + year
            mth_consum = temp_dict[month_year]
            ann_consum = ann_consum + mth_consum
        temp_dict['20' + year] = ann_consum
        if ann_consum >= min_consum:
            flag = True

    if flag:
        list.append(x)    
    x = x + 1
    
    dict[file] = temp_dict

out_df = pd.DataFrame(dict.values())

file_name = output_label + '.xlsx'
file_path = '.\\' + file_name
if os.path.exists(file_path) and overwrite.__ne__('O'):
    print(file_path + ' already exists...')
    opt = input('Overwrite (y/n)?   ')
    if opt.lower().__eq__('y'):
        out_df.to_excel(file_path, index=False)
else:
    out_df.to_excel(file_path, index=False)

out_df = out_df.iloc[list]

file_name = output_label + '_filtered.xlsx'
file_path = '.\\' + file_name
if os.path.exists(file_path) and overwrite.__ne__('O'):
    print(file_path + ' already exists...')
    opt = input('Overwrite (y/n)?   ')
    if opt.lower().__eq__('y'):
        out_df.to_excel(file_path, index=False)
else:
    out_df.to_excel(file_path, index=False)
        

# df = pd.read_excel('data\\bulk_invoice\\04-060-0001.xlsx', usecols=column_names, skiprows=11, skipfooter=1)
# df = pd.read_excel('data\\bulk_invoice\\04-060-0001.xlsx')

# f = open("demofile3.txt", "w")
# f.write(df.to_string())
# f.close()

# print(df.iloc[6, 9])
# print(df.iloc[8, 9])
# print(len(df))