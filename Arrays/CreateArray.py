'''

    @Author: Sudhanshu Kumar
    @Date: 23-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 23-09-2024
    @Title : Python program to create an array and print the array

'''

import array
def createArray():
    """
    Description: 
        This function creates an array and print the array using index
    Parameters: 
        It takes no parameters
    Returns:
        Returns nothing
    """
    arr = array.array('i')
    n = int(input("enter size of the array: "))
    for i in range(n):
        ele = int(input())
        arr.append(ele)

    for i in range(n):
        print(arr[i])

def main():
    createArray()

if __name__=="__main__":
    main()