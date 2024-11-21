'''

    @Author: Sudhanshu Kumar
    @Date: 25-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 25-09-2024
    @Title : Python program to find the difference between two lists

'''

import itertools

def list_diff(lst1,lst2):
    """
    Description:
        This function will find the difference between two lists
    Parameters:
        lst1 : first list
        lst2 : second list
    Returns:
        Return a list of difference

    """

    return [item for item in lst1 if item not in lst2]


def main():
    lst1 = [1,2,3,45,6,7,8,9]
    lst2 = [1,2,3,4]
    print(list_diff(lst1,lst2))
    

if __name__=="__main__":
    main()
 