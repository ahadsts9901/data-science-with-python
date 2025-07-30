import numpy as np
import pandas as pd


data = pd.read_excel("data.xlsx", sheet_name="sheet 2")
# print("data",data)


data.iloc[0,0] = "shees"
data.to_excel("data.xlsx", sheet_name="sheet 2") # ye baaki sheets ko remove krdega lekn (isky liay documentation dekhain pandas ki)

print(data)

