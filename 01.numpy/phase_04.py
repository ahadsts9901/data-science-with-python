import numpy as np
import matplotlib.pyplot as plt

arr_1 = np.array([[1,2,3],[4,5,6]])
arr_2 = np.random.rand(3,3)
arr_3 = np.zeros((4,4))

np.save("array1.npy", arr_1)
np.save("array2.npy", arr_2)
np.save("array3.npy", arr_3)

loaded_arr_1 = np.load("array1.npy")
loaded_arr_2 = np.load("array2.npy")
loaded_arr_3 = np.load("array3.npy")

print("loaded_arr_1",loaded_arr_1)
print("loaded_arr_2",loaded_arr_2)
print("loaded_arr_3",loaded_arr_3)


try:
    logo = np.load("numpy-logo.npy")
    # logo = np.load("array1.npy")

    # display
    plt.figure(figsize=(10,5))
    plt.subplot(121)
    plt.imshow(logo)
    plt.title("numpy logo")
    plt.grid(False)
    plt.show()

    dark_logo = 1 - logo
    plt.subplot(122)
    plt.imshow(dark_logo)
    plt.title("numpy dark logo")
    plt.grid(False)
    plt.show()


except FileNotFoundError:
    print("logo fil enot found") 



