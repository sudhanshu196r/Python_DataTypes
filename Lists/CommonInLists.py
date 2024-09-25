'''

    @Author: Sudhanshu Kumar
    @Date: 25-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 25-09-2024
    @Title : Python program to find common element between two lists

'''

import itertools

def commonEle(lst1,lst2):
    """
    Description:
        THis list will find common element between two lists
    Parameters:
        lst1 : first list
        lst2 : second list
    Returns:
        List containing common elements

    """
    return list(ele for ele in lst1 if ele in lst2)

def main():
    lst1 = [1,2,3,45,6,7,8,9]
    lst2 = [1,2,3,4]
    print(commonEle(lst1,lst2))
    

if __name__=="__main__":
    main()
 