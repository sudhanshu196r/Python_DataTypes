'''

    @Author: Sudhanshu Kumar
    @Date: 25-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 25-09-2024
    @Title : Python program to get smallest element in the list

'''

def minValue(lst):
    """
    Description:
        This function will return smallest number from the list
    Parameters:
        lst : a list
    Returns:
        Min Value

    """

    min = lst[0]
    for i in range(1,len(lst)):
        if min>lst[i]:
            min = lst[i]
    
    return min

def main():
    lst = [7,2,1,3,4,2,4,5]
    print(min(lst))
    print(minValue(lst))

if __name__=="__main__":
    main()
