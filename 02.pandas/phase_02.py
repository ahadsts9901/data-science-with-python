import numpy as np
import pandas as pd

# difference between series and data frame

ser = pd.Series(np.random.rand(33))

# print("ser",ser)

df = pd.DataFrame(np.random.rand(334,5), index=np.arange(334))
# print("df", df)
head = df.head()
# print("head", head)

_type =  type(df)
# print("df type",_type)

_describe= df.describe()
# print("describe",_describe)

df[0][0] = "mani"

_data_types = df.dtypes
# print("data type", _data_types)

_head = df.head()
# print("head", _head)

_index = df.index
# print("index", _index)

columns = df.columns
# print("columns", columns)

# print("to_numpy", df.to_numpy())


df[0][0] = 0.83
# print("to_numpy", df.to_numpy())

transposed = df.T
# print("transposed", transposed)

desc_sorted = df.sort_index(axis=0, ascending=False)
# print("desc_sorted",desc_sorted)

# print("head", df.head())

# df2 = df
# df2 = df.copy()

# df2[0][0] = 9090909090

# print("df",df)
# print("df2",df2)


df.columns = list("ABCDE")
# df.loc[0,0] = 234
df.loc[0,"A"] = 234
# df.drop(0, axis=1)

# print("df.head(2)",df.head(2))

new_df = df.loc[[1,2], ['C', 'D']]
# print("new_df", new_df)

all_rows = df.loc[:, ['C', 'D']] # all_rows
all_columns = df.loc[[1,2], :] # all_columns

# print("all_rows",all_rows)
# print("all_columns",all_columns)

query_data_frame = df.loc[(df['A']>0.3) & (df['C']>0.1)]
# print("query_data_frame",query_data_frame)

specific_cell = df.iloc[0,4]
# print("specific_cell",specific_cell)

specific_cells = df.iloc[[0,1], [1,2]]
# print("specific_cells",specific_cells)

# iloc main index dengy
# loc main naam dengy index kaa



# print("before", df)
# df = df.drop(['A', 'C'], axis=1)
df.drop(['A', 'C'], axis=1, 
        # inplace=True # ye original main hi drop krdega
        )

df.drop([0, 5], axis=0, 
        # inplace=True
        )

df.reset_index(
        drop=True,
    inplace=True,
               )

# print("after", df)






# is null
# df["B"] = None
df.loc[:, ["B"]] = 58
is_null = df['B'].isnull()


print("none df",df)

print("is_null",is_null)















