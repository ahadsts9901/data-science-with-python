import numpy as np
import matplotlib.pyplot as plt

# data structure [id, 2021, 2022, 2023, 2024]

data_structure = np.array([
    [1, 150000,180000,220000,250000], # paradise biryani
    [2, 120000,140000,160000,190000], # beijing bites
    [3, 200000,230000,260000,300000], # pizza hub
    [4, 180000,210000,240000,270000], # burger point
    [5, 160000,185000,205000,230000], # chai point
])


print("=========== zomato sales analysis =========")
print("data shape", data_structure.shape)
print("first 3 restaurants", data_structure[0:3])


# total sales per year
print("total sales per year", np.sum(data_structure, axis=0))

yearly_total = np.sum(data_structure[:, 1:], axis=0)
print("yearly total", yearly_total)


# minimum sales per restaurant
min_sales = np.min(data_structure[:, 1:], axis=1)
print("min_sales",min_sales)


# maximum sales per year
max_sales = np.max(data_structure[:, 1:], axis=0)
print("max_sales",max_sales)


# average sales per restaurant
avg_sales = np.mean(data_structure[:, 1:], axis=1)
print("avg_sales",avg_sales)


# cummoliative sales
cum_sum = np.cumsum(data_structure[:, 1:], axis=1)
print("cum_sum",cum_sum)

plt.figure(figsize=(10,6))
plt.plot(np.mean(cum_sum, axis=0))
plt.title("cumuliative sales across all restaurant")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.grid(True)
# plt.show()



# vector maps

vector_1 = np.array([1,2,3,4,5])
vector_2 = np.array([6,7,8,9,10])

print("vector addition", vector_1 + vector_2)
print("vector multiplication", vector_1 * vector_2)
print("dot product", np.dot(vector_1, vector_2))

angle = np.arccos(np.dot(vector_1, vector_2) / (np.linalg.norm(vector_1) * np.linalg.norm(vector_2)))
print("angle",angle)



# vectorized operations

restaurant_types = np.array([
    "boryani",
    "chinese",
    "pizza",
    "burger",
    "cafe"
])

vectorized_upper = np.vectorize(str.upper)
print("vectorized_upper", vectorized_upper(restaurant_types))



# broadcast

monthly_avg = data_structure[:, 1:] / 12
print("monthly_avg",monthly_avg)


