'''

    @Author: Sudhanshu Kumar
    @Date: 18-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 18-09-2024
    @Title : Write a Python program to print histogram for a list of variables

'''


import matplotlib.pyplot as plt

def histPlot(data):

    plt.hist(data, bins=len(data), edgecolor='black')

    plt.title('Histogram')
    plt.xlabel('Value')
    plt.ylabel('Frequency')

    plt.show()

def main():
    data_str = input("Enter list of numbers seperated by comma : ")
    data = data_str.split(",")
    histPlot(data)


if __name__=="__main__":
    main()
