import numpy as np

# numpy array operations

arr = np.array([1,2,3,4,5,6,7,8,9,0])
print("basic slicing", arr[1:4])
print("with step", arr[1:8:2])
print("negative indexing", arr[-3])

_2d_array = np.array(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
)

print("2d_arr specific index", _2d_array[1:2])
print("2d_arr specific element", _2d_array[1,2])
print("2d_arr entire row", _2d_array[1])

print("2d_arr entire column", _2d_array[:, 0])







# sorting

unsorted = np.array([1,5,7,3,9,4,1,7,2,4,5])
print("sorted np array", np.sort(unsorted))

arr_2d_unsorted = np.array(
    [
        [3,1],
        [1,4],
        [2,3]
    ]
)

print("sorted 2d array", np.sort(arr_2d_unsorted, axis=0))





# filtering

_numbers = np.array([1,2,3,4,5,6,7,8,9,10])
even_numbers = _numbers[_numbers % 2 == 0]
print("even_numbers",even_numbers)

# filter with mask

mask = _numbers > 5
print("mask", _numbers[mask])

# fancy indexing vs np.where()

indices = [1,2,4]
print("indoces", _numbers[indices])

where_result = np.where(_numbers > 5)
print("where result" ,where_result)
print("np where", _numbers[where_result])


# condition array

condition_arr = np.where(_numbers > 5, _numbers*2, _numbers)

# if _numbers > 5:
#     _numbers * 2
# else:
#     _numbers
# 

print("condition_arr",condition_arr)





# adding and removing data

arr_1 = np.array([1,2,3])
arr_2 = np.array([4,5,6])
combined_arr = arr_1 + arr_2
print("combined_arr",combined_arr)

concatenated_arr = np.concatenate((arr_1, arr_2))
print("concatenated_arr",concatenated_arr)




# array compatibility

a = np.array([1,2,3])
b = np.array([4,5,6,7])
c = np.array([7,8,9])

print("compatibiity shape", a.shape == b.shape)

original = np.array(
    [
        [1,2],
        [7,8]
    ]
)
print("original",original)


new_row = np.array(
    [
        [5,6]
    ]
)

with_new_row = np.vstack((original, new_row)) # vertical stack
print("with_new_row",with_new_row)


new_col = np.array(
    [
        [16],
        [17],
    ],
)

with_new_col = np.hstack((original, new_col))
print("with_new_col",with_new_col)


# deleting
new_arr = np.array([1,2,3,4,5])
print("before_deletion", new_arr)

deleted = np.delete(new_arr, 2)
print("after_deletion",deleted)



