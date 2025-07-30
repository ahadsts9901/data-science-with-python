import numpy as np



# numpy basics 

print(np.array([1,5,6]))
print(np.array([[1,2,3], [4,5,6]]))



# list vs numpy array
py_list = [1,2,3]
print("list multiplication", py_list * 2)
np_arr = np.array([1,2,3])
print("np array multiplication", np_arr * 2)

# chcking multiplication time
import time

start = time.time()
py_list = [i*2 for i in range(100000)]
print("list operation time", time.time() - start)

start = time.time()
np_array = np.arange(100000 * 2)
print("np array operation time", time.time() - start)




# creating array from scratch
zeros = np.zeros((3,4))
print("zeros arr", zeros)

ones = np.ones((6,9))
print("ones arr", ones)

full = np.full((4,5), 5)
print("full arr", full)

random = np.random.random((4,6))
print("random arr", random)


sequence = np.arange(1,102, 4)
print("sequence arr", sequence)



# vector, matrix and tensor

vector = np.array([1,2,3])
print("vector", vector)

matrix = np.array(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
)

print("matrix", matrix)


tensor = [
    [
        [11,12,13],
        [14,15,16],
        [17,18,19],
    ],
    [
        [21,22,23],
        [24,25,26],
        [27,28,29],
    ],
    [
        [31,32,33],
        [34,35,36],
        [37,38,39],
    ]
]

print("tensor", tensor)




# array properties

arr = np.array(
    [
        [1,2,3],
        [4,5,6]
    ]
)

print("arr", arr)
print("shape", arr.shape)
print("dimension", arr.ndim)
print("size", arr.size)
print("data_type", arr.dtype)





# array re-shaping

arr = np.arange(12)
print("original arr", arr)

reshaped = arr.reshape((4,3))
print("reshaped arr", reshaped)

flattened = reshaped.flatten()
print("flatenned arr", flattened)

# returns view instead of copy
raveled = reshaped.ravel()
print("raveled arr", raveled)

transposed = reshaped.T
print("transposed arr", transposed)

