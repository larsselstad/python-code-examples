import pandas as pd

data = {
    1243: ['Max', '2018-04-17', 2352, 4722],
    9384: ['Polly', '2018-04-17', 2352, 4722],
    2353: ['Fong', '', -1, -1],
    4722: ['Edward', '', -1, -1],
    1198: ['Jessie', '', -1, -1]
}
cols = ['Nickname', 'Date of birth', "Mother's ID", "Father's ID"]

rows = []
data_list = []
for ikey in data:
    rows.append(ikey)
    data_list.append(data[ikey])

data_df = pd.DataFrame(data_list, index=rows, columns=cols)

print(data_df)
print('indexs', data_df.index)
print('columns', data_df.columns)

print('List nicknames:')
print(data_df['Nickname'])
print('Nickname is a Series', type(data_df['Nickname']))

print('List nicknames and Mothers ID:')
print(data_df[['Nickname', "Mother's ID"]])
print('Nickname and Mothers ID is a DataFrame', type(data_df[['Nickname', "Mother's ID"]]))

print('Select rows and columns based on keys')
print(data_df.loc[4722, :])
print(data_df.loc[9384:4722, 'Nickname':"Mother's ID"])
print(data_df.loc[[9384,4722,1198], ['Nickname','Date of birth']])

print('Select rows and columns based on indexs')
print(data_df.iloc[0:2, 1:3])
print(data_df.iloc[[0, 2], [1, 3]])

print("Adding data to dataframe")
copy_df = data_df[['Nickname', 'Date of birth']].copy()
copy_df['Color'] = pd.Series(['brown', 'brown', 'dark brown', 'dark brown', 'brown'], index=rows)
copy_df['Weight'] = pd.Series([71, 65, 59, 60, 60], index=rows)
copy_df['Length'] = pd.Series([26, 29, 32, 33, 30], index=rows)
print(copy_df)

print('Adding new beaver to dataframe')
copy_df.loc[7844, :] = pd.Series(['Lily', '', 'dark brown', 62, 34], index=copy_df.columns)
print(copy_df)