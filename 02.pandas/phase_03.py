import numpy as np
import pandas as pd

# more functions

df = pd.DataFrame({
    "name": ["babar", "babar", "zeeshan"],
    "toy": [np.nan, "Bat", "Football"],
    "born": [pd.NaT, pd.Timestamp("2000-4-25"), pd.NaT]
})

# print("drop_na", df.dropna(how='all', axis=1)) # jab tk saary colunm N/A nahi hongy jab tk drop nahi hoga


# print("drop_duplicates", df.drop_duplicates(subset=["name"], keep="last")),

# print("info", df.info())

# print(df['name'].value_counts(dropna=True))

# print("not null", df.notnull())








# exercise

data = np.array([[10, 5], [20, 15], [30, 25]])
df = pd.DataFrame(data, columns=['A', 'B'])

# Display the DataFrame
print("DataFrame:")
print(df)

# Run the methods
print("\ndf.describe():")
print(df.describe())

print("\ndf.mean():")
print(df.mean())

print("\ndf.corr():")
print(df.corr())
# Ye check karta hai ki do columns ka rishta kaisa hai – kya dono sath badhte/girhte hain ya nahi?
# A = [10, 20, 30]
# B = [5, 15, 25]

# 1.0 → dono sath badhte/girhte hain
# -1.0 → ek badhta hai to dusra ghatta hai
# 0.0 → koi rishta nahi

print("\ndf.count():")
print(df.count())

print("\ndf.median():")
print(df.median())

print("\ndf.min():")
print(df.min())

print("\ndf.max():")
print(df.max())

print("\ndf.std():")
print(df.std())
# Har number ka difference from mean(darmya ka number):
# 10 → 10 door
# 20 → 0 door
# 30 → 10 door




