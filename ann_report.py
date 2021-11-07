import pandas as pd
import os.path
import math

years = ['2016', '2017', '2018', '2019', '2020']
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
# years = ['2016', '2017']
# months = ['01', '02', '03', '04']

file_path = 'mth_consum.xlsx'
if not os.path.exists(file_path):
    print(file_path + ' does not exist...')
    exit(1)

df = pd.read_excel(file_path)
column_names = df.columns

list = []
for i in range(len(df)):
    temp_dict = {}
    temp_dict['CUSTOMER CODE'] = df.loc[i, 'CUSTOMER CODE']
    temp_dict['CUSTOMER NAME'] = df.loc[i, 'CUSTOMER NAME']
    temp_dict['SERVICE ADDR.'] = df.loc[i, 'SERVICE ADDR.']
    temp_dict['MTH.LOAD'] = df.loc[i, 'MTH.LOAD']

    for year in years:
        ann_consum = 0
        for month in months:
            label = year + '-' + month
            mth_consum = df.loc[i, label]
            if math.isnan(mth_consum):
                mth_consum = 0
            ann_consum = ann_consum + mth_consum
        temp_dict[year] = ann_consum

    list.append(temp_dict)

out_df = pd.DataFrame(list)

label = 'ann_consum'
file_name = label + '.xlsx'
file_path = 'data\\' + file_name
if os.path.exists(file_path):
    print(file_path + ' already exists...')
    opt = input('Overwrite (y/n)?   ')
    if opt.lower().__eq__('y'):
        out_df.to_excel(file_path, index=False)
else:
    out_df.to_excel(file_path, index=False)
