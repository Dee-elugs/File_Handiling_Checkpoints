# How to read

# with open("Text.txt", "r") as file:
#     content = file.read()
#     print(content)

# How to write

# with open("Text.txt", "w") as f:
#     f.write("I just changed the content of this text file.")

# with open("Text.txt", "a") as f:
#     f.write("\nI appended a new line")

# with open("Text.txt", "r") as f:
#     content = f.read()
#     print(content)

# with open("Dee.txt", "w") as f:
#     f.write("\nI appended a new line")

# x checks if the file already exists

# with open("data.csv", "r") as f:
#     c = f.read()
#     print(c)

#Add new row to the csv file
# with open("data.csv", "a") as obj:
#     obj.write("\nAyo,50,UK")

#Check Point
# import numpy as np
# data = np.genfromtxt("data.csv", dtype=None, delimiter = ",", usecols=(0,1))
# print(data)
# usecols = is used to specify the column

# with open("Loan.csv", "r") as f:
#     data = f.read()
#     print(data)

import numpy as np
data = np.genfromtxt("Loan.csv", delimiter = ",", usecols=(8), filling_values=0)
# # print(data)

#Creating a 1D array
Loan = np.array(data)

#Calculate the mean of the array
# mean = np.mean(Loan)
# print(f"The mean is : {mean}")
# print(Loan)

# median = np.median(Loan)
# print(f"The median is : {median}")

std = np.std(Loan)
print(f"The std is : {std}")

max = np.max(Loan)
print(f"The max is : {max}")

min = np.min(Loan)
print(f"The min is : {min}")

var = np.var(Loan)
print(f"The var is : {var}")

