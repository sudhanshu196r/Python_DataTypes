'''

    @Author: Sudhanshu Kumar
    @Date: 25-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 25-09-2024
    @Title : Python program to get sum of elements of list

'''

def sumElements(lst):
    """
    Description:
        This function will take the sum of all the elements of the list
    Parameters:
        lst : a list
    Returns:
        Sum of elements

    """

    sum = 0
    for i in range(len(lst)):
        sum+=lst[i]
    
    return sum

def main():
    lst = [1,2,1,3,4,2,4,5]
    print(sumElements(lst))

if __name__=="__main__":
    main()
