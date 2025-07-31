import numpy as np
import pandas as pd

dict_1 = {
    "name": ["ahad", "aryan", "asif", "aliyan"],
    "marks": [83, 67 ,34 ,55],
    "city": ["karachi", "sialkot", "gujrat", "Islamabad"]
}

df = pd.DataFrame(dict_1)
print("df",df)

df.to_csv("friends.csv",)
df.to_csv("friends_without_index.csv", index=False)

print("head",df.head(2))
print("tail",df.tail(2))


print("describe", df.describe())


_csv = pd.read_csv("mani.csv")

print("_csv",_csv)

_csv["city"][0] = "new_york"

_csv.to_csv("mani2.csv", index=False)

_csv.index = ["one", "two", "three", "four"]

print(_csv)








