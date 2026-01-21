from pickle import TRUE

import pandas as pd
df = pd.read_csv('gradedata.csv')

# print(df.to_string())
#
# new_df = df.dropna()
#
# print(new_df.to_string())

# df['grade'] = pd.to_datetime(df['grade'], format='mixed')
#
# print(df.to_string())

# for x in df.index:
#   if df.loc[x, "age"] > 25:
#     df.drop(x, inplace = True)
#
# print(df.to_string())
print(df.duplicated())
