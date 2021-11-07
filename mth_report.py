import pandas as pd
import os.path

column_names = ['CUSTOMER CODE', 'CUSTOMER NAME', 'SERVICE ADDR.', 'ACTUAL CONSUM', 'MTH.LOAD']
years = ['2016', '2017', '2018', '2019', '2020']
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
# years = ['2016', '2017']
# months = ['01', '02', '03', '04']
n_years = len(years)
n_months = len(months)

df_arr = []
for year in years:
    for month in months:
        label = year + '-' + month
        file_name = label + '.xlsx'
        file_path = 'data\\'+ file_name
        if os.path.exists(file_path):
            df = pd.read_excel(file_path, usecols=column_names)
            df_arr.append({'Name': label, 'Data': df})
            print(file_path + ' read...')
        else:
            print(file_path + ' does not exist...')

dict = {}
for item in df_arr:
    label = item['Name']
    df = item['Data']
    for i in range(len(df)):
        code = df.loc[i, 'CUSTOMER CODE']
        name = df.loc[i, 'CUSTOMER NAME']
        addr = df.loc[i, 'SERVICE ADDR.']
        load = df.loc[i, 'MTH.LOAD']
        consum = df.loc[i, 'ACTUAL CONSUM']

        if code not in dict:
            temp_dict = {}
            temp_dict['CUSTOMER CODE'] = code
            temp_dict['CUSTOMER NAME'] = name
            temp_dict['SERVICE ADDR.'] = addr
            temp_dict['MTH.LOAD'] = load
            dict[code] = temp_dict

        dict[code][label] = consum
    print('Processing Dataframe %s...' %(label))

out_df = pd.DataFrame(dict.values())

label = 'mth_consum'
file_name = label + '.xlsx'
file_path = 'data\\' + file_name
if os.path.exists(file_path):
    print(file_path + ' already exists...')
    opt = input('Overwrite (y/n)?   ')
    if opt.lower().__eq__('y'):
        out_df.to_excel(file_path, index=False)
else:
    out_df.to_excel(file_path, index=False)