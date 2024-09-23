'''

    @Author: Sudhanshu Kumar
    @Date: 23-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 23-09-2024
    @Title : Python program to create an array and print the array

'''

import array

def reverseOrder(arr):
    """
    Description: 
        Function to reverse the order of elements of array
    Parameters:
        arr: It takes an array as parameter
    Returns:
        Nothing
    """


    #arr.reverse()

    rev_arr = arr[::-1]
    print("Reversed Array : ")
    for i in range(len(arr)):
        print(rev_arr[i])

def main():
    arr = array.array('i')
    n = int(input("Enter size: "))
    for i in range(n):
        ele = int(input())
        arr.append(ele)

    reverseOrder(arr)

if __name__=="__main__":
    main()