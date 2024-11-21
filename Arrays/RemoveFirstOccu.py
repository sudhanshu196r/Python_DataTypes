'''

    @Author: Sudhanshu Kumar
    @Date: 23-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 23-09-2024
    @Title : Python program to remove first occurence of an element

'''

import array
"""
Description:
    Function to remove the first occurence of an element
Parameters:
    arr: takes array as a parameter
    ele: element to be removed
Returns:
    arr : after removing the first occurence of element
"""
def removeOccurence(arr,ele):
    arr.remove(ele)
    return arr

def main():
    arr = array.array('i')
    n = int(input("Enter size: "))
    for i in range(n):
        ele = int(input())
        arr.append(ele)

    ele = int(input("Enter element to be removed : "))
    arr1=removeOccurence(arr,ele)
    print(arr1)

if __name__=="__main__":
    main()