import pandas as pd

data = {
    1243: ['Max', '2018-04-17', 2352, 4722, 'brown'],
    9384: ['Polly', '2018-04-17', 2352, 4722, 'brown'],
    2353: ['Fong', '', -1, -1, 'dark brown'],
    4722: ['Edward', '', -1, -1, 'dark brown'],
    1198: ['Jessie', '', -1, -1, 'brown']
}
cols = ['Nickname', 'Date of birth', "Mother's ID", "Father's ID", "Color"]

rows = []
data_list = []
for ikey in data:
    rows.append(ikey)
    data_list.append(data[ikey])

data_df = pd.DataFrame(data_list, index=rows, columns=cols)

copy_df = data_df.copy()
copy_df['Weight'] = pd.Series([71, 65, 59, 60, 60], index=rows)
copy_df['Length'] = pd.Series([26, 29, 32, 33, 30], index=rows)
print(copy_df)

print('Group color and get mean')
print(copy_df.groupby('Color').mean())


print(copy_df.groupby('Color').get_group('brown'))

print(copy_df.groupby('Color').groups)


