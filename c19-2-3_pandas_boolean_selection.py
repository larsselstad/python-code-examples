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
print('Check Mothers ID > 0')
print(data_df["Mother's ID"] > 0)

mask = data_df["Mother's ID"] > 0
print(data_df[mask])

print(data_df[(data_df["Mother's ID"] > 0) & (data_df.index > 5000)])